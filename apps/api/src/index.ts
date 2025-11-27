import { Hono } from 'hono';
import { cors } from 'hono/cors';

type Bindings = {
	DB: D1Database;
	GOOGLE_CLIENT_ID: string;
	HUGGINGFACE_API_URL: string;
};

const app = new Hono<{ Bindings: Bindings }>();

// Enable CORS
app.use('/*', cors());

// Health check
app.get('/', (c) => {
	return c.json({ status: 'ok', message: 'IndoParaphrase API' });
});

// Paraphrase endpoint
app.post('/api/paraphrase', async (c) => {
	try {
		const { paragraphs } = await c.req.json();

		if (!paragraphs || !Array.isArray(paragraphs)) {
			return c.json({ error: 'Invalid input. Expected array of paragraphs.' }, 400);
		}

		const results = [];

		for (const paragraph of paragraphs) {
			// Call HuggingFace Space API
			const response = await fetch(c.env.HUGGINGFACE_API_URL, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({
					data: [paragraph]
				})
			});

			const data = await response.json();
			results.push({
				original: paragraph,
				paraphrased: data.data?.[0] || paragraph
			});
		}

		return c.json({ results });
	} catch (error) {
		return c.json({ error: 'Failed to paraphrase' }, 500);
	}
});

// Save draft endpoint
app.post('/api/drafts', async (c) => {
	try {
		const { userId, content } = await c.req.json();

		if (!userId || !content) {
			return c.json({ error: 'Missing userId or content' }, 400);
		}

		// Check draft limit (max 5 per user)
		const { results } = await c.env.DB.prepare(
			'SELECT COUNT(*) as count FROM drafts WHERE user_id = ?'
		).bind(userId).all();

		const count = results[0]?.count || 0;

		if (count >= 5) {
			return c.json({ error: 'Draft limit reached (max 5)' }, 429);
		}

		// Insert draft
		const result = await c.env.DB.prepare(
			'INSERT INTO drafts (user_id, content, created_at) VALUES (?, ?, ?)'
		).bind(userId, content, Date.now()).run();

		return c.json({ id: result.meta.last_row_id, message: 'Draft saved' });
	} catch (error) {
		return c.json({ error: 'Failed to save draft' }, 500);
	}
});

// Get user drafts
app.get('/api/drafts/:userId', async (c) => {
	try {
		const userId = c.req.param('userId');

		const { results } = await c.env.DB.prepare(
			'SELECT id, content, created_at FROM drafts WHERE user_id = ? ORDER BY created_at DESC LIMIT 5'
		).bind(userId).all();

		return c.json({ drafts: results });
	} catch (error) {
		return c.json({ error: 'Failed to fetch drafts' }, 500);
	}
});

// Delete draft
app.delete('/api/drafts/:id', async (c) => {
	try {
		const id = c.req.param('id');

		await c.env.DB.prepare('DELETE FROM drafts WHERE id = ?').bind(id).run();

		return c.json({ message: 'Draft deleted' });
	} catch (error) {
		return c.json({ error: 'Failed to delete draft' }, 500);
	}
});

export default app;

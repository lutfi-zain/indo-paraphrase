-- Create drafts table for saving user work
CREATE TABLE IF NOT EXISTS drafts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id TEXT NOT NULL,
  content TEXT NOT NULL,
  created_at INTEGER NOT NULL
);

CREATE INDEX idx_drafts_user_id ON drafts(user_id);
CREATE INDEX idx_drafts_created_at ON drafts(created_at DESC);

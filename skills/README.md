# Chimera Agent Skills

This directory defines the core runtime capabilities ("Skills") for Chimera Agents. Each skill is a self-contained module with clearly defined input/output contracts, ready for future implementation.

## 1. skill_download_youtube
**Description:** Downloads video or audio from a given YouTube URL.  
**Input:**  
```json
{
  "url": "string",
  "format": "string"  // "mp4", "mp3"
}

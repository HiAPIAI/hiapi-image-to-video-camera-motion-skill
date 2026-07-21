# Research Sources

Reviewed on 2026-07-21. Recheck provider documentation before relying on current model names, parameters, limits, pricing, or availability.

## Contents

- Official and first-party sources
- Public Skill references
- Professional principles added by this Skill

## Official and First-Party Sources

### Runway: Image to Video Prompting Guide

- URL: https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide
- First-party article ID: `48324313115155`
- Key takeaways used by this Skill:
  - the input image defines composition, subject, lighting, and style;
  - the prompt should focus primarily on motion, camera work, and temporal progression;
  - separate subject action, environmental motion, camera motion, motion style/timing, direction, and speed;
  - start with the critical motion and add detail through iteration;
  - the input acts as the first frame;
  - source artifacts can intensify in video;
  - sequential prompts and timestamps must fit the selected duration.

### Runway: Camera Terms, Prompts, and Examples

- URL: https://help.runwayml.com/hc/en-us/articles/47313504791059-Camera-Terms-Prompts-Examples
- First-party article ID: `47313504791059`
- Key takeaways used by this Skill:
  - professional distinctions among pan, tilt, dolly, truck, orbit, pedestal, crane/jib, zoom, handheld, steadicam, and whip pan;
  - shot size and camera angle should be directed separately from movement;
  - camera terms should map to visible physical behavior.

### Runway: Creating with Gen-4.5

- URL: https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5
- First-party article ID: `46974685288467`
- Facts observed at review time:
  - supports Text to Video and Image to Video;
  - official guidance says I2V prompts should describe scene motion;
  - official page documented 2-10 second generation and detailed camera choreography;
  - exact limits and availability are volatile and must be rechecked.

### Google Cloud: Veo video generation notebook

- URL: https://github.com/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/veo3_video_generation.ipynb
- Key takeaways used by this Skill:
  - Text to Video planning separates subject, action, scene, camera angle, camera movement, lens effects, style, temporal elements, and audio;
  - Image to Video planning separates camera motion, subject animation, environmental animation, and audio;
  - this supports the Skill's explicit motion hierarchy.

### PixVerseAI official Skills and CLI

- Repository: https://github.com/PixVerseAI/skills
- Skills directory: https://skills.sh/PixVerseAI/skills/pixverse-ai-image-and-video-generator
- Key takeaways used by this Skill:
  - official CLI workflow for local or URL image inputs;
  - structured model, duration, quality, aspect ratio, seed, count, audio, reference, task, and download handling;
  - provider-specific capability tables must be checked before selecting flags;
  - local inputs are uploaded for cloud processing.

## Public Skill References

These sources informed workflow comparisons but are not treated as universal truth.

### inference.sh image-to-video

- URL: https://skills.sh/inference-sh/skills/image-to-video
- Repository: https://github.com/inference-sh/skills
- Useful material:
  - camera-movement prompt examples;
  - model-selection patterns;
  - short-clip and iterative generation practices;
  - product orbit, portrait, architecture, and environmental examples.

### inference.sh video-prompting-guide

- URL: https://skills.sh/inference-sh/skills/video-prompting-guide
- Repository: https://github.com/inference-sh/skills
- Useful material:
  - shot types, camera vocabulary, lighting, style, and cross-model prompt structure.

### fal-ai-community cinematography

- URL: https://skills.sh/fal-ai-community/skills/cinematography
- Repository: https://github.com/fal-ai-community/skills
- Useful material:
  - shot language, framing, camera, lens, light, color, and model-routing discipline;
  - preservation language for product and character continuity;
  - instruction to inspect actual schemas before using controls.

### RunComfy image-to-video

- URL: https://skills.sh/skills-collective/skills/image-to-video
- Repository observed through redirect: https://github.com/runcomfy-com/skills
- Useful material:
  - intent-based I2V model routing;
  - product reveal, macro motion, identity preservation, and audio/reference workflows;
  - one primary motion beat per short clip.

### Eachlabs image-to-video

- URL: https://skills.sh/eachlabs/skills/image-to-video
- Repository: https://github.com/eachlabs/skills
- Useful material:
  - Ken Burns, cinemagraph, product showcase, parallax, portrait, landscape, and artwork patterns.

### Reference-driven video prompting

- Repository: https://github.com/nolanx-ai/nolanx.ai
- Skill path: `.nolanx/skills/reference-driven-video-prompting/SKILL.md`
- Useful material:
  - reference hierarchy;
  - separation of subject and camera motion;
  - one dominant camera move;
  - continuity across prior video and keyframes.

### Image-to-video motion director

- Repository: https://github.com/muuhdra/content-gen
- Skill path: `packages/factory/Image-to-video-motion-director/skill.md`
- Useful material:
  - narrative motivation before camera choice;
  - approved-image preservation;
  - blocking, spatial relationship, emotion, and motion priority;
  - rejection of decorative 360-degree orbit.

## Professional Principles Added by This Skill

The following synthesis is based on standard cinematography and visual-effects practice rather than a single provider claim:

- pan/tilt are camera rotations; dolly/truck/pedestal/crane/orbit are translations; zoom is an optical framing change;
- translation creates perspective and parallax change, increasing unseen-surface reconstruction load;
- a single approved image should normally support one bounded primary move;
- real product turnaround and large orbit require multi-view or 3D information;
- camera, subject, and environment need an explicit motion hierarchy;
- end-frame design and deceleration are part of direction, not post-generation cleanup;
- identity, anatomy, text, logo, and rigid geometry are critical acceptance gates;
- successful task completion is not visual approval.

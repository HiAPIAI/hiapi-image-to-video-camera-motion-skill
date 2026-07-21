# Model and Tool Routing

Route by capability, not by brand preference. Provider names, versions, pricing, duration, and parameter schemas change frequently. Inspect the actual tool schema or current official documentation before every generation workflow.

## Contents

- Routing sequence
- Capability classes
- Prompt adaptation
- Known provider patterns
- Settings decisions
- Execution contract
- Privacy and cost controls

## Routing Sequence

1. Identify whether the user wants direction only, generation, or review.
2. List the authorized image-to-video tools already available in the environment.
3. Inspect their schemas, supported input types, duration, aspect ratios, camera controls, reference inputs, negative prompts, seeds, audio, and output handling.
4. Compare the shot's reconstruction risk with the tool's controls.
5. Select the least complex tool that can execute the intended motion.
6. Generate a conservative baseline before using expensive quality settings or multiple variants.

Do not require a provider account when the user only asked for a motion plan. Do not upload private images to a third-party service without making that processing boundary clear.

## Capability Classes

### A. Prompt-led image-to-video

Inputs usually include one image, a motion prompt, duration, and aspect ratio. Camera movement is expressed in natural language.

Best for:

- push, pull, pan, tilt, small arc, subject micro-motion;
- atmospheric animation;
- general product or portrait shots;
- quick baseline testing.

Risks:

- the model interprets camera language rather than following a deterministic path;
- large translation and orbit may invent geometry;
- unsupported negative wording may have little effect.

### B. Explicit camera preset or camera-control workflow

Inputs may expose named presets, motion strength, path, direction, start/end camera state, or composable camera moves.

Best for:

- repeatable commercial shot families;
- constrained push, truck, pedestal, arc, or follow motion;
- creators who need consistent terminology across many clips.

Verify whether the preset is a real structured parameter or only prompt text hidden behind a UI.

### C. Start-frame and end-frame control

Inputs include first and last images or keyframes.

Best for:

- exact reveal destinations;
- product transitions;
- controlled pull-out or push-in end composition;
- longer sequences built from short connected shots.

The end frame must be geometrically compatible with the start. Large identity, lighting, or perspective mismatch creates morphing rather than camera motion.

Before using start/end control for a camera-led shot, compare outer silhouette, subject scale, camera height, support surface, background layout, lighting direction, and the intended focal feature. If several of these change materially, classify the brief as a transition or transformation shot. Regenerate a compatible end frame or use the start frame alone when the deliverable must demonstrate camera movement. Do not score an attractive morph as successful camera-direction compliance.

### D. Multi-image or multi-reference generation

Inputs can include several subject, style, scene, product, video, or audio references.

Best for:

- identity continuity;
- exposing product side or back information;
- stronger orbit and angle evolution;
- matching a brand environment or prior shot.

Number references clearly in the prompt when the provider supports multiple inputs. Do not mix incompatible perspectives, lighting, or product versions.

### E. Motion-reference or performance-transfer workflow

Inputs include a still subject plus a reference video.

Best for:

- dance, gestures, pose, walking rhythm, or exact human performance;
- camera path imitation only when the tool explicitly supports camera motion transfer.

Do not confuse body-motion transfer with camera-motion transfer. Many tools support only the former.

### F. 2.5D or 3D reconstruction workflow

Inputs may create depth maps, layers, point clouds, NeRFs, Gaussian splats, or 3D assets before rendering.

Best for:

- large camera translations;
- repeatable product orbit;
- architecture fly-through;
- exact multi-shot camera paths.

Use this class when the deliverable depends on geometry, not just a plausible generative impression.

## Prompt Adaptation

### Image-first prompt-led models

Focus almost entirely on what changes:

```text
The camera slowly pushes forward along the corridor while the subject walks at a
steady pace. Light haze drifts through the windows. The perspective lines,
wardrobe, face, and architecture remain stable. One continuous five-second shot.
```

Do not spend tokens restating colors, clothing, or background already visible unless the requested change depends on them.

### Explicit camera parameters

Move physical motion out of prose when the schema has dedicated controls.

```text
camera_preset: dolly_in
motion_strength: low
prompt: The subject takes one calm breath as window light shifts subtly. Preserve identity and scene geometry.
```

Use the provider's exact enum values. Never invent `motion_strength`, `camera_preset`, or similar fields.

### Multi-reference models

Assign roles:

```text
image 1: primary subject and identity
image 2: product side geometry
image 3: lighting reference
video 1: walking pace only
```

Then state which reference controls which attribute. Avoid asking one reference to control identity, style, environment, and motion simultaneously.

### Negative prompt support

If a dedicated field exists, use concrete failure terms:

```text
warped label, duplicate limbs, unstable face, geometry drift, flicker,
unmotivated camera shake, abrupt cut
```

If no negative field exists, convert essential constraints to positive statements:

```text
The label remains fixed and legible. The camera stays stabilized. The face
remains identity-consistent throughout.
```

## Known Provider Patterns

These notes summarize official or first-party material reviewed on 2026-07-21. Verify current documentation before relying on exact limits.

### Runway Gen-4.5

Runway's official Image to Video guide states that the image defines composition, subject matter, lighting, and style, while the prompt should focus almost exclusively on motion, camera work, and temporal progression. It recommends simple direct language, starting with critical motion, and adding detail through iteration. The input image acts as the first frame; source artifacts may intensify in video.

The official Gen-4.5 page documented Image to Video durations of 2-10 seconds and support for detailed camera choreography and sequenced instructions at the time reviewed.

Use for:

- prompt-led shots with clear camera and temporal direction;
- short sequential motion when the duration can support it;
- source-first composition preservation.

### Google Veo

Google's official generative AI notebook separates Image to Video prompting into:

- camera motion;
- subject animation;
- environmental animation;
- audio.

This maps directly to the motion hierarchy in this Skill. Keep camera, subject, and environment as separate decisions before compiling one prompt.

### PixVerse CLI

The official PixVerse Skill and CLI expose local or URL image input, multiple video models, duration, quality, aspect ratio, seed, count, audio, and multi-shot controls where supported. It also documents reference, transition, motion-control, asset, task, and download workflows.

Use when:

- an official CLI is available and the user accepts PixVerse cloud processing;
- the workflow needs structured task management, download, or model routing;
- multiple provider models should be accessed through one interface.

Inspect the current model table before selecting quality, duration, reference mode, or aspect ratio.

### RunComfy and inference.sh

Their public Skills provide practical model routing and CLI execution across several I2V backends. They are useful execution layers when already authorized. Treat their model recommendations and limits as provider-specific operational guidance, not universal cinematography rules.

### Camera-preset platforms

Platforms such as Higgsfield advertise large camera preset libraries. Confirm the current official API or installed tool schema before treating any public Skill's preset list as executable. A written preset catalog without a verified endpoint is reference material only.

## Settings Decisions

### Duration

- Start at `3-6s` for identity and geometry tests.
- Use `2-3s` for impact, macro detail, or loopable micro-motion.
- Use `6-8s` only when the shot needs a readable development and settle.
- Above `8-10s`, expect more drift unless the model is designed for longer clips.
- Build long sequences from approved short shots or last-frame continuation.

### Aspect ratio

Preserve the source ratio for the first test. Reframe only after confirming:

- focal subject remains protected;
- movement direction has enough edge reserve;
- label, hands, face, and action remain inside the safe area;
- the target platform actually requires a different ratio.

### Resolution and quality

Use preview quality for motion design when credits are expensive. Increase quality after the move works. Upscaling does not repair geometry or identity failure.

### Seed and count

Use a fixed seed when comparing prompt variants if supported. Generate multiple variants only when the plan is structurally sound. More samples do not compensate for an impossible source/motion combination.

### Audio

Enable generated audio only when it is part of the brief. Camera-direction testing is easier to compare without changing both motion and audio simultaneously.

### Multi-shot

Keep off for a single professional camera move unless the user explicitly wants a montage and the provider supports shot sequencing. Unrequested cuts can hide continuity failures.

## Execution Contract

Before calling a tool, record:

```yaml
provider: ""
model: ""
input_type: image-to-video
image_processing_boundary: local|uploaded|remote-url
camera_control: prompt|preset|path|start-end-frame
duration: 5
aspect_ratio: ""
quality: ""
seed: null
negative_prompt_supported: false
estimated_cost_or_credits: "unknown"
output_handling: download|remote-url|task-id
```

After calling a tool, preserve:

- request or task ID;
- exact model and parameters;
- exact prompt and reference mapping;
- output file or URL;
- generation cost when reported;
- visual review result;
- selected best version and rejected variants.

## Privacy and Cost Controls

- State when local images will be uploaded to a third party.
- Do not use confidential product designs with opaque hosted proxies without authorization.
- Do not echo access keys, tokens, or signed URLs.
- Avoid repeated generation loops without inspecting outputs.
- Use idempotency keys or stable task identifiers when the provider supports safe retries.
- Distinguish a failed task from a completed but visually unacceptable clip.

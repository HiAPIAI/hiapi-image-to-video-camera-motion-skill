# Image-to-Video Quality Control

Review the generated clip as moving photography, not as a successful API response. A technically completed task can still be unusable.

## Contents

- Review protocol
- Scoring rubric
- Failure diagnosis
- Iteration protocol
- Product and portrait gates
- Delivery record

## Review Protocol

Inspect:

1. the entire clip at normal speed;
2. the first frame against the source image;
3. the first second, where many clips jump or recompose;
4. the midpoint, where geometry drift often begins;
5. the maximum camera displacement;
6. the final frame and final half-second;
7. frame sequences around any focus change, subject turn, occlusion, or camera stop;
8. the clip looped twice to expose discontinuity and jitter.

When tools permit, extract a contact sheet or representative frames. Inspect the actual pixels rather than relying on task metadata or a small thumbnail.

## Scoring Rubric

Score each category `0-3`:

- `3`: production-ready;
- `2`: usable with a minor compromise or post fix;
- `1`: visible failure that distracts from the shot;
- `0`: structurally broken or misleading.

| Category | What to inspect |
| --- | --- |
| First-frame fidelity | source composition, identity, product, lighting, crop |
| Camera intent | requested move is readable and correctly directed |
| Motion smoothness | acceleration, path stability, camera stop, jitter |
| Perspective and parallax | foreground/background behavior, horizon, verticals |
| Subject identity | face, age, hair, body proportions, wardrobe |
| Anatomy and contact | hands, feet, gait, object interaction, ground contact |
| Product geometry | silhouette, proportions, seams, ports, label, typography |
| Material continuity | metal, glass, liquid, reflection, shadow, texture |
| Temporal consistency | flicker, texture crawl, object appearance, lighting |
| Focus behavior | focal target, focus breathing, pumping, unwanted blur |
| End-frame quality | deliberate settle, readable hero frame, no late collapse |
| Brief compliance | shot function, mood, duration, platform framing |

Recommended acceptance gate:

- no `0` scores;
- identity and product geometry must be `3` when they are commercial evidence;
- camera intent, motion smoothness, and end-frame quality should be at least `2`;
- total score alone cannot override a critical identity, label, or safety failure.

## Failure Diagnosis

### Source changes immediately

Symptoms:

- the first frame jumps to a new composition;
- face or product changes before motion starts;
- crop or lighting changes at time zero.

Likely causes:

- source image artifacts;
- aspect-ratio override;
- prompt re-describes and reinterprets the image;
- model applies creative visual change.

Fix one variable:

- preserve source ratio;
- remove visual restatement;
- add a stable `0.25-0.5s` start;
- repair or upscale the source;
- use a more source-faithful model or reference mode.

### Camera move is missing

Symptoms:

- only subject or environment moves;
- output is nearly static despite a requested dolly or pan.

Likely causes:

- motion instruction is buried;
- too many competing actions;
- move has no direction or magnitude;
- the model favors subject animation.

Fix:

- lead with the camera verb;
- remove secondary actions;
- state direction, speed, and end target;
- use a camera preset or control field if available.

### Camera move is too aggressive

Symptoms:

- rapid reframing;
- perspective collapse;
- subject leaves the safe area;
- the move feels like a transition instead of a shot.

Fix:

- reduce travel or arc degrees;
- change `fast` to `slow`;
- hold source frame longer;
- replace translation with pan, tilt, or zoom;
- shorten the requested path rather than the clip duration.

### End keyframe turns the shot into a morph

Symptoms:

- the outer silhouette changes more than the viewpoint;
- a product becomes a different form while the requested camera move becomes secondary;
- the final frame is attractive, but the path reads as transformation rather than photography.

Likely causes:

- start and end keyframes differ in geometry, scale, camera height, or support surface;
- the prompt asks the model to preserve the subject while the end frame contradicts it;
- a long duration gives the model room to invent a transition between incompatible states.

Fix:

- decide whether the deliverable is camera-led or transformation-led;
- for camera-led work, regenerate a compatible end frame or remove the end-frame constraint;
- for transformation-led work, name the transformation explicitly and grade camera intent as secondary;
- protect critical logos and typography in post-production when temporal generation deforms them.

### Orbit invents geometry

Symptoms:

- changing face profile;
- product grows a new side, port, label, or handle;
- background wraps unnaturally;
- hidden limbs or surfaces morph into view.

Fix:

- reduce orbit to `10-25 degrees`;
- use a small truck or arc around the visible surface only;
- supply side/back references;
- build a turnaround or 3D asset;
- choose a locked hero move instead.

Do not solve invented geometry by adding more preservation adjectives to the same impossible 360 prompt.

### Identity drift

Symptoms:

- facial proportions, age, ethnicity, hair, expression, or wardrobe change;
- identity is stable at the start but changes near maximum displacement.

Fix:

- reduce angular change and subject rotation;
- remove simultaneous expression and camera motion;
- use identity references;
- keep focus and exposure stable;
- regenerate the source if it contains weak facial detail.

### Hands, gait, or contact fail

Symptoms:

- extra fingers or limbs;
- sliding feet;
- object floats or changes grip;
- walking lacks weight.

Fix:

- simplify body action;
- keep camera relationship constant;
- shorten the clip;
- use motion reference or performance transfer;
- crop to a safer shot size when full-body action is not essential.

### Product label or UI text deforms

Symptoms:

- changing letters;
- logo drifts;
- screen UI redraws;
- package dimensions change with camera motion.

Fix:

- reduce angle and scale change;
- shorten the shot;
- use a front-facing push or macro move;
- replace critical text in post-production;
- composite the original label or screen back onto the approved clip.

### Reflection or material failure

Symptoms:

- glass turns solid;
- metal highlight sticks to the image instead of the object;
- mirrored environment changes incoherently;
- liquid volume changes.

Fix:

- reduce travel;
- specify one restrained reflection behavior;
- keep the environment stable;
- use product references or a 3D render for exact commercial work.

### Flicker or texture crawl

Symptoms:

- surface detail changes every frame;
- foliage, fabric, skin, or grain crawls;
- lighting pulses unintentionally.

Fix:

- reduce environmental motion;
- remove style or texture overload;
- use a more stable model or higher-quality mode;
- apply temporal cleanup only after the underlying geometry is acceptable.

### Focus pumps or misses the target

Symptoms:

- focus oscillates;
- background becomes sharp unexpectedly;
- subject drifts in and out of focus.

Fix:

- request locked focus on one target;
- remove rack focus unless two planes are clearly separated;
- reduce camera travel;
- avoid combining shallow depth, tracking, and rapid subject motion.

### Final frame collapses

Symptoms:

- the shot works until the last few frames;
- camera stops abruptly;
- face or product deforms during the settle;
- the clip cuts before the result is readable.

Fix:

- ask for smooth deceleration and a stable final hold;
- shorten the motion development, not the final hold;
- trim before the collapse if the earlier frame is strong;
- use a selected strong frame as the next continuation input.

## Iteration Protocol

Change one primary variable per generation:

1. **Path**: direction, arc, or camera relationship.
2. **Magnitude**: travel distance or degrees.
3. **Speed**: very slow, slow, medium, fast.
4. **Subject action**: simplify or isolate.
5. **Environment action**: reduce or redirect.
6. **Preservation**: add one specific protected attribute.
7. **Model or control mode**: change only after prompt and source feasibility are sound.

Keep an iteration log:

| Version | Single change | Result | Keep/reject | Reason |
| --- | --- | --- | --- | --- |
| V1 | baseline small push | stable identity, weak movement | keep as fallback | safest source fidelity |
| V2 | increase travel | product side deforms | reject | exceeds source geometry |
| V3 | same travel, preset control | stable move | select | best camera intent |

Do not keep generating without watching the result. Stop after repeated evidence that the source cannot support the move.

## Product Gate

For commercial product shots, require:

- silhouette and proportions unchanged;
- logo and text correct or intentionally replaced in post;
- no new buttons, seams, ports, stones, hands, or packaging folds;
- material and reflection behavior plausible;
- shadow and support surface remain attached;
- final frame presents the intended feature clearly;
- no camera path reveals unsupported surfaces.

If any protected commercial fact changes, the clip is not approved even if it looks visually impressive.

## Portrait Gate

Require:

- face remains the same person throughout;
- eyes, mouth, ears, hairline, and skin texture remain coherent;
- expression change is intentional and restrained;
- hands and body remain anatomically plausible;
- camera angle does not reveal an invented profile;
- clothing and accessories do not mutate;
- final frame remains emotionally consistent with the brief.

## Delivery Record

Record:

```yaml
source_image: ""
provider: ""
model: ""
prompt_version: ""
duration: 0
aspect_ratio: ""
seed: null
task_id: ""
output_path_or_url: ""
scores: {}
critical_failures: []
selected: false
review_notes: ""
```

State what was actually inspected. For example: full-speed playback, first/middle/final frames, contact sheet, or frame-by-frame review around the camera stop.

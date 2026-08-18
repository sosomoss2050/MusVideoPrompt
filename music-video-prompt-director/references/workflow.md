# Music-video planning workflow

## Contents

1. Input contract
2. Song segmentation
3. Coverage allocation
4. Performance modes
5. Prompt construction
6. Review and regeneration

## 1. Input contract

Use available facts before inference:

| Input | Preferred source | Fallback |
|---|---|---|
| Duration | audio metadata | user statement |
| Lyrics timing | word/line transcription | untimed lyrics |
| Musical sections | audio analysis | lyric structure |
| BPM and energy | audio analysis | explicit estimate |
| Character identity | reference image analysis | written identity block |
| Visual DNA | reference analysis | user creative direction |
| Model capability | current official docs | conservative single-shot plan |

User creative direction overrides inferred aesthetics but does not override physical feasibility or explicit model constraints.

## 2. Song segmentation

Default to one generated clip per 10–15 seconds.

1. Identify phrases, verses, choruses, breaks, drops, solos, and outro.
2. Start with small phrase units around five seconds when transcription is detailed.
3. Combine neighboring units into 10–15 second sections.
4. Prefer a musical boundary over an exact equal duration.
5. Absorb a short final tail into the preceding section when feasible.
6. Cover the entire duration with no gaps or overlaps.

Do not create one clip per lyric line. A model can stage multiple related shots inside a longer section, preserving continuity and reducing generation count.

## 3. Coverage allocation

Plan coverage globally to prevent local prompt decisions from converging on the same shot.

Suggested vocal rotation:

| Role | Framing | Orientation | Camera | Purpose |
|---|---|---|---|---|
| hero_performance | close/medium-close | front | subtle push-in | direct lip sync or emotional peak |
| angled_performance | medium | three-quarter | lateral track | body language and performance |
| narrative_action | medium-wide | over-shoulder | gentle follow | story progression under vocals |
| moving_performance | medium | three-quarter | controlled orbit | energetic performance |
| detail_insert | detail | profile/detail | controlled pan | tactile musical punctuation |
| performance_wide | wide | silhouette/stage | crane arc | scale and chorus release |
| reaction_closeup | extreme close | profile/detail | micro push-in | non-singing emotion |

Suggested instrumental rotation:

| Role | Framing | Camera | Purpose |
|---|---|---|---|
| environment_cutaway | wide | slow pan | establish world |
| narrative_action | medium-wide | follow | move story forward |
| detail_insert | macro/detail | rack focus | texture and rhythm |
| symbolic_cutaway | wide/oblique | tilt or drift | visual metaphor |

Avoid consecutive sections with the same opening framing or camera move. Reserve the most dynamic movement for musical peaks.

## 4. Performance modes

- `direct_lipsync`: one singer, visible mouth, front/three-quarter, stable close framing; minimize occlusion and excessive camera motion.
- `expressive_performance`: performer may sing, but prioritize pose, body movement, angle, and atmosphere over exact mouth sync.
- `non_vocal_action`: vocals may continue in the soundtrack, but the visible character does not sing or talk.
- `no_singer`: environment, object, crowd, abstract, or symbolic coverage.

A vocal section does not require a talking-head image. Use direct lip sync only where it contributes to the edit.

## 5. Prompt construction

### Image keyframe

Use this order:

`single frame + subject/action + setting + mandatory composition + lens/perspective + light/exposure + material/atmosphere + continuity + exclusions`

Keep one visible moment. Do not describe sequential actions.

### Video motion

For each internal shot use:

`time range + framing + camera behavior + primary action + physical detail + transition motivation`

Example structure:

```text
Shot 1 (0–5s): Wide low-angle establishing frame; slow crane arc as the band enters the pool of amber stage light, foreground cables producing natural parallax.
Shot 2 (5–11s): Motivated cut on the snare hit to a three-quarter medium performance; restrained lateral track, realistic cloth and hair inertia.
Shot 3 (11–15s): Tight reaction detail; micro push-in as the performer looks off-camera, focus breathes subtly and highlights retain texture.
```

## 6. Review and regeneration

Review in this order:

1. Does the visual action match the musical section?
2. Is identity and wardrobe stable where recurrence matters?
3. Does the opening composition match the coverage plan?
4. Is motion physically plausible and visually motivated?
5. Is lip sync used only in eligible shots?
6. Is the section distinct from adjacent sections?
7. Are there unrequested words, logos, panels, or UI?

Regenerate only failed sections. Keep successful outputs and document the reason for each retry.

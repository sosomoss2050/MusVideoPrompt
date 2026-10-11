# Concept & Insight (MV adaptation)

Lightweight adaptation of the Creative Director methodology (Serge Shima, github.com/smixs/creative-director-skill, CC BY 4.0) for music-video concept work. Apply this BEFORE the global visual contract, so the visual world serves a concept instead of accumulating pretty shots.

## 1. Song insight (do this first)

Distill the song's core creative tension in one sentence:

`[listener] wants X, but Y stands in the way, because Z`

Draw the tension from one of three sources, whichever the song actually carries:

- **Human tension** — what the singer/person wants vs what blocks it (most songs)
- **Cultural tension** — what the song's world says vs what it does
- **Category tension** — what this genre usually promises vs what this song delivers

Quality test: a listener hears the line and says "yes, exactly — but I've never put it that way." If the line could describe ten other songs in the genre, keep digging.

This insight sentence becomes the first field of `creative_direction` in `music-video-plan.json` (prefix it, then append the user's own direction). Every scene's `narrative_purpose` should be defensible against it.

## 2. Concept generation rules

Generate 3–5 candidate visual concepts for the MV before committing to one:

- The **first 2 concepts are warmup** (serial-order effect: later candidates are statistically more original). Keep them, but bias toward candidates 3–5.
- Each candidate = one sentence: the visual world + how the song's tension resolves (or deliberately stays unresolved) inside it.
- Prefer concepts that keep some tension unresolved. If everything resolves cleanly and happily, originality is usually weak.

Kill-your-darlings pass: for the leading candidate, argue AGAINST it once. If the argument beats the concept, go back one round.

## 3. Anti-cliché calibration

Before locking the concept, check it against MV-genre stock ideas, for example:

- rain walk / running after someone / beach freedom / car window gaze
- band performs in an empty warehouse / rooftop at dusk
- one-take lip-sync walk / breakup in an apartment
- slow-motion confetti / party that turns melancholic at the bridge

If the concept matches a stock idea without a structural twist, the concept is sub-par: either add a genuinely new variant (different mechanic, not different styling) or move to the next candidate. A stock idea with new lighting is not originality.

## 4. Emotion tiers (score the concept's emotional payload)

Anchor the target emotion using three tiers:

| Tier | Examples | Bar |
|------|----------|-----|
| 1 — generic | happy, sad, angry, excited | floor: never the concept's stated goal |
| 2 — specific | nostalgic, defiant, proud, lonely, tender | acceptable minimum |
| 3 — complex | bittersweet pride, ironic sincerity, vulnerable defiance, grief with relief | target for a strong MV concept |

Record the chosen Tier-2/3 emotion in `project.mood` (it may differ from the song's surface mood — that contrast is often the concept). During scene planning, `reaction_closeup` and `symbolic_cutaway` sections should serve the Tier-3 emotion; if the whole plan only expresses Tier-1 feelings, revisit the concept instead of rewriting prompts.

## What NOT to import

Business/campaign taxonomies, media-planning scoring, and brand-platform evaluation from the source methodology are advertising-context tools and do not apply to music-video planning. Keep only: insight sentence, warmup rule, tension test, anti-cliché check, emotion tiers.

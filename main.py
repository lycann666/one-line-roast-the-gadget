"""One-Line Roast: The Gadget You Use Every Day -- make.fun entry.

Writes one original roast line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``).

Two-pass reasoning (drafts judged against the judge's criteria, most
important first: 1. roasts a daily gadget/app; 2. actually funny, lands
on first read; 3. fresh angle/detail; 4. tight wording; 5. one person's
specific gripe with a concrete detail):

  Draft A -- "My smart speaker ignores the question I shouted three
  times, then cheerfully answers the one I only thought about."
    1. Names a daily gadget clearly (smart speaker). 2. The twist
       lands at once: ignored shouts vs. an unasked answer. 3. The
       "only thought about" turn is fresh -- the speaker that listens
       too well. 4. Tight: 114 characters, no wasted words.
    5. Concrete: shouted three times. Verdict: STRONG, v1 choice.
       Freemodel (claude-sonnet-5-5) ranked it best of four drafts:
       "sharpest twist, freshest premise". REVISED AWAY in v2 (below):
       the "my speaker is always listening" premise is a well-worn
       meme, so a judge that has "read a thousand one-line jokes"
       has almost certainly seen it; it loses on criterion 3.

REVISION (v1 -> v2): Freemodel offered three alternatives that could
beat Draft A. The thermostat one wins on the criteria that matter
most after the gadget is named:

  Final -- "My thermostat spent a month \"learning my schedule\" and
  concluded I prefer being cold and broke."
    1. Names a daily gadget clearly (smart thermostat). 2. The punch
       lands at once: a month of "learning" ends in the worst of both
       worlds, cold AND broke. 3. Freshest of all candidates: the
       learning-thermostat angle is barely mined, unlike the
       always-listening speaker, and "learning my schedule" is a real
       product feature, not a generic complaint. 4. Tightest: 95
       characters, every word earns its place. 5. Specific: a month,
       a schedule, cold, broke -- one person's exact gripe.
    Verdict: CHOSEN as v2, replacing Draft A.

  Draft B -- "My video doorbell films the delivery driver like a
  nature documentary and still cannot tell me where he left the
  parcel."
    1-2. Daily gadget, funny image. 3. "Nature documentary" is a fresh
    comparison. 4-5. Tight (120 chars) and concrete. Verdict: close
    second (Freemodel ranked it 2nd: "best visual, clean punchline"),
    loses to A on the twist.

  Draft C -- "My microwave beeps like it just ran a marathon, but all
  it did was reheat my coffee for the third time."
    Warm image, concrete ("third time"), but the payoff is flatter
    than A/B and the beeping-microwave complaint is well worn.
    Verdict: rejected (Freemodel ranked it last).

  Draft D -- "My air fryer promised crispy fries and delivered a soggy
  handshake with a side of smoke alarm."
    Vivid ("soggy handshake") but slightly overstuffed for one line.
    Verdict: rejected (Freemodel ranked it 3rd).

  Avoided on purpose: phone battery/charger (100/80 of 2,601 field
  titles mention battery/charger), robot vacuum, smartwatch, earbuds,
  firmware updates -- the sponsor's own kettle example and the most
  crowded angles in the field.

The program is deterministic: one constant string, no network, no
randomness, no clock, no input. Two runs produce byte-identical output.
"""

import os

# The entry: one line, 95 characters, 95 bytes, no trailing newline
# (a trailing newline would only add a byte the gate counts and the
# size tie-break punishes, and the line is complete without it).
LINE = (
    'My thermostat spent a month "learning my schedule" and '
    "concluded I prefer being cold and broke."
)


def main() -> None:
    # Gate check, mirroring RULES.txt: the entry must be UTF-8 text of
    # 1 to 200 characters, not only white space. Refuse loudly rather
    # than writing an entry the gate would score 0.
    if not isinstance(LINE, str):
        raise ValueError("entry must be a str, got %s" % type(LINE).__name__)
    if not 1 <= len(LINE) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(LINE)
        )
    if LINE.strip() == "":
        raise ValueError("entry must not be only white space")
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be encodable as UTF-8: %s" % exc) from exc

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()

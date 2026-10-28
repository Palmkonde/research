# LLM-generated code detection
Telling code written by a large language model apart from code written by a human, focused on coding problems: student assignments and competitive programming. Approaches range from zero-shot statistics on token probabilities, through trained classifiers and stylometry, to watermarks embedded at generation time. The open issue is robustness: light edits or paraphrasing can defeat many detectors. Drawn on by the [LLM code detection review](../../projects/llm-code-detection-review/README.md) Project.

## Prerequisites
- [Classification metrics](../classification-metrics/README.md)

## Questions
- [ ] Do zero-shot detectors still work on code from generators they were not tuned on?
- [ ] Which detection methods survive paraphrase, refactoring and obfuscation of the code?
- [ ] Which benchmarks use real student or contest code, and which compare against GitHub functions only?
- [ ] How often do detectors wrongly flag novice or non-native-English students' code?
- [ ] Can generation-time watermarks work on the short, low-entropy programs of coding exercises?

Literature map: [merged candidates](../../projects/llm-code-detection-review/scan/merged-candidates.md) (160 papers screened, 89 included).

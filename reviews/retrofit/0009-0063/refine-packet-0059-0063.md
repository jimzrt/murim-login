# Retrospective Patch Plan — Chapters 59–63

Create bounded exact-text patches; do not return complete chapters. Every `old`
string must occur exactly once in the identified current chapter. `new` must be
finished replacement prose. Combine adjacent findings when useful, never alter
unreported text, and disposition every finding.

Return exactly one JSON object with no Markdown fence:

{
  "summary": "brief patch summary",
  "patches": [
    {"chapter": 1, "finding_ids": ["R0000-01"], "old": "exact old text", "new": "exact replacement"}
  ],
  "dispositions": [
    {"finding_id": "R0000-01", "status": "applied|rejected|unresolved", "reason": "specific reason"}
  ]
}

Reject a finding only when its proposed change is not supported by the supplied
source. Leave genuinely uncertain findings unresolved. Do not intensify or
sanitize register.

## Audit rubric

# Retrospective Translation Audit Rubric

Audit accepted chapters for defects likely to survive an ordinary review. Do
not retranslate acceptable prose or optimize merely for difference.

Prioritize in this order:

1. Reversed or altered actions, negation, subjects, identities, kinship,
   quantities, causal relations, and physical direction.
2. Omitted source beats, explanatory mechanisms, pragmatic cues, ambiguity,
   jokes, and characterization.
3. Established terminology, Murim concepts, hierarchy, and address.
4. Register mismatch: intensified or sanitized profanity, euphemisms made more
   explicit, stiffness, or flattened comic timing.
5. Clear English defects that materially impede voice or meaning.

Semantic fidelity outranks polish. Preserve the source's degree of explicitness.
Do not report optional synonyms, generic praise, or whole-chapter rewrites.
Every finding must quote an exact current-English span and provide a finished,
bounded replacement. Mark a finding critical only when it changes a scene
fact, action, identity, negation, or consequence; major for meaningful lost
hierarchy, mechanism, characterization, ambiguity, or register; minor for clear
localized defects without changed meaning.

## Structured findings

```json
{
  "summary": "22 findings in chapters 59-63",
  "findings": [
    {
      "chapter": 59,
      "confidence": 0.99,
      "current": "The First Elder was a vile old monster who had lived more than sixty years with his black heart hidden.",
      "defect": "The traditional duration 갑자 is flattened into ordinary years instead of using the established term.",
      "id": "R0059-01",
      "rationale": "갑자 is the traditional sixty-year cycle and is established as “jiazi” for this block.",
      "replacement": "The First Elder was a vile old monster who had lived for more than one jiazi while concealing his black heart.",
      "severity": "minor",
      "source": "일장로는 일 갑자를 넘게 살아오며 흑심을 감춰 왔던 비열한 노괴(老怪)다."
    },
    {
      "chapter": 59,
      "confidence": 0.99,
      "current": "Sixty years. He had accumulated profound internal energy, but even that could not stop his body from aging.",
      "defect": "The established traditional unit is again replaced by an ordinary year count.",
      "id": "R0059-02",
      "rationale": "The source explicitly frames the passage in terms of one 갑자, not merely an approximate number of years.",
      "replacement": "One jiazi. He had accumulated profound internal energy, but even that could not stop his body from aging.",
      "severity": "minor",
      "source": "일 갑자의 세월. 그는 심후한 공력을 얻었지만 육신의 노화까지는 어찌할 수 없었다."
    },
    {
      "chapter": 59,
      "confidence": 0.99,
      "current": "“As the Discipline Hall Master of the Jin Family of Taiyuan, I command you. The guilty shall abolish their own martial arts and enter the Cave of Repentance…”",
      "defect": "The formal exalted family designation 대태원진가 is reduced to the ordinary family name, and 참회동 does not use its established English name.",
      "id": "R0059-03",
      "rationale": "The source deliberately uses the exalted 대태원진가 in a formal judicial declaration, while 참회동 is established as “Repentance Cave.”",
      "replacement": "“As the Discipline Hall Master of the great Jin Family of Taiyuan, I command you. The guilty shall abolish their own martial arts and enter the Repentance Cave…”",
      "severity": "minor",
      "source": "대태원진가의, 집법당주로서, 명한다. 죄인들은 스스로 무공을 전폐하고, 참회동에……."
    },
    {
      "chapter": 59,
      "confidence": 0.98,
      "current": "They were senior members of the so-called Elders’ faction.",
      "defect": "The translation turns the named Council of Elders into a generic faction, obscuring the institutional affiliation.",
      "id": "R0059-04",
      "rationale": "장로원 is the established “Council of Elders,” and 계파 identifies these figures as its faction.",
      "replacement": "They were senior members of the so-called Council of Elders faction.",
      "severity": "major",
      "source": "소위 장로원 계파에 속하던 중진들이었다."
    },
    {
      "chapter": 60,
      "confidence": 0.99,
      "current": "“Squad Leeeader!”",
      "defect": "Hyuk Mujin’s established form of address for Taekyung is replaced with a different rank.",
      "id": "R0060-01",
      "rationale": "조장 is established as “Captain” in this relationship and context.",
      "replacement": "“Caaaptain!”",
      "severity": "minor",
      "source": "“조자아앙!”"
    },
    {
      "chapter": 60,
      "confidence": 1.0,
      "current": "A Skill that dumped several times my strength into a single blow—One Flash.",
      "defect": "The named spear technique 일섬 is given the wrong established name.",
      "id": "R0060-02",
      "rationale": "일섬 is established as “One Annihilation”; the characters 一殲 specifically denote annihilation rather than a flash.",
      "replacement": "A Skill that dumped several times my strength into a single blow—One Annihilation.",
      "severity": "major",
      "source": "인벤토리를 활용한 공격과 순간적으로 몇 배의 힘을 일격에 쏟아붓는 스킬, 일섬(一殲)."
    },
    {
      "chapter": 60,
      "confidence": 0.99,
      "current": "Sword Energy surged up, loaded with sixty years of internal energy.",
      "defect": "The established traditional unit 갑자 is flattened into a year count.",
      "id": "R0060-03",
      "rationale": "The source measures the Head Elder’s accumulated internal energy in one 갑자, established as “jiazi.”",
      "replacement": "Sword Energy surged up, loaded with one jiazi of internal energy.",
      "severity": "minor",
      "source": "일 갑자의 공력을 머금은 검기가 치솟았다."
    },
    {
      "chapter": 60,
      "confidence": 1.0,
      "current": "“Naryeotagon? What a donkey of a man.”",
      "defect": "The established martial-arts idiom is romanized incorrectly.",
      "id": "R0060-04",
      "rationale": "나려타곤 is established as “Narye tagon,” preserving both the named maneuver and the accompanying donkey joke.",
      "replacement": "“Narye tagon? What a donkey of a man.”",
      "severity": "minor",
      "source": "“나려타곤? 당나귀 같은 놈이구먼.”"
    },
    {
      "chapter": 61,
      "confidence": 0.99,
      "current": "The sixty years of internal energy coiled in the Head Elder’s dantian spread through every limb and bone.",
      "defect": "The traditional unit 갑자 is replaced by an ordinary year count.",
      "id": "R0061-01",
      "rationale": "The source explicitly quantifies his internal energy as one 갑자, established as “jiazi.”",
      "replacement": "The one jiazi of internal energy coiled in the Head Elder’s dantian spread through every limb and bone.",
      "severity": "minor",
      "source": "대장로의 단전에 웅크리고 있던 일 갑자의 공력이 전신 사지백해로 뻗어 나갔다."
    },
    {
      "chapter": 61,
      "confidence": 1.0,
      "current": "This, too, was an incomplete Hand Force, but it was enough to stop Jin Taekyung’s spear.",
      "defect": "The martial-energy manifestation 수강 uses a non-established term.",
      "id": "R0061-02",
      "rationale": "수강 is established as “Palm Force,” distinct from Sword Force and generic Force.",
      "replacement": "This, too, was an incomplete Palm Force, but it was enough to stop Jin Taekyung’s spear.",
      "severity": "major",
      "source": "이 역시 불완전한 수강(手强)이었으나 진태경의 창을 멈춰 세우기에는 충분했다."
    },
    {
      "chapter": 61,
      "confidence": 1.0,
      "current": "“One Flash.”",
      "defect": "Every occurrence of Taekyung’s named technique in this chapter uses the wrong established name.",
      "id": "R0061-03",
      "rationale": "일섬 is established as “One Annihilation,” and consistent naming matters throughout the technique’s explanation and repeated use.",
      "replacement": "“One Annihilation.”",
      "severity": "major",
      "source": "“일섬.”"
    },
    {
      "chapter": 61,
      "confidence": 1.0,
      "current": "“Then going straight into the Elder Council—was that why?”",
      "defect": "The named governing body is rendered with a different English term.",
      "id": "R0061-04",
      "rationale": "장로원 is established as “Council of Elders.”",
      "replacement": "“Then going straight into the Council of Elders—was that why?”",
      "severity": "minor",
      "source": "“그렇다면 곧장 장로원에 들어간 것도?”"
    },
    {
      "chapter": 62,
      "confidence": 0.99,
      "current": "“You should've struck a vital acupoint.”",
      "defect": "The translation generalizes 사혈 and loses its explicitly lethal nature.",
      "id": "R0062-01",
      "rationale": "사혈 specifically means an acupoint whose strike can kill and is established as “lethal acupoint.”",
      "replacement": "“You should've struck a lethal acupoint.”",
      "severity": "minor",
      "source": "“사혈을 짚었어야지.”"
    },
    {
      "chapter": 62,
      "confidence": 1.0,
      "current": "*One Flash.*",
      "defect": "Taekyung’s named technique again uses the wrong established English name.",
      "id": "R0062-02",
      "rationale": "일섬 is established as “One Annihilation.”",
      "replacement": "*One Annihilation.*",
      "severity": "major",
      "source": "‘일섬.’"
    },
    {
      "chapter": 62,
      "confidence": 0.99,
      "current": "He was a sleeping dragon.\n\nIf he obtained the dragon pearl, he could roam the heavens.",
      "defect": "The narration confuses the generic epithet 잠룡 with Taekyung’s separate title Sleeping Dragon of Shanxi and omits the established image of the azure heaven.",
      "id": "R0062-03",
      "rationale": "Standalone 잠룡 is established as “Hidden Dragon,” while 창천 is “azure heaven”; the sentence deliberately develops the hidden-dragon and dragon-pearl metaphor.",
      "replacement": "He was a Hidden Dragon.\n\nIf he obtained the dragon pearl, he could roam the azure heaven.",
      "severity": "major",
      "source": "그는 잠룡이다. 여의주를 얻으면 창천을 누빌 수 있는."
    },
    {
      "chapter": 62,
      "confidence": 0.96,
      "current": "“The Sleeping Dragon of Shanxi…”\n\nWipeng gave a faint smirk.",
      "defect": "The translation turns a brief amused exhalation into a smirk, adding a facial attitude not present in the source.",
      "id": "R0062-04",
      "rationale": "피식 웃었다 indicates a brief involuntary laugh or snort, not a sustained or contemptuous smirk.",
      "replacement": "“The Sleeping Dragon of Shanxi…”\n\nWipeng gave a quiet snort.",
      "severity": "minor",
      "source": "“산서잠룡이라.”\n\n위팽은 피식 웃었다."
    },
    {
      "chapter": 62,
      "confidence": 1.0,
      "current": "The Sect Leader of Gunggwimun,[^1] Jin Chung, was one of them.",
      "defect": "The sect’s established English name is replaced by an unestablished romanization.",
      "id": "R0062-05",
      "rationale": "궁귀문 is established as “Gunggui Sect.”",
      "replacement": "The Sect Leader of the Gunggui Sect,[^1] Jin Chung, was one of them.",
      "severity": "major",
      "source": "전투에 앞서 미리 절벽 위로 올라갔던 궁귀문(弓鬼門)의 문주, 진충이 바로 그런 경우였다."
    },
    {
      "chapter": 63,
      "confidence": 1.0,
      "current": "A gleaming silver tael had come flying from somewhere.",
      "defect": "The currency unit 냥 is replaced with a different Chinese unit rather than the established rendering.",
      "id": "R0063-01",
      "rationale": "은자 is established as “silver nyang”; tael is not the designated unit for this translation.",
      "replacement": "A gleaming silver nyang had come flying from somewhere.",
      "severity": "minor",
      "source": "번쩍거리는 은자 한 냥이 어디선가 날아온 것이다."
    },
    {
      "chapter": 63,
      "confidence": 1.0,
      "current": "A second silver tael landed perfectly in the storyteller’s bowl.",
      "defect": "The second mention repeats the wrong currency unit.",
      "id": "R0063-02",
      "rationale": "The established rendering of 은자 is “silver nyang.”",
      "replacement": "A second silver nyang landed perfectly in the storyteller’s bowl.",
      "severity": "minor",
      "source": "두 번째 은자가 매담자의 대접에 정확히 안착했다."
    },
    {
      "chapter": 63,
      "confidence": 0.99,
      "current": "*The most handsome man of all time. A heaven-bestowed martial physique. A chivalrous hero who cannot stand injustice.*",
      "defect": "The named constitution 천무지체 is paraphrased as a generic physique, losing an established Murim term.",
      "id": "R0063-03",
      "rationale": "천무지체 is the named “Heavenly Martial Physique”; the source presents it as one of the rumors attached to Taekyung.",
      "replacement": "*The most handsome man of all time. Possessor of the heaven-bestowed Heavenly Martial Physique. A chivalrous hero who cannot stand injustice.*",
      "severity": "major",
      "source": "‘고금 제일의 미남에. 하늘이 내린 천무지체. 불의를 보면 참지 못하는 협객.’"
    },
    {
      "chapter": 63,
      "confidence": 0.98,
      "current": "I heard it from a gate guard of the Jin Family of Taiyuan.",
      "defect": "The translation turns affiliation with the named Gate Guard Pavilion into the generic occupation “gate guard.”",
      "id": "R0063-04",
      "rationale": "수문각 is the established “Gate Guard Pavilion,” and 무사 identifies the source as one of its martial artists.",
      "replacement": "I heard it from a martial artist of the Jin Family of Taiyuan’s Gate Guard Pavilion.",
      "severity": "minor",
      "source": "태원진가 수문각 무사한테 들은 거거든."
    },
    {
      "chapter": 63,
      "confidence": 0.97,
      "current": "- You have successfully completed **Qi Circulation**.",
      "defect": "The translation invents a proper-name technique label instead of rendering the source action with the established verbal terminology.",
      "id": "R0063-05",
      "rationale": "운기조식 is established as the action “circulate one’s qi” and is better expressed as a verb here.",
      "replacement": "- You have successfully circulated your qi.",
      "severity": "minor",
      "source": "- [운기조식]을 성공적으로 마쳤습니다."
    }
  ]
}
```

## Chapter 59

### Korean source

```text
＃59화



쉬쉬쉬쉭!

진위경과 위팽. 그리고 세 장로의 싸움은 폭풍 같았다.

평범한 무인은 눈으로 볼 수 없을 만큼 빠르고 강맹한 검격이 사방에서 부딪쳤다.

카가각.

‘막혔다.’

위팽은 판단과 동시에 몸을 뒤집었다. 이장로가 내뻗은 검이 머리카락을 아슬아슬하게 스치고 지나갔다.

이장로와 삼장로가 한 몸처럼 그를 압박해 갔다.

“이놈들!”

노호성과 함께 달려든 진위경은 일장로에 의해 가로막혔다.

“어딜 그리 급하게 가는가?”

순간 쭉 솟구친 검기가 진위경의 정수리를 향해 떨어졌다.

일도양단의 위기. 진위경은 황급히 검을 들어 막았다. 그의 검신에도 희끄무레한 검기가 서려 있었다.

쾅!

굉음과 함께 피어오른 먼지구름 속, 한 인영이 비틀거리며 물러났다. 안색이 창백해진 진위경이 피가래를 퉤 뱉었다.

‘무슨 놈의 공력이…….’

어릴 적부터 뛰어난 무공과 영약을 섭취해 온 그였지만 상대가 좋지 않았다. 일장로는 일 갑자를 넘게 살아오며 흑심을 감춰 왔던 비열한 노괴(老怪)다.

대장로와 더불어 정마대전을 온몸으로 헤쳐 지나온 산 증인인 것이다.

“염병할 늙은이 같으니라고.”

일장로가 허허 웃으며 대꾸했다.

“소가주, 체통을 지키시게.”

그러나 일장로의 속마음도 생각만큼 편치는 않았다.

파르르 떨리는 검신과 욱신거리는 손목이 그 증거였다.

‘이 정도일 줄이야.’

저잣거리 왈패들 싸움도 머릿수가 중요한데 고수들은 오죽할까. 그러나 진위경과 위팽의 실력은 생각 이상이었다.

아니, 어쩌면 늙은이의 자존심이 스스로를 과대평가했는지도 모를 일이다.

‘야속하구나. 참으로 야속해.’

일 갑자의 세월. 그는 심후한 공력을 얻었지만 육신의 노화까지는 어찌할 수 없었다.

‘십 년만 젊었다면.’

씁쓸히 자조한 일장로가 진위경에게로 걸음을 옮겼다.

그의 의제(義弟)인 이, 삼장로의 검도 더더욱 매서워졌다.

쉬쉬쉭!

“큭!”

진위경과 위팽은 서서히 밀리기 시작했다. 앞서 항산검문의 절정 고수들을 상대한 직후인지라 더더욱 그랬다.

점차 눈앞이 어지러워졌고, 몸에 잔 상처들이 늘어났다. 손발 또한 마음처럼 움직여 주지 않았다.

‘이대로는 어렵다.’

진위경의 안색이 어두워진 그때였다.

쐐애애액!

거침없이 쇄도하던 일장로의 검기가 불현듯 방향을 틀었다. 다음 순간, 번개 같은 일격이 목표를 갈라냈다.

서걱.

촤아아악.

피보라와 함께 한 사람이 비틀거렸다. 일장로의 옆구리를 겨누던 검은 산산이 부서져 형체조차 알아볼 수 없었고, 가슴에서는 피가 폭포처럼 흘러내렸다.

그의 얼굴을 확인한 일장로가 혀를 찼다.

“집법당주, 이 미련한 친구야. 그리도 죽고 싶었나?”

“일, 장로.”

집법당주의 목소리는 금방이라도 끊어질 듯했다. 그러나 그는 쓰러지지도, 말을 멈추지도 않았다.

“당신들은, 문내 법규를, 어겼소.”

“허허, 그래서?”

“대태원진가의, 집법당주로서, 명한다. 죄인들은 스스로 무공을 전폐하고, 참회동에…….”

서걱.

일장로는 검으로 대답을 대신했다. 대쪽 같은 성정에 비해 무공이 높지 않던 집법당주는 볼 수도, 피할 수도 없었던 일 검이 그의 목을 꿰뚫었다.

진위경의 눈에서 화염이 쏟아졌다.

“이노옴!”

이 순간, 분노한 것은 진위경뿐만이 아니었다. 집법당주의 죽음은 태원진가 중진들의 가슴에 불을 질렀다.

“집법당주!”

무인이기 전에 사람이다.

적지 않은 세월을 살아온 만큼 이뤄 온 것도, 지켜야 할 것도 많았다. 그래서 절정 고수의 무위가, 개죽음이 두려웠다.

그러나 집법당주의 당당한 최후는 잠시 잊고 있던 감정을 끓어오르게 만들었다.

바로 부끄러움과 분노였다.

“저 역도들을 쳐라!”

“태원진가의 기개를 보여라!”

스스로를 부끄럽게 여긴 자들이 제일 먼저 앞장서 달려들었다. 소위 장로원 계파에 속하던 중진들이었다.

그들은 배신자를 도운 자신을, 그리고 자신과 가문을 배신한 장로들을 용서할 수 없었다.

“멍청한 것들.”

서걱. 서걱. 서걱.

세 장로의 검이 한 번 번뜩일 때마다 한 명의 목숨이 스러졌다.

명백한 힘의 우위. 하지만 장로들의 주름진 얼굴은 딱딱하게 굳었다.

‘이놈들이……!’

동귀어진을 각오한 수십 명의 일류 고수가 죽음을 두려워하지 않고 사방에서 몰려들었다.

장로들은 그들의 무공이 아니라 기세에 당황했다. 그리고 그사이, 빈틈을 놓치지 않는 두 사람이 있었다.

서걱.

“크악!”

삼장로의 입에서 비명이 터져 나왔다. 부지불식간에 솟구친 위팽의 검기가 그의 옆구리를 베어 낸 것이다.

“아우야!”

수십 년을 함께한 의형제의 비명에 이장로가 흔들렸다. 아주 찰나, 그의 신경이 다른 곳으로 향했다.

그러나 그 결과는 뼈아팠다. 일시에 내뻗어진 세 개의 검이 그의 전신을 스쳤고, 황급히 물러나는 이장로를 향해 벼락 한 줄기가 쏘아졌다.

쐐애애액!

서늘한 무언가가 등을 파고든다고 느낀 순간, 이장로는 모든 것이 끝났음을 직감했다.

푹!

살을 가르고, 뼈를 잘라 낸다. 검기(劍氣)는 살아 있는 생물처럼 날뛰며 혈맥을 찢고 태웠다.

얼마 만에 느껴 보는 고통인가. 이장로는 눈앞이 새하얗게 물들었다. 그리고 이내 아무런 고통도 느낄 수 없게 되었다.

“나, 태원진가의 소가주 진위경이 이장로를 베었다!”

이장로의 가슴에서 검을 뽑아낸 진위경이 포효할 때, 멀지 않은 곳에서는 삼장로의 목이 떨어지고 있었다. 피를 뒤집어쓴 위팽이 그의 목을 들어 올렸다.

“삼장로의 목이 여기 있다!”

살아남은 이들이 잇따라 외쳤다.

“역도의 무리를 쓸어 버려라!”

“태원진가는 항산검문의 적이 아니다! 검을 거둬라!”

곳곳에서 울려 퍼지는 외침에 태원진가의 무인들이 힘을 얻었다.

수뇌부가 괴멸하다시피 한 항산검문 측은 아직 갈피를 잡지 못했으나, 이내 흑의인들을 향해 병장기를 돌렸다.

“자네 뭐 하고 있나! 태원진가 놈들이 코앞에 있는데…….”

“멍청한 소리 작작 하게. 덤비는 놈이라고는 저 시커먼 놈들밖에 없잖나!”

누군가의 말대로였다. 태원진가의 무인들은 수뇌부의 지시에 충실히 따랐고, 덕분에 항산검문의 무인들은 적이 하나 줄었음을 깨달았다.

이제 난데없이 나타난 흑의인들이야말로 공동의 적이었다.

“항산검문의 힘을 보여 줘라!”

“어디서 튀어나온 놈들인지 몰라도, 다 쓸어 버려!”

양 세력이 힘을 합치자 이제 밀리는 것은 흑의인들이었다.

그들은 혹독한 수련을 거친 정예였지만 두 장로의 죽음에는 사기가 흔들릴 수밖에 없었다. 틈을 놓치지 않고 사방에서 짓쳐 드는 칼날에 흑의인들은 하나둘씩 목숨을 잃었다.

“으아악!”

“물러서지 마라! 물러서는 놈은 죽음뿐이다!”

그 혼란 속에서도, 일장로는 묵묵히 검을 휘둘렀다.

눈에 닿고, 손이 향하는 곳 모두가 그의 적이었다.

서걱.

스물? 서른? 모르겠다. 일장로는 홀린 것처럼 가로막는 모든 것을 베어 냈다. 그중에는 한때 그를 어르신이라 부르던 이도 있었고, 약관이나 됐을 법한 어린 청년도 있었다.

‘죽고 사는 것에 나이가 무슨 상관이랴. 칼끝에 선 것이 무림인이거늘.’

수십 명의 피를 뒤집어쓴 일장로를 막아선 것은 곰 같은 덩치의 사내였다. 그의 눈빛은 모든 걸 태워 버릴 것 같았다.

“왜 그랬나?”

“부귀영화. 태원진가를 장악하고 산서 땅을 집어삼키기 위해서였지.”

한 치의 망설임도 없는 대답에 모든 이가 분노로 몸을 떨었다. 그러나 한 사람. 진위경만큼은 고개를 저었다.

“내가 원한 대답이 아니다.”

“그럼 소가주가 대답해 보시게. 내가, 내 형제들과 주공이 왜 이런 일을 벌였겠는가?”

“복수.”

진위경의 나직한 목소리가 이어졌다.

“당신이 말한 대계는 부귀영화나 일성의 패자가 되기 위한 것이 아니야. 그러기에는 이미 많은 기회가 지나갔고, 당신들은 늙었지. 그리고…….”

“그만.”

“대장로에게는 자손이 없다. 이장로, 삼장로, 그리고 당신도 마찬가지지.”

그 순간, 잔잔하던 일장로의 눈에서 시퍼런 불똥이 튀었다.

그건 오랜 세월 참아 온 분노였고, 아주 잠깐 떠올랐다 가라앉은 찌꺼기였다.

“왜 그랬나?”

일장로는 대답 대신 검을 들어 진위경을 겨눴다. 아니, 검 끝이 가리키는 건 진위경의 어깨 너머, 어딘가에 있을 한 사람이었다.

“그분께 직접 듣게.”

결국 마지막 열쇠는 대장로가 쥐고 있다.

진위경은 일장로를 향해 성큼 걸음을 내딛었다.

“그러지. 일장로, 당신을 베고 난 후에.”

“글쎄, 이렇게 여유를 부려도 되는 건가?”

“그게 무슨…….”

눈살을 찌푸리던 진위경의 얼굴이 딱딱하게 굳었다.

‘태경이!’

눈에 넣어도 아프지 않을 막냇동생이 대장로를 막고 있다.

잠시 잊고 있던 그 사실을 떠올린 순간, 전신의 피가 차갑게 식는 것 같았다.

‘더 이상 지체했다가는 돌이킬 수 없는 일이 벌어진다.’

모든 사태를 파악한 진위경의 입에서 서릿발 같은 음성이 터져 나왔다.

“위팽. 일장로를 맡아라.”

“받들겠습니다.”

“남은 분들도 힘을 보태 주시오.”

“소가주의 명을 받듭니다.”

위팽과 살아남은 중진 십여 명이 일장로를 넓게 포위했다.

“다른 이들은 나를 따라 길을 뚫어라! 대장로를 치러 간다!”

수십의 호위 병력과 함께 이동하려던 진위경은 문득 일장로를 바라보았다. 그는 최후가 다가왔음에도 어떤 동요도 보이지 않았다. 오히려 후련해 보이기까지 했다.

“일장로.”

“할 말이 남았나?”

진위경은 한마디를 툭 던졌다.

“태원진가 소가주의 권한으로 당신을 파문한다.”

“허허, 허허허!”

일장로의 웃음소리를 뒤로하고 진위경은 전장을 향해 질주했다.

수십의 흑의인들이 그를 저지하려 했으나 전세는 이미 기운 지 오래. 그들은 사방에서 몰려든 무인들에 의해 난자당해 죽었다.

“길을 뚫어라!”

“소가주님이시다! 막아서는 놈들은 모조리 죽여라!”

촌각에 불과한 시간. 그러나 진위경에게는 억겁과도 같은 시간이 흘렀다.

‘태경아, 부디, 부디…….’

차마 죽음이라는 단어는 생각조차 할 수 없었다.

두방망이질 치는 가슴을 끌어안고 얼마나 달렸을까, 이내 목적지에 도착한 그의 눈이 부릅떠졌다.

‘이게 무슨…….’

그만큼 눈앞에 벌어진 광경은 충격 그 자체였다.



* * *



레이드(Raid).

불과 수십 년 전까지만 해도 게임에서나 통용되던 단어다.

그러나 마왕의 등장과 대격변이 시작되자 레이드는 헌터들의 상징으로 자리매김했다.

그렇게 되기까지의 과정엔 수많은 실전과 희생이 있었고, 그걸 기반 삼아 마침내 오늘날의 레이드 방식이 정립되었다.

‘탱커, 딜러, 힐러.’

탱커는 막고, 딜러는 때리고, 힐러는 치료한다.

간단해 보이지만 정식 헌터가 되기 위해서는 엄청난 분량의 레이드 교본을 학습하고 실전 경험을 통해 검증받아야 한다.

‘헌터 훈련소…… 정말 지옥 같은 시간이었지.’

하지만 그 시간들을 견딘 덕분에 나는 헌터로 거듭났고, 7년 차 베테랑이 된 지금은 어떤 상황에서도 그에 맞는 포지션과 대응책을 떠올릴 수 있다.

그리고 지금.

“야, 흙 뿌려! 계속 뿌려!”

그동안 배운 모든 것들이 쥐뿔도 쓸모없다는 사실을 깨달았다.

탱커? 힐러?

씨바…….

근접 딜러 열 명으로 레이드를 생각한 내가 병신이다.
```

### Current accepted English

```markdown
# Chapter 59

Shh-shh-shhk!

The fight between Jin Wikyung, Wipeng, and the three Elders was like a storm.

Sword strikes crashed together from every direction, too fast and fierce for an ordinary martial artist to follow.

Krshhk.

*Blocked.*

The instant he judged it, Wipeng flipped his body. The Second Elder’s thrusting sword grazed past his hair.

The Second and Third Elders pressed him as if they were a single body.

“You bastards!”

Jin Wikyung charged with a roar, only to have the First Elder cut him off.

“Where are you rushing off to?”

Sword Energy surged straight up, then dropped toward the crown of Jin Wikyung’s head.

A single stroke could split him in two. Jin Wikyung hastily raised his sword to block. A pale Sword Energy wreathed his blade as well.

Boom!

In the dust cloud that rose with the thunderous impact, a figure staggered back. Jin Wikyung’s face had gone pale. He spat a wad of bloody phlegm.

*What the hell kind of internal energy…*

He had trained in exceptional martial arts and taken elixirs since he was a child, but this was a bad matchup. The First Elder was a vile old monster who had lived more than sixty years with his black heart hidden.

Together with the Head Elder, he was a living witness who had fought his way through the Great Faction War.

“You damn old bastard.”

The First Elder answered with a hearty laugh.

“Lesser Family Head, mind your dignity.”

But the First Elder was not nearly as comfortable as he looked.

His trembling blade and throbbing wrist were proof enough.

*To think they were this strong.*

Even a street brawl came down to numbers. With masters, it mattered all the more. Yet Jin Wikyung and Wipeng were better than he had expected.

Or perhaps an old man’s pride had made him overrate himself.

*How cruel. Truly cruel.*

Sixty years. He had accumulated profound internal energy, but even that could not stop his body from aging.

*If only I were ten years younger.*

After a bitter jab at himself, the First Elder stepped toward Jin Wikyung.

The swords of his sworn younger brothers, the Second and Third Elders, grew even fiercer.

Shh-shh-shhk!

“Urgh!”

Jin Wikyung and Wipeng began to be pushed back. They had just fought the Peak masters of the Mount Heng Sword Sect, and that made it worse.

Their vision swam. Small wounds multiplied across their bodies. Their hands and feet no longer moved as they wanted.

*We can’t keep this up.*

Jin Wikyung’s face darkened.

Fwoooosh!

The First Elder’s Sword Energy had been driving in without pause when it suddenly changed course. In the next instant, a strike like lightning split its target.

Shhk.

Fwaaah!

A man staggered in a spray of blood. The sword that had been aimed at the First Elder’s side had shattered beyond recognition, and blood poured from his chest like a waterfall.

The First Elder confirmed his face and clicked his tongue.

“Discipline Hall Master, you foolish friend. Did you want to die that badly?”

“F-First Elder…”

The Discipline Hall Master’s voice sounded ready to break. He neither fell nor stopped talking.

“You have… violated the family’s laws.”

“Heh heh. And?”

“As the Discipline Hall Master of the Jin Family of Taiyuan, I command you. The guilty shall abolish their own martial arts and enter the Cave of Repentance…”

Shhk.

The First Elder answered with his sword. The Discipline Hall Master’s nature was straight as a bamboo stalk, but his martial arts were not high. He could neither see nor dodge the stroke that pierced his throat.

Fire poured from Jin Wikyung’s eyes.

“You bastard!”

Jin Wikyung was not the only one enraged. The Discipline Hall Master’s death set fire to the hearts of the Jin Family of Taiyuan’s senior members.

“Discipline Hall Master!”

Before they were martial artists, they were human.

They had lived long enough to have much they had built, and much they had to protect. That was why they had feared it: a Peak master’s prowess, thrown away on a dog’s death.

But the Discipline Hall Master’s dignified end brought the feelings they had set aside boiling back.

Shame, and anger.

“Strike down those rebels!”

“Show them the spirit of the Jin Family of Taiyuan!”

The ones who felt ashamed of themselves were the first to charge. They were senior members of the so-called Elders’ faction.

They could not forgive themselves for aiding the traitors. Nor could they forgive the Elders who had betrayed them and the family.

“Fools.”

Shhk. Shhk. Shhk.

Every time the three Elders’ swords flashed, another life went out.

The gap in strength was obvious. Even so, the Elders’ wrinkled faces had gone stiff.

*These bastards…!*

Dozens of First Rate masters, resolved to take their enemies with them, came on from every side without fear of death.

What rattled the Elders was not their opponents’ martial arts, but their momentum.

And in that gap, two men did not miss the opening.

Shhk.

“Gah!”

A scream tore from the Third Elder’s mouth. Before he knew it, Wipeng’s Sword Energy had surged up and cut across his side.

“Little brother!”

The Second Elder wavered at the cry of the sworn brother he had spent decades with. For the briefest instant, his attention went elsewhere.

It cost him dearly.

Three swords thrust out at once and skimmed his whole body. As the Second Elder scrambled back, a bolt of lightning shot toward him.

Fwoooosh!

The instant he felt something cold drive into his back, the Second Elder knew it was over.

Thuk!

It split flesh and severed bone. The Sword Energy ran wild like a living thing, tearing through his blood vessels and burning them.

How long had it been since he had felt pain like this?

The Second Elder’s vision went white. Soon he could not feel any pain at all.

“I, Jin Wikyung, Lesser Family Head of the Jin Family of Taiyuan, have cut down the Second Elder!”

As Jin Wikyung ripped his sword from the Second Elder’s chest and roared, the Third Elder’s head was falling not far away. Wipeng, soaked in blood, lifted it high.

“The Third Elder’s head is here!”

The survivors shouted one after another.

“Wipe out the rebels!”

“The Jin Family of Taiyuan is not the enemy of the Mount Heng Sword Sect! Lower your swords!”

The cries ringing from every direction put strength into the Jin Family’s martial artists.

Mount Heng’s command had been all but wiped out, and they still had not found their bearings. Before long, though, they turned their weapons on the black-clad men.

“What are you doing? Those Jin Family bastards are right in front of us—”

“Cut the stupid talk. The only ones coming at us are those black bastards!”

He was right. The Jin Family’s martial artists were following their command’s orders to the letter, and Mount Heng’s people realized one of their enemies had dropped away.

The black-clad men who had appeared out of nowhere were now the common enemy.

“Show them the strength of the Mount Heng Sword Sect!”

“I don’t know where you crawled out of, but we’ll wipe every last one of you out!”

Once the two forces joined up, it was the black-clad men who started to give ground.

They were elites hardened by brutal training, but the deaths of the two Elders were bound to shake their morale. Blades crashed in from every direction, wasting no opening, and the black-clad men began to die one after another.

“Aaargh!”

“Don’t fall back! Anyone who falls back dies!”

Even in that chaos, the First Elder swung his sword without a word.

Everything his eyes fell on, everything his hands reached toward, was an enemy.

Shhk.

Twenty? Thirty? He didn’t know. Like a man possessed, the First Elder cut down everything in his way. Among them were people who had once called him Elder, and young men who looked barely twenty.

*What does age matter to living and dying? Anyone who stands at the point of a sword is a person of Murim.*

What blocked the First Elder, drenched in the blood of dozens, was a man built like a bear. His eyes looked ready to burn everything to ash.

“Why did you do it?”

“Wealth and glory. To take the Jin Family of Taiyuan and swallow Shanxi whole.”

The answer came without a hint of hesitation, and everyone trembled with rage.

Everyone except one. Jin Wikyung shook his head.

“That isn’t the answer I wanted.”

“Then you answer, Lesser Family Head. Why would I, my brothers, and our lord do a thing like this?”

“Revenge.”

Jin Wikyung’s quiet voice went on.

“The grand plan you talked about wasn’t for wealth and glory, or to become the ruler of a single province. Too many chances for that have already passed, and you’re all old. And…”

“Enough.”

“The Head Elder has no descendants. Neither do the Second Elder, the Third Elder, or you.”

In that instant, a livid spark leapt from the First Elder’s still eyes.

It was anger he had held down for a very long time—dregs that rose for the briefest moment, then sank again.

“Why did you do it?”

Instead of answering, the First Elder raised his sword and pointed it at Jin Wikyung.

No—the tip pointed past Jin Wikyung’s shoulder, toward someone who would be standing somewhere beyond him.

“Hear it from him yourself.”

In the end, the last key was in the Head Elder’s hands.

Jin Wikyung took a long stride toward the First Elder.

“I will. After I cut you down.”

“Well? Can you really afford to take it this easy?”

“What do you—”

Jin Wikyung’s frown went rigid.

*Taekyung!*

His youngest brother, the apple of his eye, was standing in the Head Elder’s way.

The instant he remembered what he had let slip, it felt as if every drop of blood in him ran cold.

*If I delay any longer, something irreversible will happen.*

Once he grasped the whole situation, a voice like frost burst from Jin Wikyung’s mouth.

“Wipeng. Take the First Elder.”

“I obey.”

“The rest of you, lend him your strength.”

“We follow the Lesser Family Head’s command.”

Wipeng and some ten surviving senior members spread into a wide ring around the First Elder.

“Everyone else, follow me and break through! We’re going after the Head Elder!”

Jin Wikyung was about to move with several dozen guards when he glanced at the First Elder. Even with his end closing in, the man showed no agitation. If anything, he looked unburdened.

“First Elder.”

“Do you have something left to say?”

Jin Wikyung tossed out a single line.

“By the authority of the Lesser Family Head of the Jin Family of Taiyuan, I expel you from the family.”

“Heh heh. Heh heh heh!”

Leaving the First Elder’s laughter behind him, Jin Wikyung sprinted for the battlefield.

Dozens of black-clad men tried to stop him, but the fight had long since turned. Martial artists poured in from every side and hacked them apart.

“Open a path!”

“It’s the Lesser Family Head! Kill anyone who gets in his way!”

It was only a moment. For Jin Wikyung, an eternity passed.

*Taekyung. Please, please…*

He could not even let himself think the word *death*.

How long had he run with his pounding chest clutched in his arms? When he finally reached his destination, his eyes flew wide.

*What is this…*

The scene in front of him was shock itself.

* * *

Raid.

Until a few decades ago, it was a word that only meant anything in games.

But after the Demon King appeared and the Great Cataclysm began, raids became the symbol of Hunters.

Getting there had taken countless real battles and countless sacrifices. On that foundation, the raid methods used today had finally been set down.

*Tank, damage dealer, healer.*

The tank blocks. The damage dealer hits. The healer heals.

It sounded simple, but to become a proper Hunter you had to study a mountain of raid manuals and prove yourself in actual combat.

*Hunter training camp… that was a living hell.*

But because I endured it, I came out a Hunter. Now, as a seven-year veteran, I can pull the right position and the right response for any situation.

And right now—

“Hey, throw dirt! Keep throwing it!”

I realized that everything I’d learned wasn’t worth shit.

Tank? Healer?

Fuck…

I was a fucking moron for thinking ten melee damage dealers counted as a raid.
```
## Chapter 60

### Korean source

```text
＃60화



대장로는 생각했다.

‘내가 너무 오래 살았나?’

그가 기억하는 무림은, 무림인은 이렇지 않았다.

합공은 수치요, 암습은 지탄을 받았으며 등에 흙이라도 묻으면 비웃음의 대상이 되었다.

그런데…….

“흙 뿌려! 계속 뿌려!”

팔십 평생 이런 경우는 처음이다. 뭐? 흙을 뿌려?

수십 년 전 원수처럼 싸웠던 마교도들조차 쓰지 않았던, 저열하고 비겁한 수법이다.

‘저놈이 정녕 무인이란 말인가.’

더욱 기가 막히는 것은 수하라는 놈들의 반응이었다.

“조장 명령이다! 흙 뿌려!”

“거리 벌려! 검기 조심해!”

군말 없이 명령을 따라 움직이는 놈들을 보니 현기증이 돌았다.

‘이런 쳐 죽일 놈들을 보았나.’

이놈들은 무인이 아니다. 아니, 사람도 아니다.

이건 무인에 대한 모욕이자 동시에 일평생을 검에 바친 대장로 자신에 대한 모욕이기도 했다.

“감히…….”

그가 검을 뽑아 들었을 때였다.

“이 멍청한 놈들!”

반 박자 빨리 터져 나온 준엄한 외침. 벌에라도 쏘였는지 얼굴이 퉁퉁 부은 청년이 사나운 눈빛으로 주위를 쓸어 보았다.

“지금 뭣들 하자는 거야!”

행색은 우습지만 기개는 제법이다. 맞다, 무인이라면 응당 저래야 한다.

‘그래도 멀쩡한 놈이 하나는 있군.’

대장로가 내심 고개를 끄덕이던 그 순간이었다.

“흙으로 되겠냐? 돌도 섞어!”

“……!”

대장로는 벼락 맞은 사람처럼 몸을 부르르 떨었다.

난생처음 느껴 보는 치욕에 검을 휘두르는 것도 잊은 그의 얼굴로 흙덩이가 날아왔다.

철퍽!

단언컨대, 팔십 평생을 돌이켜 봐도 가장 굴욕적이고 무방비하게 허용한 공격이다. 후두둑 쏟아지는 흙 사이로 야무지게 섞어 놓은 짱돌 하나가 보였다.

“으허, 으허허허.”

실성한 사람처럼 웃던 대장로의 웃음이 뚝 끊겼다.

그와 동시에.

츠츠츠.

일 갑자의 공력을 머금은 검기가 치솟았다.

“각오는 되었느냐?”

그 모습을 지켜본 진태경이 중얼거렸다.

“돌은 섞지 말지…….”

말이 떨어지기도 전에 대장로가 사자처럼 달려들었다. 십여 명의 양 떼들은 비명을 지르며 도망쳤다.

“산개! 산개해라!”

“흙도 뿌려!”

물론 그 와중에도 흙을 뿌리는 것은 잊지 않았다.



* * *



후우웅-

대장로의 검 끝에서 거센 돌풍이 불었다. 모래, 흙, 돌. 그게 뭐든 간에 상관없었다. 압도적인 힘 앞에 부서지고 흩어질 뿐이다.

‘저 인간을 어떻게 상대하나.’

정면 승부?

말이 좋아서 근접 딜러지, 정찰조를 대장로에게 붙여 놨다간 눈 깜짝할 사이에 무더기로 죽어 나갈 거다.

그래도 정든 놈들인데 무의미한 개죽음을 당하게 만들 수는 없지.

“조자아앙!”

저놈은 죽어도 싸지만.

‘그러니까 돌을 왜 섞어, 돌을.’

대장로의 1차 목표는 혁무진이었다. 용감무쌍하게 선방을 날렸으니 당연한 결과다. 나는 깊은 한숨을 내쉬며 혁무진에게로 몸을 날렸다.

쉬이이익!

대장로의 가슴을 향해 힘껏 내지른 창.

동시에 혁무진의 등을 베려던 검기가 방향을 틀었다.

슁.

저 망할 놈의 검기.

매끈하게 잘려 나간 창두를 확인할 시간도 없다. 나는 공포에 질린 혁무진의 목덜미를 잡아챘다.

“튀어!”

그러나 쉽게 포기할 대장로가 아니었다.

쐐애애액!

파공성과 함께 옆구리가 뜨거워졌다. 단순히 스친 것만으로도 살이 한 움큼 뜯겨 나가며 피가 튄다.

‘큭.’

더럽게 아프네. 하지만 지금 상황에서는 비명도 사치다.

‘시간을 벌어야 해.’

나는 혁무진을 옆으로 밀치며 돌아섰다. 그런 내 행동에 대장로가 눈썹을 치켜올렸다.

“네가?”

단 두 글자였지만 의미는 정확하게 전달받았다. 너 따위가 날 막을 수 있겠냐. 그런 뜻이겠지.

나는 태연한 척 대답했다.

“어, 내가.”

“목숨이 아깝지 않으냐?”

“더럽게 아깝다고 하면, 살려 줄래?”

“허허, 그놈 참. 어린 녀석이 혀가 짧구나.”

“할배, 고추는 서요?”

츠츠츠.

우뚝 섰다.

크고 아름다운 검기가.

“……정정하시네.”

창을 잡은 손이 땀으로 축축해졌다.

‘이거, 남은 밑천까지 탈탈 털어야 살 수 있겠는데.’

나는 대장로가 아는 것보다 훨씬 비밀이 많은 놈이다.

인벤토리를 활용한 공격과 순간적으로 몇 배의 힘을 일격에 쏟아붓는 스킬, 일섬(一殲).

‘이럴 때를 대비해서 한 번도 안 보여 줬지.’

이런 걸 무림에서는 최후 절초라고 하던가?

대장로, 아니 무림의 누구도 예상하지 못할 수법인 것은 확실하다. 거기에 더해서…….

“포위 대형, 펼쳐.”

스스슥.

혁무진과 정찰조원들이 사방에서 조여 오기 시작한다.

대장로라는 대어를 잡기에는 허술한 그물. 그러나 날카로운 작살이 있다면 해볼 만한 싸움이다.

“고작 이 정도로 되겠느냐?”

“노인네 하나 잡는데 이 정도면 충분하지.”

대장로가 재미있다는 듯 웃었다.

“겁 없는 철부지로군. 매를 맞아야 정신을 차리는.”

그러나 그의 바람은 이뤄지지 못했다. 다음 순간 불쑥 끼어든 목소리 때문이었다.

“내가 잘못 들은 것 같은데, 다시 한번 말해 보시오.”

산악 같은 덩치에 부리부리한 눈매. 두툼한 입술 사이로 흘러나오는 음성은 얼음장처럼 차가웠다.

“우리 애를 건드리겠다고?”

후우웅.

검신을 타고 들불처럼 일어난 검기가 대장로를 겨눈다.

구세주처럼 나타난 진위경이 나를 향해 눈을 찡긋했다.

“어떠냐, 형 멋있지?”

참, 여전하다.



* * *



한 달 만에 보는 얼굴.

진위경의 등장에 굳어 있던 몸이 스르륵 녹아내렸다.

반갑고, 그저 반가웠다.

‘다행이야, 살아 있어서.’

상당한 격전을 치렀는지 진위경은 피투성이였다. 찢어진 옷 사이로 크고 작은 상처들이 보였다.

하지만 그걸로 됐다. 살아 있다는 사실이 중요한 거니까.

‘하고 싶은 말은 많지만 대화는 나중으로.’

해후는 이 전쟁이 끝난 후에 나눠도 늦지 않다. 진위경도 같은 생각인지 정면을 향해 시선을 돌렸다.

우리의 시선 끝, 대장로가 천천히 입을 뗐다.

“네가 여기까지 왔다는 건…….”

진위경의 서늘한 목소리가 말꼬리를 잘랐다.

“이, 삼장로는 죽었소. 일장로도 시간문제고.”

희소식이다. 진위경이 이렇게 언급했다면 이 전쟁에서 장로들의 비중이 작지 않았다는 의미고, 대장로의 손발이 잘려 나갔다는 뜻이니까.

“두 사람은…… 편안하게 갔느냐?”

“아마도.”

대장로는 선선히 고개를 끄덕였다.

“무인답게 싸우다 죽겠다고 입버릇처럼 말했었지. 소원대로 됐으니 다행이야.”

“무인이 아닌 배신자로 기억될 거요. 당신들 모두.”

“역사는 승자가 쓰는 법이지.”

대장로가 우리 쪽으로 검을 겨눴다. 나와 진위경을 포함한 수십 명 앞에서도 그는 당당했다.

“이제 승자를 가려 보자꾸나.”

진위경은 할 말이 있는 듯 잠시 입을 열었지만, 이내 굳게 다물었다. 다음 순간 그의 입에서 우렁찬 포효가 터져 나왔다.

“역도를 처단하라!”

스릉. 스르릉.

수십 개의 병장기가 일제히 한 사람을 향해 뽑혀 나오는 장면은, 일대 장관이었다.

“존명!”

거대한 함성과 함께 수십의 무인이 한 덩어리가 되어 돌격한다. 물론 나도 예외는 아니었다. 창을 움켜쥔 손아귀에는 힘이 들어갔고, 가슴은 터질 것 같았다.

‘이길 수 있다. 아니, 무조건 이긴다.’

대형 따위는 찾아볼 수 없는 전면전. 그러나 우리에게는 절정 고수인 진위경이 있고 그를 따르는 수십의 무인이 있다.

‘그리고 내가 있지.’

대장로는 자신의 무력을 너무 맹신했다. 최소한의 호위도 남기지 않고 모조리 전선에 투입했고, 그 결과 지금 흑의인들은 태원진가와 항산검문의 합공에 발목이 잡혀 버렸다.

대장로는…… 바로 이 자리에서 죽는다.

‘끝이다!’

그러나 내 확신이 산산이 부서지기까지는 그리 오랜 시간이 걸리지 않았다.

슈슈슈슉!

난데없이 쏘아진 수십 개의 점. 공기를 가르며 날아든 그것들은 모두의 생각 이상으로 빠르고 강했다.

“탄지공(彈指公)이다!”

진위경의 외침. 내게 탄지공이 뭔지 생각할 시간 따위는 주어지지 않았다.

퍼버버벅!

카앙!

“크아아악!”

“커흑!”

누군가는 쓰러지고, 누군가는 튕겨 냈다. 그러나 쓰러진 자들은 다시 일어나지 못했다.

‘저거 설마…….’

짧은 순간이었지만 똑똑히 볼 수 있었다. 그들의 심장 어림과 얼굴에 산탄처럼 빼곡히 박히는 작은 점들을.

‘돌?’

지금은 파편에 가깝지만, 그건 분명히 돌이었다. 대장로의 공력을 견디지 못한 돌이 박살 남과 동시에 우리를 향해 쏘아진 것이다.

‘이게 가능해?’

소름이 돋았지만 아직 끝난 게 아니었다.

대장로가 이쪽으로 손을 내뻗고 있었다.

“산개!”

이번에는 나와 진위경이 동시에 외쳤다. 안 그래도 잔뜩 경계 중이던 무인들이 순식간에 뿔뿔이 흩어졌다.

‘됐어. 이번에는 안 늦었……!’

그러나 안도감도 잠시.

쐐애애액!

탄지공 대신 쏘아진 것은 대장로였다. 무인들 사이로 파고든 그는 맹수처럼 날뛰었다.

서걱, 서걱, 서걱.

“크르륵.”

“헉.”

어둠 사이로 검이 번뜩일 때마다 하나의 목숨이 스러진다. 대장로가 휩쓸고 지나간 자리마다 숨죽인 비명과 시체만이 남겨졌다.

“대장로-!”

분노한 진위경이 달려들었을 때, 대장로는 다섯 명을 해치운 후였다. 그런데도 피 한 방울 묻지 않은 흰 얼굴은 귀신을 연상시켰다.

“왔느냐?”

“감히!”

“다들 서투르구나. 평화가 너무 길었던 모양이야.”

단 하나, 부정할 수 없는 사실이 있다. 대장로가 정마대전의 영웅이라는 것.

그는 이 자리의 그 누구보다 강하고, 노련한 사람이다. 수많은 실전을 통해 완성된 절정의 무인인 것이다.

쉬이이익!

진위경이 뽑아낸 검기가 허공을 찔렀다. 단순히 고개를 까딱이는 것만으로 공격을 피해 낸 대장로는 손가락을 튕겼다.

목표는 바로 나였다.

쉭!

아무것도 보이지 않는다. 하지만 본능적으로 알아챘다.

‘공력.’

저건 말 그대로 기(氣)의 덩어리, 그 자체다. 나는 지체하지 않고 몸을 굴렸다.

푸슉.

“컥.”

창으로 막았어야 했는데, 거기까지 생각하기에는 너무나 생소한 공격이었다. 그 대가는 이름 모를 아군의 죽음.

기분이 더러웠다.

“나려타곤? 당나귀 같은 놈이구먼.”

나는 입 안에 들어간 흙을 퉤 뱉었다.

“살고 싶으면 뭔 짓을 못 해.”

“하하, 벌써 무림인이 다 됐구나.”

캉! 카카캉!

저런 괴물을 봤나. 말하는 와중에도 진위경의 검기를 모조리 튕겨 내는 대장로의 모습에 기가 막힐 따름이다.

퍽!

그 순간에도 공력을 실어 휘두른 주먹이 그의 등을 노리고 달려든 무인의 머리통을 박살 냈다.

“아직 이십 년은 이르다.”

전투를 시작한 지 얼마 되지도 않았는데, 차 한 잔 마실 시간조차 지나지 않았는데 벌써 스물에 가까운 무인들이 싸늘한 시신으로 변했다.

“이놈!”

쉬이익!

어딘가 눈에 익은 중년 무사는 검기에 목이 달아났고.

“죽어엇!”

펑!

스무 살이나 됐을 법한 앳된 얼굴의 청년은 가슴이 움푹 꺼져 무릎을 꿇었다. NPC가 아닌 진짜 사람들.

태원진가에서 한 번쯤 마주치고, 악수를 나눴던 그 얼굴들이다. 그 사실에 나는 이를 악물었다.

‘미안합니다.’

막을 힘이 없어서 미안한 것이 아니다. 그들을 죽음을 이용했기 때문에 하는 사과였다.

쉭!

대장로의 탄지공에 또 한 사람이 실 끊긴 인형처럼 쓰러진다. 그러나 금방이라도 뒤로 넘어갈 것 같던 시체는 오뚝이처럼 일어났다. 이어 대장로에게로 고꾸라졌다.

“허튼수작!”

쾅! 펑!

대장로는 한 손으로는 진위경의 검을, 다른 한 손으로는 시신을 향해 장력을 날렸다.

그리고…….

‘지금.’

훨훨 날아가는 시신의 뒤로 모습을 숨겼던 내가 창을 뻗었다.

“일섬.”

다음 순간.

고오오옹.

귀가 먹먹해지는 굉음이 있었다.
```

### Current accepted English

```markdown
# Chapter 60

The Head Elder thought,

*Have I lived too long?*

The Murim he remembered was not like this. Martial artists were not like this.

Ganging up was shameful, ambushes were condemned, and anyone who got so much as dirt on their back became a laughingstock.

And yet…

“Throw dirt! Keep throwing it!”

In eighty years of life, he had never seen anything like this. What? Throw dirt?

It was a cheap, cowardly trick even the Demonic Cultists he had fought like sworn enemies decades ago had never used.

*Is that bastard really a martial artist?*

What left him even more speechless was the reaction of those so-called subordinates.

“Squad Leader’s orders! Throw dirt!”

“Open the distance! Watch the Sword Energy!”

Watching them obey without a word made him dizzy.

*Have I ever seen bastards this fit to die?*

These were not martial artists.

No, they were not even human.

This was an insult to martial artists—and an insult to the Head Elder himself, who had given his whole life to the sword.

“How dare you…”

He was drawing his sword when it happened.

“You idiots!”

A stern shout burst out half a beat sooner. A young man whose face was swollen as if bees had stung him swept a fierce look around them.

“What the hell do you think you’re doing?”

He looked ridiculous, but he had real mettle. Yes. That was how a martial artist was supposed to act.

*At least there’s one decent one here.*

The Head Elder was just nodding to himself when—

“Think dirt’s going to cut it? Mix in rocks too!”

“…!”

The Head Elder shuddered like a man struck by lightning.

In a humiliation he had never felt in his life, he even forgot to swing his sword as a clod of dirt flew at his face.

Splat!

He could say this without hesitation: looking back on eighty years, he had never taken a hit so humiliating, or so completely undefended.

Through the dirt pattering down, he spotted a chunk of stone mixed in nice and solid.

“Uh-heh, uh-heh-heh-heh.”

The Head Elder laughed like a madman.

Then the laugh cut off.

At the same time—

Tssssss.

Sword Energy surged up, loaded with sixty years of internal energy.

“Are you prepared?”

Jin Taekyung watched and muttered,

“Shouldn’t have mixed in the rocks…”

The words were barely out before the Head Elder charged like a lion. The dozen or so sheep screamed and scattered.

“Scatter! Scatter!”

“Throw dirt too!”

Even while they ran, they did not forget to throw dirt.

* * *

Fwoooosh—

A fierce gale tore from the tip of the Head Elder’s sword. Sand, dirt, stones—whatever it was, it made no difference. In the face of that much power, it only shattered and scattered.

*How are we supposed to fight this guy?*

A head-on fight?

Calling us melee damage dealers was putting it nicely. Leave the reconnaissance squad on the Head Elder and they’d be dying in piles before I could blink.

I’d gotten attached to the bastards, though. I couldn’t let them die a pointless dog’s death.

“Squad Leeeader!”

That one deserved to die, sure.

*So why mix in rocks? The rocks.*

The Head Elder’s first target was Hyuk Mujin. Naturally. He’d thrown the first punch without a shred of fear.

I let out a long breath and threw myself toward him.

Shiiiiing!

I drove my spear at the Head Elder’s chest with everything I had.

At the same time, the Sword Energy about to cut through Hyuk Mujin’s back changed direction.

Shing.

That damned Sword Energy.

No time to check the spearhead, sliced off clean. I snatched terrified Hyuk by the scruff of the neck.

“Run!”

But the Head Elder was not the type to let go.

Swoooosh!

A tearing whistle through the air, and my side went hot. Even a graze ripped out a handful of flesh and sent blood spraying.

*Kh.*

It hurt like hell. In this situation, though, even a scream was a luxury.

*I need to buy time.*

I shoved Hyuk aside and turned. The Head Elder raised an eyebrow at that.

“You?”

Only one word, but the meaning came through perfectly. *The likes of you, stopping me?* That was the idea.

I answered like I was calm.

“Yeah. Me.”

“Don’t you value your life?”

“If I say it’s damn precious, will you let me live?”

“Heh heh. Look at this one. Young as you are, you’ve got quite a mouth.”

“Gramps, does your pepper still stand?”

Tssssss.

It stood ramrod straight.

Large, beautiful Sword Energy.

“…You’re still going strong.”

My grip on the spear went slick with sweat.

*I’m going to have to shake out every last reserve I’ve got to survive this.*

I had a lot more secrets than the Head Elder knew.

Attacks that used my Inventory.

A Skill that dumped several times my strength into a single blow—One Flash.

*I never showed them, just in case something like this happened.*

Was this what they called a last-resort technique in Murim?

One thing was certain: neither the Head Elder nor anyone else in Murim would see it coming.

And on top of that…

“Encircling formation. Form up.”

Shff.

Hyuk Mujin and the reconnaissance squad began closing in from every side.

A flimsy net for a fish as big as the Head Elder.

But with a sharp harpoon, it was a fight we could try.

“You think this will be enough?”

“To catch one old man? This is plenty.”

The Head Elder smiled like he was entertained.

“What a fearless brat. The kind who only comes to his senses after a beating.”

But that wish of his did not come true. A voice cut in out of nowhere.

“I think I heard you wrong. Say that again.”

A mountain of a man with fierce, piercing eyes. The voice from between his thick lips was cold as ice.

“You were going to lay a hand on our boy?”

Fwoooosh.

Sword Energy climbed his blade like wildfire and pointed at the Head Elder.

Jin Wikyung, appearing like a savior, winked at me.

“Well? Big brother looks cool, doesn’t he?”

Still the same.

* * *

The first time I had seen that face in a month.

The moment Jin Wikyung appeared, the tension in my body melted away.

I was glad.

Just glad.

*Thank goodness he’s alive.*

Wikyung was covered in blood, like he’d just come through a brutal fight. Large and small wounds showed through the tears in his clothes.

But that was enough. The fact that he was alive was what mattered.

*I have a lot I want to say, but it can wait.*

A reunion after this war ended would not be too late. Wikyung seemed to think the same. He looked forward.

Where we were looking, the Head Elder slowly spoke.

“The fact that you made it this far means…”

Jin Wikyung’s chilly voice cut him off.

“The Second and Third Elders are dead. The First Elder is only a matter of time.”

Good news. If Wikyung put it that way, the Elders had been no small part of this war—and the Head Elder’s hands and feet had just been cut off.

“Did the two of them… go peacefully?”

“Probably.”

The Head Elder nodded readily.

“They were always saying they wanted to die fighting like martial artists. They got their wish, so that’s fortunate.”

“They’ll be remembered as traitors, not martial artists. Every last one of you.”

“History is written by the victors.”

The Head Elder pointed his sword at us. Even with dozens of people in front of him, including me and Jin Wikyung, he stood there utterly composed.

“Now, let’s see who the victor is.”

Jin Wikyung looked like he had something to say. His mouth opened, then shut tight.

The next moment, a thunderous roar burst from him.

“Strike down the rebels!”

Shing. Shrrring.

Dozens of weapons drawn at once, all aimed at a single man. It was quite a spectacle.

“Yes, sir!”

With a huge shout, dozens of martial artists charged as one mass. I was no exception. My grip tightened on the spear, and my chest felt ready to burst.

*We can win. No. We win, no matter what.*

A full-on brawl with no formation to speak of. But we had Jin Wikyung, a Peak master, and dozens of martial artists following him.

*And there’s me.*

The Head Elder had trusted his own strength too much. He had thrown every man into the front line without leaving even a minimal escort, and now the black-clad men were pinned down by the combined assault of the Jin Family of Taiyuan and the Mount Heng Sword Sect.

The Head Elder…

dies right here.

*It’s over!*

It did not take long for that certainty to shatter to pieces.

Shushushushush!

Dozens of tiny points shot out of nowhere. They cut through the air faster and harder than anyone had expected.

“Finger-Flicking Technique!”

Jin Wikyung’s shout. I was not given time to think about what that even was.

Pow-pow-pow-pow!

Clang!

“Aaargh!”

“Guh!”

Some went down. Others knocked the shots aside. The ones who fell did not get up again.

*Don’t tell me…*

It had lasted only an instant, but I saw it clearly. Tiny points packed into the area around their hearts and across their faces like buckshot.

*Stones?*

They were closer to fragments now, but they had definitely been stones. Stones that could not take the Head Elder’s internal energy had shattered as they were fired at us.

*Is this possible?*

I got goose bumps, but it was not over.

The Head Elder was stretching a hand this way.

“Scatter!”

This time Wikyung and I shouted together. The martial artists, already wound tight, scattered in an instant.

*Good. We weren’t late this ti—*

The relief lasted only a moment.

Swoooosh!

What shot at us this time was not the Finger-Flicking Technique. It was the Head Elder. He drove in among the martial artists and went berserk like a wild beast.

Slash. Slash. Slash.

“Grrk.”

“Hhk.”

Every time a sword flashed through the dark, another life went out. Wherever the Head Elder tore through, only stifled screams and corpses were left.

“Head Elder—!”

Jin Wikyung charged in a fury. By then the Head Elder had already finished five people. And still not a drop of blood on that white face, enough to make you think of a ghost.

“You’ve come?”

“How dare you!”

“You’re all clumsy. Peace must have lasted too long.”

There was one fact you could not deny. The Head Elder was a hero of the Great Faction War.

He was stronger and more seasoned than anyone here. A Peak martial artist finished in countless real fights.

Shiiiiing!

The Sword Energy Jin Wikyung drew out stabbed through empty air. The Head Elder slipped it with nothing more than a slight tilt of his head, then flicked a finger.

The target was me.

Shhk!

I could not see a thing. Instinct knew anyway.

*Internal energy.*

That was literally a lump of qi itself. I rolled without wasting a beat.

Pshk.

“Guh.”

I should have blocked with the spear, but the attack was too unfamiliar to think that far. The price was an unnamed ally’s death.

I felt rotten.

“Naryeotagon? What a donkey of a man.”[^1]

I spat out the dirt that had gotten in my mouth.

“If you want to live, what won’t you do?”

“Haha. You’ve already become a proper man of Murim.”

Clang! Clang-clang-clang!

Had anyone ever seen a monster like that. Even while talking, he knocked aside every last bit of Jin Wikyung’s Sword Energy. I was speechless.

Thud!

Even then, a fist loaded with internal energy smashed the skull of a martial artist who’d gone for his back.

“You’re still twenty years too early.”

The fight had barely started. Not even the time to drink a cup of tea had passed, and already nearly twenty martial artists had turned into cold corpses.

“You bastard!”

Shiiiiing!

A middle-aged warrior whose face looked vaguely familiar lost his head to Sword Energy.

“Die!”

Boom!

A young man with a baby face that might have been twenty had his chest caved in and dropped to his knees.

Not NPCs. Real people.

Faces I had run into at least once at the Jin Family of Taiyuan. Faces I had shaken hands with. I gritted my teeth at that.

*I’m sorry.*

I was not apologizing because I lacked the power to stop it. I was apologizing because I had used their deaths.

Shhk!

Another person dropped to the Head Elder’s Finger-Flicking Technique like a puppet with its strings cut. But the corpse that looked about to topple backward popped up like a roly-poly toy. Then it pitched toward the Head Elder.

“Cheap trick!”

Boom! Bang!

With one hand, the Head Elder took Jin Wikyung’s sword. With the other, he sent a palm strike at the corpse.

And then…

*Now.*

I had hidden behind the corpse as it sailed through the air. I thrust my spear.

“One Flash.”

The next instant—

Goooooong.

There was a roar that stuffed the ears.

[^1]: *Naryeotagon* is a martial-arts term for dropping and rolling on the ground to evade an attack; the Head Elder’s remark also compares Taekyung to a donkey.
```
## Chapter 61

### Korean source

```text
＃61화



고오오옹.

대장로는 공기의 떨림을 느꼈다. 동시에 자신의 가슴을 향해 쏘아지는 창날이 어떤 파괴력을 지녔는지도 깨달았다.

‘이건…… 위험하다.’

살면서 몇 번 느껴 보지 못한 생명의 위협. 전신의 털이 바짝 곤두서고, 세상이 느려진다.

쉬이익!

정면에는 진태경의 창이, 등 뒤에서는 진위경의 검이 날아든다. 두 형제의 연수합격은 절묘하게 맞아떨어졌다.

그야말로 절체절명의 순간.

솨아아.

대장로의 단전에 웅크리고 있던 일 갑자의 공력이 전신 사지백해로 뻗어 나갔다. 노쇠한 근육에 활력을 불어넣고 혈맥을 깨웠다. 변화는 거기에서 그치지 않았다.

츠츠츠.

한 자(30cm) 가까이 솟구쳤던 검기가 절반으로 압축되었다.

그러나 그것은 힘의 감소가 아닌, 힘의 응축이었다. 실처럼 하늘거리던 검기는 검신 전체를 휘감으며 또 다른 검의 형태를 갖췄다.

검강(劍强).

절정이라는 벽을 넘어 위대한 영역을 개척한 초인들의 상징.

아직 불완전한 반쪽짜리에 불과했으나 그것은 분명 검강이었고, 대장로가 평생을 익혀 온 무학(武學)의 결정체였다.

서걱.

태원진가 대대로 내려져 오는 가문의 보검조차 검기를 두른 채로 잘려 나갔다. 한순간에 공력이 흩어지고 내부가 진탕된 진위경의 얼굴이 창백하게 변했다.

일 검이면 그의 목을 취할 수 있는 상황.

그러나 대장로에게는 그럴 만한 시간이 없었다.

쐐액!

대장로는 가슴 앞까지 다가온 창으로 손을 뻗었다. 그의 주름진 손 역시 눈부신 기의 빛무리에 휩싸여 있었다.

이 역시 불완전한 수강(手强)이었으나 진태경의 창을 멈춰 세우기에는 충분했다.

아니, 충분해 보였다.

콰아아아아.

창끝에서 흘러나온 와류(渦流)가 그를 집어삼키기 전까지는.



* * *



죽음 같은 정적이 내리깔렸다. 이 자리에 있는 수십, 어쩌면 전장에 선 모두가 우리를 지켜보고 있는 것 같았다.

아니, 우리가 아니다. 오직 한 사람이다.

“이게…….”

수많은 시선 끝에서, 대장로가 천천히 입을 뗐다.

“무슨 초식이지?”

내가 대답했다.

“일섬.”

말하는 것만으로도 극심한 허기가 느껴진다. 전신의 근육이 찌릿했고 체내에는 공력 한 줌 남아 있지 않았다.

하지만 딱 그 정도다. 나는 조필 때처럼 기절하지도, 꼴사납게 주저앉지도 않았다.

‘이제는 몸이 감당할 수 있다.’

나는 일섬의 부작용을 감당할 수 있을 만큼 성장했고, 내가 성장한 만큼 일섬의 위력도 강해졌다.

지금 대장로의 모습이 바로 그 증거다.

“일섬, 일섬이라.”

작게 중얼거린 그가 어깨의 혈도를 짚었다.

흐르던 피는 멈췄지만, 그뿐. 일섬이 뿜어낸 와류에 의해 흔적도 없이 갈려 나간 팔은 돌아오지 않았다.

“이 나이에 외팔이가 될 줄은 몰랐는데. 허허.”

허탈하게 웃은 대장로가 진위경을 향해 고개를 돌렸다.

“무서운 아우를 뒀구나.”

진위경이 파리한 얼굴로 되물었다.

“당신은 저 아이가 무섭소?”

“너는 어떠하냐?”

“자랑스럽소.”

한 치의 망설임도 없는 대답. 그의 창백한 안색 위로 웃음이 피어올랐다.

“금이야 옥이야 키웠는데 강철로 자랐지. 태경이는 그런 아이요.”

대장로는 그 미소를 물끄러미 바라보았다.

“너는 제법 괜찮은 인재다. 태원진가의 미래를 책임질 만한.”

“그렇소?”

“허나, 네 아우들만큼은 아니지.”

약관에 절정의 경지에 도달했다는 진무경이야 그렇다 치고, 나까지 높게 쳐 주니 황송하긴 한데…….

‘도대체 무슨 말을 하려고?’

내 생각을 읽은 듯 대장로가 말을 이었다.

“핏줄과도 나누지 않는 것. 그게 바로 권력이다. 그때가 되어도 네 아우들이 마냥 자랑스러울까?”

순식간에 장내가 싸늘하게 식었다.

지금 근거리에서 대장로와 대치하고 있는 이들은 전부 태원진가 소속. 조심스러운 시선들이 내 뺨에 달라붙었다가 슬그머니 사라진다.

‘가주? 그딴 거 할 생각도 없다. 이놈들아.’

그때였다. 진위경이 입을 뗀 것은.

“그랬구려.”

착잡함과 후련함이 묻어 나오는 목소리였다. 대장로의 눈썹이 꿈틀거린다.

“무엇을 말이냐?”

“당신이 배반한 이유. 오늘 같은 일이 일어난 이유.”

“……!”

대장로의 떨리는 눈동자가 대답을 대신했다. 나는 내심 한숨을 내쉬었다.

‘결국 그거였나.’

후계자 싸움.

커다란 퍼즐 조각이 맞춰진 기분이다. 아직 제자리를 찾지 못한 작은 조각들은 그들의 대화를 통해 하나둘씩 맞춰지고 있었다.

“무슨 일이 있었습니까?”

진위경이 공손한 말투로 물었다.

이 자리의 누구도 알아차리지 못할 만큼 자연스러운 변화였다.

“네 조부에 대해 아느냐?”

“들은 바가 없습니다. 아버님께서도 일언반구 없으셨지요.”

“냉혹한 사람이었다. 자식에게도, 하나뿐인 아우에게도. 그리고…….”

대장로는 피식 웃었다.

“소인배였지. 여러 이유로 한때 의좋은 형제였던 우리는 점차 멀어졌다. 그러던 와중에 그 일이 터진 거지.”

“정마대전.”

“십만마도(十萬魔度)라는 말을 아느냐? 그들은 끝없이 밀려왔다. 무림맹이 결성되었지만 구파일방의 연합에 불과했고, 제 근거지를 지키기에 바빴지.”

대장로가 본격적으로 이름을 떨치기 시작한 것도 그때였다.

그는 태원진가의 깃발 아래 산서성 무인들을 결집시켰고, 마침내 마교의 군세를 몰아냈다.

“바로 이곳, 팔천협에서 마지막 전투가 있었다.”

그의 시선이 먼 과거 어딘가를 더듬는 듯했다.

“긴 전쟁이었다. 많은 이들이 죽었고, 모두가 지쳐 있었지. 그러나 희망도 있었다. 이제 가족들의 품으로 돌아갈 수 있다는 희망. 삼백 명의 결사대가 같은 마음이었다.”

“결국 대승을 거두셨지요.”

삼백 대 삼천의 싸움. 결과는 마교의 전멸.

위대한 승리였고, 대장로가 지금까지 기억되는 이유기도 했다. 모두가 그 사실을 믿어 의심치 않았다.

적어도 방금까지는.

“매복이 있었다.”

뭐?

“협곡 깊숙한 곳까지 물러서며 싸웠지만 중과부적이었지. 미친 듯이 검을 휘두르면서도 한 가지 의문이 떠나지 않았다.”

이어지는 대장로의 목소리는, 소름 끼치도록 잔잔했다.

“어떻게 놈들이 미리 매복할 수 있었을까? 팔천협으로 오는 길은 형님이 막고 있을 터인데.”

“……!”

사람들 사이로 소리 없는 경악이 퍼져 나갔다. 가뜩이나 창백하던 진위경의 얼굴에선 아예 핏기가 사라졌다.

“전투는 반나절 동안 이어졌다. 오지 않는 지원군을 기다리며 싸웠지만 허사였지. 삼백의 결사대 중 생존자는 고작 여덟. 마침내 가문에 귀환했을 때, 나를 보던 형님의 표정을 잊을 수가 없다.”

“그게…… 사실입니까?”

“강산이 몇 번은 바뀌었을 시간이다. 단순한 의심으로 여기까지 왔을 거라 생각했느냐?”

수십 년의 세월은 의심을 확신으로 바꾸기에 차고 넘치는 시간이다. 대장로가 허탈하게 웃었다.

“형님은 전쟁을 기회로 만들었다. 나는 전장에서 영웅이 되었지만 그는 가주가 되었지. 나를 따르던 사람들은 모두 전장에서 죽거나 실종된 후였다.”

“그렇다면 곧장 장로원에 들어간 것도?”

“그래야 안심할 테니까. 그래야 나와 내 사람들의 목숨을 부지할 수 있었을 테니까.”

내 사람들?

앞서 그가 했던 말을 떠올렸다. 대장로를 따라 최후에 살아남은 여덟 명의 생존자. 그들의 정체를 유추하는 것은 그리 어렵지 않았다.

‘장로들과 산서오문의 문주들.’

살아남은 자들은 복수를 다짐했다. 자신들을 배신한 가주와 가문에 대한 복수였다. 대장로는 좌중을 천천히 쓸어 보았다.

“실로 오랜 기다림이었다.”

사람들은 침묵에 휩싸였다. 불신, 충격, 부끄러움. 감정은 제각각이었지만 아무도 쉽게 입을 떼지 못했다.

아, 물론 나는 제외지.

“개소리를 길게도 하네.”

“……!”

피식피식 새어 나오는 웃음을 참을 수 없다.

무슨 얘기까지 나오나 쭉 들어 봤는데, 이건 뭐.

“결국 목적은 하나잖아.”

나는 대장로를 향해 엄지를 까딱였다.

“복수고 자시고, 당신이 이거 되려는 거, 아냐?”

“뭐라?”

“맞잖아. 태원진가와 항산검문. 방해되는 거 싹 다 치워 버리고 산서성 꿀꺽하려는 거.”

“이놈-!”

노인네가 기차 화통을 삶아 먹었나. 아, 여기엔 기차가 없구나.

“복수? 좋지. 다 좋은데…….”

나는 귀를 후비적거리며 말을 이었다.

“그 복수를 왜 지금에 와서 해?”

자그마치 40년 전의 일이다. 대장로의 나이를 생각해도 반평생을 기다린 거다.

“당신 뒤통수쳤던 인간들이 지금 몇 명이나 살아 있는데? 뒷북도 정도껏 쳐야지. 아, 이건 제발 부탁인데, 군자의 복수는 십 년을 어쩌고 하는 개소리는 하지 마시고.”

10년 참았다고 군자면, 40년 참은 대장로는 예수냐?

그저 정신 나간 노인네의 자기 합리화에 지나지 않는다.

“뚫린 입이라고 말을 함부로 하는구나.”

“함부로 했다. 어쩔래?”

“네가 모든 걸 알고 있다고 생각하느냐?”

“꼭 알아야 하나? 이렇게까지 된 마당에?”

뻔한 물음에 어이가 없어 피식 웃으며 전장을 가리켰다. 시산혈해, 아비규환. 말 그대로의 광경이 눈앞에 있었다.

“그건…….”

서늘하던 대장로의 눈빛이 흔들린다. 하지만 찰나에 불과했다.

“그렇군. 무슨 말이 더 필요할까.”

자조하듯 중얼거린 그가 검을 들어 올렸다.

“대장로.”

진위경은 입술을 달싹였지만 딱 거기까지였다.

어느 한쪽이 죽어야 끝나는 싸움. 돌이키기에는 너무 멀리 와 버렸다.

“오너라.”

사양할 내가 아니었다.

“쳐!”

이제 상처 입은 맹수를 사냥할 시간이다.



* * *



대장로를 처음 본 날이 생각난다. 나이가 무색할 만큼 당당한 풍채와 위엄. 백발의 수염은 신선을 연상시켰다.

푸화악!

물론 가차 없이 사람을 반쪽 내는 신선은 없겠지만.

‘썩어도 준치라더니.’

피를 뒤집어쓴 채 쉴 새 없이 검을 휘두른다. 그런 그를 향해 경외와 두려움 섞인 시선이 쏟아졌다.

“괴물…….”

한쪽 팔을 잃었지만 대장로는 여전히 강했다. 그러나 분명 예전만큼은 아니었다.

‘해볼 만해.’

아무리 대장로가 절정 고수라지만 이 자리의 무인들 역시 태원진가의 정예다. 진위경을 따라 전장을 누비고, 앞선 대장로와의 전투에서 살아남을 만큼의 실력자들.

따다당!

사방에서 짓쳐 드는 검날을 튕겨 낸 대장로의 안색은 어두웠다. 예전 같았다면 검기로 가로막는 모든 걸 베었을 것이다.

마르지 않는 샘 같던 공력이 바닥을 드러냈다는 증거다.

거기에 늙어 버린 육체가 한계에 도달하기까지 했다.

촤아악.

대장로의 몸에 점차 검상이 늘기 시작했다. 지금까지와는 달리 대부분이 그의 피였다.

‘지금!’

그 틈을 놓칠 내가 아니다. 힘껏 내지른 창이 그의 옆구리 살을 한 움큼 뜯어냈다.

“흡!”

고통을 느끼는 와중에도 무인 하나를 베어 낸 대장로가 나를 향해 달려들었다. 제대로 작심한 듯, 휘둘러지는 검에는 미약한 검기가 맺혀 있었다.

하지만…….

서걱.

솟구치는 피보라와 함께 검기가 흩어졌다. 비틀거리는 그의 등 뒤로 진위경이 모습을 드러냈다.

“널 잊고 있었구나.”

대장로가 일그러진 얼굴로 돌아섰다.

“등에 칼을 꽂는 것은 형님에게 배웠느냐?”

“식솔들이 죽어 나가는데 암습 따위가 대수겠습니까.”

“무인으로서 부끄럽지도 않더냐?”

“무인이기 전에 소가주입니다.”

“소가주라, 허허.”

진위경은 착잡한 표정으로 대장로를 바라봤다.

“이미 대세는 기울었습니다.”

“그래서? 항복 권유라도 할 셈인가?”

“의미 없는 싸움을 멈춰 주십시오.”

전장의 흐름은 이미 이쪽으로 넘어온 지 오래다. 그러나 흑의인들은 끈질기게 저항했고, 아직도 비명과 시체는 줄어들지 않았다.

“네 말이 옳다. 의미 없는 싸움일지도 모르지. 하지만…….”

비틀거리던 대장로가 허리를 곧게 폈다. 어느새 눈에는 정광이 번뜩였고 칼날 같은 기세가 일어나기 시작했다.

“멈추기에는 너무 멀리 와 버렸어.”

마지막 발악?

아니, 그 정도가 아니다. 나는 문득 한 사람을 떠올렸다.

조필. 놈이 죽어 가기 직전 보여 준 마지막 모습이 지금의 대장로와 겹쳐졌다.

‘선천지기. 선천지기를 끌어올린 거야.’

공력이 운기조식과 영약을 통해 축적한, 후천적인 기운이라면 선천지기는 그 반대다. 생명력 그 자체라고 봐도 무방한 인체의 근원.

대장로는 지금 생명을 담보로 선천지기를 사용하고 있는 것이다.

“쿨럭.”

핏물을 토해 낸 대장로가 검을 치켜들었다. 빠르게 꺼져 가는 생명과는 반대로 그의 검은 어느 때보다 찬란하게 빛나고 있었다. 그 압도적인 광경을 본 순간, 나도 모르게 입 밖으로 한 단어가 흘러나왔다.

“검강…….”

그건 본능이었다. 단순히 보는 것만으로도 심장이 펄떡거린다. 검기를 아득히 뛰어넘는 무시무시한 기운이 느껴졌다.

그리고.

“그래, 네가 있었지.”

실핏줄이 툭툭 터져 나간 붉은 눈동자가 나를 응시한다.

진위경이 황급히 대장로를 막으려 달려들었다.

“안 돼!”

그러나 대장로는 이미 그 자리에 없었다. 한 걸음 만에 다섯 장의 거리를 압축시킨 그가 내게로 검을 내리그었다.

후우웅.

‘이렇게 죽는구나.’

피할 수도, 막을 수도 없는 공격. 난 죽었다. 죽을 것이다.

하지만…….

‘이대로 죽을 수는 없어.’

전신의 근육을 쥐어짰다. 한 줌 남짓한 공력이 창날을 향해 질주했다. 그건 마지막 발악이었고, 지금까지 치열하게 살아왔던 내 인생에 대한 예의였다.

“일섬.”

쐐애애액!

마지막 힘을 담은 일격이 쏘아졌다.
```

### Current accepted English

```markdown
# Chapter 61

Gooooong.

The Head Elder felt the air tremble. In the same instant, he understood how much destructive power the spearhead shooting toward his chest carried.

*This is… dangerous.*

A threat to his life he had felt only a handful of times. Every hair on his body stood on end, and the world slowed.

Shiiiiing!

Jin Taekyung’s spear came from the front, while Jin Wikyung’s sword flew in from behind. The two brothers’ pincer attack meshed with perfect timing.

A truly life-or-death moment.

Fwoooosh.

The sixty years of internal energy coiled in the Head Elder’s dantian spread through every limb and bone. It poured vitality into his aging muscles and woke his blood vessels. The change did not stop there.

Tssssss.

The Sword Energy that had risen nearly a foot—thirty centimeters—compressed to half its size.

That was not a loss of power. It was condensation.

The Sword Energy that had fluttered like a thread wrapped the entire blade and took the shape of another sword.

Sword Force.

The symbol of the superhuman masters who had broken through the wall of the Peak realm and opened a great new domain.

It was still incomplete, only half-formed, but it was unmistakably Sword Force—the distilled essence of the martial arts the Head Elder had spent his life mastering.

Shhk.

Even the Jin Family of Taiyuan’s ancestral treasure sword was cut apart, Sword Energy and all. Jin Wikyung’s internal energy scattered in an instant, and his insides were wrenched. His face went pale.

One stroke would have been enough to take his neck.

But the Head Elder had no time.

Shwack!

He reached for the spear now almost at his chest. His wrinkled hand, too, was wrapped in a dazzling radiance of qi.

This, too, was an incomplete Hand Force, but it was enough to stop Jin Taekyung’s spear.

No. It looked like enough.

Kraaaaaash!

Until the vortex spilling from the spearhead swallowed him whole.

* * *

A deathly silence settled. It felt as if the dozens of people here—or perhaps everyone standing on the battlefield—were watching us.

No.

Not us.

One man.

“This…”

At the end of countless gazes, the Head Elder slowly opened his mouth.

“What form was that?”

I answered.

“One Flash.”

Even speaking the words brought on a vicious hunger. Every muscle in my body stung, and not a scrap of internal energy was left inside me.

But that was all.

Unlike with Jopil, I didn’t pass out or crumple pathetically to the ground.

*My body can handle it now.*

I had grown enough to take One Flash’s side effects. And as much as I had grown, One Flash’s power had grown with me.

The Head Elder’s current state was proof of that.

“One Flash. One Flash…”

He muttered it under his breath and pressed an acupoint on his shoulder.

The bleeding stopped, but that was all. The arm ground to nothing by the vortex One Flash had unleashed did not come back.

“I never thought I’d end up one-armed at this age. Heh heh.”

The Head Elder gave a hollow laugh and turned toward Jin Wikyung.

“You’ve got a frightening younger brother.”

Jin Wikyung asked, his face wan,

“Does that child frighten you?”

“What about you?”

“I’m proud of him.”

Not a hint of hesitation. A smile bloomed over his pale face.

“I raised him like gold and jade, but he grew into steel. That’s the kind of child Taekyung is.”

The Head Elder stared at that smile.

“You’re a fairly impressive talent. Enough to shoulder the future of the Jin Family of Taiyuan.”

“Am I?”

“But not as much as your younger brothers.”

Jin Mukyung reaching the Peak realm at twenty was one thing. Getting ranked that high myself was almost more than I could take, but…

*What is he getting at?*

As if he’d read my mind, the Head Elder went on.

“Power is what you don’t even share with your own blood. When that time comes, will you still be so proud of your younger brothers?”

The air around us went ice-cold in an instant.

Everyone facing the Head Elder at close range belonged to the Jin Family of Taiyuan. Cautious looks clung to my cheeks, then quietly slid away.

*Family Head? I have no intention of doing anything like that, you bastards.*

That was when Jin Wikyung spoke.

“So that was it.”

Bitterness and relief both sat in his voice. The Head Elder’s brow twitched.

“What are you talking about?”

“The reason you betrayed us. The reason a day like today happened.”

“…!”

The Head Elder’s trembling eyes answered for him. I sighed inwardly.

*So that was what this was about.*

A succession fight.

It felt like a huge puzzle piece had clicked into place. The smaller pieces that still hadn’t found their spots were fitting together one by one through their conversation.

“What happened?”

Jin Wikyung asked in a respectful tone.

The shift was so natural no one else there even noticed.

“Do you know anything about your grandfather?”

“I’ve heard nothing. Father never said a word about him.”

“He was a cold man. Toward his children, and toward his only younger brother. And…”

The Head Elder gave a dry little laugh.

“He was a petty man. For a lot of reasons, we brothers, who had once been close, drifted apart. And then that happened.”

“The Great Faction War.”

“Have you heard of the Ten Myriad Demonic Forces? They came in endless waves. The Murim Alliance was formed, but it was only an alliance of the Nine Sects and One Gang, and they were too busy defending their own bases.”

That was also when the Head Elder had begun making a real name for himself.

Under the Jin Family of Taiyuan’s banner, he rallied Shanxi’s martial artists and finally drove out the Demonic Cult’s forces.

“The last battle was right here, at Eight Spring Gorge.”

His gaze seemed to grope toward some distant point in the past.

“It was a long war. Many people died, and everyone was exhausted. But there was hope, too. Hope that they could finally return to their families. The three hundred volunteers sworn to die all shared that same hope.”

“In the end, you won a great victory.”

Three hundred against three thousand.

The result was the Demonic Cult’s annihilation.

It was a glorious victory, and the reason the Head Elder was still remembered. Everyone had believed that without question.

Until just now.

“There was an ambush.”

*What?*

“We fought as we fell back deep into the gorge, but we were hopelessly outnumbered. Even as I swung my sword like a madman, one question would not leave me.”

The Head Elder’s voice was unnervingly calm.

“How could they have set an ambush in advance? My elder brother should have been blocking the road into Eight Spring Gorge.”

“…!”

Silent shock spread through the crowd. What little color was left in Jin Wikyung’s already pale face vanished.

“The battle lasted half a day. We fought waiting for reinforcements that never came, and it was useless. Of the three hundred volunteers, only eight survived. When we finally returned to the family, I have never been able to forget the look on my brother’s face when he saw me.”

“Is that… true?”

“Enough time has passed for mountains and rivers to change several times over. Did you think I came this far on mere suspicion?”

Decades were more than enough to turn suspicion into certainty. The Head Elder laughed hollowly.

“My brother turned the war into an opportunity. I became a hero on the battlefield, but he became Family Head. Everyone who had followed me either died in battle or vanished afterward.”

“Then going straight into the Elder Council—was that why?”

“Because that was the only way he would feel at ease. The only way I and my people could stay alive.”

*My people?*

I thought back to what he had said. The eight survivors who had followed the Head Elder and lived to the end.

Guessing who they were was not hard.

*The Elders and the Sect Leaders of the Five Gates of Shanxi.*

The survivors had sworn revenge. Revenge on the Family Head and the family that had betrayed them.

The Head Elder slowly swept his gaze over the crowd.

“It had been a very long wait.”

Silence swallowed them. Disbelief, shock, shame. The feelings differed, but no one could easily speak.

Well. No one except me.

“You sure dragged that bullshit out.”

“…!”

I couldn’t hold back the little snorts of laughter leaking out of me.

I had listened all the way through to see where this was going, and this was what I got.

“In the end, you’ve only got one goal.”

I flicked my thumb at the Head Elder.

“Revenge, my ass. You’re trying to become this, aren’t you?”

“What did you say?”

“I’m right, aren’t I? Clear away everything in the way—the Jin Family of Taiyuan, the Mount Heng Sword Sect—and swallow Shanxi whole.”

“You insolent—!”

Had the old man swallowed a locomotive boiler? Oh, right. No trains here.

“Revenge? Sure. Fine, revenge…”

I picked at my ear and went on.

“But why now?”

This had happened a full forty years ago. Even counting the Head Elder’s age, he had waited half his life.

“How many of the people who stabbed you in the back are even still alive? There’s late, and then there’s this late. And please, I’m begging you—don’t start with that bullshit about a gentleman waiting ten years to take revenge.”

If holding out ten years made you a gentleman, did holding out forty make the Head Elder Jesus?

It was nothing more than a crazy old man’s self-justification.

“You run your mouth just because you’ve got one.”

“I did. What are you going to do about it?”

“Do you think you know everything?”

“Do I have to? After it’s gone this far?”

The question was so obvious I snorted a laugh and pointed at the battlefield.

A mountain of corpses, a sea of blood. Utter pandemonium. The scene in front of us was exactly that.

“That…”

The chill in the Head Elder’s eyes wavered. But only for an instant.

“I see. What more is there to say?”

He muttered it like a jab at himself, then raised his sword.

“Head Elder.”

Jin Wikyung’s lips moved, and that was all.

A fight that ended only when one side died. They had come too far to turn back.

“Come.”

I wasn’t about to decline.

“Attack!”

It was time to hunt the wounded beast.

* * *

I remembered the first day I saw the Head Elder.

A bearing and dignity that made his age meaningless. His white beard called an immortal to mind.

Fwoosh!

Of course, there were no immortals who mercilessly cut people in half.

*Even rotten, a prized fish is still a prized fish.*

Drenched in blood, he swung his sword without pause. Looks mixed with awe and fear poured toward him.

“Monster…”

He had lost an arm, but the Head Elder was still strong.

He just clearly wasn’t as strong as before.

*This is doable.*

Peak master or not, the martial artists here were the Jin Family of Taiyuan’s elite. Men who had fought across the battlefield under Jin Wikyung, skilled enough to have survived the earlier clash with the Head Elder.

Clang-clang-clang!

The Head Elder knocked aside blades driving in from every direction, his face darkening. In the old days, he would have cut down everything in his path with Sword Energy.

Proof that the internal energy that had once seemed like a spring that never ran dry had finally hit bottom.

On top of that, his aged body had reached its limit.

Shraaaak!

Sword wounds began to multiply across the Head Elder’s body. Unlike before, most of the blood was his.

*Now!*

I wasn’t about to miss that opening. The spear I drove with everything I had tore a handful of flesh from his side.

“Hk!”

Even through the pain, the Head Elder cut down a martial artist and charged me. He meant it this time; a faint Sword Energy gathered along the swinging blade.

But…

Shhk.

The Sword Energy scattered in a rising spray of blood. Jin Wikyung appeared behind the staggering Head Elder.

“I’d forgotten you were there.”

The Head Elder turned with a twisted face.

“Did my elder brother teach you to put a knife in someone’s back?”

“My family members are dying. Is a sneak attack really that important?”

“Aren’t you ashamed, as a martial artist?”

“I am the Lesser Family Head before I am a martial artist.”

“The Lesser Family Head, is it? Heh heh.”

Jin Wikyung looked at the Head Elder with a complicated expression.

“The tide has already turned.”

“So? Are you going to ask me to surrender?”

“Please stop this meaningless fight.”

The flow of the battlefield had been ours for a long time. But the black-clad men kept resisting stubbornly, and the screams and corpses still showed no sign of thinning out.

“You’re right. It may be a meaningless fight. But…”

The staggering Head Elder straightened his back. A sharp gleam was already flashing in his eyes, and a blade-like aura began to rise.

“We’ve come too far to stop.”

A last desperate struggle?

No. More than that. Someone suddenly came to mind.

Jopil.

The last sight of him as he was dying overlapped with the Head Elder now.

*Innate qi. He’s drawing up his innate qi.*

If internal energy was acquired power, piled up by circulating qi and taking elixirs, innate qi was the opposite. It was the root of the human body—life force itself, for all intents.

The Head Elder was staking his life to use it.

“Cough.”

He spat blood and raised his sword. His life was going out fast, but his sword shone more brilliantly than it ever had.

The moment I saw that overwhelming sight, a single word slipped out of me.

“Sword Force…”

It was instinct.

My heart pounded just from looking at it. I could feel a terrifying power that far outstripped Sword Energy.

And then—

“Yes. You were here.”

His red eyes, the capillaries bursting one after another, locked on me.

Jin Wikyung lunged to stop the Head Elder.

“No!”

But the Head Elder was already gone from that spot.

In a single step he compressed fifty feet and brought his sword down on me.

Whoooong.

*So this is how I die.*

An attack I couldn’t dodge or block.

I was dead. I was going to die.

But…

*I can’t die like this.*

I wrung every muscle in my body. The last scant handful of internal energy raced for the spearhead.

It was a final struggle, and a show of respect for the life I had lived so fiercely until now.

“One Flash.”

Shiiiiiiing!

The last strike, carrying every bit of strength I had left, shot forward.
```
## Chapter 62

### Korean source

```text
＃62화



세상이 정지한 것 같았다. 심장 박동 소리가 천둥처럼 울렸고, 흩날리는 흙 알갱이 하나까지 또렷이 보였다.

그리고…….

후우웅.

섬광이 있었다. 검강이 뿜어내는 빛은 아름다우면서도 정확했다. 창날은 물론 내 육신까지 반으로 가를 수 있을 법한 파괴적인 힘이 느껴졌다.

‘끝났군.’

나는 최선을 다했다. 일말의 후회조차 없다면 거짓말이지만 결과는 바뀌지 않을 것이다.

그저 마지막까지 있는 힘껏 부딪쳐 갈 뿐.

슈화아악!

창날이 바람을 찢었고, 검강은 바람을 지웠다. 죽음이 성큼 다가온 그 순간이었다.

쐐애액! 푹!

대장로의 눈이 부릅떠졌다. 섬전 같은 속도로 일어나 그의 단전에 비수를 박아 넣은 것은 정체를 알 수 없는 괴인이었다.

“너…….”

“사혈을 짚었어야지.”

아무도 예상하지 못한 기습이었다.

방금까지만 해도 그는 주위에 널린 수많은 시신 중 하나에 불과했으니까. 하지만 아니었다.

괴인은 극한의 인내심으로 때를 기다렸을 뿐이다. 자식의 원수를 갚을 순간을.

대장로가 비명처럼 외쳤다.

“이천백!”

“크하하하!”

이천백이 광소를 터트린 순간, 내 창날이 그의 등을 파고들었다. 살과 뼈를 가르며 거침없이 뻗어 나갔다.

띠링.



- [Lv.75 이천백]을 처치했습니다!

- 레벨 업!

- 레벨 업!

- 레벨 업!

.

.

- 레벨 업의 중첩 효과로 모든 상태 이상이 회복됩니다!



변화가 일어났다. 욱신거리던 근육이, 무겁던 발이, 텅 비어 있던 단전이 새로운 힘으로 팽창했다.

동시에 나는 무엇을 해야 할지 깨달았다.

‘일섬.’

다시 한번. 백색 와류가 뿜어져 나왔다.

콰드드득!



* * *



구사일생.

저 네 글자가 이렇게 가슴에 와닿기는 난생처음이다.

진짜 죽다 살아났다. 지옥 입국 수속 밟고, 염라대왕이랑 찐한 포옹에 기념사진까지 한 방 찍는 환상까지 봤을 정도다.

이천백이 아니었다면 환상은 현실이 되었을 텐데.

‘구하길 잘했네.’

편히 갈 수 있도록 이천백의 눈을 감겨 주고 싶었지만 아직 해야 할 일이 남아 있다.

“그러니까 착하게 살지. 좀.”

내 말에 대장로가 피식 웃었다. 그의 모습은 처참했다.

일섬은 하나 남은 팔마저 집어삼킨 것으로 모자라 가슴에 주먹만 한 구멍을 뚫었다.

“심보 한번 고약한 녀석이군. 죽어 가는 노인에 대한 예의도 없느냐?”

“내가 아는 노인은 늘그막에 손주들 재롱 보는 맛으로 사는 분들이야. 당신처럼 손주들 죽이려고 날뛰는 영감탱이가 아니라.”

“예끼 이놈! 손주 노릇이나 하고 나서 그런 말을 해라.”

껄껄 웃는 그는 허탈하면서도, 모든 걸 털어낸 듯 후련해 보였다.

“태경이는 착한 아이입니다. 대장로께서 먼저 마음을 열었다면 좋은 조손 지간이 되었겠지요.”

대장로가 고개를 돌렸다. 검을 쥔 진위경이 그곳에 있었다.

“그 검으로 나를 찌를 셈이냐?”

“고민 중입니다.”

“그 고민, 빨리 끝내야 할 게다. 남은 시간이 많지 않으니.”

그의 말은 사실이었다. 양팔이 잘려 나간 단면과 아랫배에서는 멀쩡한 척 이야기를 나누는 지금도 핏물이 폭포수처럼 흐르고 있었다.

거기에 선천지기를 끌어올린 후폭풍까지. 그가 아직도 살아 있다는 사실이 기적처럼 느껴질 정도다.

“힘들어 보이십니다.”

“아니, 편안해지는 중이지.”

단호한 대답이었다.

“정마대전이 일어났을 때 내 나이가 고작 이립(而立)이었다. 그 후로 단 한순간도 맘 편히 쉬어 본 적이 없지. 아니…….”

대장로가 힘겨운 목소리로 말을 이어 갔다.

“사실 오래전부터 지쳐 있었는지도 모르겠다.”

나는 기가 차서 중얼거렸다.

“할 거 다해 놓고 이제 와서 뭔.”

“태경아!”

진위경은 가벼운 질책이 담긴 눈짓을 보냈지만, 대장로는 기분 나쁘지 않은 듯 다물었던 입에서 바람 빠지는 웃음소리가 새어 나왔다.

“푸흐흐. 그래, 네 말이 맞다. 노망난 늙은이의 지랄이라고 생각하거라.”

“진짜 죽을 때 됐나 보네.”

“어허! 이 녀석!”

“아, 왜요. 틀린 말 한 것도 아닌데.”

티격태격하는 나와 진위경을 대장로가 흐릿한 시선으로 바라봤다.

“우리에게도 너희 같은 때가 있었지. 그래, 분명히 그랬던 적이 있었어.”

하지만 대장로에게는 더 이상 추억을 더듬을 시간조차 남아 있지 않았다.

“쿨럭, 쿠에에엑!”

한 됫박은 될 법한 피를 토해 낸 대장로가 비틀거렸다. 그는 죽음을 목전에 두고 있었다. 눈의 실핏줄은 모조리 터져 나갔고, 몸에서 흘러나온 피는 웅덩이를 이룬 지 오래였다. 이제는 가망이 없다는 걸 한눈에도 알 수 있을 정도로.

‘정말 죽는다고? 저 대장로가?’

사람은 누구나 죽는다. 이 전장에서만 수백, 어쩌면 일천 이상의 목숨이 사라졌는지도 모른다.

하지만 대장로의 죽음은 쉬이 상상조차 할 수 없던 일이었다.

그만큼 그가 보여 준 무위는 압도적이었다. 그 탓에 지금의 모습이 처절해 보이기까지 했다. 그래서 더 궁금해졌다.

“그렇게까지 버티는 이유가 뭐지?”

대장로가 대답했다.

“먼저 떠나보낸 이들에게…… 최선을 다했다고 말하고 싶으니까.”

“후회는?”

“없다.”

그는 활짝 웃으며 가슴을 내밀었다.

“끝내라. 네 손으로 직접.”

나는 창을 들었다. 진위경은 착잡한 얼굴이었지만 그렇다고 말리지는 않았다.

쉭!

한 줄기 바람이 불었고, 꺾일 것 같지 않던 대장로의 무릎이 땅에 닿았다. 그의 주름진 얼굴 위로 편안한 미소가 떠올랐다.

마지막 순간, 입술이 달싹였지만 소리는 새어 나오지 않았다.

그뿐이었다.

띠링.



- [Lv.95 진백양]을 처치했습니다!

- 퀘스트, [배반자]를 완료했습니다!

- 레벨이 크게 올랐습니다!

- 명성치가 크게 올랐습니다!



아주 잠깐, 침묵이 흘렀다.

그리고 지금껏 들어 본 적 없는 거대한 함성이 터져 나왔다.

“산서잠룡 진태경이 화양검 진백양을 베었다!”



- 칭호, [산서잠룡]을 획득했습니다!



수십, 어쩌면 수백.

살아남은 모두가 내 이름을 외치고 있었다.

‘산서잠룡이라.’

제법 마음에 드는 새 이름이었다.



* * *



- 태원진가의 삼공자 진태경이 대장로를 베었다!

- 산서잠룡이 화양검을 꺾었다!

“산서잠룡이라.”

위팽은 피식 웃었다. 토룡(土龍) 소리도 못 듣던 망나니 삼공자다. 그러나 이제는 인정하지 않을 수 없다.

그는 잠룡이다. 여의주를 얻으면 창천을 누빌 수 있는.

“어떻게 생각하시오?”

일장로가 대답했다.

“저 말을 믿나?”

“모두가 대장로의 죽음을 외치고 있소만.”

“그건 주군이 원하셨기 때문이야. 삼공자 따위가 그분을? 웃기지도 않는 소리지.”

“여기서 그게 보인단 말이오? 눈도 좋군.”

“그렇게 한눈을 팔았으니 이 꼴이 된 것 아니겠나. 하하하.”

그는 시체 더미에 비스듬히 몸을 기대고 있었다. 어깨 어림부터 허리까지 사선으로 갈라진 검상에서는 피가 콸콸 쏟아졌다.

“투항하시오. 지금 치료한다면 살 수 있소.”

“아니. 노부의 끝은 이미 오래전에 정해 뒀네. 아주 고통스러운 죽음이지.”

위팽은 고개를 저었다.

“내가 허락하지 않을 거요.”

“내 죽음에는 허락이 필요 없네. 자네도, 심지어 나도 어찌할 수 없어.”

“그게 무슨.”

일장로의 말을 이해하지 못한 위팽이 미간을 좁혔을 때였다.

“암천(暗天)을 조심…… 크륵.”

한순간이었다. 일장로의 칠공에서 피가 쏟아졌다. 눈이 뒤집히고 전신이 경련했다.

“일장로!”

위팽이 황급히 다가섰을 때는 일장로의 숨이 이미 끊긴 후였다. 앞서 했던 말처럼 고통스러운 죽음을 맞이한 그의 얼굴은 잔뜩 일그러져 있었다.

‘이건.’

독? 혹은 금제?

지금으로써는 알 도리가 없다. 위팽은 그의 유언이 된 한 단어를 뇌리 깊숙이 새겼다.

‘암천. 분명 암천이라고 했다.’

일장로가 남긴 유일한 단서. 위팽은 복잡한 심경으로 죽은 이의 얼굴을 응시하다가 돌아섰다.

“나, 위팽이 일장로를 베었다!”

흑의인들의 얼굴에 절망이 깃들었다. 죽음과 항복. 두 가지 길에서 그들이 선택한 것은 후자였다.

텅. 터터텅.

힘없이 떨어지는 병장기들.

전쟁의 종지부였다.



* * *



죽은 자가 있다면 살아남은 자도 있다.

전투에 앞서 미리 절벽 위로 올라갔던 궁귀문(弓鬼門)의 문주, 진충이 바로 그런 경우였다.

“허망하구나.”

반평생을 바친 대계였다. 그러나 결과는 참혹했다.

주군으로 모셨던 대장로, 호형호제하던 장로들과 산서오문의 문주들이 모두 죽었다. 살아남은 자들의 발악도 끝났으니 이제 남은 것은 자신뿐이다.

‘결국 이리되는가.’

진충은 몸을 돌렸다. 궁귀문의 무사 오십 명이 그의 명령을 기다리고 있었다.

“떠나라.”

보이지 않는 동요가 번졌다. 가장 가까이에 있던 무사 하나가 조심스럽게 말을 꺼냈다.

“문주님, 그 말씀은……?”

“이미 끝난 싸움. 너희에게 희생을 강요하지 않으마. 이 길로 떠나라. 최대한 뿔뿔이 흩어져 산서를 벗어난다면 목숨만은 건질 수 있을 것이다.”

무사가 결연하게 고개를 끄덕였다.

“죽을 때까지 따르겠습니다.”

“나는…… 이곳에 남는다.”

“예?”

당황도 잠시, 무사의 목소리가 격정으로 떨렸다.

“저희 때문입니까?”

“천만에.”

진충은 단호하게 대답했지만 속마음은 달랐다.

‘내가 따라간다면 태원진가는 집요하게 추적하겠지.’

산서오문은 여럿이면서 하나. 하나면서도 여럿이다.

같은 목적으로 만들었으나 무사를 키우는 방식은 제각기 달랐다. 진충은…… 그들을 병기로 키우지 않았다. 제자로 받아들였다.

“문주님!”

“저희를 이끌어 주십시오!”

이들은 모두 갈 곳 없는 고아 출신이다.

최소 십 년. 길게는 이십 년 이상을 먹이고 재우며 무공을 가르쳤다. 대계가 성공했다면 산서 무림의 주축이 되었겠지만 실패한 지금은 반역자에 불과했다.

“지금 흘러가는 상황을 모르는 것이냐?”

“죽더라도 문주님과 함께하겠습니다.”

“이놈!”

“허락해 주십시오.”

맨 처음 나섰던 무사가 돌바닥에 이마를 찧었다. 이어 하나둘씩 무릎을 꿇기 시작하는 제자들의 모습에 진충은 하늘을 보며 한탄했다.

“대계가 미뤄지지 않았다면. 그들이 나서 주었더라면!”

‘그들’에 관한 이야기는 수뇌부 여덟 명만이 아는 비밀.

그 말을 입에 담았다는 것은 진충이 제자들과 최후를 함께하기로 결정했다는 것과 다름없었다.

‘이 또한 하늘의 뜻이겠지.’

컴컴한 밤하늘에서 시선을 돌린 진충이 엎드린 무사를 일으켜 세웠다. 그가 보여 준 충성심에 한없이 미안하고, 감격스러울 뿐이었다.

“되었다. 그만 일어나거라.”

따뜻한 목소리에 무사가 고개를 들었다. 이마에서 흐르는 한 줄기 핏방울을 날름 핥은 그가 히쭉 웃는다.

“예.”

퍼걱!

진충은 얼빠진 얼굴로 무사를 바라봤다. 그건 고통 따위는 느껴지지도 않을 정도의 충격이었다.

‘이게 도대체…….’

촤아악!

무사가 진충의 가슴에 박혀 있던 손을 빼냈다. 그의 손에는 달빛보다 환한 빛무리가 어려 있었다. 보는 것만으로도 불길함을 자아내는 핏빛 강기였다.

“넌…….”

“알면서 뭘 물어보시나. 아, 그리고 방금 당신이 했던 말. 간단하게 대답해 주지.”

무사의 웃음이 짙어졌다.

“우리가 왜 나서? 당신들 역할은 딱 여기까진데.”

진충은 눈을 부릅떴다. 그들이다. 마지막까지 결코 모습을 드러내지 않던 미지의 존재들.

암천!

“네놈들이!”

“어허, 이용당했다는 표정 짓지 마. 누구 덕분에 그 지옥에서 살아 나왔는지 잊었어?”

진충은 사십 년 전, 그날의 악몽을 떠올렸다. 주위에 가득한 아군의 시체와 끝없이 밀려오던 마교의 군세.

대장로를 중심으로 뭉친 그들은 죽음을 각오했다. 암천이 나타나기 전까지는.

“목숨도 살려 주고, 복수할 기회도 줬잖아. 뭘 더 바랐어?”

그의 말이 맞다. 마교의 군세를 몰살시킨 암천은 거래를 제의했고, 그들은 응했다. 머릿속에 고독을 심어야 했지만 복수를 위해서라면 뭐든 할 수 있었다.

하지만…….

“우리를 이용해서 산서를 지배하려던 속셈이 아니었나?”

“뭐, 처음에는 그랬을지도 모르지.”

“그럼 도대체 뭘 위해서?”

히죽.

“더 큰 그림.”

대답과 동시에 피 묻은 손이 진충의 가슴을 짚었다.

펑.

진충의 몸 안에서 작은 폭발이 일어났다. 고막을 터트리고 혈맥을 가닥가닥 끊어 낸 기운은 심장까지 다다랐다.

‘고작 이렇게…….’

생각은 이어지지 않았다. 이미 숨이 끊긴 진충의 몸뚱어리는 새처럼 훨훨 날아 절벽 아래로 추락했다.

쉬이이익, 쿵!

흘끗 아래를 내려다본 무사가 눈을 찡그렸다.

“아이고, 아프겠다.”

돌아선 그를 기다리는 것은 비명과 핏물이었다. 어디선가 홀연히 나타난 열 명의 흑의인이 궁귀문의 제자들을 학살하고 있었다.

“빨리 끝내고 가자.”

“존명.”

쐐애애액! 퍽!

무사는 절벽 아래로 시선을 돌렸다. 주위에서는 비명이 터져 나오고 있었지만 절벽 아래는 환호와 함성으로 가득했다.

- 산서잠룡!

- 진태경! 진태경!

“산서잠룡이라.”

계획은 성공했다. 그러나 진태경의 등장은 그도 예측하지 못한 변수였다. 그 사실이 마음에 들지 않았다.

‘쳐 낼까, 말까.’

마음만 먹는다면 뿌리째로 뽑아 버릴 수 있다. 깊어진 눈이 환호에 둘러싸인 진태경을 향했다.

- 우리 막내! 내 동생!

- 놔! 놔 이 인간아!

피식. 실소가 터져 나왔다.

‘살려 주마. 오늘은.’

무사가 돌아섰다. 그의 걸음마다 오십여 구의 시신이 융단처럼 깔려 있었다.
```

### Current accepted English

```markdown
# Chapter 62

The world seemed to stop.

My heartbeat thundered in my ears, and I could see every last grain of dirt drifting through the air.

And then…

Whoooosh.

A flash of light.

The glow pouring from the Sword Force was beautiful—and precise. I could feel a destructive power in it that looked ready to split not only the spearhead, but my body itself, in two.

*It's over.*

I had done my best. It would be a lie to say I had no regrets at all, but that wouldn't change the outcome.

All I could do was smash into it with everything I had left.

Shwaaaak!

The spearhead tore through the wind. The Sword Force erased it.

That was the instant death came striding in.

Shreeeek! Thunk!

The Head Elder's eyes flew wide.

A freak of unknown identity had risen at lightning speed and driven a dagger into his dantian.

“You…”

“You should've struck a vital acupoint.”

It was an ambush no one could have expected.

Until a moment ago, he had been nothing more than one of the countless corpses scattered around us.

But he wasn't.

The freak had only been waiting, with extreme patience, for his moment—the moment he could avenge his child.

The Head Elder cried out like a scream.

“Lee Cheonbaek!”

“Kahahaha!”

The instant Lee Cheonbaek burst into maniacal laughter, my spearhead punched into his back.

It tore through flesh and bone, driving forward without resistance.

> **System**
>
> - You have defeated Lv. 75 Lee Cheonbaek!
> - Level up!
> - Level up!
> - Level up!
> - …
> - All status ailments have been recovered due to the stacked effect of the level-ups!

The change came at once.

My aching muscles, my heavy feet, my empty dantian—all of them swelled with new strength.

At the same time, I knew what I had to do.

*One Flash.*

Once more, a white vortex erupted.

Kraaaack!

* * *

A narrow escape.

Never in my life had those four syllables hit so close to home.

I had really died and come back. I'd even seen a vision of going through hell's immigration, sharing a passionate hug with King Yama, and snapping a commemorative photo together.

If it hadn't been for Lee Cheonbaek, that vision would have become reality.

*Good thing I saved him.*

I wanted to close Lee Cheonbaek's eyes so he could go in peace, but there was still work to do.

“So live a little nicer. Come on.”

The Head Elder let out a faint laugh at that. He looked horrific.

One Flash had swallowed his remaining arm, and it hadn't stopped there—it had punched a hole the size of a fist through his chest.

“What a nasty-hearted brat. Have you no manners toward a dying old man?”

“The old folks I know spend their later years enjoying their grandchildren's antics. They're not old bastards like you, running around trying to kill their own grandchildren.”

“Why, you brat! Play at being a grandson first, then say something like that.”

He laughed heartily. He looked hollow, and yet relieved, as if he had finally shaken everything off.

“Taekyung is a good kid. If you had opened your heart first, the two of you might have had a good grandfather-grandson relationship.”

The Head Elder turned his head.

Jin Wikyung stood there, sword in hand.

“Are you planning to stab me with that sword?”

“I'm considering it.”

“You'd better finish considering it quickly. I don't have much time left.”

His words were true.

Even now, as he talked as if nothing were wrong, blood poured like a waterfall from the severed stumps of both arms and from his lower abdomen.

On top of that, there was the backlash from drawing up his innate qi.

The fact that he was still alive felt like a miracle.

“You look like you're having a hard time.”

“No. I'm getting comfortable.”

The answer was firm.

“I was barely thirty when the Great Faction War began. After that, I never once rested easy—not even for a moment. No…”

The Head Elder went on in a strained voice.

“In truth, perhaps I've been tired for a very long time.”

I muttered, appalled.

“You did all that, and now you're coming out with this?”

“Taekyung!”

Jin Wikyung sent me a look of mild reproach, but the Head Elder did not seem offended. A breathy laugh leaked from behind the lips he had pressed shut.

“Puh-huh. Yes, you're right. Just think of it as a senile old man's bullshit.”

“Looks like it really is time for you to die.”

“Hey! You little brat!”

“What? It's not like I said anything wrong.”

The Head Elder watched Jin Wikyung and me bicker with a fading gaze.

“We had a time like yours too. Yes. There was definitely a time when we were like that.”

But he no longer had time left even to linger over those memories.

“Cough! Guaaack!”

The Head Elder staggered after vomiting what had to be a bowlful of blood.

He was at death's door. Every capillary in his eyes had burst, and the blood pouring from his body had long since pooled at his feet.

Anyone could see there was no hope left for him.

*He's really dying? That Head Elder?*

Everyone dies.

Hundreds of lives had vanished on this battlefield alone—perhaps more than a thousand.

But the Head Elder's death was something I had never even been able to imagine.

That was how overwhelming his martial prowess had been. It made his current state look all the more wretched.

And that only made me more curious.

“Why are you holding on this hard?”

The Head Elder answered.

“Because I want to tell those who left before me… that I did my best.”

“Regrets?”

“None.”

He smiled broadly and thrust out his chest.

“Finish it. With your own hands.”

I raised my spear.

Jin Wikyung wore a troubled expression, but he did not try to stop me.

Shhk!

A single gust of wind passed, and the Head Elder's knees—which had never seemed capable of buckling—touched the ground.

A peaceful smile rose on his wrinkled face.

At the final moment, his lips moved, but no sound came out.

That was all.

> **System**
>
> - You have defeated Lv. 95 Jin Baekyang!
> - Quest **Traitor** completed!
> - Your Level has increased greatly!
> - Your Fame has increased greatly!

For a very brief moment, silence fell.

Then a colossal roar erupted—unlike anything I had ever heard.

“The Sleeping Dragon of Shanxi, Jin Taekyung, has cut down the Blade of Flowers, Jin Baekyang!”

> **System**
>
> - You have acquired the Title **Sleeping Dragon of Shanxi**!

Dozens.

Maybe hundreds.

Everyone who had survived was shouting my name.

*The Sleeping Dragon of Shanxi.*

I rather liked my new name.

* * *

“Third Young Master Jin Taekyung of the Jin Family of Taiyuan cut down the Head Elder!”

“The Sleeping Dragon of Shanxi defeated the Blade of Flowers!”

“The Sleeping Dragon of Shanxi…”

Wipeng gave a faint smirk.

He was the wastrel Third Young Master who had never even been called an earth dragon.

But now, there was no denying it.

He was a sleeping dragon.

If he obtained the dragon pearl, he could roam the heavens.

“What do you make of it?”

The First Elder answered.

“Do you believe that?”

“Everyone is shouting that the Head Elder is dead.”

“That is because my lord wanted it that way. A mere Third Young Master killing him? It's laughable.”

“You can see that from here? Sharp eyes.”

“This is what comes of letting your attention wander. Hahaha.”

He was leaning diagonally against a heap of corpses.

A sword wound split him on a slant from about the shoulder to the waist, and blood poured from it in torrents.

“Surrender. If we treat you now, you can live.”

“No. This old man's end was decided long ago. A very painful death.”

Wipeng shook his head.

“I won't allow it.”

“My death does not require permission. Neither you nor even I can do anything about it.”

“What does that mean?”

Wipeng furrowed his brow, unable to follow, when—

“Beware Dark Heaven… Grrk.”

It happened in an instant.

Blood poured from all seven of the First Elder's orifices. His eyes rolled back, and his entire body convulsed.

“First Elder!”

By the time Wipeng hurried over, the First Elder's breath had already stopped.

Just as he had said, he had met a painful death. His face was twisted grotesquely.

*This is…*

*Poison? Or a restriction?*

There was no way to know yet.

Wipeng carved the single word that had become the First Elder's last deep into his mind.

*Dark Heaven. He definitely said Dark Heaven.*

The only clue the First Elder had left behind.

Wipeng stared at the dead man's face with complicated feelings, then turned away.

“I, Wipeng, cut down the First Elder!”

Despair spread across the faces of the black-clad men.

Faced with two paths—death or surrender—they chose the latter.

Clang. Clatter-clatter.

Weapons fell weakly to the ground.

It was the end of the war.

* * *

Where there were the dead, there were also those who had lived.

The Sect Leader of Gunggwimun,[^1] Jin Chung, was one of them. He had climbed to the top of the cliff before the battle began.

“How hollow.”

It had been a grand scheme to which he had devoted half his life.

The result was horrific.

The Head Elder he had served as his lord, the Elders he had called brother, and the Sect Leaders of the Five Gates of Shanxi had all died.

The survivors' last desperate struggle had ended as well.

Now, only he remained.

*So this is how it ends.*

Jin Chung turned around.

Fifty martial artists of Gunggwimun were waiting for his orders.

“Leave.”

An invisible stir ran through them.

One of the nearest martial artists spoke cautiously.

“Sect Leader, what do you mean…?”

“This fight is already over. I will not force you to sacrifice yourselves. Leave by this road. Scatter as widely as you can and get out of Shanxi. If you do, you may at least save your lives.”

The martial artist nodded resolutely.

“I will follow you until I die.”

“I… will remain here.”

“What?”

The confusion lasted only a moment before the martial artist's voice began to tremble with feeling.

“Is it because of us?”

“Not at all.”

Jin Chung answered firmly, but his thoughts were different.

*If I followed them, the Jin Family of Taiyuan would hunt them relentlessly.*

The Five Gates of Shanxi were many, yet one.

One, yet many.

They had been created for the same purpose, but each sect had raised its martial artists in a different way.

Jin Chung had not raised them as weapons.

He had taken them in as disciples.

“Sect Leader!”

“Please lead us!”

Every one of them had been an orphan with nowhere to go.

For at least ten years—twenty or more in some cases—he had fed them, sheltered them, and taught them martial arts.

If the grand scheme had succeeded, they would have become the backbone of Shanxi's Murim.

Now that it had failed, they were nothing more than traitors.

“Do you not understand how this is going?”

“Even if we die, we will die with you, Sect Leader.”

“You brat!”

“Please allow us.”

The martial artist who had stepped forward first slammed his forehead against the stone floor.

Then, one by one, his disciples began to kneel.

Jin Chung looked up at the sky and lamented.

“If only the grand scheme had not been delayed. If only they had stepped forward!”

Talk of *them* was a secret known only to the eight at the top.

To speak those words aloud was no different from deciding to share his final moments with his disciples.

*This too must be heaven's will.*

Jin Chung turned his gaze from the dark night sky and helped the prostrate martial artist to his feet.

He felt endlessly sorry—and deeply moved—by the loyalty the man had shown.

“That's enough. Get up.”

At the warmth in his voice, the martial artist lifted his head.

He flicked his tongue over the trickle of blood running down his forehead, then gave a crooked grin.

“Yes.”

Thuck!

Jin Chung stared at the martial artist with a blank look.

The shock was so great he could not even feel pain.

*What in the world…?*

Shwaaak!

The martial artist pulled his hand from Jin Chung's chest.

A glow brighter than moonlight clung to it—a blood-red Force that inspired dread just to look at.

“You…”

“You already know, so why ask? Oh, and about what you just said—I'll give you a simple answer.”

The martial artist's smile deepened.

“Why would we step forward? Your role ends right here.”

Jin Chung's eyes flew wide.

*Them.*

The unknown beings who had never revealed themselves until the very end.

Dark Heaven!

“You bastards!”

“Don't look at me like you've been used. Forgotten who got you out of that hell alive?”

Jin Chung remembered the nightmare from forty years ago.

The corpses of allies covering the ground around him.

The endless army of the Demonic Cult surging in.

They had gathered around the Head Elder and prepared themselves to die.

That was before Dark Heaven appeared.

“We saved your lives and gave you a chance at revenge. What more did you want?”

He was right.

Dark Heaven had annihilated the Demonic Cult's army, then proposed a deal.

They had accepted.

They had to have a gu planted in their heads, but they would have done anything for revenge.[^2]

But…

“Wasn't your real aim to use us to rule Shanxi?”

“Well, maybe that was the plan at first.”

“Then what was it all for?”

The martial artist grinned.

“A bigger picture.”

At the same time, his bloodstained hand pressed against Jin Chung's chest.

Boom.

A small explosion went off inside Jin Chung's body.

The energy burst his eardrums, severed his blood vessels strand by strand, and reached his heart.

*Just like this…*

The thought went no further.

Jin Chung's body, already dead, flew like a bird and plunged off the cliff.

Shiiiiik! Crash!

The martial artist glanced down and grimaced.

“Ouch. That must've hurt.”

When he turned around, screams and blood were waiting for him.

Ten black-clad men who had appeared out of nowhere were massacring Gunggwimun's disciples.

“Let's finish this quickly and go.”

“As you command.”

Shreeeeek! Thud!

The martial artist turned his gaze toward the bottom of the cliff.

Screams erupted all around him, but below the cliff the air was filled with cheers and shouts.

“The Sleeping Dragon of Shanxi!”

“Jin Taekyung! Jin Taekyung!”

“The Sleeping Dragon of Shanxi…”

The plan had succeeded.

But Jin Taekyung's appearance had been a variable even he had not anticipated.

He did not like that.

*Take him out, or let him be?*

If he set his mind to it, he could rip him out by the roots.

His deepening gaze turned toward Jin Taekyung, ringed by cheers.

“Our youngest! My little brother!”

“Let go! Let go, you bastard!”

A snort of laughter escaped him.

*I'll let you live. For today.*

The martial artist turned away.

Some fifty corpses lay like a carpet in his wake.

[^1]: 弓鬼門, lit. Bow Ghost Gate.
[^2]: A *gu* is a traditional poison associated with venomous creatures; in Murim fiction, it may be implanted in a person's body.
```
## Chapter 63

### Korean source

```text
＃63화



끼이이익.

사내가 객잔에 들어온 것은 미시(未時) 무렵이었다.

낡은 나무문이 삐걱댔지만 객잔 안의 사람들은 아무도 돌아보지 않았다. 심지어 잽싸게 손님을 맞이해야 할 주인과 점소이마저 그랬다.

“그래서, 그래서 어떻게 됐소?”

“거, 자꾸 애타게 하지 말고 말을 좀 해 보쇼!”

사람들의 열광적인 반응에 노인이 빈 대접을 톡톡 두드렸다.

결국 주인이 죽엽청을 넘치도록 따른 후에야 노인, 매담자(賣談者)의 이야기가 이어졌다.

“치열한 격전이 벌어졌지. 혈랑검 이천백이 끌고 온 자들만 물경 삼만. 그에 비해 태원진가는 삼백의 정예가 전부였어.”

“삼만!”

“세상에, 삼만이라니!”

“그게 말이 되오? 항산검문이 무슨 구파일방도 아니고…….”

매담자가 죽엽청을 마시다 말고 도로 뱉었다.

“에이, 시발. 술맛도 더럽게 없네. 나 갈 테니까 저 구파일방 운운하는 놈한테 나머지 얘기 들으쇼.”

“어허. 왜 이러시오.”

“방금 말한 놈 누구야!”

흉흉해진 분위기에 한 청년이 엉거주춤 밀려났다.

그제야 매담자가 반쯤 뗐던 궁둥이를 다시 내려놨다. 하지만 비위가 상한 만큼 배포도 두둑해진 상태였다.

톡톡.

빈 대접을 두드리는 매담자의 모습에 모두가 인상을 썼다. 이제는 술이 아니라 돈을 줘야 한다. 사람들이 보이지 않는 눈치 싸움을 하고 있던 그 순간이었다.

팅.

“어?”

게슴츠레하던 매담자의 눈이 동그랗게 뜨였다. 번쩍거리는 은자 한 냥이 어디선가 날아온 것이다.

“허, 누군지 통도 크네.”

“누구야?”

“왜 날 봐? 마누라한테 맞아 죽을 일 있어?”

그때 사람들의 등 뒤에서 한 사람이 입을 열었다.

“이야기를 더 듣고 싶은데.”

나직하지만 울림이 있는 목소리. 앞서 객잔에 들어온 사내였다. 죽립을 푹 눌러쓴 탓에 얼굴은 제대로 보이지 않았고, 전신을 감싼 피풍의는 먼지투성이였다.

‘무림인.’

누가 말을 보태지 않아도 사람들은 모두 사내의 정체를 그렇게 생각했다.

매담자가 은자와 사내를 번갈아 보며 침을 삼켰다.

“감사합니다, 대협. 혹시 듣고 싶은 이야기가 있으신지……?”

그의 경험상 무뢰배와 무림인은 한 끗 차이다. 매담자는 살 만큼 산 노인이었으나 고작 이런 곳에서 칼 맞아 죽고 싶진 않았다.

다행히도 죽립 사내는 후자에 해당했다.

“간단하게. 사실만.”

목소리를 들어 보면 어린노무 새끼가 분명한데, 무공을 배운 어린노무 새끼다. 함부로 대할 순 없었다. 매담자는 손바닥을 비볐다.

“제가 아는 선에서 싹 다 말씀드리겠습니다요.”

“노인장이 말한 그 전투, 며칠 전 이야기요?”

“닷새 전입니다.”

“누가 이겼소?”

“태원진가가 시원하게 발라 버렸습죠. 산서잠룡이 큰 활약을 했다고 들었습니다.”

“그럼 항산검문은…… 지금 뭐라고 했소?”

“예?”

“산서, 뭐?”

“아, 산서잠룡 말입니까요?”

“맞소. 처음 듣는 별호인데.”

“외지에서 오셨다면 그럴 수도 있지요. 진 공자가 두각을 드러낸 것이 얼마 되지 않았으니.”

“소가주인 진위경 공자 말이오?”

“예에? 천만에요. 소가주님도 대단하지만, 이번에 가장 활약이 컸던 것은 아무래도 진 공자죠.”

“그러니까 그 진 공자가…… 잠깐, 지금 말하는 산서잠룡이 설마 삼공자 진태경과 연관이 있소?”

“동일 인물입죠.”

한동안 침묵을 지키던 사내가 손가락을 튕겼다. 두 번째 은자가 매담자의 대접에 정확히 안착했다.

“간단하게. 사실만 말해 달라고 했던 것 같은데.”

“제 불알을 걸겠습니다.”

매담자의 결연한 대답에 사내가 한숨을 내쉬었다.

“그렇다 칩시다. 항산검문은 어찌 되었소?”

“거의 봉문 직전입니다. 이공자 이소군은 진즉 죽었고, 문주인 혈랑검 이천백은 전사. 이틀 후에 후계자인 대공자도 마적 떼에 맞서다가 죽었답니다.”

“마적?”

“이 간 큰 놈들이 글쎄, 혈랑검이 죽었다는 소식에 항산검문으로 쳐들어왔답니다. 처음부터 그걸 노리고 인근을 배회하고 있었다는군요.”

“개판이군.”

“말판이죠. 마적 떼들 아닙니까.”

장내가 쥐 죽은 듯이 조용해졌다. 사람들은 저 통 큰 무림인 사내가 세 번째 은자를 매담자의 이마에 박아 넣는 모습을 기대했지만, 그는 군말 없이 자리에서 일어났다.

“이야기 잘 들었소.”

사내가 떠난 후에도 매담자의 이야기는 이어졌다. 그들은 쉴 새 없이 술을 들이켰고, 안주는 끊이지 않았다.

무림인들 간의 패권 다툼. 승리와 패배. 샛별처럼 떠오른 젊은 영웅의 이야기에 대해 입을 모아 떠들었다.

“태원진가가 산서를 넘어 중원에 우뚝 설 날이 얼마 남지 않았군. 문무겸전의 소가주에, 이번에 두각을 드러낸 산서잠룡. 그리고…… 그리고 또 누구더라.”

“진천검?”

“아, 그래. 이공자 진무경!”

“그 젊은이도 대단하지. 백 년에 한 번 나올까 말까 한 무학의 천재라며?”

“근데 지금은 어디서 뭐 하고 있대?”

“몰러. 이 시간이면 자고 있겄지.”

객잔의 술자리가 이어지는 그 순간에도 사내는 묵묵히 말을 몰았다. 굳게 다문 입과는 달리 그의 귀는 활짝 열려 있었다.

“자네 그 얘기 들었나?”

“또 산서잠룡인가? 귀에서 피 나니까 작작 하게.”

“그렇긴 한데…… 이건 일급 정보야. 태원진가 수문각 무사한테 들은 거거든.”

“뭔데 그렇게 호들갑이야?”

“천력부라고 아나?”

“녹림십팔채의 그 천력부? 산적 주제에 절정 고수라는 그놈?”

“그래. 바로 그 천력부도 산서잠룡이 해치웠다는군!”

“헛소문 아니야? 천력부쯤 되는 작자가 굳이 왜 산서성까지 와서 산적질을 해?”

“난들 아나. 더 놀라운 건 그 자리에 염라편(閻羅鞭)도 있었다는 거지.”

“헉. 염라편까지!”

“홍화루에서 마부로 위장하고 있다는데. 혹시 갈 일 있으면 주의하게나.”

사람들의 끊이지 않는 대화 속에서 가장 많이 들리는 단어는 두 가지였다. 산서잠룡. 그리고 진태경.

목적지에 가까워질수록 소문은 눈덩이처럼 불어나 크기를 키웠다.

‘고금 제일의 미남에. 하늘이 내린 천무지체. 불의를 보면 참지 못하는 협객.’

죽립 사내는 말에 박차를 가했다. 산서잠룡의 산 자만 들어도 내상을 입은 것처럼 속이 울렁거리고 머리가 아파 왔다.

마침내 그가 목적지에 도착한 것은 다음 날 아침이었다.

‘오랜만이군.’

수년 만에 돌아온 그곳은 여전했다.

굳이 변화가 있다면.

“멈춰라! 이 몸은 산서성의 패자, 대태원진가의 수문조장이자 산서잠룡의 오른팔 혁무진이다. 순순히 신원과 목적을…….”

영 상태가 안 좋아 보이는 놈이 수문조장을 맡고 있다는 것.

죽립 사내, 진무경이 한숨을 내쉬었다.

“입 닥치고 문 열어.”



* * *



쏴아아.

물결이 흐른다. 잔잔하게, 그리고 거침없이.

단전에서 흘러나온 공력은 수백 개의 혈도를 질주하다가, 마침내 본래 있어야 할 자리로 돌아갔다.

띠링.



- [운기조식]을 성공적으로 마쳤습니다.

- [진가심법]의 경지가 팔 성으로 상승합니다.



시스템 알림을 들으며 눈을 떴다.

‘팔 성이라.’

분명 좋은 소식이지만 살짝 실망감이 드는 건 어쩔 수 없다.

내가 기다렸던 알림은 따로 있었으니까.

‘공력이나 좀 오르지.’

시스템을 사용할 수 있게 된 지 오늘로 두 달째. 이제는 습관처럼 하는 운기조식이지만 공력은 여전히 제자리걸음이다.

‘지금 속도라면 10년은 더 걸리겠네.’

내가 익힌 진가심법의 최대 장점은 매우 안정적이라는 것이다. 일반적인 내공 심법과는 달리 움직이면서도 심법 운용이 가능할 정도다.

문제는…….

‘공력 축적 속도가 더럽게 느리다는 거지.’

무림인에게 있어 공력의 부재는 치명적인 단점이다.

일류, 이류 정도야 손쉽게 상대할 수 있겠지만 절정 고수를 적으로 만나면 목숨이 두 개여도 모자라는 것이 현실이다.

이번에 대장로의 무위를 직접 겪으면서 확실히 느꼈다.

‘대단했지, 그 영감.’

닷새가 지난 지금에도 잊히지 않는다.

아니, 닷새가 아니라 50년 후에도 잊지 못할 광경이었다.

전장을 휩쓸던 검기와 검강. 그리고 95레벨이라는 말도 안 되는 숫자.

‘일대일이었으면 얼마나 버틸 수 있었을까?’

젖 먹던 힘까지 쥐어짜도 1분은 버텼을지 의문이다.

하지만 예상치 못한 변수들이 결과를 뒤집었고, 나는 그의 가슴에 창을 박아 넣을 수 있었다.

그리고 시스템은 보상을 잊지 않았다.

“상태창 오픈.”

띠링.



상태창



[Lv.50 진태경]

직업 : 일류 무인

명성 : 1180 (+150)

칭호 : 4개 (칭호 효과 적용 중)

- 산서잠룡 (모든 능력치 +10, 명성 +100)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 초보 수련자 (수련 속도 +10%)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

근력 : 135 (+15)체력 : 142(+15)

민첩 : 130 (+15)지력 : 25(+15)

매력 : 25(+15)공력 : 15년

잔여 포인트 : 100

- 잔여 포인트를 분배하십시오.





“크으.”

지난 며칠간 수십 번은 확인한 상태창이지만 질리지가 않는다. 혈관에서 탄산이 톡톡 튀는 이 기분.

‘대장로와 싸운 보람이 있구만.’

목숨을 건 도박이었던 만큼 보상도 빵빵했다.

단숨에 13레벨을 껑충 뛰어올랐고, 명성은 세 자릿수에 접어들었으며 칭호에도 변화가 있었다.

“칭호 확인.”

띠링.



상태창



[산서잠룡]

등급 : 절정

효과 : 모든 능력치 +10, 명성 +100

설명 : 이제 당신의 명성은 산서성 곳곳에 퍼져 있습니다. 그러나 천하는 넓고 고수는 많은 법. 결코 자만하지 마십시오!





아직 전국구 급은 아니지만 산서성이라는 우리 지역구에서는 침 좀 뱉는다는 말인데…….

‘그래서 산서잠룡인가?’

고양시 꿀주먹. 인천 피바다. 뭐 그런 느낌.

어쨌든 내게는 잘된 일이다. 산서잠룡이라는 좋은 칭호에, 얼마 전까지만 해도 꼬리표처럼 붙어 있던 [가문의 수치]가 사라지니 앓던 이가 빠진 것처럼 시원했다.

‘이렇게 또 강해졌구나.’

문득 무림으로 돌아오기 전, 최 팀장과 했던 대화가 떠올랐다. 다음에 나를 볼 때는 계약서를 고쳐야 할 거라는 말.

그는 허풍으로 받아들였겠지만 나는 사실로 만들었다.

‘최대한 강해져서 돌아간다.’

내가 얻을 수 있는 힘을 최대한 얻어서 돌아갈 것이다.

공력, 무공, 능력치. 그게 뭐든 간에 모조리.

다음 로그아웃 때는 B급, 아니 A급 헌터 정도는 되어서 금의환향을…….

“어?”

아니, 잠깐만.

나 지금 뭔가 엄청 중요한 걸 잊고 있는 것 같은데.

‘뭐지?’

하고 있던 모든 걸 멈추고 기시감의 정체를 고민하던 그때였다.

“여기냐?”

“옙. 틀림없습니다요.”

문밖에서 두런두런 들리는 두 개의 목소리. 그중 하나가 혁무진이라는 사실을 알아차린 순간.

쾅!

굉음과 함께 문이 뜯겨 나갔다.



* * *



나는 기본 상식을 중요시하는 사람이다.

휴지는 휴지통에. 담배는 흡연 구역에서. 야동은 일본.

그리고 다른 사람 방에 들어갈 때는 노크를.

특히 남자 혼자 쓰는 방에 노크도 없이 벌컥 들어오는 놈들은 무기징역에 처해야 한다고 생각하는 사람이다.

“여기 있었군.”

그런 의미에서 눈앞의 이놈은 사형이다.

문을 박살 냈으니까 무기징역. 초면에 말을 놨으니 가중 처벌.

나는 점잖게 대꾸했다.

“어, 여기 있다.”

놈이 눈을 동그랗게 떴다. 아오지 탄광에서 20년쯤 일하다 왔는지 얼굴이 시커멓게 때가 껴 있었다.

젊은 나이에 초라한 행색. 대충 스토리가 나오는 듯했다.

‘떠돌이 무사1.’

산서잠룡의 명성을 듣고 무작정 찾아온 엑스트라.

나는 놈과 비슷한 표정을 짓고 있는 혁무진에게 물었다.

“얘 뭐냐?”

혁무진이 그대로 얼어붙었다. 귀신이라도 본 얼굴이다.

“모르세요?”

“내가 어떻게 알아, 인마. 소개를 해 줘야 알지.”

나는 투덜거리며 [기감]을 끌어 올렸다. 푸른 원이 두 사람을 향해 쭉 뻗어 나간다.



[Lv.??? 진무경]



진무경이라. 레벨 좀 되나 보네?

“응? 진무경?”

레벨창 한 번 보고. 얼굴 한 번 보고.

그 짓을 서너 번 반복하다가 떨리는 마음으로 그에게 다가갔다.

“저, 잠시만.”

“…….”

문질문질.

깨끗하던 내 옷소매가 까맣게 변한다. 이어 잘생긴 얼굴이 드러났다. 어디서 많이 본 얼굴이다 싶더니 매일 아침 세수하면서 마주하는 내 얼굴이다.

‘완전히 붕어빵이네.’

허허.

나는 어색하게 웃어 보였다. 떠돌이 무사1은 얼음장 같은 시선으로 나를 노려보고 있었다.

“오랜만이야, 형.”
```

### Current accepted English

```markdown
# Chapter 63

Creeeak.

The man entered the inn around early afternoon.

The old wooden door creaked, but no one inside turned to look. Not even the owner and the waiter, who should have been rushing to greet a customer.

“So? So what happened?”

“Quit keeping us in suspense and tell us already!”

At the crowd’s eager urging, the old man tapped his empty bowl.

Only after the owner filled it to overflowing with bamboo-leaf wine did the old man—the storyteller—go on.

“A fierce battle broke out. Blood Wolf Sword Lee Cheonbaek brought no fewer than thirty thousand men. Compared to that, the Jin Family of Taiyuan had only three hundred elites.”

“Thirty thousand!”

“My word, thirty thousand!”

“Does that make any sense? Mount Heng Sword Sect isn’t one of the Nine Sects and One Gang…”

The storyteller stopped mid-sip and spat the wine back out.

“Fuck this. This booze tastes like shit. I’m leaving. Hear the rest from the guy who brought up the Nine Sects and One Gang.”

“Now, hold on. Why are you doing this?”

“Who just said that?”

The mood turned ugly, and a young man was shoved back, half-stumbling.

Only then did the storyteller set his half-raised ass back down. His stomach had turned, and his nerve had thickened to match.

Tap, tap.

Everyone frowned as the storyteller tapped his empty bowl. Now they had to give him money, not more wine. They were in the middle of an unspoken standoff when—

Ting.

“Huh?”

The storyteller’s narrowed eyes flew open. A gleaming silver tael had come flying from somewhere.

“Well. Whoever that is, they’re a big spender.”

“Who was it?”

“Why are you looking at me? You trying to get me beaten to death by my wife?”

That was when someone spoke from behind the crowd.

“I’d like to hear more.”

The voice was quiet but resonant. It belonged to the man who had entered the inn earlier. His face was hidden under a bamboo hat pulled low, and the cloak wrapped around him was caked with dust.

*A martial artist.*

Nobody needed to say it. Everyone in the inn came to the same conclusion.

The storyteller looked from the silver to the man and swallowed.

“Thank you, Great Hero. Is there something in particular you’d like to hear…?”

In his experience, ruffians and martial artists were only a hair apart. He was an old man who had lived his share of years, but he had no desire to get stabbed to death in a place like this.

Fortunately, the man in the bamboo hat was the latter.

“Keep it simple. Just the facts.”

Judging by the voice, he was clearly a young bastard—but a young bastard who had learned martial arts. The storyteller couldn’t treat him carelessly. He rubbed his palms together.

“I’ll tell you everything I know, sir. The whole lot.”

“That battle you mentioned. How many days ago was it?”

“Five days ago.”

“Who won?”

“The Jin Family of Taiyuan wiped the floor with them. I heard the Sleeping Dragon of Shanxi played a major role.”

“Then Mount Heng Sword Sect… What did you just say?”

“Excuse me?”

“Shanxi, what?”

“Ah, you mean the Sleeping Dragon of Shanxi?”

“That’s right. I’ve never heard that alias before.”

“If you’re from out of town, that would make sense. Young Master Jin only rose to prominence recently.”

“You mean Young Master Jin Wikyung, the Lesser Family Head?”

“What? Not at all. The Lesser Family Head is impressive too, but the one who played the biggest role this time was Young Master Jin.”

“So that Young Master Jin… Wait. Is the Sleeping Dragon of Shanxi somehow related to Third Young Master Jin Taekyung?”

“They’re the same person.”

The man, who had been silent until then, snapped his fingers. A second silver tael landed perfectly in the storyteller’s bowl.

“I believe I asked you to keep it simple and stick to the facts.”

“I’ll stake my balls on it.”

At the storyteller’s resolute answer, the man sighed.

“Let’s say that’s true. What happened to Mount Heng Sword Sect?”

“They’re on the verge of closing their gates. Second Young Master Lee Seogeun had already died, and their Sect Leader, Blood Wolf Sword Lee Cheonbaek, fell in battle. Two days later, even their successor—the First Young Master—was killed fighting a band of mounted bandits.”

“Mounted bandits?”

“These gutsy bastards heard the Blood Wolf Sword was dead and stormed Mount Heng Sword Sect. Word is they’d been circling nearby from the start, waiting for their chance.”

“What a dog’s mess.”

“A horse’s mess, more like. They’re mounted bandits, aren’t they?”

The inn went dead quiet. Everyone expected the big-spending martial artist to drive a third silver tael into the storyteller’s forehead.

Instead, the man rose from his seat without a word.

“I heard you.”

Even after the man left, the storyteller’s tale went on. They drank without pause, and the snacks never ran out.

They all talked about the struggle for supremacy among martial artists. Victory and defeat. The young hero who had risen like a morning star.

“It won’t be long before the Jin Family of Taiyuan steps beyond Shanxi and stands tall in the Central Plains. The Lesser Family Head, who excels in both civil and martial arts, the Sleeping Dragon of Shanxi, who rose to prominence this time, and… and who else was it?”

“The Heaven Shaking Sword?”

“Ah, right. Second Young Master Jin Mukyung!”

“That young man is incredible too. They say he’s a martial arts genius who appears once in a hundred years, if that.”

“But where is he now? What’s he doing?”

“Dunno. At this hour, he’s probably asleep.”

Even as the drinking went on inside the inn, the man rode in silence. His mouth was shut tight, but his ears were wide open.

“Did you hear?”

“The Sleeping Dragon again? My ears are bleeding. Give it a rest.”

“Yeah, but this is grade-one intel. I heard it from a gate guard of the Jin Family of Taiyuan.”

“What’s the fuss?”

“You know the Heavenly Axe?”

“The Heavenly Axe of the Eighteen Strongholds of Green Forest? That mountain bandit who’s a Peak master anyway?”

“That’s the one. Word is the Sleeping Dragon of Shanxi took him out too!”

“Isn’t that just a rumor? Why would someone like the Heavenly Axe come all the way to Shanxi to play bandit?”

“How would I know? The wilder part is that Yama Whip was there too.”

“Yama Whip too?!”

“They say he’s disguised as a coachman at Honghwaru. If you ever have reason to go there, watch yourself.”

Of all the talk that never stopped, two words came up most often.

The Sleeping Dragon of Shanxi.

And Jin Taekyung.

The closer the man came to his destination, the more the rumors swelled like a snowball, growing larger and larger.

*The most handsome man of all time. A heaven-bestowed martial physique. A chivalrous hero who cannot stand injustice.*

The man in the bamboo hat spurred his horse. Even the Shan in Sleeping Dragon of Shanxi was enough to make his stomach churn and his head ache, as if he had taken an internal injury.

He finally reached his destination the next morning.

*Been a while.*

The place he had returned to after several years was unchanged.

If there was any difference worth mentioning—

“Stop right there! I am the hegemon of Shanxi, Captain of the Gatekeepers of the Great Jin Family of Taiyuan, and the right-hand man of the Sleeping Dragon of Shanxi—Hyuk Mujin! State your identity and purpose, and—”

—it was that a guy who looked like hell was serving as Captain of the Gatekeepers.

The man in the bamboo hat, Jin Mukyung, sighed.

“Shut up and open the gate.”

* * *

Whoooosh.

The water flowed. Calm, and unimpeded.

The internal energy that had left my dantian raced through hundreds of acupoints, then finally returned to where it belonged.

Ding!

> **System**
>
> - You have successfully completed **Qi Circulation**.
>
> - The realm of the **Jin Family’s Cultivation Technique** has risen to the Eighth Stage.

I opened my eyes as I listened to the System notification.

*The Eighth Stage.*

It was clearly good news, but I couldn’t help feeling a little disappointed.

The notification I had been waiting for was a different one.

*Could’ve at least bumped my internal energy.*

Today marked two months since I had been able to use the System. Circulating my qi had become a habit, but my internal energy was still going nowhere.

*At this rate, it’ll take another ten years.*

The greatest strength of the Jin Family’s Cultivation Technique I had learned was its stability. Unlike ordinary internal cultivation techniques, I could even run it while moving.

The problem was…

*The accumulation speed is fucking terrible.*

For a martial artist, a lack of internal energy was a fatal weakness.

I could handle First Rate and Second Rate opponents easily enough, but if I ran into a Peak master as an enemy, even two lives wouldn’t be enough.

I had felt that clearly after tasting the Head Elder’s martial might firsthand.

*That old man was something else.*

Even after five days, I still couldn’t forget it.

No. Not five days.

Even fifty years from now, I would never forget that sight.

The Sword Energy and Sword Force that had swept the battlefield. And that absurd number—Level 95.

*How long could I have lasted against him one-on-one?*

Even if I had wrung out every last ounce of strength, I doubted I could have held on for a minute.

But unexpected variables had overturned the result, and I had been able to drive my spear through his chest.

And the System had not forgotten my reward.

“Open Status Window.”

Ding!

> **System**
>
> **Status Window**
>
> **Lv. 50 Jin Taekyung**
>
> **Class:** First Rate Martial Artist  
> **Fame:** 1,180 (+150)  
> **Titles:** 4 (Title effects active)
>
> - **Sleeping Dragon of Shanxi** — All Stats +10, Fame +100
> - **Scion of a Prestigious Family** — All Stats +5, Fame +50
> - **Novice Trainee** — Training Speed +10%
> - **Gambler** — Combat-related Stats +10% in one-on-one combat
>
> **Strength:** 135 (+15)  
> **Stamina:** 142 (+15)  
> **Agility:** 130 (+15)  
> **Intelligence:** 25 (+15)  
> **Charm:** 25 (+15)  
> **Internal Energy:** 15 years
>
> **Remaining Points:** 100
>
> - Distribute your Remaining Points.

“Ohhh, yeah.”

I had checked that Status Window dozens of times over the past few days, and I still wasn’t sick of it. It felt like carbonation popping in my veins.

*Fighting the Head Elder was worth it.*

It had been a gamble with my life on the line, so the reward was stacked.

I had jumped thirteen levels in one stroke, my Fame had entered the triple digits, and my Titles had changed.

“Check Titles.”

Ding!

> **System**
>
> **Status Window**
>
> **Sleeping Dragon of Shanxi**
>
> **Grade:** Peak  
> **Effect:** All Stats +10, Fame +100  
> **Description:** Your fame has now spread throughout Shanxi. But the world is vast and masters are many. Never become complacent!

I wasn’t a nationwide name yet, but in Shanxi—my local district—I apparently had some real clout…

*So that’s why it’s called the Sleeping Dragon of Shanxi?*

Goyang’s Honey Fist. Incheon’s Sea of Blood. That kind of thing.

Either way, it was good for me. I had a solid new Title, and Family Shame, the tag that had clung to me until recently, was gone. It felt as good as having an aching tooth pulled.

*I’ve gotten stronger again.*

I suddenly remembered what I had told Team Leader Choi before coming back to Murim.

“Next time you see me, you’ll have to revise the contract.”

He had probably taken it as a bluff. I had made it a fact.

*I’ll get as strong as I can, then go back.*

I would take every scrap of power I could get before I returned.

Internal energy, martial arts, stats. Whatever it was, all of it.

On my next Logout, I’d be a B-rank Hunter—no, an A-rank Hunter—and return home in glory…

“Huh?”

Wait.

I was forgetting something incredibly important.

*What is it?*

I stopped everything I was doing and tried to pin down that sense of déjà vu.

That was when—

“Is it here?”

“Yessir. No mistake.”

Two voices murmured outside the door. The moment I realized one of them belonged to Hyuk Mujin—

Boom!

The door tore off its hinges with a thunderous crash.

* * *

I take basic common sense seriously.

Tissues go in the trash. Cigarettes belong in the smoking area. Porn comes from Japan.

And when you enter someone else’s room, you knock.

I especially believe that anyone who barges into a room a man uses alone, without knocking, deserves life in prison.

By that standard, the bastard in front of me got the death penalty.

He had smashed the door, so that was life. He had spoken down to me on first meeting, so that was an extra charge.

I answered him politely.

“Yeah. I’m here.”

The bastard’s eyes went round. His face was black with grime, as if he had spent twenty years in the Aoji Coal Mine.[^1]

Young, in shabby clothes. The story practically wrote itself.

*Wandering Martial Artist #1.*

An extra who had come running after hearing about the Sleeping Dragon of Shanxi.

I turned to Hyuk Mujin, who was wearing a similar expression.

“What’s with this guy?”

Hyuk Mujin froze solid. He looked like he had seen a ghost.

“You don’t know him?”

“How would I know, idiot? You have to introduce people.”

Grumbling, I raised my Qi Sense. A blue circle stretched toward the two of them.

> **System**
>
> **Lv. ??? Jin Mukyung**

*Jin Mukyung. Guess he’s pretty high-level.*

“Huh? Jin Mukyung?”

I looked at the Level window once.

Then at his face.

I did that three or four times, then walked up to him with my heart pounding.

“Uh. Just a second.”

“…”

Rub, rub.

My clean sleeve turned black. Then a handsome face emerged. I thought I had seen it somewhere before, and then I realized it was the face I met every morning when I washed up.

*Carbon copies.*

I gave an awkward laugh. Wandering Martial Artist #1 was glaring at me, his eyes like ice.

“Long time no see, hyung.”

[^1]: Aoji Coal Mine was a notorious coal mine in North Korea, associated with harsh working conditions.
```

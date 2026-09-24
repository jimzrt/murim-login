<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0957.txt",
      "sha256": "3b3589b2892250a44d64dcc63f9cae46718f7401947bffb470bcf1bc31bf88fd",
      "bytes": 13281
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "98d6e206c36104b95d9300ede8ad0494c213f2a5bccaa2f64086f31070eb5277",
      "bytes": 2126
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1137d196ebb7a3df40f3a1d1d2799f090a60df6cd515b0bab92da528b06e39b2",
      "bytes": 234528
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "ccecdb57ff6bd2a2cd78c76a07f386be93f7c588b161be36fea7cae51f5c0722",
      "bytes": 642
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d3c87ebeff1f9ddee738bcc0117c39c916dd024e6e89e36c9640f902337dda26",
      "bytes": 759
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "034d87ca480470c40d2887945899e50f7003926413f99aa24165725c940e908b",
      "bytes": 918
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "a052c001f2b7607dc2d30d79c966ee268a31a4ead9a74934452489bdffce4cb7",
      "bytes": 1119
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a20f593116af26c44513a62978f9565dd0243e9d8b9b1d44d682a18b3511712e",
      "bytes": 267908
    }
  ],
  "estimated_tokens": 9710
}
-->

# Durable State Update — Chapter 957

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 957. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 957. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 957,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 957,
    "continuity_sources": [957],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The steppe army has begun its assault on Eight Spring Gorge; the defenders’ battle remains unresolved, and Jamukha has ordered Chinggen to seize the cliffs.",
    "Jin Wikyung promised his defenders they will celebrate the next Double Ninth Festival together on Mount Heng.",
    "Temur knows the man beside Jamukha is Chinggen’s killer and impostor but conceals his knowledge.",
    "Jamukha has long awaited a call from “that person”; the person’s identity and purpose remain unknown.",
    "The Emperor remains gravely ill from Blood Soul Gu; saving him requires him to die once, and Taekyung’s quest to treat him remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "The real Chinggen was killed; an impostor wearing his face continues to accompany Jamukha.",
    "Jin Mukyung wields a sword forged by Jang Taebo from material comparable to Ten-Thousand-Year Cold Iron; the Jin forces also use armor made from the Water God Dragon’s remains.",
    "Taekyung resolves to trust his allies rather than try to bear every burden alone."
  ],
  "continuity_sources": [
    955,
    956
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge fare, and can the defenders hold the cliffs?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will the Chinggen impostor do, and what is their purpose?"
  ],
  "safe_through": 956,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 일신     | **One God**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 명성               | **Fame**                       |
| 태원     | **Taiyuan**            |
| 팔천협    | **Eight Spring Gorge** |
| 노부      | **this old man / I**                                            |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 좌장 | **presiding chair** | Authority overseeing the Star-Array Grand Banquet. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 심마니 | **Mountain Herb Gatherer** | Achievement earned after obtaining the Thousand-Year Snow Ginseng. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 흑목조간 | **black-wood fishing rod** | The Dongting Fisherman's distinctive weapon; the broken rod is his only known trace. |
| 천잠사 | **Heavenly Silkworm Thread** | Rare treasure used as the Dongting Fisherman’s fishing line and weapon. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 956
- **Aliases:** None
- **Role:** The real Chinggen was a Khan of the eastern grasslands and Temur’s brother, but he was killed in the attack on their gathering; an impostor now wears his face.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur was Chinggen’s cousin and sworn brother through the anda oath; an impostor wearing Chinggen’s face now accompanies Jamukha and deceives Temur.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 956
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 492
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he joined Dark Heaven, committed the Dongting Lake massacre, was captured alive, and is now severely injured with crushed limbs, substantial Internal Injury, and serious Fear exposure after encountering the Water God Dragon at Donghu Stronghold.
- **Personality:** The Dongting Fisherman appears eerily emotionless and savage, eating live fish raw and reacting violently when provoked.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 956
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he can agonize over costly decisions but commits firmly once resolved.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and the people of Shanxi—including many commoners the Jin Family once aided—are willing to help defend their home alongside him.

## Korean source

```text
＃957화



팔천협을 양옆으로 둘러싼 절벽은 그 자체로 거대한 성벽이나 다름없었다.

왜 아니겠나.

다른 모든 것을 떠나 그 높이만 무려 삼십여 장이다.

먼 옛날 대륙을 통일했던 폭군이 백성들의 고혈을 쥐어짜서 만든 장성(長城)조차 그 높이는 삼 장 남짓에 불과하다.

만약 우회하여 이곳까지 닿기 위해서는 며칠에 걸쳐 험준한 산등성이를 넘어야 했고, 정면으로 뚫으려면 아득게 솟아 있는 암반을 타고 올라야 한다.

물론 그 자체가 불가능한 일은 아니다.

숙련된 심마니나 사냥꾼도 충분한 대비책을 마련한다면 긴 시간에 걸쳐 오를 수 있다는 것이 정설이었다.

울퉁불퉁한 암벽으로 이루어진 절벽은 손과 발의 지지대가 되어 주기도 하니까.

단.

협곡을 사이에 둔 두 개의 절벽을 가득 채운 일천의 궁수가 불청객을 달가워하지 않는다면 이야기는 달라진다.

지금처럼.

으아아아아!

비명인지 함성인지 모를 외침과 함께 개미 떼처럼 절벽을 향해 몰려드는 유목민들.

바로 그 순간이었다.

날카로운 눈빛으로 발아래 펼쳐진 어둠 속 광경을 응시하던 군관(軍官)들이 일제히 입을 연 것은.

“전원!”

“발시(發矢)!”

펄럭!

어둠 속에서도 흐릿하게 색이 구별되는 붉은 깃발이 벼락처럼 내려감과 함께, 팽팽하게 당겨져 있던 일천 개의 활시위가 비로소 자유를 되찾았다.

투투퉁, 솨아아악!

깊은 산속에서 울려 퍼지는 파도 소리.

흐릿한 달빛 사이를 가르며 쏘아진 화살들이 파르르 몸을 떨었다. 마치 이 짧은 여행의 종착지에 무엇이 기다리고 있는지 알고 있는 것처럼.

터텅! 푸푸푹!

“끄아아아악!”

“안돼! 홀로구!”

비명과 함께 사방에 나뒹구는 신형들.

그러나 아득한 절벽 위에서 그 참혹한 광경을 바라보던 한 사내의 표정은 깊게 가라앉아 있었다.

‘모든 궁수를 동원하여 집중 사격을 가했음에도 고작 일백이라.’

은은한 정광(正光)이 흐르는 두 눈동자는 사내가 상승의 무공을 익혔다는 증거이며, 발아래에 펼쳐진 짙은 어둠 속을 꿰뚫어 볼 능력이 있다는 뜻이기도 하다.

‘예상보다 놈들의 피해가 적군. 방어를 위해 미리 말을 버리고 방패로 대비하고 있었다고 해도 이건…….’

결국 답은 하나다.

짧은 생각 끝에 결론을 내린 사내는 지휘봉을 들었고, 긴장한 얼굴로 대기 중이던 부관은 상관의 명령을 화살에 묶어 맞은편 절벽으로 날려 보냈다.

쉬익.

비록 원만한 곡선을 그렸다고는 해도 화살은 화살.

그러나 파공성과 함께 날아든 그것은 누군가의 손아귀에 빨려가듯 붙잡혔다.

그것도 아주 손쉽게.

턱.

보지도 않고 화살을 잡아낸 노인은 화살대에 묶여 있던 전서(傳書)를 풀어 주위의 군관에게 건넸다. 갑옷을 갖춰 입은 군관은 신속하게 전서의 내용을 훑었다.

“그래, 뭐라던가?”

“피해가 확연히 줄어든 것으로 보아, 놈들이 정예들을 동원한 것 같다고 합니다.”

“골치 아프긴 한데…… 뭐, 아군의 입장에서는 오히려 잘된 일일 수도 있겠군.”

노인은 새하얀 수염을 쓰다듬었다.

이 압도적인 높이의 절벽은 수성(守城)을 위한 최고의 요충지나 다름없다.

팔천협을 천혜의 요새로 거듭나게 한 가장 큰 요인 중 하나이자, 지금껏 있었던 두 차례의 대전(大戰)에서 결정적인 승리를 거둘 수 있었던 이유.

절벽으로 투입된 적들의 정예병들은, 이제 곧 지옥도를 보게 될 것이다.

“그리고 또?”

“협곡을 정면 돌파하려는 적들은 우군(右軍)이 견제할 테니, 우리 좌군(左軍)은 절벽을 오르는 자들을 처리해 달라 청하셨습니다.”

“청은 무슨. 나이로 따졌을 때는 노부가 좌장(座長)이지만, 지금 같은 전장에서는 장군의 명령대로 따라야지. 안 그런가?”

군관은 대답 대신 애매하게 미소를 지었다.

그가 아는 눈앞의 노인은 무림에서 명성을 날린 엄청난 고수고, 맞은편의 사내는 까마득한 상관이다.

어중간한 중급 지휘관인 그로서는 당장 내놓을 수 있는 대답이 마땅치 않았다.

그저 명령에 따라 조심스럽게 제안할 수밖에.

“도지휘첨사(都指揮僉事)께서 청하시길…….”

“됐네. 됐어. 결국 이 늙은이가 나서야 한다는 말 아닌가?”

손을 내저은 노인이 허리를 두드리며 일어났다. 그의 손에는 어느새 거무튀튀한 무언가가 들려 있었다.

퉁.

지팡이라고 하기에는 그 길이가 일장에 달할 정도로 길고, 나무라고 부르기에는 암반과 부딪치는 소리가 제법 무겁다.

‘저건 도대체 뭐지?’

들리지 않는 군관의 의문을 뒤로한 채, 노인은 쉴 새 없이 화살을 쏘아 대는 궁수들의 앞으로가 털썩 걸터앉았다.

전투가 시작되기 전, 진위경과 나누었던 대화를 떠올리며.



‘노 선배께서는 절벽 위를 맡아 주셔야겠습니다.’

‘그간 빚을 졌으니 응당 따라야겠지만…… 이 제안은 자네답지 않군. 차라리 노부가 밑에 있는 것이 훨씬 더 도움이 되지 않겠나?’



노인의 반박은 일견 당연했다.

만오천의 병력 중 가리고 가려 뽑은 일천의 궁수가 절벽 위를 점하고 화살비를 쏟아내는데, 살아서 절벽을 오를 적들이 몇이나 될 것이며 고강한 고수가 왜 필요하단 말인가.

그러나 망설임 없이 돌아온 진위경의 대답은 단호했다.



‘맞습니다. 놈들도 그리 생각하겠지요.’

‘……!’

‘놈들은 절벽을 오를 겁니다. 반드시.’

‘자네, 이미 확신하고 있군.’

‘지상의 아군은 온 힘을 다해 결사 항전할 것입니다. 시간의 차이만 있을 뿐, 결국 놈들은 절벽을 노릴 것입니다. 그리고 그중에는 가장 뛰어난 정예들 역시 포함되어 있겠지요.’

‘바로 그 정예들을, 노부가 막아라?’

‘절벽을 오르려는 적들의 시도를 막아 내면 큰 타격을 입힐 수 있습니다. 그곳만 끝까지 지켜 낸다면 한참이나 기울어 있는 저울추를 수평으로 맞출 수 있지요.’



그제야 노인은 떠올렸다.

비록 일 년도 채 되지 않는 짧은 시간이기는 하나, 그가 보고 겪은 태원진가의 소가주는 늘 현명한 선택만 해 왔다는 것을.



‘좋아. 자네가 원하는 대로 노부가 이번 전투에서 반드시 대어(大漁)를 낚아 주지.’

‘너무 무리하지는 마십시오. 노 선배께서 완치되셨다고는 하지만 충분한 회복 기간이…….’

‘걱정 말게. 태원진가에는 이미 두 번이나 목숨을 빚진바, 내 이번에 그 값을 톡톡히 치러 줄 테니.’



무림인은 은원(恩怨)을 잊지 않는다.

늙고, 적잖은 명성을 쌓은 무림인일수록 더더욱 그렇다.

그리고 노인은 두 가지 경우에 모두 해당하는 사람이기도 했다.

그는 어느 문파에도 몸담지 않은 채 고향 땅에서 일평생을 보냈고, 초절정이라는 지고한 경지에 오른 후에도 그곳을 떠나지 않았다.

노인은 자신이 나고 자란 고향에서 뼈를 묻을 생각이었다.

어느 날, 빼어난 미모를 지닌 한 여인과의 만남 직후 이지를 상실하기 전까지는.

“드디어…… 빚을 갚을 때가 왔군.”

노인은 낮게 가라앉은 목소리로 중얼거렸다.

그가 빚을 갚아야 할 대상은 타의에 의해 빼앗겼던 자신의 정신을 되돌리고, 수개월에 걸쳐 극심한 부상까지 치료해 준 태원진가뿐만이 아니다.

암천(暗天).

놈들에게도 원한이라는 빚을 갚아야 한다.

아니, 복수해야 한다.

“그래, 오너라.”

왜소한 체구의 노인은 흐릿하게 웃으며 자신의 애병(愛兵)을 쥐었다. 그리고 어릴 적부터 헤아릴 수 없이 반복했던 그 동작으로, 힘차게 두 팔을 떨쳤다.

후웅.

자그마치 삼 장에 달하는 애병이 거무튀튀한 섬광을 흩뿌리며 낭창하게 휘어진다.

그 끝에 이어진 새하얀 은빛 선과 갈고리가, 화살비를 피해 절벽을 기어오르던 적들을 향해 쏘아졌다.

슈화아아악! 서거걱!

사방을 찢어발기는 새하얀 빛줄기.

살과 뼈가 두부처럼 갈라지고, 갑옷과 함께 토막 난 수십 개의 사지가 절벽 아래로 미끄러진다.

압도적인 힘.

일신의 무위도, 지형적 우위도 가져간 노인의 공격을 피할 수 있는 적들은 아무도 없었다.

아니, 그런 것처럼 보였다.

바로 다음 순간, 절벽에 펼쳐진 그 빼곡한 은빛 그물 사이로 붉은 섬광이 번뜩이기 전까지는.

쉭, 서걱!

바람 소리보다도 작은, 미세한 파공성.

하지만 노인은 똑똑히 느낄 수 있었다.

살아있는 것처럼 꿈틀거리며 적들을 찢어발기던 은빛 선의 일부가 조금 전의 그 일격으로 끊어졌다는 것을.

그리고 그 붉은 섬광에 담긴 힘은, 결코 자신의 아래가 아니라는 것을.

‘강기(罡氣)……!’

틀림없다.

단 한 번의 휘두름으로 강기를 머금은 천잠사(天蠶絲)를 끊어 낼 수 있는 것은 동류의 힘뿐이다.

“감히!”

쉬릭!

노호성을 내지른 노인의 손이 흐릿해졌다.

힘과 속도가 더해진 애병은 이무기처럼 몸부림쳤고, 심상치 않음을 알아차린 궁수들은 이를 악물며 활시위를 당겼다.

“집중사격하라!”

“저놈, 선두에 선 저놈이 우두머리다! 일제히 발사하라!”

투퉁! 쉬쉬쉬쉭!

푸푸푹!

“커, 커헉!”

“으아아악!”

쉴 새 없이 울려 퍼지는 파공성과 비명.

그러나 절벽 위를 뒤덮은 막강한 화망(火網)을 벗어난 그림자를 막을 수 있는 것은 아무것도 없었다.

캉!

날아드는 노인의 공격을 다시 한번 받아치고.

슈확!

전신을 향해 날아든 수십여 발의 화살을 마치 묘기를 부리듯 몸을 비틀어 피해 냈으며.

툭.

가파른 절벽을 밟았다.

아니, 터트리며 쏘아졌다.

콰앙! 쐐애애액!

그것은 질주인 동시에 비행이었다.

경지에 오른 벽호공(壁虎功)의 고수조차 따라 할 수 없을 만큼 쾌속했고, 태곳적부터 정해진 세상의 법칙을 정면으로 거스르며 나아갔다.

그리고 마침내.

턱.

아득한 절벽의 끝자락에 다다른 그림자는, 자신을 기다리던 노인과 마주했다.

정확히는 그의 손끝을 따라 휘몰아치는 은빛 섬광과.

후웅, 슈화아아악!

공간이 갈라졌다.

노인은 수십, 수백 조각으로 쪼개진 바람과 새하얀 강기의 빛 속에서 그림자의 얼굴을 보았다.

메마른 체구. 날카로운 눈매.

유목민임이 분명할 그 사내는, 지금 이 순간 웃고 있었다.

“……!”

콰드드득!

거대한 힘을 이기지 못한 채 힘없이 무너지는 절벽의 일각(一角).

그러나 그 어디에도 죽음의 흔적은 보이지 않는다.

절벽 위의 궁수들이 동요하던 그때, 작게 혀를 찬 노인은 텅 빈 허공을 밟은 채 우뚝 서 있는 사내를 향해 불쑥 입을 열었다.

“누구냐, 네놈은.”

사내가 대답했다.

“사냥꾼.”

“그렇다면 잘못 찾아왔군.”

“나도 처음에는 그런 줄 알았는데, 생각이 바뀌었어.”

사내, 칭겐이 노인을 바라보며 입술을 핥았다.

“좀 늙긴 했지만 꽤 먹음직해 보이는데. 안 그래?”

노인이 코웃음 쳤다.

“삼류 사냥꾼이로군. 늙은 만큼 질기다는 것도 모르다니.”

“괜찮아. 이빨이 튼튼해서.”

이를 드러내며 웃은 칭겐이 물었다.

“그래서, 그쪽은 누구신가?”

“낚시꾼.”

담담하게 대답한 노인이 덧붙였다.

“송사리들만 가득한 줄 알았는데, 생각지도 못한 월척을 낚아서 기분이 썩 괜찮아진 낚시꾼이지.”

“그 월척, 당신 같은 늙은이가 잡기에는 너무 큰 것 같은데.”

“제깟 놈이 펄떡거려 봤자 뭘 할 수 있겠나. 꼬리를 붙잡고 두어 번 내리치면 그만이지.”

“아, 그래?”

사냥꾼은 낚시꾼을 바라보며 웃었다. 지금 이 순간 그의 뇌리에는, 눈앞의 늙은 낚시꾼을 닮은 누군가의 별호가 맴돌고 있었다.

고강한 무위를 지녔음에도 강가를 떠나지 않으며, 기이한 병기를 쓰는 전대의 노고수.

“누가 사냥에 성공할지는 금방 알게 되겠지. 안 그런가? 동정어옹(洞庭漁翁).”

노인, 동정어옹이 애병인 흑목조간(黑木釣竿)을 들어 올리며 대답했다.

“과연, 월척이로다.”

슈확!

두 갈래의 바람이, 서로를 향해 맞부딪쳤다.
```

## Final English reading copy

```markdown
# Chapter 957

The cliffs flanking Eight Spring Gorge were practically enormous walls in their own right.

How could they not be?

They stood more than thirty *jang* high.

Even the Great Wall, built long ago by a tyrant who unified the continent by squeezing the lifeblood out of his people, was barely three *jang* tall.

To go around the cliffs and reach this place, an army would have to spend days crossing rugged mountain ridges. To break through head-on, they would have to climb the sheer rock face rising into the sky.

Of course, that wasn’t impossible in itself.

It was commonly accepted that even an experienced Mountain Herb Gatherer or hunter could climb one over a long period of time, provided they made sufficient preparations.

The uneven cliff face gave them footholds for their hands and feet, after all.

But—

If a thousand archers filled the cliffs on either side of the gorge and had no intention of welcoming their uninvited guests, that changed everything.

Just as it did now.

“AAAAAAAH!”

The nomads surged toward the cliffs like a swarm of ants, their cries impossible to distinguish as screams or battle shouts.

At that very moment, the officers, their sharp eyes fixed on the scene in the darkness below, spoke as one.

“Everyone!”

“Loose!”

*Flap!*

A red flag, its color barely discernible in the dark, plunged down like lightning. At once, a thousand tightly drawn bowstrings were finally set free.

*Thrum-thrum-thrum! Fwoooooosh!*

The sound of waves echoed through the deep mountains.

Arrows shot through the faint moonlight quivered as they flew, as if they knew what awaited them at the end of their brief journey.

*Clang! Thud-thud-thud!*

“Gaaah!”

“No! Holrogu!”

Bodies tumbled in every direction amid the screams.

But the expression of the man watching the gruesome sight from atop the distant cliffs remained grim.

*Even with every archer firing in a concentrated volley, we only got a hundred.*

A faint, clear light shone in his eyes—a sign that he had mastered high-level martial arts, and that he could pierce the darkness spread out below.

*Their losses are smaller than expected. Even if they abandoned their horses in advance and used shields to protect themselves, this is…*

There was only one answer.

After a moment’s thought, the man made his decision and raised his baton. His adjutant, standing by with a tense expression, tied his superior’s order to an arrow and shot it toward the opposite cliff.

*Fwish.*

It was still an arrow, though it traced a smooth arc.

And yet the moment it arrived with a sharp whistle, it was caught as if sucked into someone’s hand.

Effortlessly, at that.

*Tap.*

The old man caught the arrow without looking, untied the missive fastened to its shaft, and handed it to an officer nearby. Clad in armor, the officer quickly scanned its contents.

“Well? What does it say?”

“He says that, judging by how sharply their casualties have fallen, the enemy must have sent in their elite troops.”

“That’s a headache, but… well, it might actually be a good thing for us.”

The old man stroked his snow-white beard.

These towering cliffs were the perfect position for a siege defense.

They were one of the main reasons Eight Spring Gorge had become a natural fortress—and why the defenders had won decisive victories in both of the great battles fought here.

The enemy elites sent to scale the cliffs were about to see a hellscape.

“And what else?”

“He asked our left wing to deal with the men climbing the cliffs, while the right wing keeps the enemy attempting a frontal assault through the gorge in check.”

“Asked? I may be the senior one by age, but on a battlefield like this, I follow the general’s orders. Don’t I?”

The officer offered no answer, only an uncertain smile.

As far as he knew, the old man before him was an astonishing master with a great reputation in Murim, while the man on the opposite cliff was his superior by far.

As a middling commander, he couldn’t think of an answer to give.

All he could do was follow orders and offer a cautious suggestion.

“The Assistant Military Commissioner did ask…”

“That’s enough. Enough. In the end, it means this old man has to get involved, doesn’t it?”

The old man waved a hand, slapped his lower back, and stood up. Something dark and dull was already in his hand.

*Thump.*

It was far too long to be called a cane, reaching nearly a *jang*. And it struck the rock with a weight that made it hard to call it wood.

*What in the world is that?*

Leaving the officer’s unspoken question behind, the old man walked to the front of the archers who were firing without pause and plopped himself down.

He recalled the conversation he’d had with Jin Wikyung before the battle began.

*“Senior, I’ll need you to take charge of the cliffs.”*

*“I owe you a debt, so of course I’ll do as you ask… but this doesn’t sound like you. Wouldn’t I be far more useful down below?”*

The old man’s objection was reasonable on the face of it.

Of the fifteen thousand troops, a thousand carefully selected archers held the cliffs and poured down a rain of arrows. How many of the enemy would make it up alive? And why would they need a master with profound skill?

But Jin Wikyung’s immediate answer had been firm.

*“You’re right. They’ll think the same thing.”*

*“……!”*

*“They’ll climb the cliffs. They’ll have to.”*

*“You’re already certain of it.”*

*“Our allies on the ground will fight to the death with everything they have. It’s only a matter of time before the enemy targets the cliffs. And their very best elites will be among them.”*

*“And you want this old man to stop those elites?”*

*“If we can stop them from scaling the cliffs, we can deal them a major blow. If we hold that position to the end, we can level the scales, even though they’re tipped so heavily against us.”*

Only then had the old man remembered.

Though he’d known him for less than a year, the Lesser Family Head of the Jin Family of Taiyuan had always made the wise choice.

*“Fine. I’ll land you a big fish in this battle, just like you want.”*

*“Don’t push yourself too hard. I know you’ve recovered completely, Senior, but you still need time to recuperate…”*

*“Don’t worry. I’ve already owed the Jin Family of Taiyuan my life twice. This time, I’ll repay every bit of it.”*

People of Murim did not forget gratitude and grudges.

The older they were, and the more Fame they had built, the more so.

And the old man was both old and renowned.

He had spent his whole life in his hometown, never belonging to any sect. Even after reaching the lofty realm of Supreme Peak, he had never left it.

He’d intended to lay his bones in the place where he was born and raised.

That is, until the day he lost his mind, soon after meeting a woman of extraordinary beauty.

“At last… the time has come to repay my debt.”

The old man murmured in a low voice.

The Jin Family of Taiyuan was not the only one to whom he owed a debt. They had restored the mind that had been taken from him against his will and spent months treating his grievous injuries.

There was also Dark Heaven.

He owed them a debt of vengeance, too.

No—he had to take revenge.

“Come on, then.”

The small-framed old man smiled faintly and gripped his beloved weapon. Then, with the same motion he’d repeated countless times since childhood, he swung both arms with force.

*Whoom.*

His weapon—an impressive three *jang* long—whipped and bent as it scattered a dark, dull flash.

A white-silver line and hook trailed from its tip, shooting toward the enemies who were climbing the cliff to evade the rain of arrows.

*Shwaaaaa! Shhk!*

White streaks of light tore through everything around them.

Flesh and bone split like tofu. Dozens of severed limbs, armor and all, slid down the cliff.

Overwhelming power.

The enemies had no way to evade the old man’s attack, which combined his personal martial prowess with the advantage of the terrain.

Or so it seemed.

Until, the very next moment, a flash of red flickered through that dense silver net spread across the cliff.

*Shhk. Shhk!*

A faint whistle, quieter than the wind.

But the old man felt it clearly.

The blow had severed part of the silver line that writhed like a living thing as it tore the enemy to pieces.

And the power behind that red flash was in no way beneath his own.

*Force…!*

No doubt about it.

Only the same kind of power could sever Heavenly Silkworm Thread imbued with Force in a single swing.

“How dare you!”

*Shwick!*

The old man’s hand blurred as he roared.

His beloved weapon, imbued with strength and speed, thrashed like an imugi. The archers, sensing something was wrong, gritted their teeth and drew their bows.

“Concentrate your fire!”

“That one! The man at the front is their leader! Fire together!”

*Thrum! Sh-sh-sh-shhk!*

*Thud-thud-thud!*

“Gah… urk!”

“Aaaah!”

Whistles and screams rang out without pause.

But nothing could stop the figure that had slipped through the mighty web of arrows covering the cliff.

*Clang!*

He batted away the old man’s next attack.

*Whoosh!*

He twisted his body, dodging dozens of arrows aimed at him from every direction as if performing an acrobatic feat.

*Tap.*

He stepped onto the steep cliff.

No—he blasted off it.

*Ka-boom! Fwoooooosh!*

It was a run and a flight at once.

He moved so fast that even a master of the Wall Lizard Technique could not have replicated the feat, charging straight against the laws of the world laid down since time immemorial.

And finally—

*Tap.*

The figure reached the edge of the distant cliff and faced the old man waiting for him.

Or, more precisely, the silver flash whipping around at the old man’s fingertips.

*Whoom. Shwaaaaa!*

Space split apart.

Amid the wind cut into dozens, then hundreds of pieces and the brilliant white glow of Force, the old man saw the figure’s face.

A gaunt build. Sharp eyes.

The man was unmistakably a nomad—and at that moment, he was smiling.

“……!”

*Crack!*

A section of the cliff crumbled helplessly under the tremendous force.

But there was no sign of death anywhere.

As the archers on the cliff wavered, the old man clicked his tongue and suddenly spoke to the man standing upright on empty air.

“Who are you?”

The man answered.

“A hunter.”

“Then you’ve come to the wrong place.”

“That’s what I thought at first, too. But I changed my mind.”

The man—Chinggen—looked at the old man and licked his lips.

“You’re a little old, but you look pretty appetizing. Don’t you think?”

The old man snorted.

“Third Rate hunter. You don’t even know that the older you get, the tougher you are.”

“That’s fine. My teeth are strong.”

Chinggen bared his teeth in a grin, then asked,

“So who are you?”

“A fisherman.”

The old man answered calmly, then added,

“I thought this place was full of minnows, but I’ve just caught a whopper I never expected. It’s put me in a pretty good mood.”

“That fish looks too big for an old man like you to catch.”

“What can a brat like you do, no matter how much you flop around? I’ll grab you by the tail and smack you against the ground a couple of times. That’ll be the end of it.”

“Oh, yeah?”

The hunter looked at the fisherman and smiled. At that moment, the title of someone who resembled the old fisherman before him was circling through his mind.

A previous-generation master who had reached great heights, yet never left the riverbank—and wielded a strange weapon.

“We’ll soon see who succeeds in the hunt. Won’t we, Dongting Fisherman?”

The old man, Dongting Fisherman, raised his beloved black-wood fishing rod and answered,

“Indeed. What a catch.”

*Shwaaa!*

Two currents of wind collided head-on.
```

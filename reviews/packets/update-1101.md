<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1101.txt",
      "sha256": "8cdfb9cbea8ba53851275f74ef8585afed5381bfa6a7424ed458acecacda7e5c",
      "bytes": 12553
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6f9485d620e98b487870a3ccdf4bda212ac622f3eb071495cf2ad41b99615ec5",
      "bytes": 1428
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e58ae46a1bac772cc7720c130c81de8fb5906bb3ba1496eb8e7943cb290731fa",
      "bytes": 244132
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5b35c06a9a3ad89903c12bd15ebcaeb62c8b6f918c35c49e8e8c23d407b010ab",
      "bytes": 760
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "6135fd0533bc44596ec91e4dc3f40b5e85b4d59e6a53d31844d68eed69f7c72c",
      "bytes": 568
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8376f1560ec040ce771b6e46f755f340933e31b087c435fbda444965b1d154a5",
      "bytes": 1513
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f15b6bb616e0bd10e582c2c20db1381f3647dfe2374b0b254aed2c21ef827565",
      "bytes": 287948
    }
  ],
  "estimated_tokens": 9483
}
-->

# Durable State Update — Chapter 1101

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
1 and safe_through 1101. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1101. Profile updates may replace only one
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
  "chapter": 1101,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1101,
    "continuity_sources": [1101],
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
    "Dark Heaven and the Potala Palace are attacking Xining; the battle is underway.",
    "The defenders repelled the initial ice spikes and arrows, and their strongest fighters destroyed the Grand Mage’s water spheres and protective veil.",
    "Jeok Cheongang, the Slaughter Saint, the Bow Saint, other Supreme Peak masters, and Jin Taekyung are defending Xining; their resistance has rallied the defenders.",
    "Hulking monsters have charged and struck the city wall; the damage and outcome are unknown.",
    "The Blood Lord privately wants Jin Taekyung dead but conceals this from the Grand Mage and will not defy that person’s will."
  ],
  "continuity_sources": [
    1099,
    1100
  ],
  "open_questions": [
    "Will Xining’s wall hold after the monsters’ impact, and how will the battle develop?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Whom do the Eldest Senior Brother and Elders serve, and what was Mu Song about to reveal?",
    "Who were the new allies gathering near the river?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?"
  ],
  "safe_through": 1100,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 절정고수                | **Peak master** / **Peak martial artist** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 중원     | **Central Plains**                               |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 칭호               | **Title**                      |
| 몬스터     | **monster**           |
| 청해     | **Qinghai**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 황하 | **Yellow River** | River along which civilization began. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 일기당천 | **One Against a Thousand** | Title that temporarily increases Taekyung’s attributes and Intimidation when facing many enemies. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 남문 | **South Gate** | A gate that was never built because of the rear cliff. |
| 언데드 | **undead** | Supernatural beings that are neither dead nor alive. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 무아 | **No-self** | The brief self-forgetting state the disciple mistakes for a breakthrough. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1100
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 966
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1100
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

## Korean source

```text
1101화




아주 오래전부터, 이 세상의 사람들은 황하를 기준으로 나뉜 남북의 땅을 가리켜 중원(中原)이라 칭하고 천하의 중심으로 여겨 왔다.

첫 고대 문명의 발원지이자, 비옥한 대지와 풍부한 자원을 바탕으로 한 미친 생산력.

이와 같은 훌륭한 조건을 갖추고 있으니 온 사방에서 사람들이 몰려들 수밖에 없었다.

문제는 그중에 머나먼 변방의 이민족들이 포함되어 있었다는 것이고, 그들은 종종 중원의 금은보화를 ‘빌려’ 가길 원했다.

약탈 혹은 점령이라는 자신들만의 방식으로.

물론 당연하게도, 중원인들은 그 방식이 썩 마음에 들지 않았다.

하여 그 길이만 장장 만 리에 달하는 장성(長城)을 쌓고, 변방에 주둔한 군대를 강화하는 한편, 곳곳에 철옹성과도 같은 요새와 성을 세워 누대에 걸쳐 꾸준히 보강해 왔다.

변방 중의 변방. 대륙의 GOP나 다름없는 청해성의 성도(成都)인 서녕의 경우에는 두말할 필요조차 없을 정도로.

하지만 그러한 명령을 내린 과거의 지배자들과 피땀을 흘려 가며 작업에 참여한 장인과 인부들은 꿈에도 생각지 못했을 것이다.

단단한 암석을 다듬어 층층이 쌓고, 석회(石灰)를 빈틈없이 발라 굳힌 성벽을 맨몸으로 들이받는 미친놈들이 존재한다는 사실을.

그리고 그 미친놈들이, 엄청난 괴력과 흉측한 외관을 지닌 거구의 괴물들이라는 것을.

구구구구궁!

땅이, 아니 성이 흔들린다.

물경 수천에 달하는 괴물들이 맨몸으로, 혹은 어디서 가져왔는지 모를 커다란 나무와 몽둥이로 성벽을 두드리는 광경은 보는 것만으로도 피를 얼어붙게 할 만큼 압도적이었다.

잠시 뜨겁게 타올랐던 아군의 전의에 찬물을 끼얹듯이.

“흐읍……!”

“전열을 이탈하지 마라! 각자의 자리를 지켜라!”

곳곳에서 새어 나오는 헛숨과 빗발치는 고함.

이는 비단 내가 지키고 있는 서문(西門)에서만 벌어지고 있는 일이 아니었다.

북문과 남문, 그리고 비교적 적들의 공세가 심하지 않은 동문 역시도 마찬가지였다.

수십 리에 걸쳐 서녕을 포위한 무수한 적들이, 끈질긴 생명력을 지닌 괴물들을 앞세워 본격적인 공성(攻城)에 돌입한 것이다.

“궁수, 준비!”

“발시! 발시하라!”

쉬쉭, 푸푸푹!

아군의 대응 또한 기민했다.

촘촘한 화망(火網)을 갖춘 채 직사에 가깝게 떨어져 내리는 화살 비로 암천의 교도들을 저지하는 한편, 괴물들을 염두에 둔 대비책을 꺼내 들었으니까.

“준비는?”

내 나직한 물음에, 이미 투구 안이 땀으로 흥건하게 젖은 장수 하나가 대답했다.

“상산후께서 명하신 대로 모두 끝마쳐 두었습니다.”

그렇다면 더는 망설일 필요가 없다.

나는 긴장한 얼굴로 대기하고 있던 장수와 관군들을 향해 입을 열었다.

“모조리 쏟아부어. 화끈하게.”

마침내 명령이 떨어진 그 순간.

그그긍.

힘차게 신호를 보내는 깃발의 움직임에 맞춰, 묵직한 쇳소리와 함께 성벽 곳곳에 설치되어 있던 커다란 무쇠 항아리들이 기울어지며 그 안에 가득 차 있던 내용물을 토해 냈다.

끈적하고 새카만, 끓는 기름을.

촤악, 치지지직!

- 그어어어어!

매캐한 연기와 타는 냄새가 뒤섞이고, 그 위로 괴물들이 내지르는 고함이 덧씌워진다.

하지만 고작 이 정도로 이미 언데드 몬스터나 다름없는 놈들을 소멸시키기에는 역부족이라는 사실을, 나는 누구보다 잘 알고 있었다.

놈들을 조종하는 술사들이 모습을 드러내지 않는 지금과 같은 상황에서라면, 바로 지금이 내가 나서야 하는 가장 적절한 시점이라는 것도.

화아악.

크게 숨을 삼키자, 몸속 깊은 곳에 똬리를 틀고 누워있던 화룡이 깨어난다.

오랜 보금자리였던 하단전을 벗어나, 이제는 하늘과 맞닿은 중단전의 봉우리까지 둥지를 튼 거대한 화염이 꿈틀거리며 전신의 사지 백해로 흘러 들어갔다.

끝없이, 맹렬하게.

동시에, 빛살처럼 쾌속하게.

팟.

발걸음을 뗀 순간, 등골이 서늘해지는 듯한 부유감(浮游感)이 전신을 휘감는다.

어느덧 모든 것이 내 발아래에 있었다.

세상 끝의 장벽처럼 우뚝 서 있는 십여 장 높이의 성벽도, 그 아래를 새카맣게 물들인 괴물과 광신도들도.

지금 이 순간 나와 눈높이를 나란히 한 것은 오직 단 하나.

검푸른 강기(罡氣)의 불꽃을 머금은, 한 자루의 창뿐이다.

그그극.

전신의 근육이 활시위처럼 팽팽하게 당겨지고, 어느 때보다 날 선 감각이 손끝을 향해 집중된다.

천천히 허공을 가르며 내리꽂힐, 가장 파괴적이고 완벽한 궤적을 위해.

‘지금.’

마음속 뇌까림과 함께, 나는 저 아득한 지상을 향해 백염을 쏘아 보냈다.

슈확!

섬광이 번뜩인다. 극심한 열기에 의해 일그러지는 공간 속, 한 줄기 검푸른 불꽃이 성벽 근처의 적들 사이로 스며들었다.

그리고 이내, 하늘이 쪼개지는 듯한 굉음이 있었다.

꽈아아아앙!

끝없이 쏟아져 내리는 굵은 빗줄기를 비웃듯, 성벽을 타고 솟구치는 거대한 불의 기둥.

그 아래에는 앞서 아낌없이 퍼부은 기름으로 인해 흥건하게 젖어 있던 대지가, 적들의 살과 뼈가 있었다.

“끅, 끄아아아악!”

“꺼흐흑……!”

불행인지 다행인지, 간신히 목숨만을 부지한 적들이 불길에 휩싸여 끔찍한 비명을 토해 낸다.

그 숫자만 어림잡아 수백.

아니, 어쩌면 그 이상.

하지만 일순간 천지를 떨어 울린 그 엄청난 굉음이 가시기도 전에, 내 신형은 그들의 머리 위로 떨어지고 있었다.

펑, 펑, 퍼엉!

연달아 내딛는 발끝을 따라 폭발하는 공기.

까마득하게만 느껴졌던 대지가 어느덧 코앞까지 성큼 다가온 것을 느끼며, 나는 비바람만이 세차게 휘몰아치는 허공을 향해 손을 뻗었다.

‘인벤토리 오픈, 소환.’

띠링.

시스템 알림과 함께 텅 비어 있던 손아귀를 채우는 단단한 촉감. 그와 동시에, 허공에서 내리꽂히는 나를 발견하고 몰려들었던 적들이 눈을 부릅떴다.

“이게 뭐……!”

서걱!

일도양단(一刀兩斷).

그 네 글자를 스스로의 목숨으로 증명한 적들의 몸뚱어리가 좌우로 나뉘어 갈라진다.

어두운 하늘 아래에서도 유독 붉게 빛나는 피 분수가 솟구치고, 이미 초점이 흐릿한 적들의 눈동자 위로 광기가 번들거렸다.

“천상천하, 만마앙복.”

“쳐라!”

쉬쉬쉬쉭!

빗줄기보다도 서늘한 칼바람이 휘몰아쳤다.

전후좌우를 넘어, 삼십육방(三十六方)를 모조리 점한 적들이 목숨을 도외시하고 달려든다.

마치, 불꽃을 향해 홀린 듯이 나아가는 부나방처럼.

서걱!

사방을 난도질하는 예리한 검기(劍氣).

침범해서는 안 될 영역에 손을 댔다는 것을 알려 주듯, 그 색이 하나같이 피처럼 붉고 위태로워 보였으나 그 위력과 속도만큼은 절정고수의 그것 못지않다.

아직까지도 기억 속에 선명하게 남아 있는, 그들의 모습처럼.

‘잠력단(潛力丹).’

목숨을 장작 삼아 피워올리는 생애 마지막 불꽃.

비록 지속 시간은 짧지만, 잠력단의 효과가 그 위험성만큼이나 지대하다는 사실을 나는 잘 알고 있다.

저들이 어설프게 쌓아 올린 장작으로는, 내가 지금껏 숱한 생사의 고비를 넘어가며 만들어 낸 아궁이의 화력을 이길 수 없다는 것 역시도.

푹!

최대한 힘을 아끼기 위해 공력조차 싣지 않았다.

그러나 그것으로 충분하다.

이미 인간의 한계를 몇 단계나 벗어난 신체 능력이, 죽음의 위기 앞에서 단련된 감각이 그것을 가능케 만들었으니까.

크르륵.

순식간에 목젖이 갈라진 암천의 교도가 제 목을 부여잡았을 때, 나는 이미 놈을 지나쳐 다른 적들을 향해 뛰어들고 있었다.

쉬잉!

좌로 반보.

한 뼘 차이로 내 몸을 스쳐 지나간 세 줄기의 검기가 허공에서 얽혀들고, 서녕의 병기고에서 녹슬어 가던 투박한 박도(朴刀)가 내 손을 떠났다.

퍼걱!

한 줌의 공력조차 없이, 단지 무시무시한 힘으로 회전한 도신이 세 명의 목을 베어 낸다.

아니, 박살 낸다.

그리고 동시에, 마음속에서 울려 퍼진 명령어와 함께 새로운 날붙이가 내 양손에 쥐어졌다.

왼손에는 직도. 오른손에는 협봉검.

분명 낯설다. 하지만 모순적으로 느껴질 만큼 익숙하다.

쐐애애액! 푸푸푹!

가장 적절한 힘과 속도. 그에 더하여 전투의 흐름을 꿰뚫는 움직임.

나는 무아지경(無我之境)의 상태에 휩싸여 성벽 아래를 휩쓸었다. 검과 도를 춤추듯 휘두를 때마다 피와 비명이 터져 나오고, 나아가는 걸음걸음마다 시체가 융단처럼 깔렸다.

‘와라.’

무심코 내뱉을 수 있는 한 번의 숨결조차 아꼈다.

그저 마음속 뇌까림과 함께, 사방에서 끊임없이 짓쳐 드는 적들을 베고 또 베었다.

찔러 오는 검을 피하는 동시에 협봉검으로 심장을 꿰뚫었고, 붉게 녹이 슬어 버린 직도만으로 검기가 실린 다섯 자루의 검신을 통제했다.

카가가각!

검신의 옆면을 짓누르며 회전시킨다. 그것만으로도 서로를 향해 어지럽게 뒤얽힌 검들을 튕겨 내며 적들의 숨통을 끊는다.

힘을 써야 할 때는 힘을, 부드러움이 필요할 때는 부드러움을.

협봉검이 부러지면 무한에 가까운 인벤토리의 창고 속에서 도끼를 소환했고, 부러진 직도로 화염신장(火焰神掌)의 묘리를 담은 도법을 펼쳤다.

스스로도 이해가 안 될 만큼, 지금 이 순간의 나는 모든 제약과 한계로부터 자유로웠다.

그리고 불현듯 깨달았다.

‘이런 거였나.’

언젠가 적천강이 말했었다.

무학에 대한 깨달음이 경지에 다다른다면, 살아 숨 쉬고 움직이는 모든 것이 하나의 무공이 된다고.

그때는 힘없이 휘어진 갈대조차 신검(神劍)과 다를 것이 없게 된다고.

물론 지금의 내가 그 정도의 경지에 다다른 것은 아니겠지만, 비로소 그 말에 담긴 뜻을 어렴풋이나마 알 것 같았다.

서걱!

손끝을 타고 느껴지는 죽음의 감각과 함께, 또 다른 적을 향해 돌아서려던 나는 문득 눈을 깜빡였다.

아무도 없었다. 모든 것이 고요했다.

잠력단을 복용한 암천의 교도들도, 더는 인간이라 부를 수 없는 거구의 괴물들도.

서쪽 성벽 아래, 두 다리로 서 있는 것은 오직 나뿐이었다.

그리고 눈 앞에 펼쳐진 그 핏빛 광경은 한 가지 사실을 의미했다.

족히 일천에 달하던 적의 선봉을 궤멸시킨 것이다.

그것도 단신으로.

띠링. 띠링. 띠링.



- 칭호, [일당백(一當百)]의 효과 발동 조건을 충족시켰습니다!

- 칭호, [일기당천(一騎當千)]의 효과 발동 조건을 충족시켰습니다!

- [위압]이 크게 상승합니다!

- 강대한 [위압]으로 인해 당신의 적들이 급격히 위축됩니다!

- 일부 아군에게 적용되어 있던 상태 이상, [피어]가 해제됩니다!

- 아군의 사기가 크게 상승합니다!



둑이 허물어지듯 귓가로 쏟아지는 시스템 알림 속, 성벽 위에서 거대한 함성이 터져 나오던 그때였다.

부우우우!

몸서리칠 만큼의 깊은 울림을 지닌 뿔피리 소리와 함께, 물경 십만에 달하는 암천의 본대가 각 성벽을 향해 진군하기 시작한 것은.

그리고 그런 놈들의 움직임이 무엇을 의미하는지 깨달은 것은.

“……!”

괴물들.

아니, 거인들.

각각의 신장만 최소 일 장을 훌쩍 넘어가는 놈들의 사체는, 어느덧 성벽의 중간까지 차올라 있었다.
```

## Final English reading copy

```markdown
# Chapter 1101

For ages, people had used the Yellow River to divide the lands to its north and south, calling them the Central Plains and considering them the heart of the world.

The birthplace of the first ancient civilization, with fertile land and abundant resources driving its insane productivity.

With such ideal conditions, people were bound to flock there from every direction.

The problem was that among them were foreign peoples from distant borderlands, who often wanted to “borrow” the Central Plains’ gold and silver treasures.

In their own special way: by looting or occupying them.

Naturally, the people of the Central Plains weren’t too fond of that.

So they built the Great Wall, stretching a full ten thousand li, strengthened the armies stationed along the borders, and steadily reinforced impregnable fortresses and castles throughout the land, generation after generation.

There was no need to say more about Xining, the capital of Qinghai, the farthest of the borderlands—the continental equivalent of the GOP.

But the rulers of the past who had issued those orders, and the craftsmen and laborers who had worked themselves to the bone, could never have dreamed that there were madmen who would slam their bare bodies into walls built of solid stone, stacked layer upon layer and sealed tight with lime.

Nor could they have imagined that those madmen would be enormous monsters, with monstrous appearances and incredible strength.

*Rumble, rumble!*

The ground—or rather, the city—shook.

The sight of several thousand monsters battering the wall with their bare bodies, or with huge logs and clubs from who knew where, was so overwhelming it made the blood run cold.

As if someone had doused the defenders’ spirits, which had just burned so hot, with ice water.

“Hah…!”

“Don’t break formation! Hold your positions!”

Choked breaths escaped here and there, amid a storm of shouted commands.

And this wasn’t happening only at the West Gate, where I was stationed.

The North Gate and South Gate were the same, as was the East Gate, where the enemy assault was relatively light.

Countless enemies had encircled Xining for dozens of li, and now they were beginning their full-scale siege, leading with monsters that refused to die.

“Archers, ready!”

“Loose! Loose!”

*Shhk, thud-thud!*

Our response was swift, too.

We held back the Dark Heaven followers with a dense rain of arrows fired on nearly direct trajectories, while bringing out the countermeasures we’d prepared for the monsters.

“Is it ready?”

At my quiet question, one of the commanders answered. His helmet was already soaked with sweat inside.

“Everything’s been prepared, just as the Marquis of Shangshan ordered.”

Then there was no need to hesitate any longer.

I turned to the tense commander and imperial troops waiting nearby.

“Pour it all out. Give them the works.”

The moment the order finally came—

*Rumble.*

At the vigorous motion of the signal flags, the large iron cauldrons installed at intervals along the wall tilted with a heavy metallic groan, disgorging their contents.

Thick, black, boiling oil.

*Splash! Ssssss!*

—*GRAAAAH!*

Acrid smoke and the smell of burning mixed together, drowned out by the monsters’ screams.

But I knew better than anyone that this alone wasn’t enough to destroy these things, which were practically undead monsters already.

And with the sorcerers controlling them still nowhere to be seen, I knew this was the right moment for me to act.

*Fwoosh.*

I drew in a deep breath, and the fire dragon curled deep inside me awoke.

It left its longtime home in my Lower Dantian. The enormous flames, now nested atop the peak of my Middle Dantian, stirred and flowed into every limb and point of my body.

Endlessly. Fiercely.

And at the same time, as swiftly as a ray of light.

*Whoosh.*

The moment I stepped forward, a sensation of weightlessness swept over my whole body, chilling my spine.

Before I knew it, everything was beneath my feet.

The city wall, rising a dozen or so jang like a barrier at the edge of the world. The monsters and fanatics blackening the ground below.

Only one thing was level with my eyes now.

A spear, wreathed in the flames of dark blue Force.

*Grind.*

My muscles drew taut like a bowstring, and my senses, sharper than ever, focused at my fingertips.

For the most destructive and perfect arc, slowly cutting through the sky before plunging down.

*Now.*

With that thought, I sent White Flame hurtling toward the distant ground below.

*Whoosh!*

A flash of light. In the space warped by the intense heat, a streak of dark blue flame slipped among the enemies near the wall.

Then came a deafening roar, as if the sky had split apart.

*BOOM!*

A vast pillar of fire surged up along the city wall, mocking the heavy rain that poured down without end.

Beneath it lay the ground, soaked with all the oil we’d poured out without holding back—and the enemies’ flesh and bones.

“Ghk, aaagh!”

“Keugh…!”

Whether by misfortune or good luck, the enemies who’d barely survived were engulfed in flames, shrieking horribly.

Hundreds, by my rough count.

Maybe more.

But before the enormous roar that had shaken heaven and earth could even fade, my body was already dropping over their heads.

*Bang! Bang! Ba-bang!*

The air exploded beneath my feet with each step.

Feeling the ground, which had seemed so impossibly far away, rush up to meet me, I reached out into the empty air, where only wind and rain whipped around me.

*Inventory open. Summon.*

*Ding.*

Along with the System notification came the solid feel of something filling my empty hand. At the same time, the enemies who’d gathered around me, spotting me dropping from the sky, widened their eyes.

“What the—”

*Shhk!*

One strike, one clean cut.

The enemies’ bodies split apart left and right, proving those four words with their lives.

A fountain of blood, vivid red even beneath the dark sky, spurted up. Madness glinted in the eyes of the enemies, already losing their focus.

“Heaven above and earth below, all demons bow!”

“Attack!”

*Shh-shh-shhk!*

A chilling wind of blades swept through the air, colder than the rain.

The enemies had me surrounded on all sides, from every direction, and rushed in without regard for their lives.

Like moths, enthralled, flying toward a flame.

*Shhk!*

Sharp Sword Energy slashed in every direction.

Each streak was blood-red and looked dangerously unstable, as if betraying that its wielder had reached into a realm they had no business touching. Yet their power and speed rivaled a Peak master’s.

Just like the way I still remembered them so clearly.

*Temporary Strength Pills.*

The final flame of a person’s life, kindled with their own life as the fuel.

I knew well that though the pills’ effect lasted only a short time, their power was as great as their danger.

And I knew just as well that the shoddy kindling they’d piled up couldn’t match the heat of the furnace I’d built by surviving countless brushes with death.

*Thump!*

I didn’t even channel internal energy into the blow, conserving my strength as much as possible.

But that was enough.

My body had already surpassed human limits by several steps. My senses, honed in the face of death, made it possible.

*Grrk.*

As the Dark Heaven follower’s throat was torn open in an instant and he clutched at his neck, I’d already passed him and plunged toward the other enemies.

*Whoosh!*

Half a step to the left.

Three lines of Sword Energy brushed past me by a hair and tangled together in midair. The rough broad-bladed saber that had been rusting in Xining’s armory left my hand.

*Wham!*

The blade spun with terrifying force and not an ounce of internal energy, cutting through three necks.

No—it smashed through them.

At the same time, with a command ringing in my mind, a new pair of blades appeared in my hands.

A straight sword in my left. A narrow-bladed sword in my right.

They were unfamiliar. Yet, strangely, they felt familiar enough to be a contradiction.

*Shreeeek! Thud-thud!*

The most fitting strength and speed. And with them, movements that read the flow of battle.

I was swept into a state of No-self as I tore through the enemies beneath the wall. Each time I swung my sword and saber as if dancing, blood and screams burst forth. With every step I took, corpses spread beneath me like a carpet.

*Come.*

I spared even the single breath I might have let out without thinking.

With only those words murmured in my heart, I kept cutting down the enemies surging toward me from every direction.

I dodged a thrusting sword and pierced its wielder’s heart with the narrow-bladed sword. With nothing but a straight sword gone red with rust, I controlled the blades of five swords imbued with Sword Energy.

*Clang-clang-clang!*

I pressed down on the sides of their blades and twisted. That alone sent the swords tangled together in a wild snarl flying away from one another, while cutting off the enemies’ breath.

Strength when strength was needed. Softness when softness was needed.

When the narrow-bladed sword broke, I summoned an axe from the nearly infinite storeroom of my Inventory. With the broken straight sword, I wielded a blade technique infused with the principles of the Flame Divine Palm.

Even I couldn’t understand it, but in this moment, I was free from every restriction and limit.

And suddenly, I understood.

*So this is what it means.*

Jeok Cheongang had once told me:

When one’s understanding of martial arts reached a certain realm, everything alive and moving became a martial art of its own.

Even a reed, bent weakly in the wind, would be no different from a Divine Sword.

Of course, I hadn’t reached that level. But at last, I thought I could faintly grasp what he’d meant.

*Shhk!*

With the sensation of death running through my fingertips, I started to turn toward another enemy—then blinked.

There was no one. Everything was quiet.

The Dark Heaven followers who’d taken Temporary Strength Pills. The enormous monsters that could no longer be called human, either.

Beneath the western wall, I was the only one left standing on two feet.

And the blood-soaked scene spread before me meant one thing.

I’d wiped out the enemy vanguard, which had numbered a thousand at the very least.

All by myself.

*Ding. Ding. Ding.*

> **System**
>
> You have met the activation conditions for the Title **One Against a Hundred**!
>
> You have met the activation conditions for the Title **One Against a Thousand**!
>
> **Intimidation** rises significantly!
>
> Your enemies are rapidly cowed by your powerful **Intimidation**!
>
> The status effect **Fear**, applied to some allies, is removed!
>
> Allied morale rises significantly!

As the System notifications poured into my ears like a dam breaking, a tremendous roar erupted from atop the wall.

*BWOOOOO!*

A horn sounded, its deep reverberation enough to make me shudder. With it, the main force of Dark Heaven—no less than a hundred thousand strong—began advancing toward the city walls.

And then I understood what their movement meant.

“……!”

The monsters.

No—the giants.

Their corpses, each one well over a jang tall, had piled up to the middle of the wall.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0885.txt",
      "sha256": "3f9a23c0b5ee4f287c0fcc2f0310e7977294f3e23b4229355fdd8a8064b3c031",
      "bytes": 14302
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "52ac964cdd82f0f3f6cb2e5bb657b019114343f324986d58327e40d8a8cdaaed",
      "bytes": 2934
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "050bbcc53d7e64068c401dce99921e55fb476b863c1a9de039518036eced1bca",
      "bytes": 759
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "c037b97391e6090031d321c64b0853897b865128812465705bc589c5ee172c1a",
      "bytes": 796
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "09b53280f2f55380f3c06063ad7ba1703945c2a87f5ff6dbfc057024484b3303",
      "bytes": 259022
    }
  ],
  "estimated_tokens": 9672
}
-->

# Durable State Update — Chapter 885

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
1 and safe_through 885. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 885. Profile updates may replace only one
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
  "chapter": 885,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 885,
    "continuity_sources": [885],
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
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him.",
    "The Emperor plans a banquet attended by Shangshan and civil and military officials; Hong Jin suspects it could be a trap.",
    "Ma Sanbao spread rumors using information Taekyung gave him; the Emperor ordered the arrested rumor-spreaders released.",
    "Ma Sanbao leads a covert faction of survivors seeking to overthrow the Emperor; they have signed a pact and expect the banquet to become a confrontation.",
    "Ma Sanbao says the person his allies asked about is safe and expects the young martial artist to help; he believes the martial artist’s master could be decisive.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "The late Emperor died after a period of mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Jeok Cheongang received two letters, burned them, and said the group was formally invited to the imperial palace; their contents remain unknown.",
    "Taekyung’s group has an official invitation to perform as the Blazing Flame Troupe at the imperial banquet.",
    "Jeok Cheongang’s group entered the Outer Palace disguised as a circus troupe; the Divine Physician gave them Energy-Dispersing Poison to conceal their martial skill during screening, while Jeok can conceal his aura without it.",
    "A courtesan seeking revenge against the Emperor died by her own hand during Jeong Hogun’s screening; her companions were taken to prison."
  ],
  "continuity_sources": [
    884
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Will the banquet become a confrontation, and what does the Emperor intend?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Who is the person Ma Sanbao’s allies asked about, and what preparations has the faction made?",
    "Who is the familiar young man who approached Jeong Hogun, and what will happen when Hogun questions Taishan?"
  ],
  "safe_through": 884,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake.",
    "Render 연판장 as “a pact bearing their signatures”; retain “Hongmen Banquet” for 홍문연.",
    "Treat 거산 as Taishan’s uncertain name variant, not a confirmed separate person; render 열화단 as “Blazing Flame Troupe” and 마희단 as “circus troupe.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 무림맹    | **Murim Alliance**               |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 산공독 | **Energy-Dispersing Poison** | Poison that temporarily prevents the use of internal energy and causes it to dissipate. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 수마 | **sleep demon** | Metaphor for the force keeping Jin unconscious. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |
| 진상 | **Jinsang** | Koizumi's punning address to Jin, retained for the Korean wordplay. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 884
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 884
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language, using calm reassurances and strategic metaphors to maintain unity while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he stayed behind to await Prince Shangshan's return and is leading a group seeking to enthrone him.

## Korean source

```text
＃885화



당연하게도 그 이상의 감동적인 재회는 이루어지지 않았다.

고작해야 며칠 정도 떨어져 있었을뿐더러, 당장 아는 척을 할 수 있는 상황도 아니었으니까.

‘곧 기회가 있겠지.’

나는 광활하다는 표현이 어울릴 만큼 드넓은 황궁 경내를 가로지르며 이곳저곳을 살폈다.

건물들의 구조와 위치. 어디에나 보이는 금위군의 숫자와 이번 연회를 준비하기 위해 유입된 외부인들까지.

그리고 그 과정에서, 생각지도 못한 사실을 눈치챘다.

‘뭐지?’

의문과 동시에 멈춘 발걸음.

나는 눈매를 좁힌 채, 불과 열 걸음 앞에서 상자를 나르는 일단의 무리를 지켜보았다.

“잠깐. 그건 이쪽으로.”

“하나, 둘. 흡!”

“광록대부(光祿大夫)께서 진상하신 물건이다. 네놈들 목숨을 전부 합친 것보다 귀중한 것이니 조심히 다루어라.”

“예. 여부가 있겠습니까요.”

깨끗하지만 군데군데 기운 흔적이 보이는 낡은 의복에, 삶의 고난이 배어 있는 얼굴의 주름살.

구슬땀을 흘리면서도 하급 관리로 보이는 이에게 굽실거리며 웃어 보인 그들은 산더미처럼 쌓인 물건들을 쉴새 없이 실어 날랐다.

하루 벌어 하루 먹고 사는, 여느 인부(人夫)들과 다를 바 없이.

하지만…….

‘달라.’

나는 느꼈다.

저들에게서 느껴지는, 아주 희미한 이질감을.

그것은 지금까지의 숱한 실전 경험과 생사를 넘나드는 위기 속에서 다듬어진 직감이었고, 현재의 경지에 이르지 못했다면 눈치채지 못할 정도의 은밀함이었다.

‘평범한 인부들이 아니다.’

별다른 공력조차 느껴지지 않았음에도 이러한 생각이 든 것은 한 가지뿐이다.

‘피비린내.’

아무리 씻고 씻어도 지워지지 않는 낙인과도 같은 것.

시큼한 땀 냄새와, 낡은 옷의 묵은내로도 완전히 감추지 못한 피비린내가 저들의 몸에서 흘러나오고 있었다.

‘무림인?’

머릿속을 스치는 의문. 하지만 아직은 불확실하다.

공력을 숨기기 위해 자발적으로 산공독(散功毒)을 복용한 무림인들인지, 아니면 주위에서 벌어지는 모든 일에 민감하게 반응할 수밖에 없는 현재의 상황이 불러온 단순한 착각인지.

‘확인해 보면 알겠지.’

나는 조금 더 자세히 그들을 지켜보기 위해 가까이 다가갔다. 아니, 다가서려 했다.

다음 순간, 무게를 이기지 못한 마차 한 대가 나를 향해 기울어지기 전까지는.

우직. 쿠우웅!

육중한 굉음과 함께 나무 파편이 이리저리 튀었다. 상자에서 와르르 쏟아진 은원보(銀元寶)며 각종 패물을 본 관리가 머리를 감싸 쥐었다.

“아니, 이게 무슨 짓거리냐!”

“죄, 죄송합니다. 소인이 짐을 잘못 싣는 바람에 그만…….”

“이런 멍청한 늙은이를 보았나! 사죄는 집어치우고 어서 주워 담기나 해라! 만약 하나라도 상한 물건이 있다면 내 경을 칠 것이다!”

“예에. 알겠습니다.”

호통과 함께 홱 돌아선 관리를 향해 부러질 듯이 허리를 숙인 것은 늙은 초로인이었다.

생기를 잃은 나무처럼 왜소한 체구에 비쩍 마른 그는, 한쪽 다리를 절뚝이며 다가와 겁먹은 눈동자로 나를 바라보았다.

“나리께서는 괜찮으십니까? 혹여 이 늙은이의 실수로 다치신 곳은 없으신지…….”

실수. 실수라.

내심 중얼거린 나는 담담하게 대답했다.

“괜찮습니다. 다친 곳도 없고요.”

“휴우. 천만다행입니다그려.”

“그러게요. 멀쩡해 보이던 마차가 갑자기 쓰러지다니, 저도 깜짝 놀랐네요.”

내 입가에 맺힌 미소를 본 노인이 황망한 얼굴로 재차 고개를 숙였다.

“소인이 다시 한번 사죄드리겠습니다.”

“뭘요. 그나저나 좀 도와드려요? 딱 봐도 주워 담을 게 많아 보이는데.”

“어이구, 어찌 그럴 수 있겠습니까. 지체 높으신 분께서 이리 말을 높여 주시는 것만으로도 송구스럽…….”

“저 지체 높은 사람 아닙니다. 이미 대충 알고 계실 텐데?”

그 찰나의 순간.

사태를 수습하기 위해 다가오던 몇몇 인부들 사이로 묘한 기류가 흘렀다. 그리고 아무도 눈치채지 못할 만큼 짧은 침묵 속에서 노인이 천천히 입을 열었다.

“도와주신다면야, 참으로 감사하지요.”

“그럼 됐네요.”

고개를 끄덕인 나는 자리에 쭈그려 앉아 쏟아진 물건들을 주워 담기 시작했다.

정말 그것만이 유일한 목적이었던 것처럼 아무 말 없이 조용히, 그러나 눈으로는 초로인을 계속해서 응시하며.

결국 먼저 침묵을 깨트린 것은, 내가 아닌 그였다.

“어떻게 알았나?”

모든 것을 시인하는 한 마디에 나는 피식 웃었다.

“인정이 빠르시네.”

“시간 낭비는 딱 질색이야. 나처럼 살 날이 얼마 남지 않은 늙은이에게는 특히 그렇지.”

“무림인입니까? 소속은요?”

“질문에 질문으로 답하는 건 예의 없는 행동이지. 명심하게.”

“그게 무슨, 아.”

“어떻게 알았지? 누구도 눈치챌 수 없으리라 자신했거늘.”

언제 그랬냐는 듯, 형형한 안광을 빛내는 초로인을 향해 나는 짤막하게 답했다.

“피비린내.”

초로인은 놀라지 않았다. 눈살을 찌푸리며 몸 이곳저곳을 킁킁대다가 입맛을 다시더니 이렇게 말했다.

“나이가 들더니 코가 잘못됐나. 늙은이 쉰내밖에 안 나는데.”

“그것도 납니다. 기왕 말 나온 김에 거리 좀 벌립시다. 숨쉬기가 좀 힘들어서.”

“무공만 고강한 줄 알았더니, 냄새도 기가 막히게 잘 맡는 친구로군.”

“절 압니까?”

“알지. 이런 일에는 정보가 필수거든. 하지만 사전에 별다른 정보를 듣지 않았더라도 곧장 눈치챘을 걸세.”

“어떻게?”

“피비린내.”

순간 말문이 막힌 내 귓가로, 초로인의 목소리가 이어졌다.

“몰랐나? 자네에게도 피비린내가 진동해. 신룡(神龍)이 아니라 살귀(殺鬼)라고 불려도 이상하지 않을 정도지.”

“……!”

“아, 그런 눈빛으로 바라볼 필요는 없네. 어디까지나 칭찬이니까. 왜 그런 말도 있지 않나.”

노인이 씩 웃었다. 검고 누런 이빨 사이로 끔찍한 악취가 풍겼다.

“백 명을 죽이면 살귀요, 천 명을 죽이면 영웅이라 불리며 만 명을 죽이면…… 왕이 된다.”

모래를 씹은 것처럼 입 안이 까끌거린다. 나는 코앞에서 악취를 풍기는 초로인을 물끄러미 응시했다.

‘도대체 뭐지?’

느낌이 좋지 않다. 마주한 것만으로도 등골이 서늘해지는 기분.

수많은 인간군상들이 뒤섞인 무림에서도 이런 부류는 쉽게 찾아볼 수 없다.

“당신, 아니 당신들은 누굽니까?”

“무림의 대선배에게 당신이라니. 자네 스승께서도 당신의 제자가 이리 버릇없이 군다는 걸 알고 계신가?”

“최근에 알게 된 누군가가 그런 말을 했습니다, 질문에 질문으로 답하는 건 예의 없는 행동이라고.”

눈을 동그랗게 뜬 채 나를 바라보던 초로인이 소리 내어 웃었다.

“이거, 제대로 한 방 먹었구먼.”

“다 웃으셨으면 이제 대답하시죠.”

“알면서 뭘 묻나. 나와 저 아이들 역시 무림인일세. 자네와 그리 다를 것 없는.”

“개인적인 생각으로는 크게 다른 것 같은데, 저만의 단순한 착각입니까?”

“걱정할 필요 없네. 비록 우리가 무림맹(武林盟)에는 소속되지 않았지만, 한배를 탄 동료나 다름없으니.”

“그게 무슨…….”

말꼬리를 흐리던 그때, 문득 뇌리를 스치는 어떤 생각이 있었다.

“설마?”

“마 태감. 이 정도면 충분한 대답이 됐나?”

“……!”

“각자의 위치와 역할이 있는 법. 자네도 이만 돌아가서 때를 기다리게. 이 이상 이목을 끌면 귀찮아지니까.”

그 말을 끝으로 자리에서 일어난 초로인은 내게 허리를 굽실거렸다.

“나머지 일은 저희가 알아서 할 테니, 이제 그만하셔도 됩니다요. 나리.”

명백한 축객령인 동시에, 어디선가 이곳을 주시하고 있을 감시자들을 향한 연기.

아니, 이 정도면 단순한 연기라고 칭하는 것은 폄하에 가깝다.

초로인은 늙은 인부 그 자체요, 움직임 하나가 혼연일체(渾然一體)나 다름없었으니까.

“조심히 들어가십시오, 나리. 그럼 소인은 이만…….”

저벅. 저벅.

그리고 다리를 절뚝이며 상자를 옮기는 초로인의 뒷모습을 바라보던 나는, 비로소 인부로 위장한 저들의 정체를 알 것 같다는 생각이 들었다.

무수한 인간군상들이 활보하는 이 광활한 무림에서도, 저토록 완벽하게 스스로를 숨긴 채 움직이는 부류는 정해져 있었으니까.

거기에 더해 그 지독한 피비린내까지.

지금 이 순간. 내 머릿속에 떠오른 단어는 하나뿐이었다.

살수(殺手).



* * *



온갖 정신병자와 안전불감증 환자가 득실거리는 무림인들조차 가까이하길 꺼리는 부류가 있다면, 언제나 빠지지 않고 등장하는 부동의 멤버들이 있다.

살귀. 마두. 뭔가 있어 보이는 늙은이와 면사를 쓴 미녀 등등.

그들은 전설의 일본 1군 팀처럼 결코 쉽게 찾아볼 수 없지만, 최소한의 정신머리와 수십 년 뒤 장수마을 입주를 꿈꾸는 무림인들은 재깍재깍 알아서 피해 간다.

이유? 간단하다.

괜히 건드려 봤자, 아니 그저 주위에 있는 것만으로도 불길함이 스멀스멀 올라오니까.

그리고 그중에서도 살귀, 마두에 이어 최소 세 손가락 안에 꼽히는 기피 직종이 바로 살수다.

소위 말하자면 개호로 잡놈 삼대천왕.

그 누구도 이에 대해서 부정하거나, 의문을 가지지 않는다.

오히려 저 삼대천왕 중 살수를 첫손가락에 꼽는 이들도 상당수였고, 당장 내 주위에도 비슷한 조언을 해 준 사람이 한 명 있었다.

그 친절한 조언가의 별호가 다름 아닌 살성(殺星)이라는 것이 조금 아이러니한 부분이었지만.

‘사실 아이러니가 아니라, 거의 뭐 블랙 코미디 수준이긴 했지.’

나는 내심 뇌까리며 계속해서 발걸음을 옮겼다.

문득 지금 걷고 있는 이 길이 어디로 향하는지 모른다는 생각이 들었지만, 그 생각은 곧이어 뇌리에 떠오른 살성과의 대화에 금세 파묻혔다.



‘살귀나 마두가 차라리 낫다. 하지만 어떤 상황에서도 살수는 피해라.’

‘왜요? 어차피 다 똑같은 미친놈 아닙니까?’

‘네 녀석의 대가리는 속이 꽉 찬 돌과 진배없으니 간단히 예를 들어 주마. 네놈이 객잔에서 식사를 하고 있는데 갑자기 살귀나 마두가 들어왔다고 생각해 보자. 하면 어떻겠느냐?’

‘좆 같죠. 밥 먹는데.’

‘그…… 틀린 말은 아니지만, 좀 더 깊게 생각하고 대답해 봐라.’

‘저한테 돌대가리라면서요. 생각하기 싫으니까 그냥 말씀해 주시면 안 됩니까?’

‘잠시 잊은 것 같아서 말해 주자면, 나는 주먹으로 돌도 부술 수 있다. 물론 돌로 이루어진 대가리도 예외는 아니지.’

‘제 생각이 짧았네요. 잠시 시간을 주시겠습니까?’

‘조금이나마 똑똑해졌군.’

‘감사합니다. 음. 일단 살귀나 마두의 눈치를 살핀 뒤 조심스럽게…….’

‘그래, 일단 조심스럽게 자리를 피하는 것이 급선무지.’

‘아뇨. 선빵 칠 건데요.’

‘……도대체 화왕이 네놈을 어떻게 가르친 거냐?’



하늘을 우러러보며 탄식한 살성은 돌도 부수는 주먹으로 내 머리를 두어 대 때린 후, 이렇게 말했었다.



‘더 쉽게 말하자면, 살귀와 마두는 앞뒤 가리지 않는 미친놈들과 진배없다.’

‘으, 머리야. 그럼 더 위험한 거 아닙니까? 아까 말씀하셨던 대로 객잔에서 마주쳤다간 온 사방이 피바다가 될 수도 있잖아요.’

‘하지만 살아남을 가능성도 충분하지.’

‘그야 무위가 높으면 당연…….’

‘무위의 문제가 아니다. 그런 부류의 미친놈들은 도무지 종잡을 수가 없어서, 기분에 따라 사람을 죽이고 살리기도 하니까.’

‘진짜 미친놈들이네요.’

‘하지만 살수는 어떨 것 같으냐?’

‘살수는, 아.’

‘이제 좀 감을 잡은 것 같군. 맞다. 놈들은 그저 단순히 미친놈들이 아니다. 표적을 암살하기 위해서는 무엇이든지 하지. 살수가 그보다 한 수, 두 수 앞서는 고수들을 죽일 수 있는 것도 바로 그 때문이다.’

‘표적을 암살하기 위해서는 무엇이든지 한다…….’

‘그것이 살수를 가장 조심하고, 멀리 두어야 하는 이유다. 알겠느냐?’

‘예. 알겠습니다.’

‘살수들이 설 자리를 잃은 탓에 더는 많이 찾아볼 수 없겠지만 그래도…… 한데 지금 뭐 하느냐?’

‘짐 챙기는데요.’

‘왜?’

‘살수는 피하라면서요.’

‘……!’

‘아, 혹시 전직 살수는 제외됩니까?’



음. 그때 진짜 많이 맞았었지.

하지만 그래서 더욱 또렷하게 남아 있는 기억이기도 하다.

지금 내가 직면한 문제는 황궁 한복판에서 바로 그 살수를 마주쳤다는 거고.

‘굳이 무림인을 끌어들일 거라면, 왜 마삼보는 살수를 황궁으로 들인 거지?’

당장은 해결할 수 없는 의문이 고개를 든 그때.

“멈춰요.”

낭랑한 목소리가 귓가를 파고들었다.
```

## Final English reading copy

```markdown
# Chapter 885

Naturally, there was no moving reunion beyond that.

We’d only been apart for a few days, and it wasn’t exactly a situation where we could openly acknowledge each other.

*There’ll be a chance soon enough.*

I crossed the sprawling grounds of the imperial palace, vast enough to deserve the word, and looked around at everything.

The layout and locations of the buildings. The number of Imperial Guards visible everywhere. Even the outsiders who’d come in to prepare for the banquet.

And in the process, I noticed something I hadn’t expected.

*What’s that?*

My steps stopped as the question crossed my mind.

I narrowed my eyes and watched a group carrying boxes just ten paces ahead.

“Hold on. Take that this way.”

“One, two. Hup!”

“Those are offerings from Grandee Guanglu. They’re worth more than all your lives put together, so handle them carefully.”

“Yes, of course. We’ll be careful.”

Their clothes were clean, but old, with patches here and there. The wrinkles on their faces were etched with the hardships of life.

Even as sweat poured down their faces, they bowed and smiled at a man who looked like a low-ranking official, then kept hauling the piles of goods without pause.

Just like any other laborers, living from one day’s wages to the next.

But…

*They’re different.*

I could feel it.

A faint sense of something off about them.

It was an instinct honed through countless real battles and brushes with death—so subtle that I wouldn’t have noticed it if I hadn’t reached my current realm.

*They’re not ordinary laborers.*

There was only one reason I’d think so when I couldn’t sense any internal energy from them.

*The stench of blood.*

A brand that wouldn’t come off, no matter how many times they washed.

The stench of blood seeped from their bodies, not entirely masked by the sour smell of sweat or the mustiness of their old clothes.

*Martial artists?*

The question crossed my mind, but I wasn’t sure yet.

Were they martial artists who’d voluntarily taken Energy-Dispersing Poison to hide their internal energy? Or was it just my imagination, brought on by the fact that I had to be sensitive to everything happening around me right now?

*I’ll know if I check.*

I moved closer to get a better look at them. Or rather, I was about to.

Until a cart, unable to bear its own weight, began to tip toward me.

Crack. Crash!

Wooden splinters flew everywhere with a heavy crash. The official clutched his head as silver yuanbao and all kinds of ornaments spilled out of the boxes.

“What the hell do you think you’re doing!”

“I-I’m sorry. This old servant loaded the cargo incorrectly, and…”

“You stupid old fool! Forget apologizing and hurry up and pick everything up! If even one item is damaged, you’ll pay for it!”

“Yes, yes. Understood.”

The one who bowed so low he looked ready to snap toward the official as he stormed off was an old man with graying hair.

He was small and emaciated, like a tree that had lost its vitality. He limped over and looked at me with frightened eyes.

“Are you all right, sir? Did this old man’s mistake hurt you at all…?”

A mistake. A mistake, huh?

I thought to myself, then answered calmly.

“I’m fine. I’m not hurt.”

“Phew. What a relief.”

“Indeed. That cart looked perfectly fine, then suddenly toppled over. It startled me, too.”

At the smile on my lips, the old man looked flustered and bowed again.

“This old servant apologizes once more.”

“Don’t mention it. Anyway, want me to help? Looks like there’s a lot to pick up.”

“Oh, how could I let you do that? It’s already more than I deserve that someone of your standing would speak so politely to me…”

“I’m not someone of high standing. I’m sure you already know that.”

For the briefest moment.

A strange current passed among the laborers who’d come over to deal with the mess. Then, in a silence so short no one else would have noticed it, the old man slowly spoke.

“If you’d help us, we’d be very grateful.”

“Then that’s settled.”

I nodded, squatted down, and began picking up the things that had spilled.

Quietly, without saying anything, as if that had been my only reason for coming over. But I kept my eyes fixed on the old man.

In the end, he was the one who broke the silence, not me.

“How did you know?”

At his admission, I let out a short laugh.

“You’re quick to admit it.”

“I can’t stand wasting time. Especially not for an old man like me, who doesn’t have much time left.”

“Are you a martial artist? Who do you belong to?”

“It’s rude to answer a question with a question. Remember that.”

“What are you—oh.”

“How did you know? I was certain no one could tell.”

The old man’s eyes gleamed fiercely, as if he’d never played the humble laborer. I gave him a brief answer.

“The stench of blood.”

The old man wasn’t surprised. He frowned, sniffed at different parts of his body, then smacked his lips and said,

“My nose must be going bad with age. All I smell is old-man stink.”

“That’s there, too. Since we’re on the subject, let’s put a little more distance between us. It’s hard to breathe.”

“I thought you were just skilled in martial arts, but you’ve got a hell of a nose, too.”

“Do you know me?”

“I do. Information is essential for this sort of thing. But even if I hadn’t heard anything about you beforehand, I’d have figured it out right away.”

“How?”

“The stench of blood.”

For a moment, I was at a loss for words. Then the old man continued.

“Didn’t you know? You reek of blood, too. Enough that it wouldn’t be strange to call you a Killing Ghost instead of a Divine Dragon.”

“……!”

“Ah, there’s no need to look at me like that. It’s a compliment, as far as I’m concerned. You know what they say.”

The old man grinned. A terrible stench poured out from between his blackened, yellow teeth.

“Kill a hundred and you’re a Killing Ghost. Kill a thousand and they call you a hero. Kill ten thousand and you become… a king.”

My mouth felt gritty, like I’d been chewing sand. I stared at the old man, whose breath stank right in my face.

*What the hell is this?*

Something felt wrong. Just standing in front of him sent a chill down my spine.

Even in Murim, where every sort of person crossed paths, you didn’t run into people like this often.

“Who are you—or rather, who are all of you?”

“You call a Senior of Murim ‘you’? Does your master know his Disciple is so rude?”

“Someone I met recently told me that answering a question with a question is rude.”

The old man stared at me with wide eyes, then burst out laughing.

“Well, you got me good.”

“Now that you’ve had your laugh, answer me.”

“You know already, so why ask? Those children and I are martial artists, just like you.”

“I think you’re very different, personally. Am I just imagining things?”

“No need to worry. We may not belong to the Murim Alliance, but we’re comrades in the same boat.”

“What does that—”

As my voice trailed off, an idea suddenly struck me.

“No way…”

“Eunuch Ma. Is this enough of an answer?”

“……!”

“Everyone has a place and a role. You should go back and wait for your moment. If you draw any more attention, it’ll become a nuisance.”

With that, the old man rose to his feet and bowed to me.

“We’ll take care of the rest, so you can stop now, sir. We’ll handle everything from here.”

It was an unmistakable dismissal, as well as a performance for any watchers keeping an eye on us from somewhere.

No, calling this a simple performance would be an insult.

The old man was a laborer through and through, every movement perfectly in character.

“Please get back safely, sir. Then this old servant will be off…”

Step. Step.

As I watched the old man limp away with a box, I finally felt I understood who these people disguised as laborers were.

Even in this vast Murim, where countless different sorts of people roamed, there were only a few groups who could move around while hiding themselves so perfectly.

And then there was that overwhelming stench of blood.

At that moment, only one word came to mind.

Assassins.

* * *

Even among martial artists, with their hordes of lunatics and people who had no sense of self-preservation, there were certain sorts they’d always avoid. A few members were fixtures on that list.

Killing Ghosts. Fiends. Suspicious old men and beautiful women wearing veils, and so on.

Like Japan’s legendary first-string team, they were never easy to find. But martial artists with even a shred of common sense, and any hope of living long enough to retire in a village for the elderly, knew to steer clear of them.

Why? Simple.

Even messing with them—and sometimes just being near them—made a sense of doom creep over you.

And among them, right after Killing Ghosts and fiends, one of the top three most avoided professions was the assassin.

To put it bluntly, they were the three kings of utter bastards.

No one disputed it or questioned it.

In fact, quite a few people put assassins at the top of that list. And there was someone around me who’d given me similar advice.

It was a little ironic that the kindly advisor’s sobriquet was none other than the Slaughter Saint.

*Actually, “ironic” doesn’t even begin to cover it. It was practically black comedy.*

I muttered to myself and kept walking.

It suddenly occurred to me that I didn’t know where this road led. But that thought was quickly buried by the conversation with the Slaughter Saint that came to mind.

*“A Killing Ghost or a fiend would be better. But no matter what the circumstances, stay away from assassins.”*

*“Why? Aren’t they all the same kind of lunatic?”*

*“Your head’s as solid as a rock, so I’ll give you a simple example. Say you’re eating in an inn and a Killing Ghost or fiend suddenly walks in. What would you do?”*

*“That’d be fucking awful. I’m trying to eat.”*

*“Well… you’re not wrong, but think a little more deeply before you answer.”*

*“You called me a blockhead. I don’t want to think, so could you just tell me?”*

*“In case you’ve forgotten, I can break rocks with my fist. A head made of stone is no exception.”*

*“I see I was too quick to answer. Could you give me a moment?”*

*“You’ve gotten a little smarter.”*

*“Thank you. Hmm. First, I’d watch the Killing Ghost or fiend, then carefully…”*

*“Right. The first priority is to carefully get out of there.”*

*“No. I’d hit them first.”*

*“……What the hell did the Fire King teach you?”*

The Slaughter Saint had looked up at the sky and sighed, then hit me on the head a couple of times with his rock-breaking fist before saying,

*“To put it more simply, Killing Ghosts and fiends are no different from madmen who don’t think about the consequences.”*

*“Ow, my head. Doesn’t that make them even more dangerous? Like you said, if I ran into one in an inn, the whole place could turn into a sea of blood.”*

*“But you’d still have a decent chance of surviving.”*

*“Well, sure, if your martial skill is high enough…”*

*“It has nothing to do with skill. You can never predict people like that. They kill or spare people on a whim.”*

*“They really are crazy.”*

*“But what do you think an assassin would do?”*

*“An assassin… Oh.”*

*“Looks like you’re finally getting it. Exactly. They’re not just ordinary lunatics. They’ll do anything to assassinate their target. That’s why an assassin can kill an expert a level or two above them.”*

*“They’ll do anything to assassinate their target…”*

*“That’s why you need to be most careful around assassins and keep your distance. Understand?”*

*“Yes. I understand.”*

*“You don’t see many of them anymore, since they’ve lost their place in the world. But still… what are you doing?”*

*“Packing my things.”*

*“Why?”*

*“You told me to stay away from assassins.”*

*“……!”*

*“Oh, does that rule not apply to former assassins?”*

Man. I got beaten up a lot that day.

But that’s why I remember it so clearly.

The problem I was facing now was that I’d run into those very assassins in the middle of the imperial palace.

*If Ma Sanbao was going to bring in martial artists, why bring assassins into the imperial palace?*

Just as a question I couldn’t answer right away rose in my mind—

“Stop.”

A clear, bright voice pierced my ears.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1082.txt",
      "sha256": "b87d424c100567867f5a7372633bcb0d3eb65f95525a5bc48e3152562f0e5b71",
      "bytes": 13626
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7d230050deb529c8f6bee497ebf2481128d99911a3c0bf9cf8120f06de76a163",
      "bytes": 1314
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2b8adc3ec49ba710317887f508328ff1c2d7d669cd812e2e370b8fc8c7a1361d",
      "bytes": 243272
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "60c29a9c3d21fbd3158bd647c42ef62ebb68f580858cbb7e9db19dbc852542f1",
      "bytes": 1115
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2c0939c3549f681962e8e52f3aef52ffb444ea493fd2b106892e7455f97f50b7",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c4eb3eda5d6a7b823f60819e84af0a21de093fcefb2510644e428b8116ea98ef",
      "bytes": 1375
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "bbbafb47978de3f9517c96ca89cdc7b51f15920305acacb1883dda47cd963ecd",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "6d9f35e490d3e8722f732c551ef3d48cc60be96f6954b2e8f4dd209947993242",
      "bytes": 623
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "12d8a58e8d56aee76ae83d513aa28404e7961d96ca5af127bfc7ac205218196a",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1f5e163732c9516193969d12cde0c91050cbf77d3192d8b0b9b4c11686fa02b5",
      "bytes": 286270
    }
  ],
  "estimated_tokens": 11480
}
-->

# Durable State Update — Chapter 1082

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
1 and safe_through 1082. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1082. Profile updates may replace only one
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
  "chapter": 1082,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1082,
    "continuity_sources": [1082],
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
    "Xining is Qinghai’s capital and a stronghold against Dark Heaven; crowds from across the province have gathered there.",
    "Xining’s food stores can sustain its people for at most fifteen days.",
    "Hak Su is Cheongheoja’s Senior Disciple, Hak Woo’s senior brother, and a possible successor to Kunlun Sect leadership.",
    "Taekyung believes the Lord of Heaven does not want him killed, but does not know why.",
    "The black-robed captive survived interrogation and treatment and can now speak; Mujin is to talk with him.",
    "Hak Eui investigated Qinghai’s affairs and presented his case to the gathered leaders.",
    "The City Lord of Qinghai and around a dozen other criminals were publicly executed.",
    "Taekyung received a missive from the Murim Alliance in Henan."
  ],
  "continuity_sources": [
    1080,
    1081
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "What did the Murim Alliance’s missive say?"
  ],
  "safe_through": 1081,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 파륜     | **Pa Ryun**        |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 지능               | **Intelligence**               |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 은형술 | **concealment technique** | Peak-level technique used by the Hidden Thread to erase his presence. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 강풍 | **Kang Pung** | False name Cheongpung uses while disguised as the Invincible Divine Sword. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 살귀 | **Killing Ghost** | Mungyeong's earlier sobriquet before he became the Slaughter Saint. |
| 이룡 | **Two Dragons** | Collective ranking beneath the Ten Kings in Murim gossip. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 진맥 | **take one's pulse** | Mungyeong's prior medical examination of Jeok. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 녹림투왕 | **Green Forest Battle King** | Epithet of the Green Forest Alliance Leader, distinguished from the Ten Kings. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 태산 | 대인 | ally addressing an elder | Sir | informal and enthusiastic | Calls out to the Great Sir while praising his shot. |
| 대인 | 태산 | elder addressing a younger ally | young friend | familiar and playful | Offers Taishan a portion of the bird as a reward. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1081
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival, and the Slaughter Saint has become his mentor in concealment.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1081
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1079
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1081
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1081
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1081
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1082화




같은 시각, 서녕의 거리가 한눈에 내려다보이는 전각에서 공개 참형을 지켜보고 있던 것은 진태경뿐만이 아니었다.

서걱!

번뜩이는 칼날을 따라 굴러떨어지는 십여 개의 수급.

피 분수가 솟구치며 목을 잃은 시체들이 힘없이 기울어지는 모습에, 까맣게 거리를 뒤덮은 군중들이 함성을 토해 냈다.

- 와아아아!

- 황제 폐하 만세!

- 상산후께서 탐관오리들을 처단하셨다!

- 이 천인공노할 놈들! 지옥에나 떨어져라!

누군가는 기뻐하며 두 손을 번쩍 치켜들고, 아직 분이 풀리지 않은 누군가는 계속해서 욕과 야유를 쏟아냈다.

그러나 그런 그들을 내려다보는 한 청년의 얼굴은 복잡미묘했다.

“……음.”

나직한 침음성만이 입술을 비집고 흘러나온 그 순간, 누군가의 목소리가 불현듯 청년의 귓가를 파고들었다.

“오, 여기에 있었구먼.”

화들짝 놀라며 고개를 돌린 청년이 불청객의 정체를 확인하고 안도의 한숨을 내쉬었다.

“깜짝이야, 언제 오셨어요?”

“언제 오긴, 하루 전에 다 같이 와 놓고. 혹시 자네 바본가?”

“그, 아저씨. 제가 지금 한 말은 서녕에 언제 왔는지를 물어본 게 아니라…….”

“그럼?”

진심으로 의아하다는 눈빛으로 되묻는 추레한 행색의 중년인, 대인의 모습에 청년이 입맛을 다셨다.

“아니에요. 대인 아저씨 말씀이 맞아요. 하루 전에 왔었죠.”

“역시 짐작했던 대로 바보로군. 강풍 자네는 나이에 비해 너무 어리숙한 면이 있어.”

“청풍인데요.”

“내 말이 바로 그 말일세. 강풍.”

순간 말문이 막힌 청년, 아니 청풍은 턱을 긁적였다.

불과 며칠 전에야 알게 된 눈앞의 중년인은, 일반인의 한계를 아득히 벗어날 만큼 드넓은 정신세계를 지닌 그로서도 가끔 이해하기 어려운 상대였다.

물론, 다른 대부분의 사람들에게 있어서는 가끔이 아니라 항상이겠지만.

“……태어나서 아저씨 같은 사람 처음 봐요.”

“천하는 광활하지. 본녀처럼 견문을 넓혀 보게.”

“음. 이건 처음 뵀을 때부터 말씀드리려고 했던 건데, 본녀는 여인들이 스스로를 자칭할 때 쓰는 말로 알고 있어요.”

“그래서?”

“예?”

“겉으로만 사람을 판단하는 건 아주 잘못된 일이라네. 중요한 것은 본질이야. 그 후에야 비로소 그 안에 숨겨진 진실을 깨닫게 되는 거지.”

얼핏 현기(玄機)마저 느껴지는 대인의 모습을 멍하니 바라보던 청풍이 겨우 입을 열었다.

“방금 뭐랄까, 약간 신선 같으셨어요.”

“그런가?”

“네. 그런데 한편으로는 조금 없어 보이기도 해요.”

“자네, 말이 너무 심한 것 아닌가? 본녀야 그렇다 치더라도, 다른 사람이 그런 말을 들으면 마음의 상처를 받을 수도 있어.”

“앗. 죄송해요.”

“사과할 필요까지는 없네. 멍청한 게 죄는 아니니까.”

“……네에.”

엉겁결에 대답한 청풍이 이게 맞나 싶은 찝찝함을 느끼고 있던 그때, 한층 더 거대해진 바깥의 함성을 들은 대인이 다가와 창밖을 바라보았다.

“잔인하군.”

대인을 따라 시선을 돌린 청풍의 얼굴이 딱딱하게 굳었다.

일부 군중들이 참수당한 시체들을 유린하고 있는 광경이 선명하게 비치고 있었다.

“……그러네요. 괜히 봤어요.”

“조금 전의 뒷모습이 영 어두워 보이던데, 저것 때문이었나?”

“살생(殺生)은 언제나 익숙해지지 않더라고요. 만약 제가 은인처럼 굳센 사람이었다면 훨씬 나았을 텐데.”

혼잣말처럼 뇌까린 청풍은 문득 한 사람을 떠올렸다.

어떤 고난과 역경의 파도 앞에서도 늘 거침없고 흔들리지 않는 그, 진태경을.

세상 사람들은 그와 자신을 이룡(二龍)이라 칭하며 치켜세우지만, 청풍에게 있어 진태경은 선망의 대상이나 다름없었다.

그리고 그것은 강함과 약함, 무공에 대한 재능의 기준이 아니라 삶을 살아가는 모습 자체에 대한 선망이었다.

아마도 그래서였을 것이다.

다음 순간 들려온 대인의 한마디에, 일순간 할 말을 잃어버린 것은.

“그거 아나? 살생에 익숙해진 자를 이 세상은 살귀(殺鬼)라고 부른다는 것.”

“……!”

“굳센 자들은 내색하지 않을 뿐이네. 익숙해진 것이 아니라, 지쳐서 기진맥진해 있는 것에 가까워. 본녀가 알던 누군가도 그랬지.”

“아저씨도 그런 사람을 알고 계세요?”

“말했잖나. 본녀처럼 견문을 넓혀 보라니까.”

입을 벌려 하품을 쩍 내뱉은 대인이 말을 이었다.

“다만 그는 자신이 처한 현실을, 운명을 선택하고 받아들였네. 아마 자네가 닮고자 하는 그 사람도 같은 마음일걸?”

“……대인 아저씨, 이런 사람이었어요?”

“이런 사람이었냐니, 그게 대관절 무슨 소린가?”

“아니, 아니에요.”

물 흐르듯 흘러나오는 말에 눈을 깜빡이던 청풍이 이내 한숨을 푹 내쉬었다.

“아저씨 말씀이 옳아요. 제가 너무 멍청한 나머지 생각 없이 실언을 내뱉었어요.”

“다시 한번 말하지만, 멍청한 게 죄는 아니라네. 죽어서도 능욕을 당하고 있는 저자들도 진짜 죄인은 아니고.”

“죄인이 아니라고요?”

“아, 물론 저들이 죄인인 것은 맞지. 죽을죄를 지었으니 죽어도 싸. 하지만 진짜 죄인은 이 아수라장을 만든 장본인 아니겠나?”

대인이 손을 뻗어 어딘가를 가리켰다.

해가 중천에 떠 있을 시간임에도 우중충하게 잠겨 있는, 끝없이 펼쳐진 하늘을.

“상제(上帝)인지 뭔지가 저 위에 있는지는 몰라도, 그리 썩 대단한 놈은 아닐 거라는 데에 본녀의 불알을 걸지.”

진지한 표정으로 대인의 말을 경청하던 청풍이 고개를 갸웃거렸다.

“어어, 그건 저 같은 사내한테만 있는 건데…….”

“본녀도 있다니까.”

“아니, 그러니까 그걸 저도 갖고 있다니까요?”

“그럼 확실해졌군.”

대인이 준엄한 음성으로 말을 이었다.

“자네도 본녀와 같은 여인인 것이 분명해.”

만약 과거의 청풍이었다면 정말 그런가 생각했을지도 모른다. 그러나 이 년 남짓한 시간 동안 조금이나마 상식을 갖추게 된 현재의 청풍은 달랐다.

“둘째 할아버지가 그랬어요. 저는 남자라고.”

“그래? 그럼 그 둘째 할아버지도 그것을 갖고 있었나?”

“네. 소피 누실 때 살짝 봤어요. 바로 걸리는 바람에 하마터면 죽을 뻔했지만.”

“그렇단 말이지.”

심각한 얼굴로 고민하던 대인이 헉, 하고 헛숨을 토해냈다.

“이제야 알겠군.”

“뭘요?” 

“그자는 할아버지가 아닐세. 앞으로는 둘째 할머니라고 부르게.”

“……조심하세요. 그분 귀에 들어갔다가는 진짜 죽을지도 몰라요.”

“둘째 할머니는 본녀를 죽일 수 없네. 능치처참, 그 악독한 대마두도 결국 본녀의 앞에 무릎을 꿇었지. 결국 백두강산의 뱃속으로 들어갔지만.”

“지금 혹시 태산 소협 말씀하시는 거예요?”

“뭐, 그게 그거지. 중요한 건 본질이라고 몇 번을 말하나.”

왠지 모르게 정신이 어지러워진 청풍이 관자놀이를 문질렀다.

“대인 아저씨랑 얘기하면 왠지 모르게 혼란스러워져요. 이런 경험 처음이에요.”

“이해하네. 자네는 지능이 낮으니까.”

“멍청하다는 얘기만 몇 번째 듣는지 모르겠어요. 이러려고 저 찾아오신 거예요?”

“그야 당연히 아니지. 본녀가 그리 한가해 보이나?”

청풍이 그 어느 때보다 확신에 찬 음성으로 대답했다.

“네.”

“전혀 아닐세. 자네를 찾은 이유는…….”

자신 있게 말을 이어가던 대인이 순간 말꼬리를 흐렸다.

“그, 이유는…….”

“대인 아저씨.”

“왜 자꾸 부르나. 지금 말하려고 하는데.”

“처음 불렀고, 솔직히 말씀하세요. 뭐 때문에 왔는지 기억 안 나시죠?”

“말도 되는 소리!”

벌컥 성을 낸 대인이 머뭇거리며 덧붙였다.

“사실 가물가물하네만. 뭐, 별로 중요한 얘기는 아닐 테니 넘어가세.”

“안 중요한 얘기인 거, 확실해요?”

“확실하네. 아마 누가 자네를 불러오라고 했던 것 같긴 한데…… 엄청나게 중요한 얘기였다면 본녀가 기억하지 못했을 리가 없어.”

대인이 더 이상의 반박은 허용하지 않겠다는 듯이 단호하게 대답한 그때, 저 멀리서 빠르게 가까워지는 인기척이 있었다.

“청풍 소협! 어디 계세요! 에이씨, 청풍 소협!”

익숙한 목소리와 얼굴.

헐레벌떡 여기저기를 오가는 혁무진의 모습을 본 청풍이 손을 번쩍 치켜들었다.

“어, 혁 무사님!”

“미치겠네. 왜 아직도 여기 계세요? 대인 그 인간은 또 어디 갔고?”

“네? 대인 아저씨는 여기에 저랑 같이…….”

반사적으로 말꼬리를 흐린 청풍이 눈을 깜빡였다.

조금 전까지만 하더라도 바로 옆에 서 있던 대인은, 어느샌가 그의 등 뒤에 바짝 몸을 움츠린 채 숨어 버린 후였다.

“……아저씨?”

“쉿. 아는 척 말게. 자네는 정말 지능이 낮은 건가?”

청풍으로서는 뭐라 대꾸할 틈도 없었다.

실로 간단하면서도 완벽한 은형술을 펼친 대인의 모습에 어이없음을 느끼기도 전, 숨을 헐떡이며 다가온 혁무진의 한 마디가 벼락처럼 뇌리를 관통했으니까.

“지금 여기서 이러고 있을 때가 아닙니다! 서장(西藏)의 포달랍궁(布達拉宮)이 암천과 손을 잡았다고요!”

“……!”

일순간 크게 부풀어 오르는 청풍의 두 눈동자.

하지만 혁무진의 말은 그것으로 끝이 아니었다.

아니, 오히려 그와는 비교할 수 없는 그 이상의 충격이었다.

“그뿐만이 아닙니다! 해상왕(海上王) 파륜과 녹림투왕(綠林鬪王) 태군악이……!”

암천과의 대립이 본격화될 무렵부터 무림맹이 우려해 왔던 서장 무림의 합류.

거기에 더해 흑도(黑徒) 무림을 양분하는 두 거인의 별호와 이름이 흘러나온 순간, 청풍은 뒤에 이어질 말이 무엇인지 깨달았다.

‘배반.’

그리고 그 불길한 짐작은 이내 확신이 되었다.

언제나 그렇듯이.



* * *



“백 리 밖에서부터 거름 냄새가 진동하더라니. 역시 자네였군.”

먼저 침묵을 깬 것은 압도적인 거구를 지닌 노인이었다.

부리부리한 눈매에서 뿜어져 나오는 안광은 손에 쥔 언월도(偃月刀)가 간직한 예기보다 강렬했고, 전신에서 뿜어져 나오는 기세는 파도처럼 거대했다.

해상왕이라는 그 별호만큼이나.

“생선 비린내보다야 낫지. 일평생을 날로 처먹었으니 지금쯤 배 속에 회충이 드글거릴 텐데, 슬슬 뱃일 접고 노부의 밑으로 들어오는 건 어떤가?”

그러나 백여 장의 거리를 두고 마주 선 또 한 명의 노인 역시 만만치 않았다.

왜소하기 짝이 없는 체구와 나뭇가지처럼 가느다란 뼈대.

닭 모가지 비틀기에도 힘들어 보이는 고령의 노인임에도 불구하고, 그에게는 파륜을 향해 비아냥거릴 자격이 충분했다.

해상왕 파륜이 장강의 왕이라면, 그는 산맥의 지배자였으니까.

지금의 녹림맹(綠林盟)을 일구어 낸 장본인, 녹림투왕 태군악이었으니까.

“노부는 지랄이. 핏덩이 주제에 못하는 말이 없군. 썩은 하오수라도 잘못 처먹었나?”

“기껏해야 한 살 차이 가지고 핏덩이 운운하는 것도 우습군. 무림에서의 경륜만 따져도 분명히 노부가 선배일 텐데?”

“그래서, 아무도 십왕이라 불러 주지 않는 것 같아 스스로 왕을 자처했나?”

기다렸다는 듯이 받아치는 파륜의 모습에 태군악의 눈빛이 침잠하게 가라앉았다.

“네놈은 늘 그 혀가 문제야.”

“누가 할 소리인지 모르겠군.”

두 노인은 말없이 서로를 응시했다. 어느덧 유형화된 기운이 어깨 위로 피어올라 넘실거렸다.

마치 지금 당장이라도 목숨을 건 일전을 펼칠 것처럼.

하지만 다음 순간.

스아아악.

단숨에 기세를 가라앉힌 흑도의 두 거인은 조용히 입맛을 다셨다.

원하는 것을 얻기 위해 수단과 방법을 가리지 않고 살아온 그들이다. 이 기나긴 견원지간(犬猿之間)의 끝이 언제일지는 모르나, 적어도 지금이 아니라는 것쯤은 서로가 알고 있었다.

“계획은?”

“순조롭게 흘러가고 있지. 전달받은 대로.”

자신의 등 뒤, 빽빽하게 늘어선 삼림을 가라앉은 눈빛으로 바라본 태군악이 파륜을 향해 덧붙였다.

“잊지 마라. 이틀, 이틀 뒤다.”

깊고, 나직하게.

“장강을 장악해라. 그것이 시작이다.”
```

## Final English reading copy

```markdown
# Chapter 1082

At the same time, Jin Taekyung wasn’t the only one watching the public executions from a pavilion overlooking the streets of Xining.

*Shhk!*

A dozen or so heads rolled from the flashing blades.

As fountains of blood erupted and the headless bodies crumpled lifelessly, the crowds that blanketed the streets roared.

“Waaaaah!”

“Long live His Majesty the Emperor!”

“The Marquis of Shangshan has punished the corrupt officials!”

“You fiends! Rot in hell!”

Some people threw up their hands in celebration, while others, still too angry to be satisfied, continued to curse and jeer.

But the young man looking down at them wore a conflicted expression.

“...Hmm.”

A low groan slipped from his lips. Then someone’s voice suddenly pierced his ears.

“Oh, there you are.”

The young man spun around in alarm. When he saw who the unexpected visitor was, he let out a sigh of relief.

“You startled me! When did you get here?”

“When did I get here? We all arrived yesterday. Are you an idiot?”

“Um, Uncle… I wasn’t asking when you came to Xining…”

“Then what?”

The shabby, middle-aged man—Great Sir—looked genuinely puzzled. The young man clicked his tongue.

“No, you’re right, Uncle Great Sir. We got here yesterday.”

“As I suspected. You are an idiot. Kang Pung, you’re far too naïve for your age.”

“It’s Cheongpung.”

“That’s exactly what I said. Kang Pung.”

For a moment, the young man—no, Cheongpung—was at a loss for words. He scratched his chin.

Even with the breadth of mind to reach far beyond the limits of ordinary people, he sometimes found the middle-aged man before him difficult to understand. They’d only met a few days ago.

Of course, for most people, it probably wasn’t just sometimes. It was all the time.

“...I’ve never met anyone like you.”

“The world is vast. You should broaden your horizons like this maiden.”

“Hmm. I’ve been meaning to say this since we first met, but I thought ‘this maiden’ was what women called themselves.”

“So?”

“Huh?”

“Judging people by appearances alone is a grave mistake. What matters is the essence. Only then can you understand the truth hidden within.”

Cheongpung stared blankly at Great Sir, who seemed, for a moment, to possess some profound insight. At last, he managed to speak.

“You almost sounded like an immortal just then.”

“Did I?”

“Yeah. But at the same time, you also seemed a little… unimpressive.”

“Isn’t that a bit harsh? I don’t mind, being this maiden and all, but someone else might be hurt by that.”

“Oh! I’m sorry.”

“No need to apologize. Being stupid isn’t a sin.”

“...Okaaay.”

Cheongpung answered without thinking. He was still feeling uneasy about whether that had been the right thing to say when Great Sir, hearing the roar outside grow louder still, came over to look out the window.

“How cruel.”

Cheongpung followed his gaze, his face stiffening.

The scene was clear: some of the crowd were desecrating the bodies of the executed men.

“...It is. I shouldn’t have looked.”

“You seemed down when I saw you from behind a little while ago. Was that why?”

“I never get used to killing. If I were as strong-willed as my Benefactor, I’d be much better off.”

Muttering as if to himself, Cheongpung suddenly thought of someone.

Jin Taekyung. No matter how high the waves of hardship and adversity rose, he always faced them head-on, never wavering.

People in the world praised Cheongpung and Taekyung as the Two Dragons, but to Cheongpung, Jin Taekyung was someone to look up to.

Not because of strength or weakness, or talent in martial arts. He admired the way Taekyung lived.

Perhaps that was why, at Great Sir’s next words, Cheongpung was momentarily speechless.

“Did you know? This world calls someone who’s grown used to killing a Killing Ghost.”

“...!”

“The strong-willed ones simply don’t show it. They haven’t gotten used to it. They’re closer to being worn out and utterly exhausted. Someone I knew was like that, too.”

“Do you know someone like that, Uncle?”

“I told you. You should broaden your horizons like this maiden.”

Great Sir let out an enormous yawn, then continued.

“But he chose to accept the reality and fate he was dealt. The person you want to be like probably feels the same way.”

“...Uncle Great Sir, is this really who you are?”

“What on earth do you mean, ‘is this who I am’?”

“No, it’s nothing.”

Cheongpung blinked at the words that had flowed so easily from Great Sir’s mouth, then let out a long sigh.

“You’re right. I was so stupid that I spoke without thinking.”

“I’ll say it again: being stupid isn’t a sin. And those men being desecrated even after death aren’t the real sinners, either.”

“They aren’t?”

“Oh, of course they’re sinners. They committed crimes worthy of death, so they deserved to die. But isn’t the real sinner the one who created this asura’s hell?”

Great Sir pointed somewhere.

At the endless stretch of sky, gloomy and overcast even at midday.

“I don’t know if some so-called Lord of Heaven is up there, but I’ll bet my balls he’s not all that impressive.”

Cheongpung, who had been listening to Great Sir with a serious expression, tilted his head.

“Um, only men like me have those…”

“I told you, I have them too.”

“No, I mean, I have them too.”

“Then that settles it.”

Great Sir continued in a solemn voice.

“It’s obvious you’re a woman like me.”

If this had been the old Cheongpung, he might have wondered whether that was true. But after a little over two years of gaining some common sense, the Cheongpung of today was different.

“My Second Grandfather said I’m a man.”

“Really? And did your Second Grandfather have them, too?”

“Yeah. I caught a glimpse while he was peeing. I got caught right away and nearly died, though.”

“I see.”

Great Sir thought it over with a serious expression, then gasped.

“Now I understand.”

“What?”

“He isn’t your grandfather. From now on, call him Second Grandmother.”

“...Be careful. If that gets back to him, he might really kill you.”

“Second Grandmother can’t kill this maiden. Slow Slicing—the vicious fiend—even he eventually knelt before me. Though he ended up in Baekdu Gangsan’s belly.”

“Are you talking about Young Hero Taishan?”

“Well, same difference. How many times have I told you? What matters is the essence.”

Cheongpung rubbed his temple, feeling disoriented for some reason.

“Whenever I talk to you, I get confused. This is a first for me.”

“I understand. Your Intelligence is low.”

“I’ve lost count of how many times you’ve called me stupid. Is that why you came to find me?”

“Of course not. Do I look like I have that much free time?”

Cheongpung answered with more certainty than ever.

“Yes.”

“Not at all. The reason I came to find you was…”

Great Sir had confidently begun, but his voice faltered.

“The, um, reason…”

“Uncle Great Sir.”

“Why do you keep interrupting me? I’m trying to tell you.”

“That was the first time I called you. And be honest—you don’t remember why you came, do you?”

“What nonsense!”

Great Sir snapped, then added hesitantly:

“Truthfully, it’s a little hazy. But it can’t have been important, so let’s move on.”

“Are you sure it wasn’t important?”

“I’m sure. I think someone may have asked me to come get you, but if it had been anything terribly important, I’d remember.”

Just as Great Sir answered firmly, as if to allow no further argument, someone’s presence came rushing toward them from far away.

“Young Hero Cheongpung! Where are you? Damn it, Young Hero Cheongpung!”

A familiar voice and face.

Cheongpung raised his hand at the sight of Hyuk Mujin rushing around in every direction.

“Oh, Captain Hyuk!”

“I’m going crazy. Why are you still here? And where’d that Great Sir go?”

“Huh? Great Sir is right here with me…”

Cheongpung trailed off and blinked.

Great Sir, who had been standing right beside him just a moment ago, had somehow ducked down and hidden himself close behind Cheongpung.

“...Uncle?”

“Shh. Don’t let on that you know me. Are you really that low in Intelligence?”

Cheongpung had no time to answer.

Before he could even feel exasperated at Great Sir’s simple yet flawless concealment technique, Hyuk Mujin hurried over, panting, and said something that struck Cheongpung like a bolt of lightning.

“This is no time to stand around here! The Potala Palace in Tibet has joined forces with Dark Heaven!”

“...!”

Cheongpung’s eyes widened in an instant.

But Hyuk Mujin wasn’t finished.

No—the next news was an even greater shock, one that put the first to shame.

“And that’s not all! Seafaring King Pa Ryun and Green Forest Battle King Tae Gunak…”

Since the conflict with Dark Heaven had begun in earnest, the Murim Alliance had feared that the Murim world of Tibet would join them.

On top of that, the moment he heard the names and titles of the two giants who divided the dark-path Murim between them, Cheongpung understood what was coming next.

*Betrayal.*

And as always, his ominous suspicion soon became certainty.

* * *

“The smell of manure was wafting all the way from a hundred li away. I knew it had to be you.”

The first to break the silence was an old man with an overwhelming build.

His blazing eyes were more intense than the sharp edge of the crescent-bladed guandao in his hand, and the aura pouring from his entire body was as vast as a surging wave.

As immense as his title, the Seafaring King.

“Better than the smell of fish. You’ve spent your whole life eating it raw. Your belly must be crawling with worms by now. How about you quit your life at sea and come work under this old man?”

But the other old man facing him from more than three hundred yards away was no pushover, either.

He was pitifully small, his bones thin as twigs.

Though he was so old he looked as if he might struggle to wring a chicken’s neck, he had every right to sneer at Pa Ryun.

If the Seafaring King Pa Ryun was the king of the Yangtze, then he was the ruler of the mountains.

The man who had built the Green Forest Alliance of today—the Green Forest Battle King, Tae Gunak.

“‘This old man,’ my ass. You’re a squirt, yet you run your mouth like that. Did you swallow some rotten sewage by mistake?”

“Funny, calling me a squirt over a mere one-year age difference. And even if we’re only counting our experience in Murim, I’m clearly your Senior.”

“Is that why you named yourself a king, since no one would call you one of the Ten Kings?”

Pa Ryun fired back as if he’d been waiting for the chance. Tae Gunak’s gaze sank.

“Your tongue’s always been the problem.”

“Funny. I was about to say the same thing.”

The two old men stared at each other in silence. Their auras had taken on visible form, billowing above their shoulders.

As if they might risk their lives in a fight at any moment.

But the next instant—

*Fwoosh.*

The two giants of the dark-path Murim swiftly suppressed their auras and quietly clicked their tongues.

They had lived without hesitation, using any means necessary to get what they wanted. They didn’t know when this long-standing rivalry would end, but they both knew it wouldn’t be today.

“How’s the plan?”

“Going smoothly. Just as we were told.”

Tae Gunak looked toward the dense forest behind him, his gaze darkening, then added to Pa Ryun:

“Don’t forget. Two days. Two days from now.”

His voice was deep and low.

“Take control of the Yangtze. That’s where it begins.”
```

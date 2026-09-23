<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0900.txt",
      "sha256": "1b738d222ca1a5c7c7409b391b7cbbd30240a9bc196f439411b387fdc2ad8c49",
      "bytes": 13277
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "297454a5cb4fae537d6e8541d7d55d0acbb3db37e825831597e60c9f7a2915aa",
      "bytes": 1179
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "15b7559bed5551ab89a765328d3f0a3fb2d8b907d46fb1c26625499fb4cab311",
      "bytes": 230936
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "8ee24c109ae1827894a7bdf5cf78e8e1dbe1a14a2e864838d870abd50f99b285",
      "bytes": 983
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "7f119ad9422abff2f13ee5437a86ff50c7a848b43234b8cf0e62b4c5b119b6e9",
      "bytes": 1369
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3eac30ce5c2cdee3937ecf3565ffa4241289ede2542d946bca48a36190b73a18",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "3dc90c66b85dc7c7752897019e3ec1aff31ee5d36277acb99c0fa4d87f1d7b4d",
      "bytes": 970
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "cdcf8d553c53a06efe5849039aa3bd6d39b6d208d5ff94d84712001944ed0026",
      "bytes": 952
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8ead4207b37bea0c8bdc317b844fae2124946506bd434491dd7489b0ce8d1c7b",
      "bytes": 261385
    }
  ],
  "estimated_tokens": 10840
}
-->

# Durable State Update — Chapter 900

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
1 and safe_through 900. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 900. Profile updates may replace only one
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
  "chapter": 900,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 900,
    "continuity_sources": [900],
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
    "The imperial birthday banquet is underway; Taekyung and Hong Jin are being escorted to the Grand Banquet Hall by the Embroidered Uniform Guards.",
    "Taekyung suspects the Emperor smokes opium, having recognized its scent from his earlier audience at Qianqing Palace; the reason is unknown.",
    "The Emperor is preparing to leave Qianqing Palace for the banquet. Taekyung and his Master are present, while the other martial artists have left the palace.",
    "So Gyo stopped the Emperor’s agents from pursuing the departing martial artists and has reclaimed her weapons.",
    "A vast golden procession is approaching the Grand Banquet Hall five hours late."
  ],
  "continuity_sources": [
    898,
    899
  ],
  "open_questions": [
    "Why might the Emperor be smoking opium?",
    "What will happen when the Emperor’s procession reaches the banquet hall?",
    "What purpose do the departed martial artists have, and where are they going?"
  ],
  "safe_through": 899,
  "temporary_decisions": [
    "Translate 앵속 as “poppy” in the explanation and use “opium” when Taekyung identifies the substance."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 사천당가   | **Sichuan Tang Clan**            |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 표국     | **Escort Bureau**                            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 진가표국 | **Jin Family Escort Bureau** | New name for the former Seongun Escort Bureau under the Jin Family. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 진가상단 | **Jin Family Trading Company** | Commercial organization belonging to the Jin Family of Taiyuan. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 진수 | **Jinsu** | Named budding talent who receives Taekyung's autograph. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 대역 | **stand-in** | Jin's term for the substitute Go Jun used to fake Song Cheonwoo's departure. |
| 신인 | **divine man** | Descriptive term for a human who became something beyond humanity. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 건청궁 | **Qianqing Palace** | The Emperor's palace, where Baek Yeon meets him. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 중년인 | 상산왕 | unknown imperial subject addressing a prince | His Highness, Prince Shangshan | formal and deferential | Addresses him as 상산왕 전하 while remarking on seeing him grown. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 896
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a former martial arts instructor to the Crown Prince, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, he enforces authority with ruthless decisiveness but speaks with striking defiance to the Emperor in private when their shared undertaking is at stake.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; they share an old promise tied to a great undertaking, and Baek urges the Emperor to restore matters before their adversaries' moves unravel it. He orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 899
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Ma Sanbao recruited Jin and Jeok for the restoration effort supporting Prince Shangshan, and Jin has signed its pledge and arranged for Ma to summon Murim Alliance reinforcements.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 899
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 896
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and Supreme Peak martial artist, leading it in place of the bedridden Cang Gong and organizing a secret restoration effort for Prince Shangshan.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin, leads the restoration effort for Prince Shangshan, and recruited Jin Taekyung and Jeok Cheongang as discreet allies; Jin has signed the pledge and entrusted Ma with summoning Murim Alliance reinforcements.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 897
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

## Korean source

```text
＃900화



쿵. 쿵쿵.

땅이 울린다. 이글거리는 횃불이 밤을 깨운다.

황실의 깃발을 휘날리며 오와 열을 맞추어 진군하는 천 명의 금의위. 그 뒤를 따라 이동하는 수많은 환관과 궁녀들.

그리고 그 중심에, 오직 한 사람을 위해 만들어진 거대하고도 화려한 어가(御駕)가 있었다.

쿠웅!

마침내 대연회장에 진입한 일천의 금의위가 동시에 발을 굴렀다.

동시에 발산된 막강한 기파(氣波)가 대기를 떨어 울리며 모두의 피부에 닿았다.

“드디어…….”

누군가의 입술 사이로 흘러나온 목소리를 들은 이들은 문득 생각했다.

저 목소리의 주인은 과연 누구일까.

둘 중 어느 편에 섰으며, 어떤 결과를 기다리고 있을까.

그러나 의문에 대한 답을 떠올릴 시간은 주어지지 않았다.

대연회장에 이르러 멈춘 거대한 행렬 속에서, 한 마리의 준마를 천천히 몰아 앞으로 나선 누군가가 천둥 같은 외침을 토해 냈으니까.

“하늘과 땅, 천하 만물의 주인이신 대국의 지존께서 친히 납시었으니, 대소신료(大小臣僚)는 모두 무릎을 꿇고 황제 폐하를 배알하라!”

화아악!

전신을 감싼 황금빛 갑옷과 깊게 눌러쓴 투구로도 감출 수 없는, 실로 압도적인 존재감.

명실상부한 황제의 오른팔이자 금의위 지휘사인 백연이 공력을 실어 터트린 외침에, 대연회장의 모두가 자리에서 일어나 무릎을 꿇었다.

처척.

문무백관만 수백이요, 이미 주위를 빈틈없이 경계하고 있던 병력만 수천이다.

마치 한몸처럼 일사불란하게 움직인 그들은 이 광활한 대륙의 주인을 향해 고개를 조아렸다.

비록 누군가에게는 그것이 허울뿐인 예라고 해도, 아직 이 연회를 끝장낼 도화선의 불꽃은 끝까지 타들어 가지 않았으니까.

“황제 폐하, 만세.”

마삼보의 나직한 읊조림을 시작으로, 이내 모두가 외치기 시작했다.

“황제 폐하, 만세! 만세! 만만세!”

바로 그때였다.

그 쩌렁쩌렁한 외침의 끝자락에서, 사인교에서 내린 황제가 느린 발걸음으로 인의 장막을 가로지른 것은.

저벅. 저벅.

유독 선명하게 울려 퍼지는 발걸음.

하지만 자신들을 스쳐 지나가는 황제의 모습을 고개 숙인 그들은 볼 수 없었고, 마침내 드높은 계단 위 옥좌(玉座)의 빈자리가 채워진 후에야 비로소 자세를 바로 하며 황제를 대면할 수 있었다.

장장 수년 동안이나 건청궁에서 두문불출하며 정사(政事)를 돌보았던 천하의 주인을.

대국의 네 번째 황자에서 반역자로, 반역자에서 마침내 황위를 거머쥔 희대의 패륜아이자 학살자.

또한 하늘 아래 가장 높은 곳에 선 풍운아를.

그리고, 경악했다.

“……!”

“……!”

찰나의 순간, 보이지 않는 동요와 충격이 물결처럼 대연회장을 휩쓸었다.

긴 칩거 끝에 모습을 드러낸 황제에게서 젊고 준수했던 과거의 흔적 따위는 찾아볼 수 없었으니까.

그러나 황제는 아랑곳하지 않았다.

그는 헤아릴 수 없을 만큼 무수한 시선들을 오연하게 내려다보고 있었다.

과거의 모습을 찾아볼 수 없는 노쇠한 모습으로, 하지만 이 자리의 누구보다 번뜩이는 눈빛으로 대연회장을 가득 메운 대소신료들을 차례차례 응시했다.

이 거대한 제국을 지탱하는 기둥이자, 명실상부한 중추들.

그중에는 일군을 이끄는 장군도 있었고, 굽은 허리와는 달리 꼿꼿한 눈을 한 늙은 학사도 있었다.

동창의 실질적인 수장이자 가장 큰 정적인 마삼보 역시 빠질 수 없으리라.

하지만 황제의 시선이 마지막으로 향한 곳에는, 저 멀리 끝자리에서 조용히 그를 응시하는 한 청년이 있었다.

‘진태경.’

허공에서 맞닿은 시선.

황제가 진태경을, 진태경이 황제를.

두 사람은 한동안 아무런 말 없이 서로를 바라보았고, 마침내 굳게 닫혀 있던 황제의 입술이 열렸다.

“시작하라.”

아마도 비단 몇몇 사람만의 착각은 아니었을 것이다.

둥. 둥. 두웅!

대연회의 시작을 알리는 저 북소리가, 마치 전쟁의 서막을 알리는 전고(戰鼓)와 같다고 느낀 것은.



* * *



빙하처럼 얼어붙어 있던 분위기가 조금씩 녹기 시작한 것은 어마어마한 양의 진수성찬과 함께 입장한 악공과 무희들이 공연을 시작하면서부터였다.

듣는 것만으로도 심금을 울리는 선율과 그에 맞춰 흩날리는 옷자락.

거기에 더해 황실 숙수들이 한껏 솜씨를 발휘한 음식과 내로라하는 명주(銘酒)까지 무한정 제공되었으니.

초조한 마음 때문에 술 한잔을 기울인 이들의 마음이 조금이나마 느슨해지는 것은 당연한 일일지도 몰랐다.

“후, 이제야 좀 숨이 트이는군.”

“그러게나 말입니다. 정말 무슨 일이라도 터지는 줄 알았…….”

“그 입 닥치게. 말 한마디 잘못했다가 괜한 오해를 사고 싶나?”

“소, 송구합니다. 대감.”

“두 번 다시 그따위 불경한 소리를 입에 올렸다간, 내 가만있지 않을 걸세.”

한껏 억누른 목소리로 옆자리의 젊은 관리를 윽박지른 중년인이 날카로운 눈빛으로 주위를 훑는다.

혹여 누가 듣진 않았을까 하는 불안한 기색.

나는 자연스럽게 앞에 놓인 안주를 한 점 집어 먹었다.

다음 순간 맞은편에 앉아 있던 중년인의 시선이 유독 끈질기게 달라붙는 것을 느낄 수 있었다.

때마침 귓가로 전해지는 젊은 관리의 목소리도 함께.

“대, 대감. 제가 실언을 하긴 했으나 아무도 듣지 못했을 겁니다. 금의위도 저리 멀리 떨어져 있지 않습니까.”

틀린 말은 아니었다.

오늘 대연회장으로 쓰이는 이곳은 수천의 군사를 동시에 훈련시켜도 될 만큼 넓었고, 그런 이유로 일정한 간격으로 자리를 배치받은 관리들의 거리 역시 상당했으니까.

더군다나 한 사람 한 사람이 뛰어난 고수인 금의위는 수장인 백연을 비롯한 몇몇만이 황제의 곁에 머무르고 있을 뿐.

나머지는 저 멀리 떨어져 정해진 위치를 고수하고 있는 중이었다.

하지만 그런 젊은 관리의 말에도 중년인은 한동안 나를 유심히 지켜본 후에야 이렇게 말했다.

“저자에 대해 아는 바가 있나?”

“예? 예에. 강호의 무뢰배라는 이야기는 언뜻 들은 적이 있습니다.”

“그게 전부인가?”

“무슨 말씀이신지…….”

“쯧. 이렇게 생각이 없어서야. 자네 부친과 내가 인연이 있다는 걸 감사히 여기게. 아니었다면 지금 이 자리까지 오지도 못했을 테니.”

작게 혀를 찬 중년인이 말을 이었다.

시종일관 그랬듯이 속삭이듯 낮은 목소리로.

“한낱 무뢰배가 어찌 이런 자리에 참석할 수 있겠나? 저자는 상산왕 전하께서 데려오신 호위이자 빈객일세. 근래 들어 장강 이남까지 세력을 확장한 태원진가의 삼남이기도 하지.”

“태원진가. 태원진가…… 혹시 진가상단과 진가표국을 운영하는 그곳을 말씀하시는 겁니까?”

“그래. 그리고 그 태원진가는 상산왕 전하의 봉지(封地)인 산서땅에 자리 잡고 있지.”

“허어.”

젊은 관리가 희미한 탄성을 흘렸다.

“그 정도 가문이라면 산서성에는 상당한 위세를 떨치고 있겠군요.”

“상산왕 전하의 비호를 받고 있으니 아닐 말이겠나. 대국의 지엄한 국법을 거스르는 강호인들에게는 가당치도 않은 이야기지만…… 산서성 일대에서는 사실상 패자(霸者)로 군림하는 모양이더군.”

“하여 대감께서도 저자를 신경 쓰시는 것입니까? 무공을 익힌 무림 세가의 자제라서?”

“단순히 그 정도가 아닐세.”

“하면…….”

“열화신룡(烈火神龍). 그것이 저자의 별호일세. 이미 강호에서는 모르는 이가 없는, 약관 어림의 나이에 숱한 전공을 세운 엄청난 고수라고.”

“나름대로 조사를 하긴 했군.”

“굳이 자세히 알아볼 필요도 없었네. 황도의 백성들 사이에서도 열화신룡 진태경에 대해 아는 이들이 수두룩…….”

내게서 눈을 떼지 않은 채 말을 이어 가던 중년인이 문득 눈살을 찌푸렸다.

“자네, 지금 나한테 반말했나?”

하지만 젊은 관리는 대답하지 않았다.

평소였다면 허둥지둥 변명했을 그는, 이미 새하얗게 질린 얼굴로 자신과 중년인의 등 뒤에 서 있는 한 사람을 바라보고 있었다.

일 초.

이 초.

삼 초.

세상이 멈춘 듯한 그 침묵 끝에, 중년인은 젊은 관리의 시선을 따라 느릿느릿 고개를 돌렸다.

그리고 석상처럼 굳었다.

“화, 황제 폐하……!”

폐부를 쥐어짜 낸 듯한 그 한 마디가 비명처럼 들렸던 것은 결코 나 혼자만의 착각이 아닐 것이다.

황제.

천자(天子)라는 그 명칭처럼, 하늘의 후손이라 불리는 절대자는 말없이 두 사람을 내려다보았다.

마치 저들을 어떤 방식으로 죽일까 고민하는 사람처럼.

십여 년 전, 물경 수만 명의 ‘역적’들을 숙청하는 것에 앞장섰던 백연이 황제의 뒤에 우뚝 서 있었기에 더더욱 그렇게 보이는지도 몰랐다.

“폐, 폐하. 부디…….”

펄럭.

황제의 작은 손짓과 동시에 뚝 끊기는 목소리.

그렇다. 저 오만하고 잔혹한 절대자는 아직 입을 열지 않았다.

그리고 누구도 자신보다 먼저 입을 여는 것을 허락하지 않을 것이다.

어느덧 쥐죽은 듯이 고요해진 대연회장 속에서, 황제는 불현듯 고개를 돌려 나를 바라보았다.

“태원진가의 진태경.”

“……!”

“……!”

느껴진다.

흔들리는 공기가.

내 전신을 사정없이 꿰뚫는 무수한 시선들이.

제국을 지탱하는 고관대작과 숱한 대소신료. 그 사이에서 유일한 이방인인 내게 황제가 먼저 말을 걸었다.

그것도 옥좌와는 한참 떨어진 말석(末席)까지 손수 걸음을 옮기면서까지.

“짐이 네게 묻건대, 이들을 어찌해야 할까.”

며칠 전이었다면 놀랐을 거다.

이 미친 새끼가 왜 갑자기 지랄이지, 뭐 그런 생각과 함께 슬슬 오줌이 마려워졌겠지.

하지만 오늘만큼은 아니었다.

‘그래, 아니지.’

나는 이미 각자의 생사를 판돈으로 건 도박판에 발을 디뎠다.

황궁이라는 호랑이 굴에 들어온 순간부터 이 모든 것은 예정되어 있던 것일지도 몰랐다.

때가 됐다.

주사위는 던져졌고, 지금부터는 주사위의 눈을 확인할 시간이다.

“글쎄요. 우선 대답하기 전에 술 한잔만 해도 되겠습니까?”

솨아아.

다시 한번 공기가 흔들린다.

아니, 흔들렸다는 표현에는 약간의 어폐가 있을지도 모른다.

조금 전의 파장이 호수에 돌을 던진 수준의 잔물결이었다면, 이번에는 삼각파도와 같은 재해(災害)였으니까.

그렇게 대연회장의 모든 사람들은 삽시간에 들이닥친 파도 앞에서 멍하니 입을 벌렸고, 나는 작게 고개를 끄덕이는 황제를 향해 입을 열었다.

“그럼 허락하신 걸로 알겠습니다.”

쭈욱.

내가 대답 대신 미리 따라져 있던 술잔을 입안에 털어 넣기 무섭게, 사방에서 경악과 고성이 터져 나왔다.

직접 보고 들었음에도 현실감이 없었던 저 파도가, 마침내 그들을 휩쓴 것이다.

“이런 미친놈을 보았나!”

“저, 저놈이 감히……!”

“어찌 저리 무도한 자가 있을 수 있단 말인가!”

“금의위 지휘사께서는 무얼 하고계시오! 어서 대역 죄인의 목을 치지 않고!”

“폐하! 폐하와 황실을 모독한, 저 천인공노할 무뢰배를 즉각 처단하소서!”

“부디 처단하소서!”

데시벨 보소.

욕을 많이 먹으면 장수한다던데, 아마 지금의 이 열광적인 분위기가 일각 정도만 더 지속됐다면 내 별호가 열화신룡이 아닌 삼천갑자가 됐을 거다.

목을 치는 건 기본이고, 거열형으로 사지를 찢기 전에 불알을 자른 다음 천천히 고문으로 조지자는 특별 옵션까지 줄줄이 추가되고 있었으니까.

‘……아니, 아무리 그래도 불알은 좀.’

설마 사천당가 출신인가.

나는 중성화 수술을 건의한 놈의 얼굴을 똑똑히 눈에 담은 뒤 술잔을 내려놓았다.

그리고 황제를 바라보며 입을 열었다.

“죽일 거면 죽이고, 살릴 거면 살리십시오. 그게 폐하 주특기 아닙니까.”

음.

슬슬 오줌 마렵다.
```

## Final English reading copy

```markdown
# Chapter 900

Thud. Thud-thud.

The earth trembled. Blazing torches roused the night.

A thousand Embroidered Uniform Guards marched in ranks, imperial flags flying overhead. Behind them came countless eunuchs and palace maids.

And at the center of it all was a magnificent, enormous imperial carriage, built for one person alone.

*Boom!*

At last, the thousand Embroidered Uniform Guards entered the Grand Banquet Hall and stamped their feet in unison.

The powerful waves of qi they unleashed at the same time shook the air and washed over everyone’s skin.

“At last…”

Those who heard the voice slip between someone’s lips suddenly wondered:

Who could that voice belong to?

Which side were they on, and what outcome were they waiting for?

But there was no time to think of an answer.

From the enormous procession that had stopped at the Grand Banquet Hall, someone slowly rode forward on a fine steed and let out a thunderous cry.

“The sovereign of the Great Nation, master of Heaven and Earth and all things beneath them, has deigned to appear in person! All civil and military officials, great and small, kneel and pay your respects to His Majesty the Emperor!”

*Whoosh!*

Not even the golden armor encasing his body or the helmet pulled low over his head could hide his truly overwhelming presence.

At the shout, infused with internal energy, from Baek Yeon—the Emperor’s right hand in name and deed, and Commander of the Embroidered Uniform Guard—everyone in the Grand Banquet Hall rose and knelt.

*Clatter.*

There were hundreds of civil and military officials, and thousands of soldiers already standing guard all around them.

They moved as if they were one body, bowing their heads to the ruler of this vast continent.

Even if, for some of them, it was nothing more than an empty show of respect, the fuse that would bring this banquet to an end had not yet burned all the way down.

“Long live His Majesty the Emperor.”

At Ma Sanbao’s quiet murmur, everyone soon joined in.

“Long live His Majesty the Emperor! Long live! Long, long live!”

It was then.

At the very end of that resounding cheer, the Emperor stepped down from his sedan chair and walked slowly through the human curtain of guards.

*Step. Step.*

His footsteps rang out with unusual clarity.

But those who bowed their heads couldn’t see the Emperor as he passed them. Only after the empty seat on the throne atop the lofty stairs had finally been filled could they straighten up and face him.

The ruler of all under Heaven, who had shut himself away in Qianqing Palace for years on end while attending to the affairs of state.

The Great Nation’s fourth prince turned rebel, then rebel turned Emperor: a notorious unfilial wretch and butcher who had finally seized the throne.

And a man of tempestuous fortune, standing at the highest place beneath Heaven.

They were stunned.

“……!”

“……!”

In an instant, an unseen shock and disturbance swept across the Grand Banquet Hall like a wave.

There was no trace of the Emperor’s once-youthful, handsome appearance in the man who had emerged after his long seclusion.

But the Emperor paid it no mind.

He looked down haughtily at the countless gazes fixed on him.

Though he had aged beyond recognition, his eyes shone brighter than anyone else’s in the hall as he surveyed the gathered officials, great and small, one by one.

The pillars that held up this vast empire. The very heart of the realm.

Among them were generals who commanded armies, and old scholars with stooped backs but unbending eyes.

Ma Sanbao, the East Depot’s de facto leader and the Emperor’s greatest adversary, was there as well.

But the last place the Emperor’s gaze fell was far off at the end of the hall, where a young man watched him in silence.

*Jin Taekyung.*

Their eyes met in midair.

The Emperor looked at Jin Taekyung. Jin Taekyung looked at the Emperor.

They stared at each other for a while without saying a word. At last, the Emperor’s firmly closed lips parted.

“Begin.”

Perhaps it wasn’t just a few people who imagined it.

*Boom. Boom. Bwoom!*

The drums heralding the start of the grand banquet sounded like war drums announcing the opening of a battle.

* * *

The atmosphere, frozen like a glacier, began to thaw little by little when musicians and dancers entered with an astonishing spread of delicacies and began to perform.

A melody that stirred the heart just to hear it, and sleeves fluttering in time with the music.

On top of that, the imperial chefs had displayed all their skill, and the finest wines were served without limit.

It was only natural that those who’d nervously downed a cup of wine would feel at least a little more at ease.

“Whew. I can finally breathe.”

“Indeed. I really thought something was about to happen…”

“Shut your mouth. You want to say something wrong and invite needless suspicion?”

“M-My apologies, sir.”

“If I hear you say something that disrespectful again, I won’t let it pass.”

The middle-aged man reprimanded the young official beside him in a carefully lowered voice, then swept a sharp gaze around them.

He seemed worried someone might have overheard.

I casually picked up a bite of food from the appetizer in front of me.

The next moment, I felt the middle-aged man across from me fixing me with an unusually persistent stare.

At the same time, the young official’s voice reached my ears.

“S-Sir. I did misspeak, but no one could’ve heard me. The Embroidered Uniform Guards are far away, too.”

He wasn’t wrong.

The hall being used for today’s grand banquet was large enough to hold training for thousands of soldiers at once. For that reason, the officials seated at regular intervals were also quite far apart.

And the Embroidered Uniform Guards were all exceptional masters. Only a few, including their commander, Baek Yeon, remained by the Emperor’s side.

The rest were far away, holding to their assigned positions.

But even after hearing the young official, the middle-aged man kept watching me closely for a while before asking,

“Do you know anything about that man?”

“Pardon? W-Well, I’ve heard in passing that he’s a ruffian from the martial world.”

“Is that all?”

“I’m not sure what you mean…”

“Tsk. Honestly, you never think. Be grateful that your father and I have a connection. Otherwise, you wouldn’t have made it this far.”

The middle-aged man clicked his tongue and continued, as he had all along, in a low whisper.

“How could some ruffian attend a banquet like this? He’s Prince Shangshan’s bodyguard and guest, brought here by His Highness. He’s also the third son of the Jin Family of Taiyuan, whose influence has recently spread all the way south of the Yangtze.”

“The Jin Family of Taiyuan. The Jin Family of Taiyuan… Do you mean the family that runs the Jin Family Trading Company and the Jin Family Escort Bureau?”

“That’s right. And that Jin Family of Taiyuan is based in Shanxi, Prince Shangshan’s fief.”

“Ah.”

The young official breathed out softly.

“A family of that standing must have considerable influence in Shanxi Province.”

“With Prince Shangshan’s protection, how could it be otherwise? Martial artists who defy the Great Nation’s solemn laws have no business wielding that kind of power… but apparently they rule as de facto overlords across Shanxi Province.”

“Is that why you’re paying attention to him, sir? Because he’s the son of a martial arts family?”

“It’s more than that.”

“Then…”

“Blazing Flame Divine Dragon. That’s his sobriquet. A tremendous master, barely in his twenties, who’s already accomplished countless feats of arms. There’s no one in the martial world who hasn’t heard of him.”

“You’ve done a fair amount of digging.”

“There was no need to look into it in detail. Even among the people of the imperial capital, there are countless who know of Blazing Flame Divine Dragon Jin Taekyung…”

The middle-aged man, who hadn’t taken his eyes off me as he spoke, suddenly frowned.

“Did you just speak casually to me?”

But the young official didn’t answer.

Normally, he would’ve scrambled to make excuses. Now, though, his face had gone white as he stared at the person standing behind him and the middle-aged man.

One second.

Two seconds.

Three.

After a silence in which the world seemed to stop, the middle-aged man slowly turned his head to follow the young official’s gaze.

Then he froze like a statue.

“Y-Your Majesty…!”

It was no illusion of mine that the words, forced from deep in his lungs, sounded like a scream.

The Emperor.

Like the title Son of Heaven, the absolute being called a descendant of Heaven looked down at the two men without a word.

As if considering how to kill them.

Perhaps he seemed all the more like it because Baek Yeon stood tall behind him—the very man who had led the purge of tens of thousands of “traitors” more than a decade ago.

“Y-Your Majesty. Please…”

*Flap.*

The voice cut off with the Emperor’s small gesture.

That was right. This arrogant and cruel absolute ruler still hadn’t spoken.

And he would allow no one to speak before him.

By now, the Grand Banquet Hall had fallen into deathly silence. The Emperor abruptly turned his head and looked at me.

“Jin Taekyung of the Jin Family of Taiyuan.”

“……!”

“……!”

I could feel it.

The air quivering.

Countless gazes piercing my entire body without mercy.

The Emperor had spoken first to me, the only outsider among the high officials who supported the empire and the gathered civil and military officials.

And he’d done it after walking all the way to the far end of the hall, where I sat in the lowliest seat, far from his throne.

“I ask you: what should I do with these people?”

If this had happened a few days ago, I would’ve been shocked.

Why the fuck is this crazy bastard pulling this shit out of nowhere? I probably would’ve thought something like that—and started to feel like I needed to piss.

But not today.

*Yeah. No.*

I’d already stepped into a gamble where each side had staked their lives.

The moment I entered the tiger’s den that was the imperial palace, perhaps all of this had been inevitable.

The time had come.

The die had been cast. Now it was time to see how it landed.

“Well, before I answer, would it be all right if I had a drink?”

*Haaaa.*

The air quivered again.

No, saying it quivered might not be quite right.

If the wave just now had been a small ripple from a stone dropped into a lake, this one was a disaster like a towering wave.

Everyone in the Grand Banquet Hall gaped as that wave swept over them in an instant. I looked at the Emperor, who gave a small nod, and spoke.

“Then I’ll take that as permission.”

*Gulp.*

The moment I tossed back the wine already poured into my cup instead of answering, cries of shock and angry shouts erupted from every direction.

That wave, which hadn’t felt real even when they’d seen and heard it themselves, had finally swept them up.

“What a lunatic!”

“H-How dare that man…!”

“How can there be such a lawless man in this world?”

“Commander of the Embroidered Uniform Guard, what are you doing? Why haven’t you cut down that high traitor yet?”

“Your Majesty! Punish that outrageous ruffian at once for insulting Your Majesty and the imperial household!”

“Please punish him!”

Listen to that decibel level.

They say the more people curse you, the longer you live. If this raucous enthusiasm had lasted even fifteen minutes longer, my sobriquet might’ve become Three Thousand Jiazi instead of Blazing Flame Divine Dragon.

Beheading was the basic option, and they kept piling on extras: cut off my balls, torture me slowly, then tear me limb from limb by quartering.

*…No, I mean, the balls are a bit much.*

Was that guy from the Sichuan Tang Clan or something?

I took a good look at the face of the man who’d proposed castrating me, then put down my cup.

Then I looked at the Emperor and spoke.

“Kill them if you want, or spare them if you want. Isn’t that what Your Majesty does best?”

Well.

I was starting to feel like I needed to piss.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0879.txt",
      "sha256": "5670af5ed6f5ff611969af9c3affc5ed0132b2d03ba67045fd8a0a0253cb09ae",
      "bytes": 21461
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2af8f861fbc94fb295e10c399365559a25614a0455c1dd734a79b4c083b3b9ed",
      "bytes": 2123
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "77f7f9625d663fdeec408b3696199ba3f21d98f335ae9eae4e9465caec345d0f",
      "bytes": 230213
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "82143009beee36bcbefc68afec87194b80a8a1601d04dbb60ccd57f534f33423",
      "bytes": 759
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cef86ca7dc17d64cc65fda9deed641da0b753750ec80d21933beaa63fbac06b4",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "850f00587bc93d43e005a5c9d8894d113abf5d09c40b8f0a58e09bc59b76783c",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "bf49535cae0d538ce2cea4e13c3e7546a7b6042f679bbdc5262a7a65d3e3bebe",
      "bytes": 952
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "e78d60f7d803d2d8a8feeb95fa6ed26a7fd16cfbd0ba38f13cf9d7f4659bb326",
      "bytes": 624
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d9384e9ac1b5e8435b4526eb3ad43743df747a3184af7f49792e9027db164ec5",
      "bytes": 258472
    }
  ],
  "estimated_tokens": 14805
}
-->

# Durable State Update — Chapter 879

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
1 and safe_through 879. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 879. Profile updates may replace only one
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
  "chapter": 879,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 879,
    "continuity_sources": [879],
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
    "Taekyung gave Shangshan the Myriad-Poison Ring for protection against poisoning.",
    "The palace attendants assigned to Shangshan are First Rate martial artists who carry flexible swords.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "Hong Jin believes Aehyang is very likely pregnant; the pregnancy and the Emperor’s plans remain unconfirmed.",
    "The late Emperor died after a period of mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Hong Jin plans to contact Ma Sanbao about Shangshan’s danger; Taekyung also made a personal request of Hong Jin whose contents remain unrevealed.",
    "Jeok Cheongang received a letter from Taekyung and another from someone closely connected to Hong Jin; he burned both, and their contents remain unknown.",
    "Jeok Cheongang says the group is formally invited to the imperial palace and plans to go there soon."
  ],
  "continuity_sources": [
    877,
    878
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Will the Myriad-Poison Ring protect Shangshan from Blood Soul Gu?",
    "What did Taekyung’s and Hong Jin’s contacts write to Jeok Cheongang, and what is the purpose of the imperial invitation?",
    "What personal task did Taekyung ask Hong Jin to perform?"
  ],
  "safe_through": 878,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 은자 | **silver nyang** | Silver currency unit. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 산군 | **mountain lord** | Traditional epithet for a tiger; retain an explanatory footnote on first use. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 광서 | **Guangxi** | Region bordering Nanman. |
| 조이 | **Joey** | U.S. military or political official introduced by first name only. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 초일류 | **Supreme First Rate** | Realm attained by each Baekcheon Unit member. |
| 대지모신 | **Earth Mother Goddess** | New deity proclaimed by Jin Taekyung as Nanman's One God. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 백호 | 진태경 | guardian_spirit_to_human_ally | you | terse and irritated | The White Tiger responds telepathically after Jin calls it Whitey and jokes about its former name. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 중년인 | 상산왕 | unknown imperial subject addressing a prince | His Highness, Prince Shangshan | formal and deferential | Addresses him as 상산왕 전하 while remarking on seeing him grown. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 878
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 878
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 878
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 878
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother and an exceptionally skilled young swordsman.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; the Emperor says he will take care of Zhu Bao.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 724
- **Aliases:** Whitey
- **Role:** The White Tiger is a snow-white guardian presence overlooking Nanman's assembled forces and roared when the Beast Miao King called the people to war.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger shared a roughly three-hundred-year friendship with Yayul Cheon and entrusted Jin Taekyung and Jeok Cheongang with killing it if corruption overcame it.

## Korean source

```text
＃879화



사람이 많으면 떠도는 말도 많아진다.

천하의 중심이자 대국의 새로운 황도(皇都)로 자리 잡은 절강성 항주 역시 예외는 아니었다.

아니, 오히려 가장 심한 축에 속했다.

항주 어느 곳을 가더라도 누군가에게 들었던 소문을 침까지 튀겨 가며 사실인 양 읊어 대는 사람들이 득실거렸다.

그들은 나는 새도 떨어트린다는 고관대작이 새로 들였다는 애첩의 미모에 대해 떠들었고, 그가 애첩에게 값비싼 패물을 선물하기 위해 백성의 고혈을 쥐어짰다는 이야기에 분노했으며, 금의위가 이미 조사에 착수했다는 소식에 연신 건배를 외쳤다.

“역시 이럴 때는 금의위만큼 든든한 존재가 없지. 폐륜까지 저지르며 황위에 오르긴 했지만 그래도 일 처리 하나는 확실…….”

“쉿, 그 방정맞은 주둥이 좀 닥치게. 한데 그 영감 아들 중에 한 명이 금의위라고 하지 않았었나?”

“그랬지.”

“그런데 그걸 걸려? 금의위에 연줄이 있는데도?”

“아, 그놈. 그렇지 않아도 얼마 전에 잘렸다는군.”

“그래? 왜?”

“몰라. 무슨 비밀 임무라도 맡았는지 한 달 전쯤부터 안 보이더니, 며칠 전에 얼굴이 퉁퉁 부은 채로 복귀했다더라고.”

“퉁퉁 부어?”

“그래. 무슨 잘못을 저질렀는지 호되게 처맞은 모양이야.”

누군가의 입에서 흘러나온 이야기는 금세 스쳐 지나갔다.

명승고적에서 영감을 얻고자 하는 시인 묵객. 향락의 도시라 불리는 항주를 위해 천릿길을 달려온 한량.

값싼 화주와 만두를 시킨 후 조용히 술잔을 기울이는 가난한 선비와 불룩 나온 배를 두드리는 부유한 장사치까지.

항주에는 수많은 인간군상이 존재했고, 그들은 각자 보고 들은 것들을 마음껏 떠들어 댔다.

“드디어 서호(西湖)에 가 봤으니 당장 죽어도 여한이 없어. 마음 같아서는 항주에서 일 년만 더 머무르고 싶군.”

“돌아가려면 아직 달포도 더 남았는데 뭐가 걱정인가? 천천히 둘러보고 떠나기 전에 주산군도(舟山群島)에도 한번 가 보자고.”

“주산군도라면, 혹시 보타산(普陀山)이라도 보러 갈 생각인가?”

“맞네. 내가 부처를 믿는 것은 아니지만 그런 명산이 근처에 있다면 기왕 온 김에 한 번쯤은 가 봐야지.”

“하지만 그곳에 있는 여승들은 강호인이나 다름없다던데…….”

“보타암(普陀庵)의 비구니들을 말하는 거라면 걱정할 필요 없네. 황도가 이전되면서 항주의 무림인들을 솎아 내면서부터 자취를 감춘 지 벌써 십 년도 넘었다더군.”

명승고적을 탐방하기 위해 항주를 찾은 시인 묵객들의 대화는 비교적 분위기가 좋았다. 가까운 곳에 자리 잡은 상인들은 좋지 않은 표정으로 연신 술을 들이붓고 있었으니까.

“요새 사천 쪽 분위기가 심상치 않아. 물품들의 시세가 예측 불가 수준으로 요동치는 바람에 손해가 이만저만이 아니야.”

“하면 그 소문이 사실인가? 곧 청해(海省) 땅으로부터 외적들이 물밀듯이 몰려올 거라던데. 그 때문에 청해성에 자리 잡은 곤륜파도 풍전등화의 위기고.”

“외적은 무슨. 기껏해야 강호의 무뢰배, 그것도 마귀에 단단히 홀린 광신도들 아닌가. 이름만 그럴듯하게 바꿨을 뿐이지 결국 과거의 마교가 그랬듯이 중원 무림 문파에 박살 날 거야. 이번에도 금위군이 나설 필요도 없을걸.”

“자네, 요 몇 년간 항주에서만 지내다 보니 세상 돌아가는 꼴을 몰라도 너무 모르는군.”

“응? 무슨 정보라도 들었나?”

“내가 오래전부터 지내던 무림인이 현재 무림맹 소속인데…… 과거 마교가 쳐들어왔을 때보다 훨씬 더 심각한 상황이야.”

“뭐? 그 정도란 말인가?”

“이미 몇 달 전에 사천에서 벌어진 사건만 봐도 모르겠나? 무려 일 만에 가까운 대병력이 모여 한바탕 혈전을 벌였어. 이 정도면 단순히 무림 내부의 분쟁이 아니라 소국 간의 전쟁이라고 봐도 무방하지.”

“……!”

“그뿐만이 아닐세. 아직 정확히 확인된 것은 아니지만 운남(雲南)에서도 모종의 움직임이 포착됐어.”

“운남? 설마 남만의 그 오랑캐들?”

“맞네. 남만야수궁이 모든 전력을 동원하여 중원으로 북상 중이라더군. 그 소문이 사실이라면 지금쯤 사천이나 광서 땅에 접어들었을지도 몰라.”

“허. 광신도들로도 모자라서 이제는 오랑캐들까지 중원을 넘본다고?”

“아니, 완전히 정반대일세. 무림맹에 합류하여 암천과 맞서려는 거지. 한데 좀 희한해.”

“그 말이 사실이라면 다행인 거지, 희한할 건 또 뭔가?”

“그게…… 그 오랑캐들도 광신도나 다를 바 없다는 소문을 들었거든.”

“뭐?”

“그, 뭐라더라? 암천과 맞서 싸우는 것이 성전(聖戰)이니, 대지모신이 굽어보신다느니 별 이상한 소리를 온종일 씨부린다더군.”

“그게 무슨 병신같은 소린가?”

“그야 나도 모르지. 연줄을 통해 건너 건너 들은 것뿐인데. 여하튼 모두가 생각하는 것 이상으로 큰일이 벌어지고 있는 건 확실해.”

대륙은 광활하다. 하지만 직업 특성상 귀가 밝을 수밖에 없는 상인들은 온갖 정보들을 여러 경로로 전해 듣고는 했다.

그 소문이 진실이든 사실이든 간에, 우선 기억해 놓는다면 언젠가는 큰 재물을 벌어다 줄 수도 있을 테니까.

그리고 서로를 향해 오가는 대화와 술잔으로 한창 객잔이 시끌벅적해졌을 무렵, 누군가가 잔뜩 취기 어린 목소리로 한마디를 툭 내던졌다.

“아, 혹시 그 얘기 들었나? 듣자 하니 상산왕 전하께서 황궁에 머무르고 계신다던데.”

“……!”

“……!”

찰나의 순간. 후끈하게 달아올랐던 공기가 차갑게 식었다.

삽시간에 침묵이 내려앉은 객잔 내부. 이미 모두의 시선은 한 곳을 향해 쏠린 후였다.

“어?”

갑자기 자신을 향해 쏟아지는 무수한 시선에, 거나하게 취한 와중에도 화들짝 놀란 중년인이 더듬더듬 입을 열었다.

“왜, 왜들 그러시오?”

그때였다. 순식간에 조용해진 객잔 안의 인파 속에서 몇몇 사람이 입을 연 것은.

“지금 뭐라 했소?”

“상산왕 전하께서 황궁에 머무르고 계신다고? 봉지(封地)인 산서성이 아니라?”

“방금 그 말, 확실한 거요?”

모든 재앙은 술과 혀에서 나오는 법.

빠르게 빗발치는 질문들에 무언가 잘못되었음을 직감한 중년인은 술이 확 깨는 것을 느꼈다.

“사, 사실인지 아닌지는 모르오. 나도 그냥 주워들은 것이라서. 아마도 헛소문이겠지.”

“헛소문이라도 좋으니 말해 보시오. 당신이 아는 것 전부.”

“아니, 아니오. 아무래도 내가 만취하여 실언한 모양이오. 이만 나가 봐야겠으니 길 좀 비켜 주…….”

불콰하게 달아올랐던 안색은 이미 창백해진 지 오래.

그러나 비틀거리면서도 용케 자리에서 일어난 중년인은 한 걸음도 채 움직이지 못하고 제자리에 멈춰 서야만 했다.

이미 거하게 올라온 술기운 때문이 아닌, 어디선가 뚝 떨어져 내린 물체에 의해서.

쿵.

제법 큰 소리를 내며 바닥에 내려앉은 그것은 정확히 중년인의 발 앞에 떨어졌고, 동시에 입구를 조이고 있던 가죽끈이 풀리며 안의 내용물을 쏟아냈다.

촤르륵.

전낭(錢囊)에서 흘러넘친 은자가 흐릿한 불빛을 받아 번쩍였다.

언뜻 봐도 서른 냥은 넘어 보이는 액수.

그 엄청난 거금에 눈을 부릅뜬 사람들의 귓가로, 나직한 목소리가 파고들었다.

“제법 흥미로운 이야기였소.”

다시 한번 모두의 고개가 돌아갔다. 아니, 올라갔다.

이 층.

탁자 하나를 홀로 차지한 어느 젊은 유생이 중년인을 물끄러미 응시하고 있었다.

“오십 냥이오. 이 정도면 이야기 값으로는 충분할 듯한데. 귀하는 어찌 생각하는지?”

“……!”

중년인의 눈꼬리가 파르르 떨렸다.

은자 오십 냥이라는 엄청난 액수, 그리고 그런 거금을 툭 내던진 저 젊은 유생에 대한 충격으로.

충분?

그럴 리가. 충분하다 못해 차고 넘친다.

무려 은자 오십 냥이다.

항주 운하에서 막일을 하는 그로서는 언감생심 만져 본 적도 없는 거금. 보는 것만으로도 심장이 크게 뛰었다.

다만 자신이 조금 전 대수롭지 않게 던진 말이 가져올 결과가, 저 전낭의 무게만큼이나 무겁게 중년인의 마음을 짓눌렀다.

“뉘, 뉘십니까요? 일견하기로는 있는 집 자제분 같으신데, 혹시 소인이 뭔가 해서는 안 될 말이라도…….”

“걱정할 필요 없소. 그저 궁금할 뿐이니까.”

그저 궁금증을 해결하기 위해 은자 오십 냥을?

말도 안 되는 소리다.

제아무리 있는 집 자식이라지만 그게 말이 되나.

젊은 유생의 대답을 들은 중년인은 더욱 큰 불길함에 사로잡혔지만, 인생을 바꿀 기회를 놓칠 수는 없었다.

천하의 중심지라 불리는 이 거대한 황도에도 가난뱅이는 있고, 그중 한 사람인 중년인에게 은자 오십 냥은 곧 새로운 삶을 의미했으니까.

촤르륵.

고민을 끝낸 중년인은 그 틈에 누가 훔쳐 갈세라, 흘러넘친 은자를 허겁지겁 주워 전낭에 집어넣었다. 그리고 마른침을 꿀꺽 삼키며 젊은 유생을 향해 입을 열었다.

“새벽 무렵 투전판에 기웃거리다가 이야기를 들었습니다. 며칠 전 북문(北門)을 통해 무려 수백이 넘는 금의위가 입성했다고요. 제아무리 황도라지만 그날따라 대로변의 경계나 분위기가 좀 유별났다고 합디다.”

“계속하시오.”

“그중 눈치 빠른 몇몇이 이상하다 싶어 불호령을 감수하고 슬쩍 고개를 들었는데, 글쎄 그 무시무시한 금의위들이 마차 한 대를 빽빽하게 에워싸고 있었다지 뭡니까.”

“마차?”

“예. 그리 화려하지도, 작지도 않은 마차 말입니다. 표물 운송할 때나 쓸 법한 그런 거요.”

“그리고 그 마차 안에 상산왕 전하께서 타고 계셨다?”

“두 눈으로 똑똑히 봤다고 했습니다. 척 봐도 범상치 않아 보이는 소년의 얼굴이 창가에 나타났는데, 말로만 듣던 그 상산왕 전하가 틀림 없…….”

“단지 그것만으로는 부족한 것 같소만.”

“예?”

중년인의 말을 단칼에 끊어낸 젊은 유생이 말을 이었다.

“상산왕 전하께서 황도를 떠나신 지 어언 십 년이 넘었소. 당시에도 워낙 어리셨던 터라 세월이 흐른 지금도 아직 지학(志學. 열다섯 살)도 되지 않은 연배이시지. 한데 새벽까지 투전판이나 기웃거리는 작자가 어찌 그 귀한 분의 얼굴을 알아볼 수 있겠소?”

“그, 그게. 수백 명이나 되는 금의위들이 이리 야단법석을 떠는 걸 보니 짐작한 것 아니겠습니까.”

“물론 그럴 수도 있겠지. 허나 필시 그런 짐작을 한 또 다른 이유가 있었을 터. 본인은 이미 충분한 값을 치렀으니, 당신은 보고 들은 것을 빠짐없이 말해야 할 거요.”

불과 촌각 전만 해도 온갖 소음으로 시끌벅적하던 객잔 내부는 어느덧 쥐 죽은 듯이 조용해진 지 오래.

평범한 백성들에게 있어 상산왕은 그런 의미였다.

고귀하면서도 불쌍하신 분.

천륜(天倫)을 거스른 형에 의해 모든 가족을 잃고 만리타향인 산서성에 유배되다시피 한 비운의 황족.

한데 그런 상산왕 전하께서 황도로 돌아오셨단다.

무려 십 년이 지난 이 시점에, 그것도 금의위에게 둘러싸인 채 은밀히.

의문을 담은 채 사방에서 쏟아지는 그 무수한 시선에, 중년인은 어깨를 움츠리며 어렵사리 입을 열 수밖에 없었다.

“사실 처음에는 저도 공자님과 비슷하게 생각했습니다요. 그게 말이 되냐, 네깟놈이 상산왕 전하를 어찌 알아보느냐. 십 년 넘게 변방에 있던 분이 왜 갑자기 황도에 오겠느냐. 뭐 하여간 그랬습죠. 한데…….”

“한데?”

“뒷말을 들어보니 제법 그럴듯하지 뭡니까.”

중년인은 숨을 골랐다. 그리고 이제는 숨소리조차 들리지 않는 고요한 침묵 속에서, 천천히 말을 이었다.

“그 인간이 펄쩍 뛰며 그러더군요. 황제, 아니 지엄하신 황제 폐하께서 후사(後嗣)를 보셨으니 아우인 상산왕 전하께서 오시는 건 당연한 일 아니냐고. 곧 있을 축하연에 초대받은 것이 분명하다고.”

“……!”

“……!”

순간. 보이지 않은 파장이 객잔 내부를 휩쓸었다.

곳곳에서 흡, 하고 헛숨을 들이키는 소리가 침묵을 깨트렸고 흐릿한 등잔불은 얼어붙은 사람들의 모습을 비추었다.

이루 말할 수 없이 딱딱하게 굳은, 젊은 유생의 얼굴 역시도.

“후……사?”

“예에. 그분이 황후신지, 어느 후궁이신지까지는 몰라도 회임(懷妊)하신 것은 틀림없다 했습니다.”

젊은 유생의 눈동자가 깊게 가라앉았다.

백 명이 넘는 객잔 안의 손님 중 일부도 마찬가지였다.

경악을 감추기 위해 입술까지 깨문 그들은 시인 묵객이나 유생. 혹은 상인들이었고, 중년인을 비롯한 몇몇 무식쟁이들과는 달리 조금 전 들었던 말의 의미인지 정확히 꿰뚫고 있었다.

‘만약 저 말들이 모두 사실이라면…….’

그들은 그저 생각하는 것만으로도 두려움을 느꼈다.

오랫동안 후사를 보지 못했던 황제의 새로운 후계자. 그리고 십여 년 전 불어닥친 피바람 속에서 살아남았던 황실의 유일한 직계, 상산왕의 귀환.

이것이 의미하는 바가 도대체 무엇이겠나.

‘숙청(肅淸)……!’

소리 없는 비명이 머릿속을 울린다. 위기를 인식한 등허리는 이미 식은땀으로 축축하게 젖어 있었다.

진즉 자리를 떴어야 했다.

저 소문의 사실 여부를 떠나, 이건 처음부터 들어서는 안 되는 이야기였으니까.

지금 이 순간. 그들은 조금만 삐끗해도 두 번 다시 기어 올라올 수 없는 천 길 낭떠러지 앞에 서 있는 것 같은 환상에 사로잡혔다.

은자를 하나씩 세며 희희낙락하는 중년인과 이 상황의 심각성을 조금도 느끼지 못한 일부 사람들과는 달리.

“허어, 황상께서 마침내 후사를 보셨다니. 나라 전체의 흥복이로군.”

“흥복은 무슨. 천륜까지 어겨가며 그 자리에 오른 핏줄을 고스란히 물려받…….”

“제발 그 입 좀 닥치게. 목숨이 서너 개쯤 되나? 나까지 죽는 꼴 보고 싶어? 밀고라도 당하면 전부 끝장이라고.”

“주위 이목이 그리 무서우면 집에나 처박혀 있게. 원래 안 보이는 곳에서는 나랏님 욕도 하고 그러는 거야. 금의위가 무슨 유령도 아닌데 만날 일이 뭐가 있다고. 허 참.”

“그런데 상산왕 전하께서는 이제 어떻게 되시는 거지?”

“나 같은 무지렁이가 뭘 안다고 묻나. 다만 앞으로도 쭉 황도에 머무르시면 좋을 텐데. 어릴 적부터 참담한 일을 당했으니 그 속이 오죽할까. 이제 좀 편안히 머무르실 때도 되었지.”

말은 늘 부풀려지고 과장되며, 사람은 언제나 제가 믿고 싶은 대로 받아들이는 법.

중년인의 입에서 흘러나온 믿을 수 없는 소문은 어느덧 확실한 증거를 갖춘 사실이 되어 있었고, 진즉 두려움을 느끼고 있던 몇몇 사람들은 후들거리는 두 다리를 움직여 다시 왁자지껄해진 객잔을 가로질렀다.

감당할 수 없는 불길을 피해 살아남기 위해서.

혹은 이 정보의 진위를 확인하여 이용하기 위해서.

그리고 마침내 입구에 다다른 순간. 자신들이 더는 빠져나올 수 없는 수렁에 발을 담갔음을 깨달았다.

“어딜 그리 급히들 가시오.”

가라앉은 목소리와 함께, 낡은 문 앞을 가로막은 십여 개의 그림자가 동시에 걸음을 내디뎠다.

저벅.

그 순간. 마치 세상이 멈춘 듯했다.

서둘러 객잔을 빠져나가려던 이들의 눈동자에 비친 것은 죽립을 눌러쓴 열 명의 사내. 그리고 그들이 걸친 피풍의(避風衣) 사이로 번뜩이는 황금빛 갑옷이었다.

“금의위(錦衣衛)……!”

누군가의 입술 사이로 튀어나온 그 비명 같은 세 글자에 객잔 내부가 차갑게 얼어붙은 그때. 말없이 상념에 잠겨 있던 젊은 유생이 입을 열었다.

“참으로 흥미로운 이야기였소. 은자 오십 냥이 아깝지 않을 정도로.”

은자가 가득 찬 전낭을 끌어안고 있던 중년인이 멍하니 입을 벌렸다.

“공자님. 도대체 이게 무슨…….”

“나는 공자가 아니오. 허나 당신의 이야기를 더 자세히 듣고 싶은 마음은 변함없지.”

“고, 공자! 이러시면 안 됩니다! 이러시면……!”

뭐라 외치는 중년인의 모습은 이미 안중에도 없다.

젊은 유생, 아니 금의위 백호(百戶)는 객잔의 입구를 가로막은 자신의 수하들에게 부드럽게 말을 건넸다.

“무엇들 하고 있나. 모조리 추포하지 않고.”

“충(忠)!”

힘찬 군례와 함께 열 개의 금빛 신형이 사방을 가로질렀다.

그들 한 사람, 한 사람이 초일류에서 절정의 무공을 익힌 고수들.

곳곳에서 고함과 울음 섞인 간청이 터져 나오고, 황급히 도주하거나 반항하려던 이들의 비명이 그 위를 뒤덮기까지 걸린 시간은 그야말로 찰나였다.

쿵! 콰지직!

곳곳에서 울려 퍼지는 굉음 속, 이 층 난간을 박차고 사뿐히 지면에 착지한 금의위 백호는 벌벌 떨고 있는 중년인의 어깨를 두드렸다.

“자. 이곳은 소란스러우니 자리를 옮겨서 다시 이야기해 봅시다. 당신이 무엇을 더 알고 있는지, 당신에게 그 개소리를 지껄인 것이 누구인지. 또 누가 그 이야기를 알고 있는지.”

그는 굳이 말해 주지 않았다.

이번에는 은자 대신 다른 무언가로 이야기 값을 치르리라는 것을.

그리고 그것은 은자만큼이나 반짝이고, 은자와는 비교도 할 수 없을 만큼 날카로운 무언가가 될 터였다.



* * *



보고를 들은 황제는 전령이 물러간 후에도 오랫동안 침묵을 지켰다. 그리고 주위에 단 한 사람만이 남았을 때, 비로소 입을 열었다.

“그대는 어찌 생각하는가?”

빽빽한 주렴(珠簾)과 사방에 흩날리는 하늘하늘한 비단 사이, 누군가가 대답했다.

“누군가 의도적으로 퍼트린 것이 분명하겠지요.”

“흉수는?”

“뻔하지 않습니까. 동창이 아니라면 열화신룡 진태경. 혹은…… 둘 다.”

“힘을 합쳤다?”

“지금으로서는 그것밖에 없습니다.”

“조금은 후회되는군. 짐이 그대의 말만 듣고 진태경을 황궁에 들인 것이 잘한 일인지 모르겠어.”

작게 혀를 찬 황제가 혼잣말처럼 중얼거렸다.

“그대를 짐에게 보낸 그자는, 이런 상황까지 예측했을까?”

비단 자락 너머의 누군가가 대답했다.

“그분은 제가 아는 누구보다 위대하고 현명한 존재. 하지만 진태경은 쉽게 재단할 수 없는 예측불허의 인물입니다.”

황제는 자신도 모르게 고개를 끄덕였다.

도무지 그 끝을 짐작하기 어려운 대담함. 무위와 신념.

각자의 위치를 떠나 전날 본 진태경의 모습은 황제로서도 헛웃음이 터져 나올 정도였다.

“대업을 망치기 전에 적당한 선에서 제지하는 게 좋겠군. 그나저나 표적에 관한 일은 어떻게 되어 가고 있나?”

“쉽지 않습니다. 지금으로서는.”

“그래, 쉬웠다면 십 년이 넘도록 골칫덩이로 남아 있진 않았겠지. 허나 놈이 사라져야 대국이 바로 설 터. 반드시 해내야 하네.”

스륵.

대답 대신 어디선가 불어온 옅은 바람이 비단 자락을 어루어만졌다.

조금전까지만 해도 그곳에 있던 누군가가 사라진 것을 깨달은 황제는 쓰게 웃으며 뇌까렸다.

“이미 소문이 났으니 숨겨 봤자 어쩔 수 없겠지. 그 소문을 사실로 만드는 수밖에.”

대국을 물려받을 새로운 후계자의 탄생을 기념하는, 거대한 축하연의 시작을 알리는 순간이었다.
```

## Final English reading copy

```markdown
# Chapter 879

Where there are people, there are rumors.

Hangzhou, Zhejiang Province—the heart of the world and the new imperial capital of the Great Nation—was no exception.

If anything, it was one of the worst places for them.

Wherever you went in Hangzhou, people were packed together, repeating rumors they’d heard from someone else as if they were facts, spittle flying from their mouths.

They talked about the beauty of a high official’s new concubine—the sort of official said to be powerful enough to knock a bird from the sky. They were furious over the story that he’d squeezed the people dry to buy her expensive jewelry. And when they heard the Embroidered Uniform Guard had already begun investigating, they kept raising their cups in celebration.

“Even so, there’s no one you can count on like the Embroidered Uniform Guard. He may have climbed to the throne after committing such a heinous crime, but at least he knows how to get things done…”

“Shh. Shut that reckless mouth of yours. Didn’t you say one of that old man’s sons was in the Embroidered Uniform Guard?”

“I did.”

“And he still got caught? Even with connections in the Guard?”

“Oh, that guy. Apparently, he got fired not long ago.”

“Really? Why?”

“Don’t know. Maybe he was given some secret assignment. He disappeared about a month ago, then came back a few days ago with his face all swollen.”

“Swollen?”

“Yeah. Looks like he got a real beating for something he did wrong.”

The story drifted away as quickly as it had come.

Poets and scholars seeking inspiration from scenic landmarks. Idlers who’d traveled a thousand *li* to visit Hangzhou, the city of pleasure.

Poor scholars quietly sipping liquor after ordering cheap strong liquor and dumplings, and wealthy merchants patting their bulging bellies.

Hangzhou was full of all kinds of people, and they talked freely about what they’d seen and heard.

“I’ve finally seen West Lake. I could die right now without a single regret. If I had my way, I’d stay in Hangzhou for another year.”

“You’ve still got more than a month before you have to go home. What’s the rush? Let’s take our time looking around, then visit the Zhoushan Archipelago before we leave.”

“The Zhoushan Archipelago? Are you thinking of going to Mount Putuo?”

“That’s right. I don’t believe in Buddha, but if a famous mountain like that is nearby, I might as well visit while I’m here.”

“But I heard the nuns there are no different from martial artists…”

“If you mean the Buddhist nuns at Putuo Temple, there’s no need to worry. They disappeared more than ten years ago, when the imperial capital moved here and the martial artists of Hangzhou were driven out.”

The conversation among the poets and scholars who’d come to Hangzhou to visit its famous sights was in fairly high spirits. The merchants seated nearby, on the other hand, kept pouring liquor down with sour expressions.

“Things are looking bad in Sichuan these days. Prices are swinging around so wildly they’re impossible to predict. I’ve taken quite a hit.”

“Then is that rumor true? That foreign forces are about to pour in from Qinghai Province. They say even the Kunlun Sect, based in Qinghai, is in dire straits.”

“Foreign forces? They’re nothing but lawless thugs from the martial world—fanatics thoroughly bewitched by demons, at that. They’ve given themselves a fancy new name, but they’ll still get smashed by the Central Plains sects, just like the Demonic Cult did in the past. The Imperial Guard won’t even need to get involved this time.”

“You’ve been in Hangzhou too long these past few years. You don’t know the first thing about what’s happening in the world.”

“Oh? Have you heard something?”

“A martial artist I’ve known for a long time is with the Murim Alliance now… He says this is far worse than when the Demonic Cult invaded.”

“What? That bad?”

“Just look at what happened in Sichuan a few months ago. Nearly ten thousand troops gathered and fought a bloody battle. At that scale, you can hardly call it an internal dispute within the martial world. It’s practically a war between small nations.”

“……!”

“And that’s not all. Nothing’s been confirmed yet, but there are signs of some kind of movement in Yunnan, too.”

“Yunnan? You don’t mean those Nanman barbarians?”

“That’s right. They say the Nanman Beast Palace is mobilizing all its forces and marching north into the Central Plains. If the rumor’s true, they may have already reached Sichuan or Guangxi.”

“Heh. The fanatics weren’t enough, now the barbarians are eyeing the Central Plains too?”

“No, it’s the complete opposite. They’re joining the Murim Alliance to fight Dark Heaven. But something about it is strange.”

“If that’s true, shouldn’t we be glad? What’s strange about it?”

“Well… I heard those barbarians are fanatics too.”

“What?”

“Apparently they spend all day spouting weird nonsense about how fighting Dark Heaven is a holy war, and how the Earth Mother Goddess watches over them.”

“What kind of fucking nonsense is that?”

“How should I know? I only heard it secondhand through my connections. Anyway, it’s clear something much bigger is happening than anyone thinks.”

The continent was vast. But merchants, whose line of work forced them to keep their ears open, often heard all kinds of information from all kinds of sources.

Whether those rumors were true or not, it was worth remembering them. Someday, one of them might make you a fortune.

And just as the inn had grown noisy with all the conversations and clinking cups, someone tossed out a slurred remark.

“Oh, have you heard the news? They say His Highness, Prince Shangshan, is staying in the imperial palace.”

“……!”

“……!”

In an instant, the air that had been warm with drink went cold.

Silence fell over the inn. Everyone’s gaze had already turned toward the same place.

“Huh?”

Startled by the many eyes suddenly fixed on him, a thoroughly drunk middle-aged man stammered.

“W-Why is everyone looking at me?”

That was when a few people in the now-quiet inn spoke up.

“What did you just say?”

“His Highness, Prince Shangshan, is staying in the imperial palace? Not in Shanxi Province, his fief?”

“Are you sure about what you just said?”

Disaster always came from liquor and loose tongues.

As the questions came flying at him, the middle-aged man realized something was wrong. He felt the alcohol leave his system all at once.

“I-I don’t know if it’s true or not. I only heard it somewhere. It’s probably just a rumor.”

“Even if it’s a rumor, tell us. Everything you know.”

“No, no. I must’ve said something foolish because I’m drunk. I need to leave now, so please let me through…”

His flushed face had long since turned pale.

Though he managed to stagger to his feet, he couldn’t take even one step. Something that had dropped from somewhere had stopped him in his tracks.

Thud.

The object hit the floor with a solid thump, landing right in front of the middle-aged man’s feet. At the same time, the leather cord cinched around its opening came loose, spilling its contents.

Clatter.

Silver nyang spilled from the money pouch, glinting in the dim light.

At a glance, there seemed to be more than thirty.

As people gaped at the enormous sum, a quiet voice reached their ears.

“That was quite an interesting story.”

Everyone turned around again. No—looked up.

On the second floor, a young scholar sat alone at a table, watching the middle-aged man.

“Fifty silver nyang. I’d say that’s enough for the story. What do you think?”

“……!”

The middle-aged man’s eyelid twitched.

He was stunned by the staggering sum of fifty silver nyang—and by the young scholar who’d tossed it down so casually.

Enough?

It was more than enough. It was an absurd amount.

Fifty silver nyang.

As a day laborer on Hangzhou’s canals, he’d never even dreamed of touching so much money. Just looking at it made his heart pound.

But the consequences of the words he’d tossed out so carelessly weighed on him as heavily as that pouch.

“W-Who are you, sir? You look like you come from a good family. Did I say something I shouldn’t have…?”

“There’s no need to worry. I’m simply curious.”

Fifty silver nyang just to satisfy his curiosity?

That was ridiculous.

Even a rich young master wouldn’t throw away that kind of money for no reason.

The middle-aged man grew even more uneasy at the young scholar’s answer, but he couldn’t let a chance to change his life slip away.

Even this vast imperial capital, the center of the world, had its share of poor people. For a middle-aged man like him, fifty silver nyang meant a whole new life.

Clatter.

Having made up his mind, the middle-aged man hurriedly gathered up the spilled silver and stuffed it back into the pouch before anyone could steal it. He swallowed, then spoke to the young scholar.

“Near dawn, I was hanging around a gambling den when I heard the story. They said that more than a few hundred members of the Embroidered Uniform Guard had entered through the North Gate a few days ago. Even in the imperial capital, the streets were guarded more heavily than usual, and the atmosphere was strange that day.”

“Go on.”

“A few sharp-eyed fellows thought something was off, so they risked drawing a reprimand and snuck a look. Would you believe it? Those terrifying guards had surrounded a single carriage so tightly you could barely see it.”

“A carriage?”

“Yes. Not particularly grand, not especially small, either. The sort of thing you’d use to transport goods.”

“And His Highness, Prince Shangshan, was inside?”

“They said they saw it with their own two eyes. A boy’s face appeared at the window—he looked extraordinary at a glance. They said he was definitely the very Prince Shangshan everyone’s heard about…”

“That alone doesn’t seem like enough.”

“Pardon?”

The young scholar cut the man off and continued.

“It’s been more than ten years since His Highness, Prince Shangshan, left the capital. He was very young even then, and even after all these years, he still isn’t fifteen. How could someone who spends his nights hanging around a gambling den recognize His Highness’s face?”

“I-I suppose he guessed after seeing hundreds of guards make such a fuss.”

“Perhaps. But there must have been another reason he made that guess. I’ve already paid you well. You should tell me everything you saw and heard.”

The inn had been bustling with noise only moments ago. Now it was as quiet as a grave.

That was what Prince Shangshan meant to ordinary people.

A noble, yet pitiful, man.

An unfortunate member of the imperial family, exiled to Shanxi Province in a far-off land after losing his entire family to his older brother, who’d defied the bonds of kinship.

And now they said His Highness, Prince Shangshan, had returned to the capital.

After more than ten years—and in secret, surrounded by the Embroidered Uniform Guard.

Under the weight of all those questioning looks, the middle-aged man hunched his shoulders and struggled to speak.

“At first, I thought the same thing as you, Young Master. How could it be true? How could the likes of you recognize His Highness, Prince Shangshan? Why would someone who’d spent more than ten years in the provinces suddenly come to the capital? That sort of thing. But…”

“But?”

“When I heard the rest, it sounded pretty convincing.”

The middle-aged man paused to catch his breath. Then, in a silence so deep not even breathing could be heard, he continued.

“That guy jumped up and said, ‘The Emperor—no, His Majesty the Emperor—has had an heir. Of course his younger brother, His Highness Prince Shangshan, would come. He was surely invited to the celebration that’s about to be held.’”

“……!”

“……!”

For an instant, an invisible shockwave swept through the inn.

A few sharp intakes of breath broke the silence, and the dim lamplight fell on people frozen in place.

The young scholar’s face had gone stiff beyond words, too.

“An… heir?”

“Yes. He didn’t know if it was the Empress or one of the concubines, but he said she was definitely pregnant.”

The young scholar’s eyes sank into shadow.

Some of the more than a hundred customers in the inn looked the same.

The people biting their lips to hide their shock were poets, scholars, and merchants. Unlike the middle-aged man and a few other simpletons, they understood exactly what those words might mean.

*If all of that is true…*

The thought alone filled them with fear.

A new heir to an Emperor who’d long been without one. And the return of Prince Shangshan, the only direct member of the imperial family to survive the bloodshed more than a decade ago.

What could that possibly mean?

*A purge…!*

A silent scream rang in their heads. Their backs were already slick with cold sweat as they sensed the danger.

They should have left long ago.

Whether the rumor was true or not, this was a story they should never have heard in the first place.

At that moment, they felt as if they were standing at the edge of a thousand-*zhang* cliff, one misstep from a fall they could never climb back from.

Unlike the middle-aged man, who was happily counting his silver, and the few others who had yet to grasp the severity of the situation.

“So His Majesty has finally had an heir. What a blessing for the whole country.”

“What blessing? What blessing? The child will inherit the blood of a man who broke the bonds of kinship to take the throne—”

“Please, just shut your mouth. Do you have three or four lives to spare? You want to get me killed too? If someone reports us, we’re all finished.”

“If you’re so afraid of people overhearing, go hide at home. People have always cursed the ruler where he can’t hear them. The Embroidered Uniform Guard aren’t ghosts. How often are you even going to run into them? Honestly.”

“But what will happen to His Highness, Prince Shangshan?”

“What would a nobody like me know? I just hope he stays in the capital from now on. He suffered such terrible things as a child. Who knows what he’s been through? It’s about time he had somewhere peaceful to live.”

Words were always embellished and exaggerated, and people always heard what they wanted to believe.

The unbelievable rumor that had come from the middle-aged man’s mouth had already become a fact backed by solid evidence. Some of the people who’d been afraid from the start moved their trembling legs and crossed the now noisy inn.

To escape a fire too great to contain and survive.

Or to confirm the truth of this information and use it.

But when they finally reached the entrance, they realized they’d stepped into a swamp they could no longer escape.

“Where are you all hurrying off to?”

At the subdued voice, a dozen shadows stepped forward at once, blocking the old doorway.

Step.

For a moment, it was as if the world had stopped.

In the eyes of those hurrying to leave the inn were ten men with bamboo hats pulled low—and, flashing between their wind-cloaks, golden armor.

“The Embroidered Uniform Guard…!”

At those three words, which escaped someone’s lips like a scream, the inn froze over.

Then the young scholar, who’d been sitting silently in thought, spoke.

“That was a truly interesting story. Interesting enough to make fifty silver nyang worthwhile.”

The middle-aged man, clutching the pouch full of silver, stared blankly.

“Young Master, what on earth is going on…?”

“I’m no young master. But I still want to hear more of your story.”

“Y-Young Master! You can’t do this! You can’t…!”

The middle-aged man’s shouts were already out of the young scholar’s mind.

The young scholar—no, the Embroidered Uniform Guard captain—addressed his subordinates, who were blocking the inn’s entrance.

“What are you waiting for? Arrest every one of them.”

“Loyalty!”

With a crisp salute, ten golden figures raced in every direction.

Every one of them was a martial arts master at Supreme First Rate or Peak.

Shouts and tearful pleas burst out from every corner. It took no more than an instant for the cries of those trying to flee or fight back to drown them out.

Bang! Crash!

Amid the crashes ringing through the inn, the Embroidered Uniform Guard captain leaped from the second-floor railing and landed lightly on the ground. He patted the trembling middle-aged man on the shoulder.

“Now, it’s noisy here. Let’s move somewhere else and talk. We’ll discuss everything else you know, who told you that bullshit, and who else has heard it.”

He didn’t bother to tell the man.

This time, he would pay for the story with something other than silver.

And it would shine like silver, yet be incomparably sharper.

* * *

After hearing the report, the Emperor remained silent for a long time, even after the messenger had withdrawn. Only when one person remained nearby did he finally speak.

“What do you think?”

Between the dense strings of pearls and the gauzy silks drifting all around, someone answered.

“Someone must have deliberately spread the rumor.”

“Who’s behind it?”

“Isn’t it obvious? If not the East Depot, then Jin Taekyung, the Blazing Flame Divine Dragon. Or… both.”

“They joined forces?”

“That’s the only possibility for now.”

“I regret it a little. I wonder if it was wise of me to let Jin Taekyung into the imperial palace just because I listened to you.”

The Emperor clicked his tongue and murmured, almost to himself.

“Did the person who sent you to me predict a situation like this, too?”

Someone beyond the silks answered.

“That person is greater and wiser than anyone I know. But Jin Taekyung is unpredictable. He cannot be easily judged.”

Without realizing it, the Emperor nodded.

That audacity, so impossible to fathom. His strength and conviction.

Regardless of their respective positions, Jin Taekyung’s appearance the other day had nearly made even the Emperor laugh out loud.

“We’d better rein him in before he jeopardizes the great undertaking. And what of the target?”

“It won’t be easy. Not at present.”

“Of course. If it were easy, he wouldn’t have been a thorn in our side for more than ten years. But the Great Nation cannot stand firm while he remains. We must do it.”

Rustle.

In place of an answer, a faint breeze from somewhere caressed the silks.

When the Emperor realized that the person who’d been there only moments ago had vanished, he gave a bitter smile and muttered,

“The rumor’s already out. There’s no point hiding it now. We’ll just have to make it true.”

And so began the great celebration commemorating the birth of a new heir to inherit the Great Nation.
```

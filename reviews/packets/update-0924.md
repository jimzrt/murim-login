<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0924.txt",
      "sha256": "275346c0cdc8d93a633206ebb1e4f3ebd0d08ae80613dbeac35a4f97ee467ef5",
      "bytes": 16273
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e5167b76d324def4c852a2b9b32a0e5ffd13e3a7ea345094439c53f03fd9c259",
      "bytes": 1539
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e4f261a256443b1a8267b983fdbd4ae7aa3530803a007681e483b189b757b921",
      "bytes": 231635
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7eb6a168debb9576a47a0c3422066d5fb4d7d61493465c6d0192afae15210ddf",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "ff2ce1714bc0d205ea911bfe6f8f58650f864974311e7b88a46e0bf313e2bc0b",
      "bytes": 806
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "6f31acd3521c30d3ff59fa024ecfacd941da2e8e398e74b05d4367d583ec484f",
      "bytes": 837
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c38cd2178b92e0aec7199f316d8c4ec836483bb6d553e4f179e75dac2567a43a",
      "bytes": 1290
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5f1c4cfb11e3e738e74d6de9b61ffaf79d7996b744ee01a87dc75242ad35676f",
      "bytes": 622
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "f488ac05d81308c998a344722e1a8d4f90d54634cf5c2cf41740d4f48aca1cbc",
      "bytes": 1094
    },
    {
      "path": "characters/Wei Zhong.md",
      "sha256": "e94f50567df38fb2b8b8f052e68ebaca2c9d101ac951cf27cbfb4aadaf840b73",
      "bytes": 705
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8cb5c2ae972283f00b8b56c16eee487e9a5f65c3c8989723ccf0f81ff5e619df",
      "bytes": 265615
    }
  ],
  "estimated_tokens": 12931
}
-->

# Durable State Update — Chapter 924

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
1 and safe_through 924. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 924. Profile updates may replace only one
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
  "chapter": 924,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 924,
    "continuity_sources": [924],
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
    "The Eastern Heaven Demon Lord is dead; the Emperor executed him after Prince Shangshan apologized for his grandfather’s actions.",
    "The Emperor revealed that the fourth prince’s restoration was a response to the Eastern Heaven Demon Lord’s poisoning and takeover of the imperial court, and that he spared the Demon Lord to avert civil war.",
    "Ma Sanbao remains missing.",
    "So Gyo identified Jin Taekyung as the Martial God’s chosen one and intends to explain the story behind it later; her allegiance remains unknown.",
    "The Salcheonmun vowed to pursue Mungyeong regardless of cost or delay and may pursue Jin Taekyung if it learns he killed Gye Yabu.",
    "Jeok Cheongang, Hyuk Mujin, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and the Divine Physician survived and reunited with Jin Taekyung."
  ],
  "continuity_sources": [
    922,
    923
  ],
  "open_questions": [
    "What enabled Jin Taekyung to return from his seemingly fatal injuries?",
    "Where is Ma Sanbao, and what is his current status?",
    "What does the Martial God’s reference to a chosen one mean for Jin Taekyung, and what story has So Gyo kept to herself?",
    "Will the Salcheonmun pursue Mungyeong or discover that Jin Taekyung killed Gye Yabu?"
  ],
  "safe_through": 923,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 반정 as “restoration,” while preserving that it was disguised as a rebellion."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 사형     | **Senior Brother**                           |
| 태원     | **Taiyuan**            |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 위충 | **Wei Zhong** | The pledge’s first signer and the personal name of Lord Cang Gong. |
| 평화 | **Peace Guild** | Guild name. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 태조 | **Taizu** | The Great Nation’s founding emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 아이들 | 청년 | children_to_stranger | beggar bastard | childlike-insulting | The children repeat their mother's insulting description of Taekyung's beggar-like appearance. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 주표 | 홍진 | prince to loyal subject | you | formal and reassuring | Zhu Bao refers to Hong Jin as 그대 while apologizing for the hardship he has endured. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 위충 | Emperor addressing the East Depot’s Seal-Holding Eunuch | Cang Gong | familiar and authoritative | The Emperor addresses Wei Zhong by his East Depot title while asking after his recovery. |
| 위충 | 황제 | East Depot’s Seal-Holding Eunuch addressing the Emperor | Your Majesty | formal and deferential, with pointed flattery | Wei Zhong uses 폐하 while indirectly challenging the Emperor. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 상산왕 | 동천마군 | young imperial prince addressing the enemy who killed his parents and brothers and suffered at the hands of his grandfather | you | formal-polite | He apologizes for his grandfather’s actions using 당신 and deferential speech. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 923
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 923
- **Aliases:** None
- **Role:** The Eastern Heaven Demon Lord is a former Maoshan Sect disciple who commands the dead with a bell and has spent half a century infiltrating the imperial court while building a far-reaching rebellion.
- **Personality:** His hatred of rulers is rooted in the loss of his family and the destruction of the Maoshan Sect; the grief endures, while memories of their happiness have faded.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 923
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care; the Fourth Prince spared him because of their old ties, and his longtime friend and former East Depot cohort Ma Sanbao stayed behind in the palace.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 923
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while her allegiance remains unknown.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 923
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 923
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s twelve-year-old youngest younger brother, an exceptionally skilled young swordsman, and the heir publicly designated by the Emperor.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship and his grandfather’s wrongs, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s youngest younger brother; the late Emperor entrusted Hong Jin with his care. Zhu Bao admires Jin Taekyung, seeks to emulate him, and calls him a friend; he apologized to the Eastern Heaven Demon Lord for his grandfather’s actions before the Emperor executed him.

### Wei Zhong.md

# Wei Zhong (위충)

- **Safe through:** Chapter 901
- **Aliases:** None
- **Role:** Wei Zhong, addressed as Cang Gong, is the East Depot’s Seal-Holding Eunuch and has recovered enough from a prolonged illness to move about.
- **Personality:** Politically perceptive and self-possessed, he uses courteous remarks and veiled barbs to challenge the Emperor.
- **Voice:** He speaks in formal, deferential language, using repeated praise and respectful address to deliver pointed challenges.
- **Relationships:** He has a long-standing connection to the Emperor, with whom he exchanges polite but adversarial remarks about the succession.

## Korean source

```text
＃924화



푹.

어떠한 저항이나 막힘도 없었다.

황가의 보검(寶劍)은 검신에 맞닿은 살과 뼈를 두부처럼 갈랐다. 오직 제 역할에 충실하게, 주인의 의지와는 상관없이.

“……!”

“……!”

일순간 사방에 내려앉은 침묵.

이 자리의 누구도 예상치 못했던 일이었다.

저주받을 황실과 대국을 무너트리기 위해 일평생을 바친 복수귀(復讐鬼)가 이런 길을 택하리라고는.

원수의 후손이 들이민 칼날에 스스로 제 목을 박아 넣으리라고는.

하지만 그럼에도 불구하고, 한번 뒤틀린 운명은 쉽사리 죽음을 허락하지 않았다.

크륵, 컥.

쩍 갈라진 목젖 사이로 피가래가 끓는다. 가쁘게 숨을 헐떡이던 동천마군은 느리지만 조금씩 회복되어 가는 몸을 느끼며 너털웃음을 터트렸다.

참으로 우습기 짝이 없었다.

살기 위해 스스로 괴물이 되었으나, 이제는 죽기 위해 몸부림치고 있는 자신의 모습이.

한때는 축복이라 여겼던 그 힘이, 어느덧 저주가 되어 그를 옭아매고 있다는 것이.

‘이 무슨 촌극(寸劇)이란 말이냐.’

동천마군은 하늘을 바라보며 공허하게 웃었다.

죽고 싶어도 죽지 못하는 몸뚱어리가 원망스러워서.

알 수 없는 눈빛으로 내려다보는 진태경의, 황제의 눈빛을 마주하기 싫어서.

그리고…….

아직도 자신을 향해 깊이 허리 굽혀 절하는, 핏덩이나 다름없는 한 아이를 마주할 자신이 없어서.

아니, 부끄러워서.

“십이 년. 십이 년 전이었지.”

쿨럭.

울컥거리며 차오른 피거품을 뱉어 내며, 동천마군은 천천히 말을 이었다.

“아직 젖도 떼지 못했을 어린아이가 어느 환관의 품에 안겨 황궁을 떠나는 것을, 저 멀리서 지켜보았더랬다.”

환관의 이름은 홍진이요, 아이의 이름은 주표였다.

“죽이려 했었다. 그 후에도 몇 번이나.”

하지만 그러지 못했다.

상산왕 주표가 언젠가 황제를 몰아내고 빈자리를 채울 가장 적합한 허수아비였기 때문만은 아니었다.

황제가 자신의 막냇동생을 상산왕에 봉하여 저 멀리 떠나보낸 것이 일종의 기만책이라는 것을 어렴풋이 짐작하면서도, 동천마군은 끝끝내 암살을 지시하지 못했다.

자신이 왜 이리 고민하는지에 대한 이유조차 몰랐다.

아니, 알면서도 모르는 척했다.

“그 아이는…… 나를 닮아 있었다.”

동천마군은 부모와 형제를 잃은 어린아이의 모습에서, 환관의 품에 안겨 쫓기듯 황궁을 떠나는 그 작은 녀석에게서 자신의 과거를 보았다.

일정 주기마다 찾아오는 전서구(傳書鳩)가 가져온 소식을 보며, 그 몇 줄의 글귀에서 아이의 외로움을 읽었다.

“만 리도 넘게 떨어진 그곳에서, 다섯 살이 된 그 아이는 밤마다 울었다고 했다. 그 울음소리가 담벼락을 넘어서까지 들려올 정도라고 했지.”

불행인지 다행인지 아이는 조숙했고, 다섯 살이 되던 해 알아 버렸다.

자신이 남들보다 훨씬 더 특별하고, 어쩌면 그만큼 불행하다는 것을.

또래의 아이들은 어머니를 유모(乳母)라고 부르지 않는다는 것을.

“시간은 빠르게 흘렀고, 일곱 살이 된 아이는 더 이상 울지 않았다. 대신 밤낮으로 무예를 익히며 활발해졌다고 했지.”

하지만 동천마군은 알고 있었다.

전서에 적힌 짧은 글귀 몇 줄에서, 그는 여전히 울고 있는 아이를 발견할 수 있었다.

“그 아이는…… 그저 울음을 참는 법을 배웠을 뿐이었다. 오래전의 내가 그러했듯이.”

익숙해지고 싶지 않은 일.

그러나 익숙해질 수밖에 없는 일.

아이는 그렇게 울음을 참았다. 지극정성으로 그를 보살피는 환관과 유모의 눈을 피해 밤마다 이불에 얼굴을 파묻고 소리 없이 울었다.

자신의 울음소리를 들으면 그들이 슬퍼할까 봐.

이 울음소리가 담벼락을 넘어가면, 군왕으로서의 체통을 잃을까 봐.

일곱 살.

아이는 성숙해졌고, 현실과 마주했다.

누구도 바라지 않았던 이른 시기에.

“그날, 나는 마침내 깨달았다. 더는 그 아이를 죽일 수 없다는 것을.”

그 후에도 시간은 강물처럼 흘렀다.

끝끝내 궁성에게서 입은 부상을 회복하지 못한 동천마군은 사문의 금지된 대법(大法)을 펼쳐 스스로를 강시로 만들었고, 언제나 비슷한 일상 속에서 살아가던 아이는 한 청년을 만났다.

진태경.

태원진가의 삼 공자.

이제 막 갱생의 길을 향해 한 걸음을 뗀 가문의 망나니.

그리고 이 별 볼 일 없는 무가(武家)의 삼 공자는, 지금껏 아이의 삶에 존재하지 않았던 것을 처음으로 던져 주었다.

그건 바로 꿈이었다.

“꿈은 이루어진다. 분명 그리 쓰여 있었지.”

전서에 적힌 그 내용을 보았을 때, 동천마군은 자신도 모르게 헛웃음을 지었다.

제아무리 어린아이라지만 감히 왕에게 저런 헛소리를 지껄인 애송이가 우스웠고, 그 애송이의 헛소리를 무려 현판으로 만들어 왕부(王府)에 걸어둔 아이의 모습이 재미있었다.

동시에 한편으로는 씁쓸해졌다.

그 역시 한때는 맑고 반짝이는 꿈이 있었으니까.

아이의 꿈은, 자신이 있는 한 이루어지지 못할 테니까.

“하지만 그런 와중에도 문득 궁금해지더군. 그 아이가 마음속 깊이 바라는 꿈이 무엇인지. 이루고자 하는 목표가 무엇인지.”

동천마군은 천천히 고개를 돌렸다.

언제부터인가 눈물에 젖어 버린 눈을 감추기 위해, 깊숙이 굽힌 허리를 펼 생각조차 못 한 채 그저 가늘게 떨고만 있는 아이가 그의 시선에 닿았다.

“이제는 그 의문에 대한 대답을 듣고 싶다. 어느덧 열세 살이 되었을 그 아이에게.”

어언 십이 년이 흘렀다.

아이는 소년이 되었고, 노인은 괴물이 되었다.

그리고 소년은, 상산왕 주표는 지금 이 순간 애써 신형을 가누었다.

“과인의 꿈은.”

깊숙이 굽혀져 있던 허리를 천천히 바로 세우며, 마음속에 담아두었던 꿈을 입에 담았다.

“그대와 내가 겪어야 했던 불행을, 그 누구도 겪지 않게 만드는 것이오.”

“……!”

동천마군의 눈동자가 파르르 떨렸다.

아니, 이 자리의 모두가 마찬가지였다.

“……불가능할 것이다.”

“그렇기에 꿈이오.”

“이루지 못할 것을 알면서도, 그저 바라기만 할 심산이더냐.”

“그럼에도 포기하지 않고 계속해서 시도하기에, 반드시 이루고자 필사적으로 노력하기에 꿈이오.”

“네가 지금 말하는 그것이, 무엇을 뜻하는지 알고 있느냐?”

숨길 수 없는 격동을 드러내는 동천마군을 향해, 상산왕 주표는 조용히 입을 열었다.

“태평성대(太平聖代).”

아득한 태곳적부터 만백성 모두의 소원이었으나, 언제나 그들을 배신했던 네 글자.

그런데 고작 열셋밖에 되지 않은 소년이 말하고 있다.

자신만큼은 그들을 배신하지 않겠다고. 모두가 평화롭고 행복했던 요순(堯舜)의 시대를 다시 열겠노라고.

오롯이 진심을 담아 이야기하고 있었다.

“신분 고하에 상관없이 악한 이는 벌하고, 선한 이에게는 상을 내리겠소.”

이는 정(正)이다.

“언제나 백성을 살피고 아끼며, 주위의 조언을 귀담아듣겠소.”

인(人)이며, 의(義)이다.

“백성 모두를 공경하겠소. 타고난 핏줄을 떠나, 그들의 올바른 마음과 지혜를 받아들이겠소.”

이것은 예(禮)와 지(智)다.

“또한, 그 어떤 불행의 씨앗도 뿌리지 않겠소. 설령 그것이 어떠한 결과로 되돌아온다 해도, 오롯이 감내하고 거둬들이겠소.”

“아.”

동천마군은 신음을 토해 냈다.

어린 왕의 마지막 말에 담긴 의미가, 관용(寬容)이라는 두 글자가 칼날이 되어 그의 마음을 난자했기 때문이었다.

“나는…… 나는 그 무엇도 용서하지 못했다. 어느 순간부터 모든 것을 저주해 왔다.”

지독한 난세의 끝자락에서, 가족들을 잃게 만들었던 군웅들은 흙이 되어 사라졌다.

사문을 불태우고 스승과 사형제들을 도륙했던 태조 역시 불귀의 객이 되었다.

그러나 동천마군은, 그의 복수심은 여전히 남아 있었다.

아니, 오히려 더욱 거세게 타올랐다.

남아있는 자들을 향해. 아무런 죄 없는 그들을 향해.

“한데, 한데 너는 어떻게……!”

차마 똑바로 바라볼 자신이 없어 동천마군은 눈을 감았다. 끓어오르는 목소리로 부르짖었다.

전과 같은 분노가 아니었다.

그저, 어느 때보다 비통했다.

지금 이 순간에조차 모든 걸 완전히 내려놓지 못하는 자신이.

동시에 부끄러웠다.

자신이 일평생 이루지 못한 용서를, 눈앞의 소년이 자그마한 두 손에 담아 건네고 있다는 것이.

“그거 아시오?”

불현듯 들려온 목소리에, 동천마군은 눈을 떴다.

상산왕 주표가 떨리는 시선으로 그를 바라보고 있었다.

“오늘 이 자리에서 모든 사실을 알게 되었을 때, 누구보다 당신을 죽이고 싶었소.”

“그런데 왜…….”

“안타까웠기 때문이오. 과인에게는 행운처럼 찾아왔으나 당신에게는 주어지지 않았던, 우리의 차이를 깨달았기 때문이오.”

상산왕 주표는 천천히 고개를 돌렸다. 초췌한 몰골을 하고 있음에도 당연하다는 듯 옆에 서있는 한 사내가 어린 왕의 눈에 비쳤다.

“내게는 가족보다도 가까운 신하가 있었고.”

가장 오래된 기억에서부터 지금까지, 늘 곁을 지켰던 그의 이름은 홍진이었다.

“오직 이 나라를 위해 수많은 오욕(汚辱)을 감내해야 했던 형님과 충신들이 있었으며.”

황제가 나직한 신음과 함께 눈을 감았다.

더 큰 불의에 맞서 황위를 찬탈할 수밖에 없었던 충성스러운 노장과 금의위들이 차오르는 격동을 억누르기 위해 이를 악물었다.

“한 줄기 빛조차 보이지 않던 그때, 아무런 대가 없이 손을 내밀어 준 이들이 있었소.”

무림인(武林人).

대국의 법도를 벗어나 자신만의 울타리를 세운 자들.

그러나 기꺼이 그 울타리를 무너트리고, 숱한 위험이 도사린 사지(死地)로 달려와 준 이들.

상산왕 주표의 눈길이 그들 한 사람, 한 사람을 스쳤다. 누군가는 멋쩍게 민머리를 긁적였고, 누군가는 부드럽게 눈인사를 건넸으며, 누군가는 배가 고픈 듯이 배를 쓰다듬고 있었다.

그리고, 그 시선 끝에 맞닿은 한 사람이 있었다.

그들 중 가장 강하지도, 현명하지도 않지만, 그럼에도 당연하다는 듯 모두의 중심에 서 있는 청년이.

누군가의 마음에 꿈을 심어 주고, 벗이 되어 주겠다 말했던 그는 지금 이 순간 눈부시게 성장한 소년을 향해 웃고 있었다.

동천마군마저 일순간 눈앞이 밝아졌다고 착각할 만큼 환하고, 따뜻하게.

‘협(俠).’

너무나도 오랫동안 잊고 있었기에 낯설게까지 느껴지는 그 한 글자를, 동천마군은 텅 빈 마음속에서 만지작거렸다.

그리고 이내 물기에 젖은 어린 왕의 눈동자에 비친, 괴물처럼 온통 일그러지고 흐릿한 자신의 모습을 보았다.

“과인이 본 당신은 씻을 수 없는 업보를 쌓은 만고의 죄인이기 이전에, 나와는 다른 길을 걸을 수밖에 없던 불행한 사람이었소.”

불행(不幸)하여 용서가 아닌 복수를 택했고.

불인(不人)하여 괴물이 되었다.

복수만이 유일한 길이라고 생각했다. 그것만이 동천마군을 인간으로, 괴물로 살아오게 만든 이유였다.

하지만 틀렸다.

목적도, 이유도.

“이제는…… 그만해도 괜찮소.”

귓가를 파고든 그 나직한 한 마디에, 동천마군의 몸이 덜컥 굳었다.

그만해도 괜찮다.

이제는, 멈추어도 괜찮다.

그 별것 아닌 한 마디가, 오랜 세월 동안 타올라 재가 되고 얼어붙기를 반복하던 누군가의 마음을 녹였다.

비로소 평화를 가져다주었다.

‘그래, 그랬던가.’

동천마군은 말없이 하늘을 바라보았다.

끊임없이 원망해 왔다.

저 하늘을. 세상 모두를.

그러나 마음속에 드리워져 있던 마지막 한 겹의 분노마저 걷어내자 새로운 세상이 보였다.

저 암흑만이 가득했던 하늘에는 무수한 별이 반짝였고, 어디선가 불어오는 바람에는 풀 내음이 느껴졌다.

자신이 만들어낸 이 지옥도(地獄道)가 풍기는, 짙은 피비린내와 뒤섞인 채.

‘늦었구나. 너무나도 늦게 알아 버렸어.’

이미 수천, 수만 명이 죽거나 다쳤다.

하물며 자신의 선택으로 인해 앞으로 희생당할 이들의 숫자는 얼마나 많을 것인가.

감히 짐작할 수조차 없었다.

거대한 전란(戰亂)에 휩쓸려 매몰될 무수한 생명들도, 그들을 죽음으로 몰아간 그가 짊어질 죄의 무게도.

다만 끝자락에 다다라 동천마군에게 주어진 새로운 갈림길은, 조금이라도 더 옳은 선택을 하라며 끊임없이 속삭이고 있었다.

온통 검게 점칠 되었던 일생을 무색하게 만들 만큼.

- 지금부터 내가 하는 말을, 똑똑히 듣게.

솨아아아.

달싹이는 입술 사이로 흘러나온 전음이 바람에 뒤섞여 나아갔다.

어린 왕과 황제를 스치고, 사방을 에워싼 금의위와 문무백관을 넘어 한 사람에게로.

진태경에게로.

“……!”

크게 뜨인 눈으로 자신을 내려다보는 그 모습에, 동천마군은 씁쓸하게 웃었다.

비록 한참이나 늦었지만, 마지막에 이르러 조금이라도 나은 선택을 했다.

단지 그뿐이었다.

- 이야기를 들려주었으니, 이제 복채(卜債)를 받아야 할 때로군.

깊게 가라앉은 시선으로 말없이 동천마군을 응시하던 진태경이 고개를 끄덕이며 앞으로 나섰다.

철벅.

끈적하게 고인 피 웅덩이 위로 파문이 번졌다.

진태경이 하려는 일을 모두가 알고 있음에도, 이 상황을 지켜보던 문무백관 중 누구도 막지 않았다.

아니, 감히 그럴 수 없었다.

황제가, 상산왕 주표가 친히 걸음을 옮겨 길을 터 주었으니까.

지금 이 순간, 진태경은 천자를 대신하여 만고의 역적을 처단할 권위를 부여받은 대리자였다.

스릉.

서늘한 바람이 역수(逆手)로 쥐어진 창날을 스친다. 그 끝에 서서히 모여드는 청백색의 화염을 바라보며, 동천마군은 문득 입을 열었다.

“나 같은 놈에게도, 내세(來世)라는 것이 주어지리라 생각하나?”

“아마도. 대신 바퀴벌레나 모기로 삼천 갑자쯤 살아야겠지만.”

그래, 그렇겠지.

망설임 없는 대답에 동천마군이 실소를 흘린 그 순간, 진태경이 담담한 목소리로 말을 이었다.

“하지만, 다음 내세에는 꼭 다시 사람으로 태어나라.”

“그게 무슨.”

“혹시 모르잖아. 그때는 이번 삶과 달리 누군가가 당신을 도와줄지도.”

“……!”

“기회가 된다면 그때 다시 만나자. 너무 늦지는 않게.”

동천마군은, 아니 위충(胃蟲)은 침묵했다. 그리고 이내 희미하게 웃어 보였다.

아무런 말도 없이, 눈앞을 물들이는 눈부신 화염을 바라보며.

화아악.

기이할 만큼 따뜻한 그 온기가, 그의 전신을 휘감았다.
```

## Final English reading copy

```markdown
# Chapter 924

*Thud.*

There was no resistance. Nothing to stop it.

The imperial family’s treasured sword split the flesh and bone it touched as easily as tofu, doing its job faithfully, regardless of its master’s wishes.

“……!”

“……!”

Silence fell over the entire place in an instant.

No one here had expected this.

Who could have imagined that a vengeful ghost who had devoted his entire life to bringing down the accursed imperial court and the Great Nation would choose this path?

That he would thrust his own neck onto the blade held out by his enemy’s descendant?

And yet, even so, a fate twisted once did not easily grant him death.

*Grrk. Cough.*

Blood and phlegm bubbled through the gaping wound in his throat. Gasping for breath, the Eastern Heaven Demon Lord felt his body slowly, little by little, beginning to recover. A rasping laugh escaped him.

It was absurd.

He had made himself a monster to stay alive, and now he was struggling to die.

The very power he had once considered a blessing had become a curse, binding him in its grasp.

*What kind of farce is this?*

The Eastern Heaven Demon Lord gazed up at the sky and laughed emptily.

He resented the body that wouldn’t die, no matter how much he wanted to.

He didn’t want to meet the Emperor’s gaze, or Jin Taekyung’s as he looked down at him with those inscrutable eyes.

And…

He didn’t have the courage to face the boy who was still bowing deeply to him, a child no more than a scrap of blood.

No. He was ashamed.

“Twelve years. It was twelve years ago.”

*Cough.*

Spitting out the froth of blood that welled up in his throat, the Eastern Heaven Demon Lord slowly continued.

“I watched from a distance as a little child, still too young to be weaned, left the imperial palace in the arms of a eunuch.”

The eunuch’s name was Hong Jin. The child’s name was Zhu Bao.

“I wanted to kill him. More than once, even after that.”

But he hadn’t.

It wasn’t only because Prince Shangshan Zhu Bao would one day make the perfect puppet—someone to depose the Emperor and fill the vacant throne.

The Eastern Heaven Demon Lord had vaguely suspected that the Emperor’s decision to make his youngest brother Prince Shangshan and send him far away was a kind of deception. And still, he had never given the order to assassinate him.

He hadn’t even known why he agonized over it so much.

No. He had known, but pretended he didn’t.

“That child… reminded me of myself.”

In the little boy who had lost his parents and siblings, in that small child being carried out of the palace as if in flight, the Eastern Heaven Demon Lord had seen his own past.

The messenger pigeon arrived at regular intervals, bringing news. In those few lines of writing, he could read the child’s loneliness.

“They said that far away, more than ten thousand li from here, the five-year-old cried every night. His sobs were so loud they could be heard over the walls.”

By misfortune or good fortune, the child was precocious. In the year he turned five, he learned the truth.

That he was far more special than other people—and perhaps just as unfortunate.

That other children his age didn’t call their mothers wet nurses.

“Time passed quickly. They said that when the child turned seven, he stopped crying. Instead, he grew lively, practicing martial arts day and night.”

But the Eastern Heaven Demon Lord knew.

In those few short lines of the missive, he could still find the child who was crying.

“That child… had only learned how to hold back his tears. Just as I once did.”

Something he didn’t want to get used to.

But had no choice but to get used to.

And so the child held back his tears. Every night, he buried his face in his blanket and cried silently, out of sight of the eunuch and wet nurse who cared for him so devotedly.

He was afraid they would be sad if they heard him crying.

Afraid his sobs would carry over the walls and rob him of his dignity as a prince.

Seven years old.

The child had grown up, and faced reality.

Far earlier than anyone had wished.

“That was when I finally understood. I could no longer kill him.”

After that, time flowed on like a river.

The Eastern Heaven Demon Lord, unable to recover from the injuries he had suffered at the hands of the Bow Saint, performed his sect’s forbidden ritual and turned himself into a jiangshi. Meanwhile, the child, whose days had always been much the same, met a young man.

Jin Taekyung.

The Third Young Master of the Jin Family of Taiyuan.

A wastrel who had only just taken his first step toward turning his life around.

And this unimpressive young master of an unremarkable martial family gave the boy something he had never had in his life.

A dream.

“‘Dreams come true.’ That’s what it said, wasn’t it?”

When the Eastern Heaven Demon Lord read that in the missive, he laughed despite himself.

The cheek of that young punk, spouting such nonsense to a prince, was amusing, even if he was only a child. And the boy’s decision to turn that punk’s nonsense into a plaque and hang it in his residence was funny, too.

At the same time, he felt a pang of bitterness.

He, too, had once had a clear, shining dream.

The child’s dream would never come true as long as he was alive.

“But even then, I found myself wondering. What was the dream that child wished for, deep in his heart? What goal did he want to achieve?”

The Eastern Heaven Demon Lord slowly turned his head.

He saw the boy still bowed low, trembling faintly. Tears had filled the boy’s eyes at some point, and he couldn’t bring himself to straighten up and show them.

“Now I want to hear the answer. From that child, who must be thirteen by now.”

Twelve years had passed.

The child had become a boy, and the old man had become a monster.

And now, in this very moment, the boy—Prince Shangshan Zhu Bao—steadied himself with effort.

“My dream…”

Slowly straightening his deeply bowed back, he gave voice to the dream he had kept in his heart.

“To ensure that no one else ever suffers the misfortune that you and I had to endure.”

“……!”

The Eastern Heaven Demon Lord’s pupils trembled.

No—everyone here felt the same.

“That… will be impossible.”

“That’s why it’s a dream.”

“Do you intend to simply wish for something you know you can’t achieve?”

“It’s a dream because I won’t give up, even so. Because I’ll keep trying, and struggle with all my might to make it come true.”

“Do you understand what it is you’re talking about?”

Facing the Eastern Heaven Demon Lord, who could no longer hide his agitation, Prince Shangshan spoke quietly.

“An age of peace and prosperity.”

It was a four-character phrase that had been the wish of all the people since time immemorial, and had always betrayed them.

And yet, a boy of only thirteen was speaking of it.

He was telling them he, at least, wouldn’t betray them. That he would usher in a new age like the reigns of Yao and Shun, when everyone lived in peace and happiness.

He spoke with all his heart.

“I will punish the wicked and reward the good, regardless of their station.”

That was righteousness.

“I will always watch over and cherish the people, and listen carefully to the counsel of those around me.”

That was humanity, and justice.

“I will respect all my people. I will look beyond their birth and accept their goodness and wisdom.”

That was propriety and wisdom.

“And I will sow no seeds of misfortune. Whatever consequences that choice brings, I will bear them and take responsibility for them.”

“Ah.”

The Eastern Heaven Demon Lord groaned.

The meaning behind the young prince’s final words—the two characters for *mercy*—cut into his heart like a blade.

“I… I couldn’t forgive anything. At some point, I began cursing everything.”

At the end of a brutal age of turmoil, the warlords who had caused him to lose his family had turned to dust and disappeared.

Taizu, who had burned his sect to the ground and slaughtered his Master and fellow disciples, was dead too.

But the Eastern Heaven Demon Lord—and his thirst for revenge—remained.

No, it had only burned more fiercely.

Against those who remained. Against people who were completely innocent.

“But how… how can you…!”

Unable to bring himself to look straight at the boy, the Eastern Heaven Demon Lord closed his eyes and cried out, his voice boiling over.

It wasn’t anger like before.

He was simply more anguished than ever.

Even now, he couldn’t let go of everything.

And he was ashamed.

The boy before him was offering him the forgiveness he had never managed to achieve in his entire life, cradled in his small hands.

“You know something?”

At the sudden voice, the Eastern Heaven Demon Lord opened his eyes.

Prince Shangshan was looking at him with trembling eyes.

“Today, when I learned the whole truth, I wanted to kill you more than anyone.”

“Then why…?”

“Because I felt sorry for you. I realized what made us different: something that came to me like good fortune, but was never given to you.”

Prince Shangshan slowly turned his head. A man stood beside him, looking haggard but entirely at ease, as if there were nowhere else he could be. The young prince’s gaze fell on him.

“I had a subject who was closer to me than family.”

His name was Hong Jin. From the prince’s earliest memories to this very moment, he had always been by his side.

“And I had an elder brother and loyal subjects who endured countless humiliations for the sake of this country.”

The Emperor closed his eyes with a low groan.

The loyal old general and the Embroidered Uniform Guards, who had been forced to seize the throne to confront a greater injustice, clenched their teeth, trying to suppress their agitation.

“When there was not a glimmer of light to be seen, there were people who offered me a hand without asking for anything in return.”

The martial artists of Murim.

People who had stepped outside the Great Nation’s laws and drawn a boundary around their own world.

And yet they had willingly crossed that boundary and rushed into a deadly place full of danger.

Prince Shangshan’s gaze passed from one to the next. One awkwardly scratched his bald head. Another gave him a gentle nod. One was rubbing his stomach as if he were hungry.

And at the end of his gaze stood one man.

He wasn’t the strongest or the wisest among them. Even so, he stood at the center of them all as naturally as if he belonged there.

The young man who had planted a dream in someone’s heart and promised to be his friend was smiling at the boy who had grown so brilliantly.

So bright and warm that, for an instant, even the Eastern Heaven Demon Lord thought the world before his eyes had grown brighter.

*Chivalry.*

He had forgotten that single word for so long that it felt strange. The Eastern Heaven Demon Lord turned it over in his empty heart.

Then, reflected in the young prince’s tear-filled eyes, he saw his own warped, blurred face—the face of a monster.

“The man I saw in you was not only a sinner of the ages, burdened with unforgivable karma. You were also an unfortunate person who had no choice but to walk a different path from mine.”

Unfortunate, he had chosen revenge instead of forgiveness.

Inhuman, he had become a monster.

He had believed revenge was the only path. That was what had made the Eastern Heaven Demon Lord live as a human being, then as a monster.

But he had been wrong.

About his goal. About his reason.

“Now… you can stop.”

At that quiet murmur, which pierced his ears, the Eastern Heaven Demon Lord’s body stiffened.

*You can stop now.*

*It’s all right to stop.*

Those plain words melted the heart of someone who had spent so many years burning to ashes, only to freeze solid again.

At last, they brought him peace.

*So that was how it was.*

The Eastern Heaven Demon Lord gazed silently up at the sky.

He had resented it endlessly.

The sky. The whole world.

But when he let go of the last layer of anger that had hung over his heart, he saw a new world.

Countless stars glittered in the sky that had once been filled with nothing but darkness. The wind blowing from somewhere carried the scent of grass.

It mingled with the thick stench of blood rising from the hellscape he had created.

*It’s too late. I understood far too late.*

Thousands upon thousands of people had already been killed or wounded.

And how many more would be sacrificed because of his choices?

He couldn’t even begin to guess.

Nor could he measure the weight of the crime he would bear for the countless lives swallowed up in the great war he had set in motion.

But as he reached the end, a new fork in the road appeared before the Eastern Heaven Demon Lord, whispering insistently for him to make the better choice—even if only by a little.

A choice that could make his whole life, painted black, seem like nothing.

*—Listen carefully to what I’m about to tell you.*

*Whoosh.*

The Sound Transmission slipped between his moving lips and rode the wind.

It passed the young prince and the Emperor, crossed the Embroidered Uniform Guards and the assembled ministers, and reached one man.

Jin Taekyung.

“……!”

The Eastern Heaven Demon Lord gave a bitter smile at the sight of him staring down in surprise, eyes wide.

It was far too late. But at the very end, he had made a slightly better choice.

That was all.

*—I’ve told you my story. Now it’s time to collect my fortune-telling fee.*

Jin Taekyung watched the Eastern Heaven Demon Lord in silence, his gaze sunk deep. Then he nodded and stepped forward.

*Splash.*

Ripples spread across a pool of thick, sticky blood.

Everyone watching knew what Jin Taekyung was about to do. Still, not one of the ministers stopped him.

No—they couldn’t.

The Emperor and Prince Shangshan Zhu Bao had personally stepped aside to clear the way.

At this moment, Jin Taekyung was the Emperor’s appointed proxy, granted the authority to execute this great traitor on the Son of Heaven’s behalf.

*Shing.*

A cold breeze brushed against the spearhead, held in a reverse grip. Watching the blue-white flames slowly gather at its tip, the Eastern Heaven Demon Lord suddenly spoke.

“Do you think someone like me will be given an afterlife?”

“Probably. But you’ll have to spend about three thousand jiazi as a cockroach or a mosquito first.”

“I see. I suppose so.”

At Jin Taekyung’s matter-of-fact answer, the Eastern Heaven Demon Lord let out a dry laugh. Jin Taekyung continued in an even voice.

“But in your next life, make sure you’re born human again.”

“What do you mean…?”

“You never know. Maybe someone will help you then, unlike in this life.”

“……!”

“If we get the chance, let’s meet again then. Just don’t wait too long.”

The Eastern Heaven Demon Lord—or rather, Wei Zhong—fell silent.

Then, at last, he gave a faint smile.

Without a word, he watched the dazzling flames that filled his vision.

*Whoosh.*

That warmth, strangely enough, wrapped around his entire body.
```

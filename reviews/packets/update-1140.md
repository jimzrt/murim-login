<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1140.txt",
      "sha256": "f18db066ffdf166a3fbded45c746c73f45802ba978303953604f34f02ad554f4",
      "bytes": 11494
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b6750cb8a39d0ea45eea6b1ba3860025039e9be58c4a1472405f033299bdca23",
      "bytes": 1082
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a77573feec836df54e35248f8b975bf7696cac58abec08a1c5a945ccb8c3d729",
      "bytes": 245575
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "06b4d22d84ad6567defdac2701afa5cbe0481f531ece6018f7469efd7f3555fa",
      "bytes": 878
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "632e259acb1b82a21259b8ec2e4eb464bc430e2db118965dca14afe91ee18e24",
      "bytes": 779
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "fd999832f0fe6a85474d18a10332a2c8ea471c51882a505936f4e1f67efec5b9",
      "bytes": 1230
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "87c44682f779ac8e029634ec2781a61e7715e320a5c875e6525529f8317afbd7",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "80568ba292609d0c961424be0362ec4fd89ad50b953e6f53e3890999d6366a50",
      "bytes": 554
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "6895bb50d42c36f27353bbd93b89b738cf9f24fde84d1fe6a64b2ab28d401e24",
      "bytes": 1001
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "204bdfae0f3448f376fe98f2c08d7167564fb815d2310b1a48a82e8503f73eb5",
      "bytes": 1656
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "657066cd81af922659fc6093ec9d7c2ba72054ec2c8ed4f2cf15f9ac06c9fe55",
      "bytes": 1179
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c426bf54faa29ce441a9a88f9e682ce5ce785fdf5bfbb2a19ee91873da9d0420",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "490b6c07199d77bbb877c43a0df727f4f653338f7c5d44d39440daf53d0d5e09",
      "bytes": 1084
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "238499adb52281efe14c871c4f5db36c9d6839a212b822760187a1f586760369",
      "bytes": 1043
    },
    {
      "path": "characters/Son of Heaven.md",
      "sha256": "efe482b1b52c80738d539ff275b47b15434cff9956fa4da977a17eac272b166f",
      "bytes": 684
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "e11c3c7d9b42c21179780bcf506380cd6dde629902b8f8412e0dcea56c026e83",
      "bytes": 926
    },
    {
      "path": "characters/Unnamed.md",
      "sha256": "a65d075f35fb698d9c49ca6a3fa17247250b7ef7b00d58c1ff5038fe656f8a45",
      "bytes": 750
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "676505aed4634c3f13b8bf515d81274540b8d70a774e61dd52a198d24edf76c0",
      "bytes": 936
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5895951d60d69a56331fdfdc592502035283d3a48acfa6cb07fdeb7d2eb418c2",
      "bytes": 291096
    }
  ],
  "estimated_tokens": 13894
}
-->

# Durable State Update — Chapter 1140

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
1 and safe_through 1140. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1140. Profile updates may replace only one
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
  "chapter": 1140,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1140,
    "continuity_sources": [1140],
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
    "The Son of Heaven survived by accepting the White Illusion Jiangshi Art and arrived in Xining with a hundred thousand Imperial Guards.",
    "Murim forces from across the realm have gathered in Xining to fight the Lord of Heaven.",
    "Jin Taekyung is now addressed by the Emperor as Prince Shangshan, formerly Marquis of Shangshan.",
    "Jin Taekyung identifies Cheon Taemin as the Martial God; their connection remains unclear."
  ],
  "continuity_sources": [
    1138,
    1139
  ],
  "open_questions": [
    "What was the Bow Saint’s motive when Jin Taekyung was in mortal danger?",
    "What will happen in the campaign against the Lord of Heaven?",
    "What did Taekyung’s dream of the winged being and battlefield signify?",
    "What is the connection between Cheon Taemin and the Martial God?"
  ],
  "safe_through": 1139,
  "temporary_decisions": [
    "Render 大明 as “Great Ming” and 親征 as “personal expedition.”",
    "Render 滅魔正天 as “Exterminate the Demons and Set Heaven Right.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 법왕     | **Dharma King**               | Hong Dao       |
| 궁성     | **Bow Saint**                 | —              |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 화산파    | **Huashan**                      |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 장강수로맹  | **Yangtze River Channel League** |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 경험치              | **EXP**                        |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 방장      | **Abbot**                                                       |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천검진인 | **Heavenly Sword True Person** | Taoist-style title of the current Sect Leader of Huashan, who once commissioned a sword from Jang Taebo. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 대지모신 | **Earth Mother Goddess** | New deity proclaimed by Jin Taekyung as Nanman's One God. |
| 모신천국 | **Mother Goddess Heaven** | Slogan used by followers of the Earth Mother Goddess. |
| 불신지옥 | **Unbeliever Hell** | Slogan threatening unbelievers with damnation. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 무명 | 거한 | monk_to_attacking_dark_path_officer | Benefactor | deferential but frightened | Uses 시주 while pleading with the officer and insisting that he started the attack. |
| 무명 | 진태경 | newly_met_monk_to_benefactor | Benefactor | formal-polite | Uses 시주 while asking Taekyung's name. |
| 무명 | 굉도 | disciple_to_master | Master | deferential | Refers to Hong Dao as 스승님 while explaining his Dharma name and training. |
| 굉도 | 무명 | master_to_disciple | Disciple | affectionate and familiar | Hong Dao addresses Unnamed as 제자야 while discussing his residence. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 청풍 | 당사독 | young_martial_artist_to_Sichuan_Tang_Family_Head | Family Head | formal-deferential | Cheongpung addresses Tang Sadok as 가주님 while appealing for help. |
| 당사독 | 청풍 | family_head_to_younger_ally | greenhorn | blunt and protective | Tells Cheongpung not to interfere while calling him a 핏덩이. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 당사독 | 진위경 | Tang Clan Family Head to Lesser Family Head | Lesser Family Head | formal and remorseful | Asks whether Wikyung is the Lesser Family Head of the Jin Family of Taiyuan and addresses him while accepting judgment. |
| 진위경 | 당사독 | Lesser Family Head to Tang Clan Family Head | Family Head | cold, formal, and restrained | Addresses Tang Sadok as 가주 while asking what punishment he seeks and presenting the possibility of self-sacrifice. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진위경 | 청풍 | Jin Family Lesser Family Head to young martial companion | Young Hero Cheongpung | formal-polite | Uses 청 소협 while summoning Cheongpung to the Alliance Leader's Hall. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 상산왕 | 황제 | younger brother addressing the Emperor | Your Majesty | deferential royal address | Shangshan addresses the Emperor as 폐하 while pleading for Taekyung. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 1095
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, the publicly recognized sole priest of the Earth Mother Goddess, and the ruler of unified Nanman committed to opposing Dark Heaven.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 1139
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1128
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1138
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1139
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 1128
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1139
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard and the Emperor now addresses him as Prince Shangshan.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, trusts Sama Pyo despite suspecting his betrayal, was regarded as a worthy successor by Peng Cheolhu, and received the Martial God’s message through the Bow Saint.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 1132
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he uses calculated leverage to keep dangerous allies in line and commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1139
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1139
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 1139
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

### Son of Heaven.md

# Son of Heaven (천자)

- **Safe through:** Chapter 1139
- **Aliases:** Emperor, Zhu Di
- **Role:** The Son of Heaven is the Emperor of Great Ming and Zhu Bao’s elder brother; he has ordered a personal expedition to Xinjiang and will not return to the palace until the traitors are rooted out.
- **Personality:** Coldly strategic and imperious, he is willing to break taboos to remain with his younger brother.
- **Voice:** Calm and commanding, with dry, understated humor.
- **Relationships:** Zhu Bao is his younger brother and heir; Jin Taekyung gave him the White Illusion Jiangshi Art; he killed Ma Sanbao.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 1027
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, overseeing its recovery and relying on allied martial artists to help treat patients and guard against another Dark Heaven attack.
- **Personality:** Blunt and unsentimental, yet grateful to those who remain with the Tang Clan; he has consciously chosen to change and speaks candidly about the clan’s vulnerability.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor, his unnamed nephew serves as Master of the Gatekeeper Pavilion, Mimi is his cherished old friend and companion temporarily entrusted to Cheongpung, and he regards Jin Taekyung and Cheongpung as benefactors, openly welcoming Jin with a warmth he usually conceals.

### Unnamed.md

# Unnamed (무명)

- **Safe through:** Chapter 542
- **Aliases:** None
- **Role:** Unnamed is a young Shaolin monk and practical Disciple of the late Hong Dao who achieved enlightenment after three months of treatment and training in Repentance Cave, becoming a Supreme Peak master and Jung Ho's young Martial Uncle.
- **Personality:** Naturally timid and introverted, but unable to control himself once angered.
- **Voice:** His current voice is rough, formal, and polite, punctuated by Buddhist invocations.
- **Relationships:** Hong Dao was his Master; Jung Ho is his Martial Nephew; he carries Hong Dao's will and recognizes the Morning Star whom Hong Dao intended him to find.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 1095
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, Great Chieftain of the Miao people, and public priest of the Earth Mother Goddess.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
＃1140화



헤아릴 수도 없이 많은 관무(官武) 연합군이 수백 개의 깃발을 휘날리며 모습을 드러내기 전부터, 지원군에 관한 소식을 접한 서녕성의 사람들은 이미 한껏 기대에 부풀어 있었다.

“내 살아생전 이런 광경을 보게 될 줄이야.”

황실과 무림맹의 연합.

이것만으로도 대륙의 역사상 유례를 찾아볼 수 없는 일이지만, 그 안에 포함된 면면 또한 실로 대단했으니까.

“구, 구파일방에 오대세가까지? 전부?”

“그렇다니까. 이참에 저 간악한 암천 놈들이 중원에 심어 둔 사술(邪術)까지 모조리 뿌리 뽑았으니, 이제 무엇이 두렵겠나?”

“그, 듣자 하니 은섬창(銀閃槍) 대협과 태백신옹(太白神翁)께서도 합류하셨다던데.”

“아니, 은섬창 대협이야 그렇다 쳐도 태백신옹 그 늙은이는 흑도 아니었나?”

“……나도 흑도인데.”

“아, 맞다. 깜빡했네. 자네 장강수로맹이었지.”

“그냥 웃게. 분위기 잡치지 말고.”

내로라하는 명문대파(名門大波)의 영수들은 물론 홀로 천하를 종횡하던 대협객, 거기에 더해 이미 오래전 죽었다 알려진 은둔 고수들까지.

정파인들은 물론 조금이라도 수틀렸다 하면 병장기부터 뽑고 보는 흑도 무림인조차 이번만큼은 설레는 마음을 감출 수 없었다.

이미 삼성(三星)이라 칭해지는 전설들과 함께 전투를 치른 그들이었지만, 이것이야말로 진정한 대통합이 아닌가.

심지어 그 끔찍했던 정마대전 때조차, 천하 무림의 힘이 이토록 일치단결하여 한곳에 총집결된 적은 없었다.

더불어 이러한 무림인들의 반응처럼, 관군과 백성들 역시 저마다의 이유로 떨림을 감출 수 없었다.

천자(天子).

용의 핏줄.

하늘이 이 땅에 내린 만인의 어버이이며 지배자.

황도(皇都)에 살아도 볼 수 없다는 그가 친히 대군을 이끌고 온다는 소식에 그들은 귀를 의심했고, 이내 곧 모든 것이 사실이었음을 알게 되었다.

소문을 통해서만 들었던 천자의 드높은 위엄과 기품.

그리고.

“오랜만이구나, 상산후(上山侯) 진태경.”

한 사람과의 인연까지도.

하지만 다음 순간 이어진 천자의 뒷말은, 그 자리의 누구도 감히 예상치 못했던 것이었다.

“아니, 이제는 상산왕(上山王)이라 불러야겠군.”

“……!”

“……!”

일순간 사방의 공기가 찌르르 울렸다 느낀 것은, 결코 누구 한 사람만의 착각이 아니었다.

무림인, 관군, 백성.

그들 모두는 잠시 다 함께 환청을 들었나 고민했고, 크게 뜨인 눈으로 서로를 바라보는 시선을 통해 깨달았다.

절대, 절대 잘못 들은 것이 아니다.

지금 막 천자는 선언했다.

아니, 선포했다.

고귀한 용의 피가 단 한 방울도 섞이지 않은, 저 새파란 청년을 왕으로 봉하겠노라고.

이미 수백 년 전에 역사 속으로 사라졌던 이성왕(異姓王)이, 바로 이곳에서 새롭게 탄생한 것이다. 

그리고 모두를 얼어붙게 만든 이 사상 초유의 사태 속에서, 어째서인지 텅 빈 허공만을 바라보던 진태경이 문득 입을 열었다.

“와, 업적 달성 경험치 미쳤네.”

“……?”

“……?”

저게 무슨 개소리지?

도무지 이해할 수 없는 말로 모두를 혼란에 빠트린 진태경이, 천자를 똑바로 응시한 채 말을 이었다.

“폐하.”

한없이 진지한 얼굴로.

“기왕 주신 거, 통 크게 왕 자리 몇 개 더 안 됩니까?”

천자는 크게 소리 내어 웃었고, 일순간 멍해진 사람들은 동시에 같은 생각을 떠올렸다.

진짜, 미쳐도 단단히 미친놈이라고.

하지만 왕이 되어 버린 미친놈의 활약은, 거기에서 끝나지 않았다.



* * *



그 후로도 사람들은 끊임없이 자문하고 상기시켜야 했다.

진태경이라는 이름을 가진, 한 인간에 대해서.

지금껏 알음알음 들었던 그와 관련된 소문에 대해서.

그리고 머지않아 두 눈과 귀로 똑똑히 확인할 수 있었다.

“왜, 상산왕으로는 부족한가? 짐의 아우가 맡던 자리이기도 하여 상징성이 클 텐데.”

“어우, 부족하긴요. 좋죠. 그냥 혹시 하나 더 주실 수 있나 해서요. 헤헤.”

무슨 소면에 국물 추가하는 것도 아니고, 왕위(王位)로 넉살을 부리는 진태경의 모습에 모두가 숨을 삼켰다.

심지어 그중 일부는 철혈(鐵血)이라 불리는 작금의 천자가 지금 당장 진태경을 엄벌할 것이라 생각하기도 했다.

그러니까, 아주 잠깐은.

“이유를 말해 주면 안 될 것도 없지.”

어?

“으음. 자세히 말씀드리긴 좀 곤란한데요. 그냥 시험 삼아 해보는 거라.”

왜지.

“흠. 그대 나름의 이유가 있겠지. 하면 하북의 예왕(郳王)도 겸하도록.”

뭐지.

“감사합니, 음.”

“왜 그러나?”

“아닙니다. 예왕은 안 맡을게요. 아, 이거 중복이 안 되네.”

“무슨 소린지는 모르겠지만, 편할 대로 하게.”

……진짜, 이거 뭐지.

이 모든 상황을 빠짐없이 지켜보던 사람들은 반쯤 넋이 나갔다.

진태경과 웃으며 몇 마디를 더 주고받은 천자가 금위군과 함께 내성(內城)으로 향한 뒤에도 그들이 느낀 충격은 쉽게 사라지지 않았다.

아니, 오히려 새로운 느낌의 충격이 그들을 기다리고 있었다.

두두두두!

활짝 열린 성문 사이로 물밀 듯이 쏟아지는 인마(人馬)의 물결과 명문대파를 상징하는 무수한 깃발들.

범상치 않은 기세와 안광을 흩뿌리며 모습을 드러낸 면면들을 본 사람들은 탄성을 흘렸고, 곧 기시감을 느껴야만 했다.

조금 전과 같은 충격도 함께.

“진 시주, 소승을 기억하시는지요?”

“진 도우. 그간 정말로 고생 많았네.”

“오랜만일세. 다친 곳은 없나?”

구파일방에 속한 승려와 도사들은 물론, 오대세가의 명망 높은 고수들까지.

그들은 약속이라도 한 것처럼 진태경을 중심으로 모여들었고, 그는 아무렇지 않게 천하 무림의 거목들과 인사를 주고받았다.

“제가 무명(無名) 스님을 어찌 잊겠습니까. 그런데 못 본 사이에 근육이 더…… 이야.”

법왕 굉도가 남긴 유일한 제자이자, 암천을 뿌리 뽑을 때까지 소림사의 방장 직에 앉지 않겠다고 천명한 무명.

“천검진인(天劍眞人)께서도 오셨군요. 아, 청풍이요? 저쪽에 있, 었는데 없어졌네요. 그나저나 제자분들도 같이 왔습니까?”

검성 매종학의 제자이기 이전에 화산파 장문인 직을 맡고 있는 천검진인.

그리고.

“진 도우께서는 여전하십니다.”

“사천에서는 큰 신세를 졌네. 자네가 아니었다면…….”

“호북에서의 일이 생각나는군.”

또 다른 문주, 가주, 장문인.

그나마 한 발이라도 걸칠 수 있던 이가 명문대파의 장로급이고, 그 밑으로는 진태경에게 아는 척도 못했다.

공간이 없어서.

아미, 무당, 개방을 비롯한 명문대파의 영수‘들’에게 에워싸인 진태경의 모습은 모두의 눈을 의심케 만들기에 충분했다.

특히, 성질 더럽기로는 모르는 이가 없다는 사천당가의 가주와 소문으로만 들었던 남만야수궁주의 등장은 불길에 기름을 끼얹는 수준이었다.

“당가(唐家)의 은인에게 인사 올리겠네. 불가피하게 늦을 수밖에 없었던 점, 부디 용서하시게.”

한마디 말보다 한 방울 독을 선호한다는 만독수라(萬毒修羅) 당사독은 극진한 예를 갖추어 포권을 취했고.

“빌어먹을, 놈들이 사천으로도 올 줄 알았는데…… 그 호랑이 먹이로 던져 줘도 시원치 않을 것들 때문에 발이 묶였었어. 면목이 없군.”

호피로 전신을 두른 거한, 야수묘왕(野獸苗王) 야율척은 고개를 숙인 채 진태경의 눈치를 살피기까지 했다.

마치 죄인이라도 되는 것처럼.

“……이 정도였나.”

누군가의 입술 사이로 흘러나온 뇌까림에, 이 모든 광경을 빠짐없이 지켜보던 사람들은 알 수 없는 전율을 느꼈다.

저들이 누구인가.

각 성(省)을 넘어, 천하 무림을 대표하는 거인들이다.

제아무리 진태경이 바로 그 화왕의 제자라 한들, 까마득할 정도의 연배와 휘하에 거느린 세력의 면에서 보자면 하늘과 땅 차이.

하지만 오늘에서야 알았다.

아니, 정확히는 막연히 짐작만 하고 있던 실체를 똑똑히 보고 느꼈다.

작금의 이 천하에서, 진태경이라는 존재가 얼마나 큰 위상을 지니고 있는지.

그리고 동시에, 불현듯 직감했다.

어느덧 별과 왕의 시대가 저물어 가고 있다는 것을.

무수한 거목들 사이에 똬리를 튼 저 젊은 신룡(神龍)이야말로, 암천이라는 먹구름을 집어삼키며 아득한 창공으로 날아오를 영웅이라는 것을.

바야흐로.

새로운 시대가 천하를 향해 손짓하고 있었다.



* * *



자리를 빠져나오기까지의 과정은 쉽지 않았다.

짧게나마 일면식이 있는 이들은 모두 나와 인사를 나누고 싶어 했고, 그건 일면식이 없는 이들 역시 마찬가지였다.

“진 대협!”

“아, 예. 반갑습니다.”

“제 술 한 잔 받으십시오! 일생의 광영으로 여기겠습니다!”

“그 말만 벌써 오십 번쯤 들은 거 같긴 한데…… 우선 주십쇼.”

곳곳에 기쁨이 넘쳐흐르니, 술잔도 넘쳐흐르는 것은 당연한 일일지도 모른다.

포권지례만 수백 번에, 받은 술잔만 수십여 잔.

어느새 서녕성은 하나의 거대한 연회장으로 돌변한 지 오래였고, 나는 한참의 시간이 흐른 뒤에야 가까스로 자리를 빠져나올 수 있었다.

“어머니, 우리 막내가아, 왕이 돼씁니다. 흐흐흑.”

“모신천국 불신지옥! 위대하신 대지모신께서 개씨벌 천주를 벌하시리라!”

“황제 폐하 만만세! 내 당장 사막 너머로 쳐들어가서 저 역도 놈들의 대가리를 박살……!”

“…….”

어지럽네 진짜.

술이 들어가자 엄근진 코스프레를 풀고 울기 시작하는 진위경, 어느덧 남만의 유일신 정도로 자리 잡은 대지모신의 광신도들.

거기에 더하여 충성심으로 무장한 대명국 신민들의 외침을 뒤로한 채, 나는 홀로 조용히 걸음을 옮겼다.

그 모든 소음들이 멀어질 때까지.

온 거리를 가득 메운 서녕성의 불빛이 닿지 않는, 동문(東門) 너머의 강줄기까지.

그리고 그곳에서, 지난 사흘간 보지 못했던 한 사람과 마주했다.

아니, 수없이 뒤얽힌 머릿속 생각을 정리하기 위해 일부러 찾지 않았던 그녀를.

사박.

천천히 내디딘 발끝을 따라 부드럽게 파이는 젖은 모래알.

궁성(弓星)과 나란히 선 나는, 출렁이는 강물을 말없이 지켜보았다.

그 후에도 아주 오랫동안.
```

## Final English reading copy

```markdown
# Chapter 1140

Long before the countless government and Murim forces appeared, hundreds of banners flying in the wind, the people of Xining City were already bursting with excitement at the news of reinforcements.

“I never thought I’d live to see a sight like this.”

The imperial court and the Murim Alliance, united.

That alone was unprecedented in the history of the continent. But the people gathered under those banners were just as extraordinary.

“T-The Nine Sects and One Gang, and the Five Great Families, too? All of them?”

“That’s right. They’ve even rooted out every last one of those Dark Heaven bastards’ dark arts planted in the Central Plains. What is there to fear now?”

“I-I heard the Silver Flash Spear Hero and the Taebaek Divine Elder have joined them, too.”

“Hold on. The Silver Flash Spear Hero, sure—but wasn’t that old Taebaek Divine Elder a dark-path figure?”

“……I’m a dark-path figure, too.”

“Oh, right. I forgot. You’re with the Yangtze River Channel League.”

“Just laugh it off. Don’t ruin the mood.”

The leaders of the most renowned orthodox sects. Great Heroes who had roamed the realm alone. Even reclusive masters who had supposedly died long ago.

The orthodox martial artists weren’t the only ones unable to hide their excitement. Even the dark-path martial artists, who reached for their weapons at the slightest provocation, felt it this time.

They had already fought alongside the legends known as the Three Saints, but wasn’t this the true unification of the realm?

Even during the terrible Great Faction War, the power of the entire Murim had never gathered in one place with such unity.

And just like the martial artists, the government troops and commoners couldn’t hide their trembling excitement, each for their own reasons.

The Son of Heaven.

A descendant of the dragon.

The father and ruler of all people, sent by Heaven to this land.

They could scarcely believe their ears when they heard that the man said to be impossible to see even if you lived in the Imperial Capital was personally leading a great army here. Before long, they learned it was true.

The Son of Heaven’s lofty authority and grace, known to them only through rumor.

And—

“It’s been a long time, Marquis of Shangshan Jin Taekyung.”

Even his connection to one particular person.

But the Son of Heaven’s next words were something no one there could have predicted.

“No, I suppose I should call you Prince Shangshan now.”

“……!”

“……!”

The sudden sense that the air around them had crackled wasn’t the delusion of just one person.

Martial artists, government troops, commoners.

They all wondered for a moment if they’d shared a collective hallucination. Then, as they looked at one another with wide eyes, they understood.

They hadn’t misheard. Not at all.

The Son of Heaven had just declared it.

No—proclaimed it.

He would enfeoff that young man, not a single drop of whose blood was noble dragon’s blood, as a prince.

A king with a different surname, gone from history for hundreds of years, had just been born anew right here.

And amid the unprecedented scene that had frozen everyone in place, Jin Taekyung—who, for some reason, was staring into empty space—suddenly spoke.

“Wow. The EXP for that achievement is insane.”

“……?”

“……?”

What the hell was he talking about?

Having thrown everyone into confusion with words no one could understand, Jin Taekyung looked straight at the Son of Heaven and continued.

“Your Majesty.”

His expression was utterly serious.

“Since you’re handing them out anyway, could you give me a few more royal titles while you’re at it?”

The Son of Heaven burst out laughing. The people, stunned for a moment, all had the same thought.

He really was a complete madman.

But the madman who’d just become a king wasn’t done yet.

* * *

Afterward, people had to keep asking themselves, over and over, to remember what Jin Taekyung was like.

They’d heard rumors about him here and there.

Before long, they were able to confirm them with their own eyes and ears.

“Is Prince Shangshan not enough? It was also the title held by my younger brother, so it carries considerable significance.”

“Oh, it’s plenty. It’s great. I was just wondering if I could get one more. Hehe.”

At Jin Taekyung’s shameless request for another royal title—as if he were asking for extra broth with his noodles—everyone held their breath.

Some even thought the Son of Heaven, known for his iron-blooded rule, would punish Jin Taekyung on the spot.

That is, for a very brief moment.

“If you tell me why, I see no reason to refuse.”

Huh?

“Um. It’s a little awkward to explain in detail. I’m just giving it a try.”

Why?

“Hm. You must have your reasons. Then you may also take the title of Prince of Ye in Hebei.”

What?

“Thank you, Your Maj—oh.”

“What is it?”

“Nothing. I’ll pass on Prince of Ye. Ah, I guess you can’t have duplicates.”

“I don’t know what you mean, but do as you please.”

……Seriously, what was going on?

The people who’d watched every moment of this exchange were half out of their minds.

Even after the Son of Heaven had traded a few more laughs with Jin Taekyung and headed toward the Inner City with the Imperial Guards, the shock they felt didn’t fade easily.

No—instead, a different kind of shock was waiting for them.

*Thud-thud-thud-thud!*

A flood of men and horses poured through the wide-open city gates, followed by countless banners bearing the emblems of the great sects.

The people who saw the figures emerging with extraordinary auras and gleaming eyes let out cries of amazement. Then a familiar feeling struck them.

And with it, the same shock as before.

“Benefactor Jin, do you remember me?”

“Daoist Jin. You’ve been through so much.”

“Long time no see. Are you hurt?”

Monks and Daoists from the Nine Sects and One Gang, along with renowned masters from the Five Great Families.

As if they’d planned it, they gathered around Jin Taekyung. He greeted the towering figures of the realm’s Murim as casually as if nothing were out of the ordinary.

“How could I forget Master Unnamed? But you’ve gotten even more muscular since I last saw you…… Wow.”

Unnamed, the sole Disciple of Dharma King Hong Dao, and the man who had sworn not to take the seat of Abbot of Shaolin until Dark Heaven was rooted out.

“Heavenly Sword True Person, you came, too. Oh, Cheongpung? He was over there, but now he’s gone. By the way, did your Disciples come with you?”

The Heavenly Sword True Person, who was the Sect Leader of Huashan first and foremost, not merely Sword Saint Mae Jonghak’s Disciple.

And—

“You haven’t changed a bit, Daoist Jin.”

“We owe you a great debt for what happened in Sichuan. If it hadn’t been for you……”

“That reminds me of what happened in Hubei.”

Other Sect Leaders, Family Heads, and heads of sects.

Even an Elder of a great sect could barely get a foot in. Anyone below that rank couldn’t get close enough to greet Jin Taekyung.

There simply wasn’t room.

Surrounded by the leaders of the great sects—including Emei, Wudang, and the Beggars’ Sect—Jin Taekyung looked like a sight straight out of a hallucination.

The arrival of the Sichuan Tang Clan’s Family Head, whose foul temper everyone knew about, and the Palace Lord of the Nanman Beast Palace, whom they’d only heard of in rumors, poured oil on the fire.

“I’ve come to pay my respects to the Tang Family’s Benefactor. Please forgive me for being unavoidably late.”

Tang Sadok, the Myriad-Poison Asura, was said to prefer a drop of poison to a word of conversation. Yet he clasped his hands in a deeply respectful salute.

“Damn it. I thought they’d come to Sichuan, too… But I was held up by those bastards. Even feeding them to that tiger wouldn’t have satisfied me. I have no excuse.”

Yayul Cheok, the burly man wrapped in tiger hide, even lowered his head and watched Jin Taekyung’s face for a reaction.

As if he were a criminal.

“……Was he really this important?”

At the muttered words that slipped from someone’s lips, those who had watched the whole scene felt a shiver they couldn’t explain.

Who were these people?

They were titans who represented the Murim beyond their own provinces, across the entire realm.

Even if Jin Taekyung was the Fire King’s Disciple, there should have been a world of difference between him and those people, given the gulf in age and the forces under their command.

But today, they finally understood.

Or, more accurately, they saw and felt the truth they’d only vaguely suspected until now.

Just how much influence Jin Taekyung held in this world.

And, at the same time, they suddenly sensed it.

The age of the stars and kings was drawing to a close.

That young Divine Dragon, coiled among countless towering trees, was the hero who would swallow the dark clouds of Dark Heaven and soar into the boundless sky.

At last—

A new age was beckoning to the realm.

* * *

Getting away from the gathering hadn’t been easy.

Everyone who’d met me before wanted to greet me, and so did people who’d never met me.

“Great Hero Jin!”

“Oh, yes. Nice to meet you.”

“Please have a drink with me! I’ll treasure it as the honor of a lifetime!”

“I think I’ve heard that about fifty times already…… But sure, pour me one.”

With joy overflowing everywhere, it was only natural that the wine would overflow, too.

I’d clasped hands in salute hundreds of times and received dozens of drinks.

Xining City had long since become one enormous banquet hall. It took a long time before I could finally make my way out.

“Mother, our youngest is a king now. Sniff, sob.”

“Mother Goddess Heaven! Unbeliever Hell! The great Earth Mother Goddess will punish that fucking Lord of Heaven!”

“Long live the Emperor! I’ll cross the desert right now and smash those rebels’ heads in……!”

“……”

This is a mess.

Jin Wikyung had dropped the stern-and-serious act and started crying as soon as he got drunk. The Earth Mother Goddess’s fanatics—who by now practically regarded her as Nanman’s One God—were shouting their slogans.

I left the cries of Great Ming’s subjects, all fired up with loyalty, behind me and walked off alone.

Until all that noise had faded away.

Past the East Gate, as far as the river beyond the reach of Xining City’s lights, which filled every street.

And there, I came face-to-face with someone I hadn’t seen in the past three days.

No—I’d deliberately avoided seeking her out to sort through the thoughts tangling around in my head.

*Shhk.*

My foot pressed slowly into the wet sand, leaving a soft depression.

Standing beside the Bow Saint, I watched the rippling river in silence.

For a long, long time afterward.
```

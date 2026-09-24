<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0999.txt",
      "sha256": "5d75c989b1cdd0b34022879f11ba5a73cfce503c897cd894b18990702538360a",
      "bytes": 12802
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d51dd69cdf68f97eba4d175dcb7146bf2f13946c688bd348b2c0780d28407396",
      "bytes": 1487
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Gong Iljung.md",
      "sha256": "355968fa5408f577fbe6def501fa2bce645469d79c96d64d4db5cc326945e134",
      "bytes": 466
    },
    {
      "path": "characters/Hwangbo Eom.md",
      "sha256": "031b16d09c01a028b3c970992f3746b680a3cc6f8228154b1bb2e4e97776fde1",
      "bytes": 629
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "da8ff9c986fba747bea677096afddb5ab15e4ac91404dd2166a216bff34f859a",
      "bytes": 1374
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "72b7b0d8c9fed43cc63276efa7a8f2af267050e90cbcf7818fddf7400e823369",
      "bytes": 1391
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "9e7a7d4cfa73e15062628a8c3a3a195c8fa21ded8a52b402b32c395c0ec140a7",
      "bytes": 1613
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "88b3a9d68d704a8d2e334ebb7cd8d9b3dc7547f59b13f67d7daa2908e3a79024",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "54d82614e1f1981937cae342f7b46b51bda41dbf530548650de7a1cfb2854bf2",
      "bytes": 973
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "899af90966bfc79579250a9e1f2478167ded48fea412052ed8a2ce4ee0df719f",
      "bytes": 964
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0cfb76de4496dfd84609e284fd61b787fe53be76130ba1752c7f0390185f35fd",
      "bytes": 274035
    }
  ],
  "estimated_tokens": 12042
}
-->

# Durable State Update — Chapter 999

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
1 and safe_through 999. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 999. Profile updates may replace only one
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
  "chapter": 999,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 999,
    "continuity_sources": [999],
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
    "Taekyung’s group has reached the Shaanxi–Gansu border after three days overland and plans to check Gansu before continuing to Qinghai.",
    "Dark Heaven’s army is reportedly advancing beyond the desert, but its destination is unknown; Qinghai, Gansu, and Tibet are possible routes into the Central Plains.",
    "Dark Heaven’s Moving Formations could transport forces into the Central Plains; their number and locations are unknown, and neutralizing them would require time and manpower.",
    "The Demon-Sealing Formation may be able to neutralize Moving Formations; Zhuge Feng’s clan used it to contain the rift at Dongting Lake.",
    "Sama Pyo’s Black Dragon Demon Gate in Gansu may be threatened by Dark Heaven’s advance through Xinjiang.",
    "The Nanman Beast Palace accepted the Murim Alliance’s request and is defending Sichuan alongside the still-intact Qingcheng and Emei.",
    "A large Zhongnan Sect party, including two recently recuperated senior Daoists and a half-white-haired Sect Leader, has stopped at the Shaanxi–Gansu border."
  ],
  "continuity_sources": [
    997,
    998
  ],
  "open_questions": [
    "Where will Dark Heaven’s advancing army strike, and what is its objective?",
    "What caused the System malfunction, and is it connected to the Lord of Heaven?",
    "Why did Sama Pyo’s father order him to return immediately?"
  ],
  "safe_through": 998,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 공일중    | **Gong Iljung**    |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 무림맹    | **Murim Alliance**               |
| 하북팽가   | **Hebei Peng Family**            |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 선배     | **Senior**                                   |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 도사      | **Daoist**                                                      |
| 황보엄 | **Hwangbo Eom** | Personal name of the Taeeul Merciless Sword. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 혀왕 | **Tongue King** | Taekyung’s joking nickname for Jeok Cheongang after his verbal intimidation. |
| 설삼 | **snow ginseng** | Elixir compared with the chapter's three selected roots. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 풍운전신 | **Wind-and-Cloud War God** | Jeok Cheongang's mistaken version of Gong Iljung's title. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 천년설삼 | **Thousand-Year Snow Ginseng** | Secret Zhongnan Sect cargo; a fully digested specimen can grant a full jiazi of internal energy. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 적천강 | 공일중 | senior_martial_master_to_sect_leader | you; man with the sycophant's beard | blunt and insulting | Jeok mocks Gong's beard and dismisses the title Wind-and-Cloud Sword Lord. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 황보엄 | visitor_to_Zhongnan_senior_martial_uncle | Great Hero Hwangbo | formal-deferential | Ju Hwaran formally introduces herself to Hwangbo Eom as the Taeeul Merciless Sword. |
| 황보엄 | 주화란 | Zhongnan senior to Yongbong Young Bureau Head | you | cold, commanding, and manipulative | Uses 자네 while ordering Hwaran to open the casket and demanding compensation. |
| 진태경 | 황보엄 | junior_martial_artist_to_Zhongnan_senior | Great Hero Hwangbo | casual-polite and teasing | Taekyung uses 황보 대협 after deliberately pretending not to recognize Hwangbo. |
| 황보엄 | 진태경 | Zhongnan_senior_to_younger_martial_artist | insolent brat | blunt, amused, and probing | Hwangbo describes Taekyung as a 건방진 아해 and later treats him as a youngster. |
| 황보엄 | 적천강 | rival_martial_masters | Fire King Jeok Cheongang | cold and taunting | Reveals that he knows Jeok's illness and threatens to settle his bad blood with the Fire Gate Clan. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |

## Listed compact profiles

### Gong Iljung.md

# Gong Iljung (공일중)

- **Safe through:** Chapter 244
- **Aliases:** Wind-and-Cloud Sword Lord
- **Role:** Current Sect Leader of the Zhongnan Sect and bearer of the Wind-and-Cloud Sword Lord title
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Gong Ilhyuk's father's cousin; Senior Brother of the Roaring Fury Swordsman.

### Hwangbo Eom.md

# Hwangbo Eom (황보엄)

- **Safe through:** Chapter 363
- **Aliases:** Taeeul Merciless Sword
- **Role:** Supreme Peak master of the Zhongnan Sect and its Second Martial Uncle, known as the Taeeul Merciless Sword.
- **Personality:** Ruthless, severe, proud, and deeply invested in restoring Zhongnan's standing.
- **Voice:** Calmly courteous when offering tea, then cold, commanding, and cutting when reprimanding others.
- **Relationships:** Song Il is his only Senior Brother, the current Sect Leader is his martial brother, and Hyuk Sopyung is his junior.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 998
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 998
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 997
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 997
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 995
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 995
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

## Korean source

```text
＃999화



내가 막 사회 초년생으로서 헌터 생활을 시작했을 때, 짬밥 좀 먹었다는 고참 헌터들이 입버릇처럼 하는 말이 있었다.

언제, 어디에서 다시 이어질지 모르는 것이 바로 사람 인연이라고.

그러니 누군가와 인연을 맺고 끊을 때는 늘 신중하고 유연하게 대처해야 뒤탈이 없다고.

현재에 이르러 돌이켜보니 이것만큼 뼈와 살이 되는 조언도 없었던 것 같다.

다만 한 가지 중요한 문제가 있다면, 나 같은 놈에게는 그런 조언이 쥐뿔도 안 먹힌다는 것이다.

“이거 오타 난 것 같은데…….”

대(大) 종남파(終南派).

화려한 비단에 수놓아진 네 글자를 읽자마자 반사적으로 튀어나온 한 마디에, 가장 가까이에 있던 도사 한 명이 눈살을 찌푸렸다.

“이보게 도우(道友), 지금 뭐라고 했나?”

“아, 그냥 혼잣말.”

“혼잣말?”

“응.”

“말이 짧군.”

“응이요.”

말문이 막힌 듯, 순간 멍해진 얼굴로 나를 바라보던 중년의 도사가 숨을 고르며 겨우 입을 열었다.

“지금 뭐 하자는 건가?”

“나한테 도우라며. 친구니까 말 놨지. 그렇지 않아도 그쪽에서 먼저 말 놓길래.”

“보아하니 같은 무림인 같은데, 나이도 한참 젊어 보이는 친구가 못 하는 말이 없군.”

“그래도 될걸. 나이만 새파랗지 배분은 노인네라서.”

“뭐……라고?”

이쯤 되면 왠지 모를 수상함을 느끼는 건 당연지사.

예상을 뒤엎는 내 대답에 중년 도사는 물론, 갑작스럽게 나타난 나와 화룡각 대원들을 주시하던 종남파의 문인들 사이로 보이지 않는 술렁임이 번지던 그때였다.

“사실이다.”

나직한 목소리와 함께 좌우로 갈라지는 인의 파도.

그 너머로 또렷하게 보이는 익숙한 얼굴들을 향해, 나는 사람 좋은 미소를 지어 보였다.

“오랜만에 뵙네요. 두 분 모두.”

반갑게 인사를 건넸지만 되돌아오는 대답은 없었다.

나는 삼 장 밖에서 불현듯 걸음을 멈춘 두 명의 노도사(老道士)를 향해 다시 한번 입을 열었다.

“기체후일, 일…… 야, 이다음이 뭐였지?”

갑작스러운 내 질문을 받은 혁무진이 망설임 없이 대답했다.

“일도양단이요.”

“기체후일도양단. 좀 이상한데. 확실해?”

“아뇨. 사실 저도 잘 모르겠습니다. 생각나는 대로 내뱉은 거라.”

“미친 새낀가. 너 때문에 더 헷갈리잖아.”

“죄송합니다.”

“됐고, 이거 아는 사람?”

말이 끝나기가 무섭게 번쩍 손을 든 주화란이 재빨리 입을 열었다.

“일향만강. 기체후일향만강(氣體候一向萬康)이요.”

“오. 역시 주 소저. 그리핀용봉표국에 십 점.”

“헤헤.”

뭔지도 모르고 쑥스럽게 웃는 주화란에게 엄지를 척 치켜세워 준 나는 두 노도사를 향해 공손히 포권을 취했다.

“아무튼, 예. 두 분 모두 기체후일도양단 하셨습니까.”

“……!”

“……!”

찬물을 뒤집어쓴 듯한 분위기.

뒤늦게 말실수를 깨달은 나는 한숨을 푹 내쉬었다.

듣는 사람에 따라서는 오해할 수도 있지만, 아무튼 말실수 맞다.

“아이 씨, 헷갈렸네. 혁무진.”

“예?”

“대가리 박아.”

“아, 예.”

혁무진이 말안장 위에서 머리를 박는 진기명기를 선보이던 그때, 굳게 닫혀 있던 입술이 마침내 열렸다.

“여전하군. 그 방자하기 짝이 없는 태도는.”

두 명 중 먼저 입을 연 것은 풍성한 백염(白髥)을 지닌 노도사였다.

배꼽까지 늘어트린 새하얀 수염은 그를 마치 현세에 머무르는 신선처럼 보이게 만들었지만, 나는 이미 알고 있다.

눈앞의 노도사, 아니 태을무정검(太乙無情劍) 황보엄이 신선과는 제법 거리가 먼 인물이라는 것을.

‘멀어도 한참 멀지. 겉모습과 속내가 절반이라도 일치했다면 그런 파렴치한 짓은 벌이지 않았을 테니까.’

종남파와 태을무정검의 입장에서는 참으로 안타깝겠지만, 내 기억력은 붕어가 아니다.

저들이 주화란이 이끌던 용봉표국에게 귀하디귀한 천년설삼(千年雪蔘)의 운반을 맡긴 뒤, 뒤로 홀랑 빼내어 배상금을 요구하는 보험 사기 수법으로 용봉표국을 한입에 삼키려던 일은 앞으로도 평생 잊기 힘들 정도였다.

물론, 전적이 화려하기로는 지금 이 순간에도 태을무정검의 옆에서 이리저리 눈을 굴리고 있는 저 영감도 만만치 않았지만.

“누구 찾으시는 분 있습니까?”

“……뭐?”

“누구 찾으시는 분 있냐고 여쭤봤습니다. 송일 대협.”

웃음기 어린 내 질문에, 노호검객(怒號劍客) 송일의 눈썹이 꿈틀거렸다.

지금으로부터 일 년 하고도 수개월 전, 초절정의 무위와 종남파 장로라는 휘황찬란한 배경을 앞세워 태원진가의 잔칫상을 엎으려 했다가 바로 초상집의 주인공이 될 뻔한 그는 불안한 눈빛으로 우리를 훑고 있었다.

종남파고 나발이고, 수틀리면 귀싸대기는 기본이요 쪼인트도 옵션으로 까댈 수 있는 한 사람을 찾기 위해.

그리고 그런 노호검객을 향해, 나는 상냥한 어투로 입을 열었다.

“안심하셔도 됩니다. 찾으시는 분은 지금 이곳에 안 계시니까.”

“……!”

“어, 혹시 제가 잘못 짚은 겁니까? 다른 사람 찾고 계셨어요?”

입을 꾹 다문 채 나를 노려보던 노호검객이 끓어오르는 목소리를 쥐어 짜냈다.

“네놈이 감히…….”

“감히, 뭐?”

내가 한 말이 아니다.

다음 순간, 텅 빈 허공에서 뚝 떨어진 적천강의 모습에 노호검객이 눈을 부릅떴다.

“다, 당신이 어찌!”

“뭐라? 당신?”

“그, 그게 아니고.”

말을 더듬은 노호검객이 뒷걸음질쳤다.

매끈한 민머리에서 어느덧 까슬까슬하게 자라난 적색 머리카락과 중년의 용모.

적천강이 다시 한 번 위대한 경지를 개척하며 젊음을 되찾았다는 소문은 이미 퍼질 대로 퍼졌고, 이는 종남파 역시 예외가 아니었다.

“화, 화왕(火王) 적천강……!”

누군가 반사적으로 내뱉은 한 마디에, 보이지 않는 충격이 좌중을 휩쓸었다.

말로만 듣던 화왕을 직접 목격했다는 것에 한번, 갑자기 나타난 새파란 놈의 정체가 바로 그 열화신룡 진태경이라는 것에 또 다시 한 번.

그리고 그중에서도 특히 믿을 수 없다는 듯한 눈빛으로 나와 적천강을 번갈아 바라보는 노호검객을 향해, 나는 기다렸다는 듯이 두 손을 활짝 펼쳤다.

“짠! 거짓말이었습니다!”

“……!”

“어때요. 깜짝 놀라셨죠?”

간만에 만났는데 이 정도 서프라이즈는 애교지.

헛숨을 삼킨 채 몸까지 파르르 떠는 노호검객의 모습을 보아하니, 확실히 깜짝 놀라긴 한 모양이었다.

놀란 정도가 아니라 경기를 일으키기 직전인 것 같지만.

하지만 노호검객은 제법 운이 좋은 편이었다.

숨이 넘어가기 직전에 맞춰 적절하게 한 사람이 끼어들었으니까.

“종남파의 공 모(某)가, 적 대협을 뵙습니다.”

짧지도, 길지도 않은 애매한 염소수염을 기른 반백의 도사.

다급한 와중에도 공손히 포권지례를 올리는 종남파 장문인의 모습에, 노호검객을 더 갈구지 못한 적천강이 아쉬움의 입맛을 다셨다.

“그래, 오랜만이로군. 자네 이름이 뭐였지? 공필중?”

“필중이 아니라 일중. 공일중입니다, 적 대협.”

“아아, 그래. 기억나는군. 풍운전신 공일중.”

“……풍운검군(風雲劍君)입니다.”

“이것 참. 오늘따라 말이 헛나오는군. 미안하네, 풍운검군 공필중.”

완전히 전의를 상실한 풍운검군 공일중이 고개를 돌려 나를 바라보았다.

이미 반쯤 체념한 그의 눈빛에는 반드시 해결하고 싶은 의문이 담겨 있었다.

- 혹시, 지금 이거 일부러 나 엿 먹이는 건가?

눈빛은 때때로 아주 좋은 대화 수단이다. 나 역시 눈빛으로 대답했다.

- 아뇨. 그냥 원래 그런 분인데요.

이것만큼은 단순한 위로가 아니다.

솔직히 나도, 적천강도 풍운검군한테는 별다른 악감정이 없는 것이 사실이니까.

그의 사형들인 노호검객과 태을무정검에게는 심히 유감스러운 감정이 남아 있지만, 성라대연과 무림맹 창설 당시에나 두어 번 마주쳤던 풍운검군은 그럴 건덕지도 없었다.

당장 노호검객을 한 대 쥐어박을 것 같은 적천강이, 풍운검군한테만큼은 자네라고 칭해 주는 게 그 증거다.

‘뭐, 종남파 장문인에 대한 세간의 평도 썩 나쁘지는 않고.’

괜히 의도치 않게 꼽을 준 것 같아 약간의 미안함을 담아 고개를 젓자, 풍운검군의 한결 마음이 편해진 얼굴로 입을 열었다.

“놀랐습니다. 이런 곳에서 다시 뵙게 될 줄은 몰랐군요.”

“이하 동문일세.”

망설임 없이 대답한 적천강이 숲길을 가득 메운 종남파 제자들을 바라보며 덧붙였다.

“감숙이든 청해든, 이미 어디로든 가 있을 줄 알았거든.”

“…….”

“섬서라면 엎어지면 코 닿을 거린데, 왜 이런 곳에서 자빠져서 쉬고 있었나?”

묵직한 팩트 폭격 보소.

종남파의 명치를 시원하게 들쑤시는 적천강의 한 마디에, 풍운검군의 얼굴이 붉게 달아올랐다.

“그, 그것이…….”

차마 말은 잇지 못하지만, 본능적으로 움직인 시선의 끝에는 정답이 담겨 있다.

노호검객과 태을무정검.

침잠하게 가라앉은 얼굴로 이쪽을 응시하는 두 사람의 모습에, 나는 대강의 전말을 파악할 수 있었다.

‘배 째고 있었구만.’

무슨 이유에선지는 몰라도 저 늙은이들이 종남파의 발길을 붙잡고 있었던 것 같다. 아니, 거의 확실하다.

비교적 최근에도 비슷한 일이 있었던 것을 생각해보면 더더욱 그렇다.

‘그러고 보니까 딱 저 새끼들만 안 왔지.’

얼마 전 산서성에서 혈겁이 벌어졌을 당시, 하북팽가는 물론 화산파와 무림맹 총단에서까지 지원군을 파견했고 때맞춰 도착한 그들 덕분에 완전한 종지부를 찍을 수 있었다.

종남파?

엄밀히 따지자면, 오긴 왔다.

전투가 끝난 지 하루가 지난 후에야.

물론 딴에는 어느 정도의 위험을 무릅쓰고 지원군을 파견해 줬으니 고마운 일이지만, 내심 기분이 더러운 것도 사실이었다.

‘일천의 병력을 파견했다더니 산서성에 도착한 머릿수는 삼백. 그중 절반 이상이 별 볼 일 없는 어중이떠중이들. 심지어 그마저도 지각.’

이 삼 박자가 기가 막히게 어우러지니, 뱃속 깊숙한 곳에서 좆 같음이 스멀스멀 올라오는 것은 당연지사.

거기에 더해 두 번 다시 마주치기 싫은 얼굴을 둘이나 보고 있자니 입술이 저절로 움직였다.

“뭐, 그럴 수도 있죠. 아프신 몸을 이끌고 가는 것만으로도 훌륭한 의기의 표상이십니다.”

정확히 표적을 겨냥한 내 말에, 노호검객과 태을무정검의 눈살이 찌푸려진 그 순간이었다.

“놈! 입방정 떨지 말라 그리 일렀거늘.”

준엄한 목소리로 나를 꾸짖은 적천강이 말을 이었다.

“피오줌 질질 싸질러 가며 여기까지 온 것만으로도 협객이나 다름없다. 이제야 겨우 나잇값 하려는 무림의 대선배들에게 그 무슨 무례한 말버릇이냐!”

“……!”

“……!”

“대관절 저들이 무엇을 그리 잘못했느냐! 배경이나 앞세워 힘없는 문파를 봉문(封門) 시키려 했느냐, 아니면 천년설삼을 빼돌려 멀쩡한 표국 하나를 집어삼키려 했느냐!”

한 마디, 한 마디가 뼈와 살을 분리시키는 혀왕의 잔혹한 손속에 풍운검군이 간신히 목소리를 쥐어짜 냈다.

“그, 적 대협. 부디 저와 제 스승님의 얼굴을 봐서라도…….”

“알겠네. 내 이쯤에서 그만하도록 하지.”

“감사합니다.”

“감사는 무슨. 그럴 필요 없네, 풍운검군 공필중.”

“…….”

아주 살벌하다. 살벌해.
```

## Final English reading copy

```markdown
# Chapter 999

When I’d just entered the workforce and started out as a Hunter, the veteran Hunters with years under their belts had a saying they repeated like a mantra.

“You never know when or where your paths might cross again. That’s what connections between people are.”

“So whenever you make or break a connection with someone, you’ve got to be careful and flexible. That way, you won’t regret it later.”

Looking back now, I don’t think I’ve ever heard advice that proved more valuable.

The only problem is that advice like that doesn’t mean a damn thing to a guy like me.

“I think there’s a typo…”

The four characters embroidered in ornate silk read **The Great Zhongnan Sect**. The moment I read them, the words slipped out before I could stop myself.

The nearest Daoist frowned.

“Friend, what did you just say?”

“Oh, nothing. Just talking to myself.”

“Talking to yourself?”

“Yeah.”

“You’re awfully casual.”

“Yeah, sir.”

The middle-aged Daoist stared at me, momentarily dumbfounded, then took a breath and finally managed to ask,

“What are you trying to do?”

“You called me your friend, so I spoke casually. Besides, you were the one who started talking casually to me.”

“You appear to be a fellow martial artist, but you’re young enough to be my junior. You really don’t hold back, do you?”

“I can get away with it. I might be young, but in martial seniority I’m an old man.”

“What… did you say?”

At this point, it was only natural for him to sense something was amiss.

My unexpected answer had thrown him off, and an invisible stir rippled through the Zhongnan Sect Disciples watching me and the Fire Dragon Pavilion members who’d suddenly appeared.

“It’s true.”

A low voice rang out as the crowd parted to either side like a wave.

I smiled warmly at the familiar faces clearly visible beyond them.

“It’s been a while. Both of you.”

I greeted them cheerfully, but neither replied.

I spoke again to the two old Daoists who’d abruptly stopped three jang away.

“May your health be… um… what comes after that?”

Hyuk Mujin answered without hesitation.

“May you be split in two.”

“May your health be split in two. That sounds a little off. Are you sure?”

“No. I’m not really sure either. I just said the first thing that came to mind.”

“Are you insane? Now I’m even more confused.”

“I’m sorry.”

“Whatever. Anybody know the right one?”

Ju Hwaran shot her hand up and quickly answered,

“May you be healthy in every way. May your health be sound in every respect.”

“Oh! As expected of Young Lady Ju. Ten points to the Griffin Yongbong Escort Bureau.”

“Hehe.”

I gave the bashfully smiling Ju Hwaran a thumbs-up, though she had no idea what I meant, then respectfully clasped my hands toward the two old Daoists.

“Anyway, yes. I hope you’ve both been split in two.”

“……!”

“……!”

The mood turned as cold as if someone had dumped a bucket of water over us.

Realizing belatedly that I’d misspoken, I let out a deep sigh.

Depending on who heard it, they might take it the wrong way—but yes, it was a slip of the tongue.

“Damn it, I got mixed up. Hyuk Mujin.”

“Yes?”

“Get down and put your head on the ground.”

“Ah, yes.”

Just then, as Hyuk Mujin performed the amazing feat of bowing his head down to his horse’s back, one of the two finally opened his tightly sealed lips.

“You haven’t changed. Still as brazen as ever.”

The first to speak was the old Daoist with a luxuriant white beard.

His snow-white beard hung down to his navel, making him look like an immortal who’d descended to the mortal world. But I already knew better.

The old Daoist before me—no, Hwangbo Eom, the Taeeul Merciless Sword—was about as far from an immortal as you could get.

*And then some. If his inner self matched his appearance even halfway, he never would’ve pulled such a shameless stunt.*

The Zhongnan Sect and the Taeeul Merciless Sword might find it unfortunate, but my memory wasn’t that of a goldfish.

They’d entrusted Ju Hwaran’s Yongbong Escort Bureau with transporting their priceless Thousand-Year Snow Ginseng, then secretly stolen it back and demanded compensation—an insurance scam meant to swallow the Bureau whole. That was the sort of thing I’d never forget as long as I lived.

Of course, the old man standing beside the Taeeul Merciless Sword, looking this way and that, wasn’t far behind when it came to having a colorful record of his own.

“Are you looking for someone?”

“……What?”

“I asked if you were looking for someone, Great Hero Song Il.”

At my amused question, the Roaring Fury Swordsman’s eyebrows twitched.

A year and several months ago, he’d tried to overturn the banquet table of the Jin Family of Taiyuan, flaunting his Supreme Peak martial prowess and his illustrious position as an Elder of the Zhongnan Sect. He’d very nearly ended up being the one everyone mourned at a funeral instead. Now he was anxiously scanning us, searching for one person.

A man who, to hell with the Zhongnan Sect or anything else, would dish out a slap across the face as a matter of course—and kick you in the shins for good measure—if he took a dislike to you.

I spoke gently to the Roaring Fury Swordsman.

“You can relax. The person you’re looking for isn’t here.”

“……!”

“Or did I get it wrong? Were you looking for someone else?”

The Roaring Fury Swordsman had kept his mouth shut, glaring at me. Now he squeezed out a voice boiling with anger.

“You dare—”

“Dare to what?”

That wasn’t me speaking.

A moment later, Jeok Cheongang dropped out of empty air, and the Roaring Fury Swordsman’s eyes went wide.

“H-How can you be here?”

“What? ‘You’?”

“N-No, that’s not what I meant.”

The Roaring Fury Swordsman stammered and stepped backward.

Jeok Cheongang’s smooth bald head now sported a bristly crop of red hair, and his face had regained the appearance of a middle-aged man.

The rumor that Jeok Cheongang had reached another extraordinary realm and regained his youth had spread far and wide. The Zhongnan Sect was no exception.

“F-Fire King Jeok Cheongang…!”

At someone’s involuntary exclamation, an invisible shock swept through the crowd.

First, they were seeing the Fire King in person after hearing about him for so long. Then they realized that the young upstart who’d suddenly appeared was none other than the Blazing Flame Divine Dragon, Jin Taekyung.

And in particular, the Roaring Fury Swordsman kept glancing between Jeok Cheongang and me, looking utterly disbelieving.

I spread both arms wide, as if I’d been waiting for the moment.

“Ta-da! I was lying!”

“……!”

“What do you think? Did I scare you?”

We hadn’t seen each other in ages. A little surprise was only fair.

Judging by the Roaring Fury Swordsman’s trembling body and the sharp breath he’d sucked in, I’d definitely startled him.

Not just startled him, actually. He looked like he was about to have a fit.

Still, the Roaring Fury Swordsman was fairly lucky.

Someone cut in just as he was about to keel over.

“This humble Gong of the Zhongnan Sect pays his respects to Great Hero Jeok.”

The Zhongnan Sect’s Sect Leader, a Daoist with a half-white beard of an awkward, in-between length, respectfully clasped his hands despite the urgency of the moment.

Jeok Cheongang, who’d been just about to keep giving the Roaring Fury Swordsman a hard time, clicked his tongue in disappointment.

“Well, it’s been a while. What was your name again? Gong Piljung?”

“Not Piljung. Iljung. I’m Gong Iljung, Great Hero Jeok.”

“Ah, right. I remember now. Wind-and-Cloud War God Gong Iljung.”

“……Wind-and-Cloud Sword Lord.”

“Good grief. I keep getting my words mixed up today. Sorry about that, Wind-and-Cloud Sword Lord Gong Piljung.”

Having completely lost the will to fight, the Wind-and-Cloud Sword Lord Gong Iljung turned to look at me.

His eyes, already half resigned to his fate, held a question he clearly wanted answered.

*Are you doing this on purpose to mess with me?*

Eyes are sometimes an excellent way to communicate. I answered with my own.

*No. He’s just like that.*

That wasn’t just empty reassurance.

Honestly, neither Jeok Cheongang nor I had any particular grudge against the Wind-and-Cloud Sword Lord.

We had plenty of grievances against his Senior Brothers, the Roaring Fury Swordsman and the Taeeul Merciless Sword. But the Wind-and-Cloud Sword Lord? We’d only crossed paths a couple of times, at the Star-Array Grand Banquet and when the Murim Alliance was founded. We had no real reason to hold anything against him.

The proof was right there: Jeok Cheongang, who looked ready to punch the Roaring Fury Swordsman, was calling the Wind-and-Cloud Sword Lord “you” in a friendly way.

*Besides, people don’t have much bad to say about the Zhongnan Sect’s Sect Leader.*

Feeling a little sorry for having insulted him unintentionally, I shook my head. The Wind-and-Cloud Sword Lord looked considerably more at ease and spoke.

“I’m surprised. I didn’t expect to see you here again.”

“Likewise.”

Jeok Cheongang answered without hesitation, then looked over the Zhongnan Sect Disciples filling the forest path and added,

“I figured you’d be in Gansu or Qinghai by now.”

“……”

“Shaanxi’s just a stone’s throw away. Why are you sprawled out resting in a place like this?”

That was a heavyweight fact bomb.

Jeok Cheongang’s words drove straight into the Zhongnan Sect’s gut, and the Wind-and-Cloud Sword Lord’s face flushed red.

“W-Well…”

He couldn’t bring himself to finish, but his gaze shifted instinctively toward the answer.

The Roaring Fury Swordsman and the Taeeul Merciless Sword.

Their faces had gone dark as they watched us, and I could piece together most of what had happened.

*They’d dug in their heels and dared anyone to do something about it.*

For some reason, those old bastards seemed to have been holding the Zhongnan Sect back from moving. Actually, I was almost certain of it.

Especially since something similar had happened fairly recently.

*Come to think of it, those two were the only ones who didn’t show up.*

When the bloodshed erupted in Shanxi Province a little while ago, the Hebei Peng Family, Huashan, and even the Murim Alliance Headquarters had sent reinforcements. Thanks to them arriving in time, we’d been able to bring things to a complete close.

The Zhongnan Sect?

Strictly speaking, they did come.

A day after the battle was over.

Of course, we were grateful they’d sent reinforcements and taken a certain degree of risk to do it. But I couldn’t deny that it had left a bad taste in my mouth.

*They said they’d sent a thousand troops, but only three hundred made it to Shanxi Province. More than half were nobodies. And even they were late.*

With all three things fitting together so perfectly, it was only natural for the feeling of *this is such bullshit* to start creeping up from deep in my gut.

And seeing two faces I never wanted to see again only made my lips move on their own.

“Well, it happens. Just making the journey while you’re unwell is a fine display of righteous spirit.”

The moment I aimed the remark squarely at my targets, the Roaring Fury Swordsman and the Taeeul Merciless Sword frowned.

“You brat! I’ve told you not to flap your mouth!”

Jeok Cheongang scolded me in a stern voice, then continued,

“Just making it this far while pissing blood all the way here makes you heroes! These great seniors of the Murim are only now beginning to act their age after all this time. How can you speak to them so rudely?”

“……!”

“……!”

“Now then, what have they done so wrong? Did they use their influence to force a weaker sect to close its doors? Or did they steal a Thousand-Year Snow Ginseng and try to swallow a perfectly innocent Escort Bureau whole?”

With each word, the merciless Tongue King’s verbal blows seemed to separate flesh from bone. The Wind-and-Cloud Sword Lord struggled to squeeze out a voice.

“G-Great Hero Jeok, please, for my sake and my Master’s…”

“All right. I’ll stop here.”

“Thank you.”

“No need to thank me, Wind-and-Cloud Sword Lord Gong Piljung.”

“……”

This was vicious. Absolutely vicious.
```

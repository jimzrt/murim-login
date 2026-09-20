<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0551.txt",
      "sha256": "5bfe5d65f740883d357b03939cf575d2a0c8d09e1394b2b2a406de3575958363",
      "bytes": 14018
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3bc4d9f8e60e979505a07af598928ff44891e066557a2a4d8496238b262e426a",
      "bytes": 3386
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8f5da66569a6ad674a557886cf6911e213f5ede53dd7180d8fb02515c8a52244",
      "bytes": 174793
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "a1fd7288f1db4d17a4a72bbd18ed230723f62fadf7032fac079010dd9f8de82c",
      "bytes": 1325
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "919284f89814c1b143e61a1cd30f2a370dac17569556f6289d4f1566c062cbc8",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c4ce9da3470d2b8556f7f52f467c12ce77f312eb0a9fa26c74718471a6de1f65",
      "bytes": 1147
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2fe95a9f0433e7ce841c957c3e94e4b9b3304f36bf3315f060a7070b47d4fca8",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1d865551bc1eb84c31070a6621299285b47408dbc2005621442b062056425bb0",
      "bytes": 2292
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "dfc6ce292694fcf30be00bb19402226d366dbe59f9e48ec888bb62a70038e4b5",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "9da69000a7021a550b65830325a1553339540d946b9c330d9f672718acaa2a55",
      "bytes": 959
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "9bf8424099c8af2fc53cc225b5b6fc161efd44e2c108921501a9c6d751d40b57",
      "bytes": 1061
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "62b905f6735b0c0e5ebbcff82e5d8edc43fb4e6f393af69cceef1fc2c0ed7072",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "964a5eeb65fdb561c3dbf9c35ef1c3ebb950db971e03d6e87cc4fd6ae66855f1",
      "bytes": 751
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "dd1d2b9c418f2c821eb88054ddfdd843c0e7d27508b55c7b7f19a8282ed1ea64",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "da7a0f36d3644731f927d26a782ad3b0419a695ed924eea713365e0f9cb3d704",
      "bytes": 165874
    }
  ],
  "estimated_tokens": 14252
}
-->

# Durable State Update — Chapter 551

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 551. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 551. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 551,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 551,
    "continuity_sources": [551],
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
    "The Fire Dragon Pavilion's first mission is to enter Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can't Go to Nanman.",
    "The six-member Fire Dragon Pavilion is preparing to leave Henan; Song Ilseom has arrived in disguise with discreet transport arranged by Ju Hwaran within half a shichen.",
    "Jeok Cheongang remains in Henan while Taekyung and the other pavilion members depart because the crisis requires more hands.",
    "Cheongpung is accompanying Mungyeong and learning his martial arts through observation to become stronger and adapt to this world.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven's second rift, with a successful attack potentially spreading chaos through Yunnan, Guizhou, Guangxi, and Sichuan.",
    "The Mount Song Resolution restored the Murim Alliance; Mae Jonghak is Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi oversees Murong Family defenses in Liaoning.",
    "Jin Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, and public S-rank-level recognition while retaining an A-rank license.",
    "Cheongpung is master of the Azure Dragon Pavilion, creator of Mimi Step, and caretaker of Mimi, whose condition was examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo processes the Water God Dragon's remains.",
    "Dark Heaven remains an enormous monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days."
  ],
  "continuity_sources": [
    550,
    549
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?"
  ],
  "safe_through": 550,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can't Go to Nanman.",
    "Preserve Taekyung's blunt profanity and financial, monster, no-kids-zone, and P-King humor, along with Taishan's clipped childlike speech.",
    "Render 폰의생 as fake physician and preserve Mungyeong's dry, threatening voice."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 로그아웃             | **Logout**                     |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 낙양 | **Luoyang** | Historic city in Henan Province and the chapter’s setting. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 여아홍 | **Yeoahong** | Traditional Chinese rice wine; literally Daughter's Red. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 맹주전 | **Alliance Leader's Hall** | Hall directly associated with the Murim Alliance Leader. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 대별산 | **Mount Daebyeol** | Secondary meeting point for the departing party. |

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
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 550
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, a Supreme Peak martial master known as the Huashan Divine Dragon, the creator of the snake-inspired Mimi Step footwork technique, and the master of the Azure Dragon Pavilion within the Alliance Leader's Two Dragons Pavilion.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi, now a large horned snake, to him, and Cheongpung is accompanying Mungyeong while learning his martial arts through observation to become stronger and adapt to this world.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 547
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 550
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 550
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 550
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master and leading its first mission to Nanman.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 550
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 550
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 550
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 550
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 550
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 549
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃551화



여섯 명의 젊은 남녀가 은밀하게 하남을 빠져나가던 그 날 밤. 두 사람은 달빛이 내리쬐는 정자에서 술잔을 부딪쳤다.

쨍.

티 없이 맑은 소리와 함께 꺾이는 술잔. 단숨에 술을 입안으로 털어 넣은 화왕(火王) 적천강이 나직이 뇌까렸다.

“오늘따라 술맛이 별로군.”

맞은편에 앉아 있던 매종학이 빙긋 웃었다.

“여아홍(女兒紅)이 입에 맞지 않으신 모양이오.”

“모르겠소. 아까부터 목이 칼칼하고 혀가 쓴데, 혹시 술에 독이라도 탄 것 아니오?

다른 사람은 농담 삼아서라도 절대 할 수 없는 말이다.

그야말로 적천강이기에 가능한 말이었고, 그 상대가 매종학이라 웃고 넘어갈 수 있는 이야기였다.

“내가 적 대협을 독살하다니. 그럴 리가 있겠소. 다만 나중에 한 번 시도는 해 보리다.”

“잘 알아보고 쓰시오. 이제는 무형지독(無形至毒)도 견딜 자신이 생겼으니까.”

“오. 그럼 무림맹의 총력을 기울여서라도 알아보겠소.”

적천강이 불퉁하게 대꾸했다.

“겁나는군. 누가 들으면 진심인 줄 알겠소.”

“아, 농이었소? 난 또.”

“……?”

설마?

이제야 깨달았다는 듯이 고개를 끄덕이는 매종학의 모습에, 적천강은 간담이 서늘해졌다.

‘이런 정신 나간 늙은이를 봤나.’

겉모습만 젊어졌을 뿐, 제정신이 아닌 부분에서는 사십여 년 전이나 지금이나 똑같다.

하긴, 굳이 멀리 갈 필요도 없이 청풍 그놈만 봐도 알 수 있는 사실이었다.

‘콩 심은 데 콩 난다고, 하여간 스승이나 제자나…….’

그 순간, 술잔을 채우던 적천강의 손길이 덜컥 흔들렸다.

‘제자라.’

촤악. 한가득 흘러넘친 술 위로 씁쓸한 표정을 짓고 있는 어느 중년인의 얼굴이 비친다.

익숙하면서도 아직은 낯선 자신의 모습을 물끄러미 바라보던 적천강이 불쑥 입을 열었다.

“아무 일도 없겠지. 그렇지 않소?”

매종학이 자신의 술잔을 채우며 되물었다.

“걱정되시오?”

“걱정은 무슨! 사내가 약관이 넘었으면 응당 제 갈 길을 가야지. 일가(一家)를 이루어도 이상하지 않을 나이인데.”

애써 큰소리를 쳤지만 적천강의 입맛은 여전히 쓰기만 했다. 지금쯤이면 남쪽을 향해 떠나고 있을, 누군가의 얼굴이 생각나서였다.

그리고 그런 그의 얼굴 위로 얼핏 스쳐 지나간 감정을, 매종학은 놓치지 않았다.

“멀리 못 갔을 거요.”

흘리듯 건넨 말에, 적천강이 씁쓸하게 대꾸했다.

“……이미 인사는 나눴거늘, 다시 마주하면 뭣 하겠소. 발길만 무거울 뿐이지.”

“듣고 보니 그렇구려.”

“그래서, 대답은?”

“음? 뭘 말이오?”

“이 양반이 맹주가 되더니 귀가 막혔나. 그…… 아까 물어본 것 있지 않소.”

술잔을 만지작거리던 적천강이 조심스럽게 말을 이었다.

“아무 일도 없을 거요. 그렇지?”

잠시 뭔가를 생각하던 매종학이 대답했다.

“그럴 수도 있고, 아닐 수도 있소.”

“……그걸 지금 말이라고 하는 거요?”

“일단 말은 맞소. 지금 막 내 입으로 한 말이니.”

“염병할. 미치고 환장하겠네. 그런 대답은 누구든 할 수 있는 거 아니오?”

“어라. 그것도 그렇구려.”

“그럼 무림 맹주로서 적절한 대답을 찾아보라고. 적절한 대답을!”

벌컥 역정을 내는 적천강의 모습에, 매종학이 빙긋 웃었다.

“그는 잘 해낼 거요. 지금까지 늘 그래 왔듯이.”

“그 말, 진심이오?”

“물론. 믿음이 없었다면 왜 화룡각에 그런 막중한 임무를 맡겼겠소.”

적천강이 한결 누그러진 목소리로 입을 열었다.

“혹, 만약의 상황을 위한 대비책도 마련해 둔 거요?”

“은영각의 눈과 귀는 천하 곳곳에 있소. 남만(南蠻)도 예외는 아니지.”

“……!”

“화룡각을 남만으로 보낸 것은 가장 빠르고 확실한 방법이기 때문이오. 당장 일군(一軍)을 일으키기에는 시일이 촉박하니.”

현재 무림맹의 규모는 과거 정마대전 때와 비교해도 결코 작지 않았다. 아니, 오히려 그 이상이라 해도 과언이 아니다.

소림사와 사천문을 비롯한 몇몇 문파가 큰 피해를 입긴 했으나, 아직 정파의 영역이라 할 수 있는 구주(九州)에 속한 어느 성도 무너지지 않았으니까.

문제는 병력을 소집하고, 남만으로 보내는 데까지 걸리는 시간과 물자였다.

그리고 진태경이 이끄는 화룡각이야말로 무림맹이 자신 있게 내밀 수 있는 몇 안 되는 패라고 할 수 있었다.

“으음.”

하지만 어떤 말을 들어도 적천강의 근심은 사라지지 않았다.

말없이 술잔만 노려보는 그에게, 매종학이 개미만 한 목소리로 중얼거렸다.

“가장 확실한 지원이 있긴 한데.”

“응? 지금 뭐라 했소?”

“별것 아니오. 그냥 혼잣말이었소.”

“감히 누굴 속이려고! 분명 뭐라 하는 것을 이 귀로 똑똑히 들었거늘!”

“고정하시고 마저 술이나 드시오. 그럼 내 생각해 보리다.”

매종학을 빤히 응시하던 적천강이 투덜거렸다.

“맛도 없는 술을 뭘 자꾸 먹이려고.”

“적 대협.”

“왜 그러시오.”

퉁명스럽게 대꾸하는 적천강을, 매종학이 그윽한 눈빛으로 응시했다.

“그 맛 없는 술을, 이미 다섯 동이나 드셨소.”

“…….”

“지금 마시고 있는 게 여섯 동이째요.”

“…….”

“우선 마십시다.”

조용히 입을 다문 적천강이 술잔을 기울였다.

향긋한 주향과 함께 목을 타고 넘어가는 술이, 말했던 것만큼 쓰지 않았다. 술잔과 함께 뒤로 젖혀진 그의 얼굴에 은은한 달빛이 닿았다.

‘저 아래쯤 어디에 있으려나.’

무정한 놈. 그래도 떠나기 전 얼굴 한 번 정도는 비춰 주지.

마음속에서 들려온 중얼거림은, 이내 어디선가 불어온 함께 흩어졌다.



* * *



다그닥. 다그닥.

나이든 말의 발걸음은 느렸고, 전신을 빈틈없이 감싼 볏짚은 차갑고 따가웠다.

마차 밖에서는 호객하는 장사치들과 사람들의 목소리가 천천히 멀어지고 있었다.

‘빠져나왔나?’

그런 생각이 뇌리에 떠오른 순간. 누군가의 속삭임이 귓가를 파고들었다.

“조장님. 똥 마려워요.”

“…….”

혁무진 이 미친놈은 여기서까지 염병하고 자빠졌네.

지금은 최대한 움직임을 줄여야 하기에 무력 진압도 불가능한 상황. 나는 한껏 목소리를 죽여 윽박질렀다.

“미친놈아. 내가 미리 싸랬지.”

“긴장해서 그래요. 긴장해서.”

“그럼 참아, 시벌 놈아.”

“왜 욕을 하고 그러세요? 무슨 말을 못 하겠네.”

“욕이 안 나오게 생겼냐, 지금? 여기서 싸면 냄새는 어쩔래?”

이불 덮고 방귀만 뀌어도 욕이 나오는데, 함께 볏짚에 파묻혀 있는 상황에서 그런 불상사가 벌어지는 건 죽어도 거부하고 싶다.

“안 그래도 제가 생각을 해 봤는데요. 차라리 그냥 싸 버리면 냄새가 나서 검문도 쉽게 통과하지 않을까요?”

“죽어. 제발 죽어.”

“죄송합니다. 참을 만큼 참았는데 안 될 것 같아요. 전 여기까지인가 봐요.”

“야, 무진아. 잠깐만. 잠깐만 기다려 봐.”

“죄는 나중에 달게 받겠습니다.”

안 돼! 개새끼야!

공포에 질린 내가 위장이고 나발이고 벌떡 일어나려던 그 순간이었다.

“낙양(洛陽)의 중심거리를 지났어요. 인적도 없는 산길이니 잠깐 나오셔도 좋아요.”

“허억!”

“푸하!”

파사삭!

볏짚을 뚫고 튀어나온 혁무진이 풀숲을 향해 냅다 뛰어간다. 벼랑 끝에서 목숨을 건진 나는 구원자를 향해 연거푸 고개를 숙였다.

“감사합니다. 착하게 살겠습니다. 정말 감사합니다.”

“검문에 시간이 걸려서 그런지, 혁 소협이 많이 급했나 보네요. 늦지 않아서 다행이에요.”

익숙한 목소리. 그러나 싱긋 웃는 여인의 얼굴은 낯설었다.

높게 솟은 나뭇가지 사이로 쏟아지는 달빛 아래, 양 볼에 가득한 주근깨와 푸석푸석한 피부가 유난히 눈에 띄었다.

‘봐도 봐도 신기하네.’

이목구비와 사소한 부분이 바뀌었을 뿐인데, 그것만으로도 인상이 확 달라지다니.

내 시선을 눈치챈 여인, 주화란이 자신의 얼굴을 매만졌다.

“아, 제가 조금 변하긴 했죠?”

“네. 그래도 눈은 여전한데요?”

아름다운 검푸른 눈동자에 웃음이 스쳤다.

“그건 면구(面具)로 어떻게 할 수 있는 부분이 아니라서요. 그나마 송 당주가 아니었다면 당장 이 정도의 면구를 구하기 힘들었을 거예요.”

마부석에 앉아 있던 송일섬이 덤덤하게 덧붙였다.

“별것 아니오. 살려고 익힌 잡기(雜器) 정도지.”

“잡기치고는 훌륭한데?”

“어차피 빈말이겠지만, 우선 칭찬은 고맙다고 해 두지.”

저놈도 어지간히 삐딱한 놈이다. 진심이었는데.

완전 다른 사람이 된 주화란의 얼굴은 송일섬의 솜씨였다.

일찍이 밑바닥부터 산전수전 겪으며 살아온 놈이라는 것 정도는 알고 있었지만, 면구 제작법까지 익혔을 줄은 몰랐다.

‘생각보다 쓸모가 많은 놈인데?’

낭인 생활을 하며 터득한 여러 가지 경험도 앞으로의 길에 있어 큰 도움이 될 것이 분명하다.

내심 송일섬에 대해 감탄하던 나는 문득 드는 생각에 눈을 크게 떴다.

“잠깐. 그런데 왜 내 건 없어?”

면구가 있었다면 언제 터질지 모르는 시한 똥폭탄을 옆에 두고 짐처럼 실려 갈 이유가 없는 것 아닌가.

억울함을 성토하는 내 모습에 송일섬이 혀를 찼다.

“사람마다 이목구비가 다르니 틀을 잡는 데에만 며칠이 걸리는 것이 면구다. 그런데 어떻게 그 촉박한 시간 동안 네놈 것까지 만들란 말이냐? 오히려 어색한 면구를 착용하면 역효과만 날 뿐이야. 정 억울하면 역용술(易容術)을 익혔어야지.”

볼일을 마치고 세상 시원한 표정으로 풀숲을 빠져나온 혁무진이 끼어들었다.

“그럼 주 소저는요? 며칠씩 걸린다면서요.”

“소국주의 면구는…….”

말꼬리를 흐린 송일섬이 문득 미간을 찌푸렸다.

“쓸데없는 이야기로군. 닥치고 도로 볏짚 속에 파묻혀라. 면전에서 똥 냄새 풍기지 말고.”

“지도 똥 싸는 주제에 되게 뭐라고 하네…….”

궁시렁거리며 볏짚 속으로 기어들어 가는 혁무진의 모습을 노려본 송일섬이 내게 물었다.

“베도 되나?”

“안 돼.”

단호하게 대답한 내가 주화란을 향해 물었다.

“지금쯤이면 다른 놈들도 빠져나왔겠죠?”

다른 놈들이 누구를 가리키는지 모를 주화란이 아니다. 그녀가 작게 고개를 끄덕였다.

“아마도요. 검문이 가장 취약한 서문(西門)으로 향했으니, 이미 저희보다 먼저 낙양을 벗어났을 거예요.”

태산의 덩치가 이만저만이 아니라 걱정이 되긴 하지만, 주화란의 조치는 그리 허술하지도 않으며 우리의 뒤에는 맹주전과 은영각이 있으니 안심해도 괜찮을 거다.

파삭.

볏짚 사이로 고개를 쏙 내민 혁무진이 물었다.

“그럼 이대로 곧장 대별산(大別山)까지 가는 겁니까?”

“물론이에요. 중간에 말을 한 번 바꾸긴 하겠지만, 그전까지는 아무 일 없을 거고요.”

주화란이 막힘없이 말을 이었다.

“멈추지 않고 이동한다면 두 시진. 만약 철저한 검문이 이뤄진다는 가정 하에는 세 시진까지도 걸리겠죠. 다른 두 사람과는 대별산에서 합류한 뒤…….”

“곧장 하남을 빠져나간다. 맞습니까?”

주화란이 싱긋 웃으며 고개를 끄덕였다.

“각주님께서 말씀하신 그대로예요.”

“……각주님?”

“왜요. 이 호칭이 맞지 않나요?”

따지고 보면 맞는 호칭이긴 한데, 몸에 맞지 않는 옷을 입은 것처럼 어색하다.

입맛을 다신 나는 고개를 끄덕였다.

“뭐, 그건 그렇다 치고. 그럼 대별산까지는 별문제 없는 겁니까?”

“그럼요. 한숨 푹 주무시고 일어나셔도 될 거예요.”

무림맹의 근거지인 하남이니, 적이 습격해 올 가능성은 전무하다고 해도 과언이 아니다.

하지만 나는 긍정도 부정도 아닌, 모호한 표정으로 피식 웃어 보였다.

“왜 그러세요?”

“아닙니다. 아무것도.”

이걸 뭐라고 해야 하나. 나는 짧은 생각 끝에 말을 이었다.

“그냥. 오랜만에 꿈을 꾼다고 생각하니까 기분이 이상해서요.”

“꿈이요?”

“네. 가끔 꿈을 꾸거든요. 누가 업어 가도 모를 만큼 깊게.”

아리송한 대답에 주화란은 의아한 표정을 지었고, 송일섬은 무슨 헛소리냐는 듯 미간을 찌푸렸다.

그리고 두 사람의 반응을 뒤로한 나는, 짐칸에 쌓인 볏짚들 깊숙이 몸을 묻었다.

‘대별산까지 빠르면 두 시진. 시간은 충분해.’

지금부터는, 아주 오랫동안 미뤄두었던 꿈을 꿀 시간이다.

‘로그아웃.’

띠링.

맑은 종소리와 함께, 또렷했던 의식이 천천히 가라앉기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 551

On the night six young men and women secretly slipped out of Henan, two men clinked their wine cups together in a moonlit pavilion.

*Clink.*

The cups tipped with a clear, spotless chime. After draining his drink in one go, Fire King Jeok Cheongang muttered,

“This wine tastes worse than usual.”

Mae Jonghak, seated across from him, smiled faintly.

“It seems Yeoahong[^1] is not to your taste.”

“I don’t know. My throat’s been scratchy and my tongue bitter for a while now. You haven’t poisoned the wine, have you?”

It was something no one else could have said, even as a joke.

It was only possible because he was Jeok Cheongang—and because the person sitting across from him was Mae Jonghak, who could laugh it off.

“Me, poison Great Hero Jeok? Surely not. Though I may give it a try sometime.”

“Do your research before you use it. I’m confident I can withstand even Formless Ultimate Poison now.”

“Oh. Then I’ll make sure to investigate it thoroughly, even if I have to devote the full strength of the Murim Alliance.”

Jeok Cheongang answered gruffly.

“How frightening. Anyone listening might think you were serious.”

“Oh, that was a joke? And here I thought…”

“...?”

*Surely not.*

Mae Jonghak nodded as though he had only just realized the truth, and a chill ran down Jeok Cheongang’s spine.

*What a lunatic old man.*

His appearance had become younger, but in terms of sanity, he was exactly the same as he had been forty years ago.

Then again, he did not have to look far for proof. Cheongpung alone made it obvious.

*Like father, like son. The master and his Disciple are both...*

At that moment, Jeok Cheongang’s hand shook as he filled his cup.

*Disciple.*

Splash.

The face of a middle-aged man wearing a bitter expression appeared in the wine that had spilled over the brim.

Jeok Cheongang gazed at his own face, familiar yet still strange, then abruptly opened his mouth.

“Nothing will happen, right?”

Mae Jonghak filled his own cup and asked in return,

“Are you worried?”

“Worried about what? Once a man is past twenty, he should follow his own path. He’s old enough to start a family.”

He put on a bold front, but the bitterness remained on Jeok Cheongang’s tongue. He had thought of the face of someone who must be heading south by now.

Mae Jonghak did not miss the emotion that briefly crossed his face.

“He can’t have gone far.”

At those casually spoken words, Jeok Cheongang answered bitterly,

“Even though we already said our goodbyes, what would be the point of seeing him again? It would only make it harder to leave.”

“Now that you mention it, I suppose you’re right.”

“So? What’s your answer?”

“Hm? To what?”

“This old man became Alliance Leader and lost his hearing. You know... what I asked earlier.”

Jeok Cheongang toyed with his cup before continuing carefully.

“Nothing will happen. Right?”

Mae Jonghak thought for a moment before answering.

“It might. Or it might not.”

“…And you call that something to say?”

“Well, it was something I said. It just came out of my mouth.”

“Damn it. This is driving me insane. Anyone could give an answer like that!”

“Oh. I suppose that’s true as well.”

“Then find an appropriate answer as the Murim Alliance Leader. An appropriate answer!”

As Jeok Cheongang flew into a rage, Mae Jonghak smiled faintly.

“He’ll do fine. Just as he always has.”

“Do you mean that?”

“Of course. If I didn’t have faith in him, why would I have entrusted such an important mission to the Fire Dragon Pavilion?”

Jeok Cheongang spoke again, his voice somewhat calmer.

“Did you also prepare a contingency plan, in case something happens?”

“The Hidden Shadow Pavilion has eyes and ears throughout the realm. Nanman is no exception.”

“...!”

“Sending the Fire Dragon Pavilion to Nanman is the fastest and most reliable option. We don’t have enough time to raise an army right now.”

The Murim Alliance was not small by any measure, even compared with its size during the Great Faction War. In fact, it would not be an exaggeration to say it was larger now.

Although Shaolin Temple, the Sichuan Sect, and several other sects had suffered heavy losses, none of the provinces within the Nine Provinces—the territory still held by the orthodox faction—had fallen.

The problem was the time and supplies required to gather troops and send them to Nanman.

And the Fire Dragon Pavilion, led by Jin Taekyung, was one of the few cards the Murim Alliance could confidently play.

“Hmm.”

But no matter what Mae Jonghak said, Jeok Cheongang’s worry did not fade.

As Jeok Cheongang silently glared at his wine cup, Mae Jonghak muttered in a voice as tiny as an ant’s.

“There is one especially reliable source of support.”

“Hm? What did you say?”

“It was nothing. I was just talking to myself.”

“You think you can fool me? I heard you say something clearly with these ears!”

“Calm down and finish your drink. Then I’ll give it some thought.”

Jeok Cheongang stared at Mae Jonghak and grumbled,

“Why do you keep trying to make me drink this tasteless wine?”

“Great Hero Jeok.”

“What?”

As Jeok Cheongang answered curtly, Mae Jonghak fixed him with a deep gaze.

“You’ve already drunk five jars of that tasteless wine.”

“...”

“You’re drinking your sixth now.”

“...”

“Let’s drink for now.”

Jeok Cheongang quietly closed his mouth and raised his cup.

The wine slid down his throat with a fragrant aroma. It was not nearly as bitter as he had claimed. Moonlight softly touched his face as he tilted his head back with the cup.

*I wonder where he is right now.*

*Heartless brat. Couldn’t you have shown your face at least once before leaving?*

The mutter that rose from his heart soon scattered with a breeze that came from somewhere.

* * *

Clip-clop. Clip-clop.

The old horse’s steps were slow, and the straw packed tightly around my entire body was cold and prickly.

Outside the carriage, the voices of hawkers and passersby gradually faded into the distance.

*Did we get out?*

The moment that thought crossed my mind, a whisper slipped into my ear.

“Captain. I need to take a shit.”

“...”

*Hyuk Mujin, you insane bastard. You’re really doing this here?*

We needed to move as little as possible, which meant I could not even subdue him by force. I lowered my voice as much as I could and barked,

“You lunatic. I told you to go before we left.”

“I’m nervous. That’s why. I’m nervous.”

“Then hold it, you son of a bitch.”

“Why are you swearing at me? I can’t even say anything around you.”

“Do I look like I won’t swear right now? What are we going to do about the smell if you shit in here?”

Even a fart under the same blanket would be enough to make me swear. I absolutely refused to let such a catastrophe happen while we were buried together in straw.

“Actually, I thought about it. Wouldn’t it be better if I just went? The smell might make it easier to get through the inspection.”

“Die. Please, just die.”

“I’m sorry. I’ve held it as long as I can, but I don’t think I can anymore. This might be the end for me.”

“Hey, Mujin. Wait. Just wait a second.”

“I’ll accept my punishment later.”

*No! You bastard!*

Terrified, I was about to spring up, camouflage be damned, when—

“We’ve passed through Luoyang’s central avenue. We’re on an empty mountain road now, so you may come out for a moment.”

“Gasp!”

“Phew!”

*Rustle!*

Hyuk Mujin burst through the straw and sprinted toward the bushes. Having escaped death at the edge of a cliff, I repeatedly bowed toward my savior.

“Thank you. I’ll live a good life. Thank you so much.”

“The inspection must have taken a while if Young Hero Hyuk was that desperate. I’m glad we weren’t too late.”

The voice was familiar, but the woman’s smiling face was not.

Under the moonlight pouring through the tall branches overhead, the freckles covering both her cheeks and her dry, rough skin stood out especially clearly.

*No matter how many times I see it, it’s amazing.*

Changing only her features and a few minor details had completely altered her impression.

The woman, Ju Hwaran, noticed me staring and touched her face.

“Ah, I did change a little, didn’t I?”

“Yes. But your eyes are still the same.”

A smile flickered in her beautiful dark-blue eyes.

“That isn’t something a disguise mask can alter. If Captain Song hadn’t helped, it would have been difficult to obtain a mask this good on such short notice.”

Song Ilseom, seated on the driver’s bench, added flatly,

“It was nothing. Just a miscellaneous skill I learned to survive.”

“That’s impressive for a mere trick.”

“It’s probably empty praise, but I’ll accept it for now.”

*That bastard is crooked as hell. I meant it.*

Ju Hwaran’s face had become that of an entirely different person thanks to Song Ilseom’s skill.

I had known that he had lived through all kinds of hardship from the very bottom, but I had not expected him to know how to make disguise masks as well.

*He’s more useful than I thought.*

The various things he had learned while living as a wandering martial artist would undoubtedly help us on the road ahead.

I was privately impressed by Song Ilseom when a sudden thought made my eyes widen.

“Wait. Why don’t I have one?”

If I had a disguise mask, there would be no reason to be transported like luggage with an explosive shit bomb beside me, one that might go off at any moment.

As I protested my unfair treatment, Song Ilseom clicked his tongue.

“Everyone’s features are different, so making the mold for a disguise mask takes several days by itself. How was I supposed to make one for you in such a short time? Wearing an awkward mask would only have the opposite effect. If you feel so wronged, you should have learned a disguise technique.”

Hyuk Mujin emerged from the bushes with an indescribably refreshed expression and joined the conversation.

“What about Young Lady Ju? You said it takes several days.”

“The Young Bureau Head’s mask was...”

Song Ilseom let his voice trail off, then suddenly furrowed his brow.

“What a pointless question. Shut up and bury yourself in the straw again. And don’t stink up my face with your shit.”

“You shit too. Why are you giving me such a hard time…”

Song Ilseom glared at Hyuk Mujin as he grumbled his way back into the straw, then asked me,

“Can I cut him?”

“No.”

I answered firmly, then turned toward Ju Hwaran.

“The others must have gotten out by now, right?”

Ju Hwaran knew perfectly well whom I meant. She gave a small nod.

“Probably. They headed for the West Gate, where inspections are the weakest, so they should have left Luoyang before us.”

I was worried because Taishan was enormous, but Ju Hwaran’s arrangements were not so careless, and we had the Alliance Leader’s Hall and the Hidden Shadow Pavilion behind us. I could afford to relax.

*Rustle.*

Hyuk Mujin poked his head out through the straw.

“Are we going straight to Mount Daebyeol, then?”

“Of course. We’ll change horses once along the way, but nothing will happen before then.”

Ju Hwaran continued without pause.

“If we keep moving without stopping, it will take two shichen. Assuming we undergo a thorough inspection, it could take as long as three. After we meet the other two at Mount Daebyeol...”

“We leave Henan immediately. Correct?”

Ju Hwaran smiled and nodded.

“Just as the Pavilion Master said.”

“...The Pavilion Master?”

“Why? Isn’t that the correct title?”

Technically, it was correct, but it felt awkward, like wearing clothes that did not fit.

I smacked my lips and nodded.

“Well, let’s say that’s fine. Then there won’t be any problems before we reach Mount Daebyeol?”

“Of course. You should be able to sleep soundly and wake up before then.”

Since Henan was the Murim Alliance’s base, it would not be an exaggeration to say there was no chance of an enemy attack.

But I gave a faint laugh with an expression that was neither positive nor negative, only vague.

“What is it?”

“It’s nothing. Nothing at all.”

What was I supposed to call this? After a brief moment of thought, I continued.

“It just feels strange thinking that I’m going to dream for the first time in a long while.”

“A dream?”

“Yes. I dream sometimes. I sleep so deeply that I wouldn’t even know if someone carried me away.”

Ju Hwaran looked puzzled by my cryptic answer, while Song Ilseom furrowed his brow as though wondering what kind of nonsense I was spouting.

Ignoring their reactions, I buried myself deep in the straw piled in the carriage’s storage compartment.

*Two shichen at the earliest to Mount Daebyeol. I have plenty of time.*

From now on, it was time to dream the dream I had put off for a very long time.

*Logout.*

*Ding.*

Along with the clear sound of a bell, my alert consciousness slowly began to sink.

[^1]: Yeoahong is a traditional Chinese rice wine; the name literally means “Daughter’s Red.”
```

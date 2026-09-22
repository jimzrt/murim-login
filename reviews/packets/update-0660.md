<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0660.txt",
      "sha256": "cefd6a1f843af6fc685193e8a4fe1143f821ffaafb1adeb426e9c72dceb36813",
      "bytes": 12890
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "93ab85bc29f721c055293a88789a7e587a35a2fbdd468a3855cc1b4b68ec6cf7",
      "bytes": 2043
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3b4f8c9b2e59618b6f0d53903359699b59b215e9a54328cc26998ba4a6b6ece8",
      "bytes": 200959
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "f1ee5148fb7c72fd932779f2d82a948a7fd46c535ac613e75c75bbec4205b71c",
      "bytes": 828
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "37892a82553227ccf51a732d27964dfe38b886cdf263c9bc8bb86fe6ab2a351b",
      "bytes": 814
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "62cf98296f503256c4feb18a4503798cd17b0bec88928d2c5983235a732839a7",
      "bytes": 589
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "44d18eea9f38f715f46a7453c47b750144079341e0630e37e18b78e438a0cd4f",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "044d79409cb6e98d0f859df86ad0098e408045fa35e3743eaf3a5a0c9f39c019",
      "bytes": 769
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "dd7b8690da0c08b05ba803744ac00534bffd224596d690d058f9ac381737d841",
      "bytes": 1411
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "12c6569943019d3f72df45370c7f8028879294cb9fd24d21b1747aa0ac646b85",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "eb97a43170f1fcb045657f5d33d314ced5b4059409de061b60ea7edf0ee64eab",
      "bytes": 1936
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "77a7a0621a9aa9120b80241d866e87fae049f897ba635f5961b62d510eb1e4c2",
      "bytes": 622
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "7e7fad69d16a857d2e1b9b5cb370001e50ff1accb5a639eca177606d09c05d06",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "30c40050410871282cb7f9923c50f0913d1ce208b9ed1984fdbd7f21cb9a4528",
      "bytes": 1021
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "41a969aa79e01a37397001648a20530bf3dac60d4878edad4665ad9c0c191bae",
      "bytes": 645
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c992eb564fa2be29ef70d87aa51e35ee3f5d2d5eb3ffb8a73495b3e7dcbbb0e8",
      "bytes": 206515
    }
  ],
  "estimated_tokens": 13349
}
-->

# Durable State Update — Chapter 660

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 660. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 660. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 660,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 660,
    "continuity_sources": [660],
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
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "The Fire Dragon Pavilion was attacked after Jin left, and Dark Heaven is suspected of organizing or enabling the assault.",
    "Yohi's Western Yao Estate was attacked by a Supreme Peak master, and Heugung and Yohi remain missing after a third party apparently abducted or confronted them.",
    "Baeksang has accused Jin of the Inner Palace massacre and demanded his arrest, while the Beast Miao King halted the attempted arrest.",
    "Jin chose apparent surrender to protect his companions and punched Baeksang immediately beforehand.",
    "The reconnaissance squad is racing south through Guangxi to stop the Blood Monk, who may cross the region and head south.",
    "The Nanman Beast Palace sent a palace-sealed missive ordering the two tribal chieftains to turn the reconnaissance squad against Song Ilseom and Hyuk Mujin.",
    "Ju Hwaran is alive but has been subdued with a Pressure-Point Strike.",
    "Song Ilseom and Hyuk Mujin have been disarmed, bound, and captured by the reconnaissance squad.",
    "Song Ilseom suspects that a major incident occurred in the Inner Palace and blames Jin Taekyung for it."
  ],
  "continuity_sources": [
    659
  ],
  "open_questions": [
    "What happened in the Inner Palace, and why did the Nanman Beast Palace issue the sealed order?",
    "Where is Ju Hwaran being held, and what will happen to her?",
    "Can Song Ilseom and Hyuk Mujin escape captivity?",
    "What consequences will follow Jin's apparent surrender and the accusation surrounding the Inner Palace massacre?"
  ],
  "safe_through": 659,
  "temporary_decisions": [
    "Retain Force for 강기 and Supreme Peak for 초절정.",
    "Retain Sound Transmission for 전음 and Either-Or for 양자택일.",
    "Retain underground prison for 뇌옥 and iron balls for 철구.",
    "Use Chief Jang for 장 족장."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 중원     | **Central Plains**                               |                                                       |
| 사형     | **Senior Brother**                           |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 철구 | **iron balls** | Training weights attached to Taekyung. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 장족 | **Zang people** | Nanman tribe whose chieftain reports that twenty-two warriors, including a family member, were saved. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |

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
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 백상 | 요희 | Bai great chieftain to Yao great chieftain | Yohi | cold and formal | Calls to Yohi from outside the tent at the chapter's end. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 흑웅 | 백상 | younger_great_chieftain_to_senior_great_chieftain | Uncle Baek | deferential and nervous | Heugung addresses Baeksang as 백 숙부 after being confronted by his icy stare. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 658
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Cold, rigid, meticulous, politically resolute, and strategically manipulative, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle, opposes the Nanman Beast Palace joining the Murim Alliance, remains distrustful of the Central Plains, and is alleged by Heugung to have colluded with Dark Heaven.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 658
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, a master among the Ten Kings, and one of only two Supreme Peak masters in Nanman.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is Baeksang's sworn elder brother and childhood companion, is responsible for the forces stationed at Ailao Mountain, has ordered Ju Hwaran, Song Ilseom, and Hyuk Mujin to investigate the Blood Monk in Guizhou, and met the Martial God twice more than fifty years ago.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 659
- **Aliases:** None
- **Role:** The Blood Monk is an unidentified, apparently middle-aged bald and beardless martial artist who carries a steel Zen staff and has killed several hundred people in Guizhou; his current destination is unknown.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 659
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 657
- **Aliases:** None
- **Role:** Heugung is the middle-aged great chieftain of the Yi people, one of Nanman's four great tribes.
- **Personality:** Heugung presents as foolish and easily flattered in public but is capable of concealed planning, disguise, and covert contact.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung genuinely loves Yohi and had promised to cooperate with Jin Taekyung; he disappeared alongside Yohi after the assault on the Fire Dragon Pavilion, and his death remains unconfirmed after a severed wrist believed to be his was found at her estate.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 659
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion; he is currently disarmed and bound by the reconnaissance squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 658
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 659
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance; he is a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 659
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 659
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 659
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently disarmed and bound by the reconnaissance squad.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 655
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes.
- **Personality:** Yohi's public presence is charismatic and captivating, drawing widespread admiration and affection.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, seeks to unite Nanman's four great tribes under Yao leadership, manipulates Heugung alongside Baeksang, and has disappeared from the Inner Palace alongside Heugung after the assault on the Fire Dragon Pavilion.

## Korean source

```text
＃660화



“전부 제압했습니다. 수혈(睡穴)까지 짚었으니 족히 하루 동안은 의식을 회복하지 못할 겁니다.”

“……잘했다.”

휘하 전사의 보고를 들은 장 족장은 착잡한 얼굴로 고개를 끄덕였다.

그의 눈동자에는 미동도 하지 못한 채 쓰러져 있는 송일섬과 혁무진의 모습이 담겨 있었다.

“무슨 일이 일어날지 모르니 잘 감시하도록. 두 시진 간 휴식 후 다시 이동한다.”

“혹시 그 말씀은…….”

“그래, 저들과 함께 이동할 것이다.”

“저어. 외람된 말씀이지만, 따로 전사 몇을 차출하여 죄인들을 내궁(內宮)으로 호송하는 것이 낫지 않겠습니까?”

용기를 내어 질문한 전사는 이내 자신의 행동을 후회했다. 장 족장이 아무런 말 없이 그를 응시하고 있었기 때문이었다.

“분부를 받들겠습니다.”

황급히 대답한 뒤 떠나는 전사의 뒷모습을 바라보던 장 족장은 문득 한숨을 내쉬었다. 전서응(傳書鷹)을 통해 전달받은 서신의 내용이 다시금 떠올라서였다.

‘흑웅과 요희, 두 대족장이 실종되고 요서부는 전멸. 게다가 그 흉수로 진태경이 지목되었다니.’

보면서도 믿기지 않아 몇 번이나 다시 읽었다.

하지만 그렇다고 해서 전서에 적힌 글씨가 바뀌는 일은 벌어지지 않았고, 장 족장에게 주어진 선택지는 하나뿐이었다.

‘미안하네, 모두.’

장 족장이 전해지지 않을 사과를 마음속으로 뇌까렸다. 하지만 곧 저들도 알게 될 것이다. 현재 상황에서는 이것이 최선이었다는 것을.

‘이건 철저히 준비된 흉계(凶計)다. 그는 그저 예기치 않게 휘말린 것뿐이야.’

장 족장은 전서의 내용을 믿지 않았다.

지금껏 진태경이 보여 준 모습은 중원의 한족들이 말하는 대협(大俠)과 같았고, 그가 독혈지에서 위험을 무릅쓰고 싸우지 않았다면 이백여 명의 전사들 역시 가족들에게 돌아오지 못했을 것이다.

그리고 그렇게 살아 돌아온 이들 중에는 자신이 이끄는 장족의 전사들과 혈육 역시 포함되어 있었다.

‘또한 그에게 입은 은덕과는 별개로, 제대로 된 명분조차 없어.’

비록 남만과 중원이 정마대전 이후 사이가 틀어지긴 했으나, 그건 막대한 희생이 불러온 일방적인 적대감에 가까웠다.

그런데 무림맹의 대표로 남만에 파견된 진태경이 도대체 무슨 이유로 이런 참극을 벌인단 말인가.

‘암천으로도 모자라 남만까지 적으로 돌리겠다는 뜻이 아니고서야…….’

하지만 별수 없었다. 이번 사건의 흐름은 이미 백상과 그를 따르는 일파에게 넘어갔으니까.

다만 궁주인 야수묘왕은 전서응을 통해 자신의 뜻을 은밀히 전해 왔다.



[척후대 내의 한족들을 억류하되, 내궁으로 호송하지 말 것.]



그리고 장 족장은 야수묘왕이 말하고자 화는 바를 정확히 알아들었다.

‘아마도 이들을 내궁으로 호송한다면 영락없이 인질 신세가 되겠지.’

다행히도 그와 함께 척후대를 이끄는 고 족장 역시 야수묘왕을 따르는 인물이었고, 생각이 일치한 그들은 휘하 전사들로 하여금 세 사람을 제압하게 했다.

인질이 아닌, 어떻게든 자신들의 손안에 두어 보호하기 위해서.

때마침 상황도 적절했다. 그들은 혈승(血僧)이라는 노괴를 경계하기 위해 이동하는 중이었으니까.

일종의 전시 상황이니 백상 일파가 이 사실을 안다 해도 약점 잡힐 만한 일은 없었다.

‘그러니 조금만 참게. 일이 잘 해결될 때까지만이라도.’

내심 중얼거린 장 족장은, 의식을 잃은 채 전사들에게 실려 가는 두 사람을 향해 걸음을 내디뎠다.

미안한 마음을 담아 포박이라도 좀 느슨하게 풀어줄 생각이었다.

“잠시 멈추거라. 포승줄이 너무 꽉 묶여 있지 않느냐.”

“부족장님! 안 됩니다!”

“안 되긴 무슨. 괜찮…….”

스윽.

전사들의 외침을 무시하고 혁무진의 등 뒤로 손을 가져간 장 족장이 문득 눈살을 찌푸렸다.

‘이게 뭐지?’

축축하고, 끈적한 감촉.

그리고 뒤이어 올라오는 악취와 함께 이어지는 전사의 목소리.

“어. 그. 등에 변이 묻어 있었습니다.”

“……!”

“그래서 다가오시지 말라고 한 건데…….”

흐려지는 말꼬리. 말없이 자신의 손과 혁무진을 번갈아보던 장 족장이 가라앉은 목소리로 입을 열었다.

“죄인이 더 쌀, 아니 도망칠 수도 있으니, 포승줄을 더 꽉 조여라.”

“옙.”



* * *



현대에서의 나는 준법정신으로 무장한 모범 시민이었다.

중학교 때까지 신호등이 초록불로 바뀌면 손을 번쩍 들고 횡단보도를 건넜고, 헌터가 된 후에는 각종 보험료며, 세금도 연체나 탈세 없이 꼬박꼬박 다 냈다.

심지어는 늙어서 얼마 받지도 못할 국민연금에 관해서도 크게 불평하지 않았다.

‘한 마디로 감옥이랑은 연관이 없었지.’

하지만 어째서일까. 무림에서의 나는 죄를 짓지 않았음에도 뇌옥(牢獄)이라는 장소에 부쩍 익숙해지게 되었다.

무림 꿈나무 시절 태원진가에서도 그랬고, 사천당가에서는 적천강의 곁을 지키느라 내리 며칠을 머무른 적도 있다.

그리고 세 번째로 방문한 이번 뇌옥은 앞서 두 번의 수감 생활과 큰 차이가 있었다.

‘태원진가에서는 사실상 뇌옥이라기보다는 수련동 같은 공간이었고, 사천당가에서는 적천강의 치료를 위해서였지.’

하지만 이번만큼은 달랐다.

자의가 아니라 타의에 의해서 갇혔다는 것도 그렇지만, 각각 천 근이 넘는 철구(鐵球)를 악세서리마냥 전신에 주렁주렁 매달고 있으면 누구든 나처럼 생각하게 될 거다.

철그럭.

“……시벌, 더럽게 무겁네.”

나는 욕설을 중얼거렸다. 사지를 구속한 거대한 쇠사슬과 철구는 그야말로 엄청난 무게를 지녔다.

이미 인간의 한계를 아득히 뛰어넘은 근력의 소유자인 나조차도 쉽게 움직일 수 없을 정도로.

‘공력이라도 사용할 수 있다면 무슨 방법이라도 생각해 볼 텐데…….’

마지막에 때리지 말 걸 그랬나?

아쉬움에 그런 생각이 들었지만, 백상이 그 정도로 호락호락한 인간이었다면 지금쯤 나는 뇌옥이 아니라 처소에 있었을 거다.

더군다나 그는 면상에 일권을 처맞아 코가 부러졌음에도 눈썹 하나 까딱하지 않고 저항하지 않는 나를 손수 포박한 다음, 휘하 부족장들에게 이런 명령을 내렸다.



‘한족 진태경을 뇌옥에 가두고, 만근의 무게로 결박해 두어라.’



그 결과가 지금 이 상황이다.

나는 곧장 남만야수궁의 뇌옥에서도 가장 깊숙한 곳에 갇혔고, 특수한 단환을 복용하여 며칠간 공력을 쓸 수 없는 몸이 되었다.

‘그나마 점혈당하지 않은 걸 다행으로 여겨야 하나.’

놈들이 내 혈도를 짚지 못한 이유는 간단했다.

자꾸 풀려서.

적천강을 비롯한 숱한 강자들에게 천무지체라고 인정받을 만큼 완벽한 신체가 제 기능을 십분 발휘한 셈이다.

물론 그렇다고 한들 공력을 다시 일으키려는 시도는 번번이 실패로 돌아갔다.

“끄응.”

나는 전신에 잔뜩 힘을 불어넣고, 심호흡과 동시에 지금껏 수백, 수천 번이나 해 왔던 대로 하단전에 정신을 집중했다.

그리고 다음 순간, 지난 한나절 동안 반복해서 들어야 했던 시스템 알림이 또다시 귓가를 파고들었다.

삐빅.



- [금력단]의 기운이 단전을 봉쇄하고 있습니다!

- [공력]을 사용할 수 없습니다!



“아.”

이제는 이게 몇 번째 실패인지도 모르겠다.

한 오십 번이 넘어간 후에는 세는 걸 포기해서.

“……빌어먹을.”

내가 한숨 섞인 욕설과 함께 몸을 늘어트린 그때, 저 멀리서 누군가의 걸음 소리가 가까워지기 시작했다.

저벅, 저벅.

축축하고 어두운 공간을 울리는 소음.

금제로 인해 당장 공력을 사용할 수는 없지만, 신체의 감각만큼은 생생하게 살아 있다.

나는 고개를 들어 창살 너머의 어두컴컴한 공간을 바라보았다.

철벅.

쇠창살 앞에서 멈춘 발걸음. 동시에 함께 바닥에 고여 있던 구정물이 무릎에 튀었다.

불빛 하나 존재하지 않는 어둠 속이었으나, 몽골 사람 뺨칠 정도로 뛰어난 안력(眼力)은 상대를 구별해 내기에 충분했다.

“뭐야, 새로 온 간수야?”

“…….”

“기본적인 예의가 없네. 오자마자 사람한테 구정물이나 끼얹고. 물어도 대답도 안 하고.”

말없이 나를 내려다보던 불청객, 백상이 나직한 목소리로 대꾸했다.

“죄인 주제에 엄살이 심하군.”

“뭐. 사실 이 정도면 애교긴 하지.”

어깨를 으쓱……하려다가 철구의 무게 때문에 움찔거린 내가 말을 이었다.

“누구는 코뼈가 주저앉았는데도 잘 버텼으니까. 안 그래?”

어둠 사이로 백상의 미간이 좁혀지는 것이 보인다. 시원시원하게 뻗은 콧날에 감긴 붕대도 함께.

“그거 상당히 아팠을 텐데. 생각보다 잘 참더라. 솔직히 나 뇌옥 보내고 나서 눈물 한 방울 찔끔 흘렸지?”

하지만 동요는 찰나뿐. 백상의 담담한 목소리가 돌아왔다.

“간지럽더군. 아마 네 일권에서 두려움을 읽었기 때문일지도 모르지.”

“뭐?”

“공력조차 실려 있지 않았고, 그렇다고 해서 온 힘을 다한 일격도 아니었다. 그건 그저 어린아이의 분풀이에 불과했어.”

“…….”

“이해한다. 두려웠겠지. 그때 전력을 다했다면 너나 네 수하들 역시 온전치 못했을 테니까.”

젠장. 딜교 씹손해네.

정확히 정곡을 찌르는 한 마디에, 뭐라 대꾸하려던 나는 입을 다물었다.

그리고 그런 내 모습을 바라보는 백상의 눈동자는 여전히 흔들림 없이 가라앉아 있었다.

“왜 그 자리를 벗어나지 않았지? 네놈 혼자 도주했다면, 목숨만큼은 부지할 수 있었을 텐데.”

나는 어처구니없는 얼굴로 대답했다.

“천라지망 펼친다며, 개새끼야.”

“물론 틀림없이 그랬을 것이다. 하지만 충분한 가능성 역시 있었어. 적어도 궁주는 네놈을 쫓지 않았을 테니까. 아니, 훼방을 놓았을지도 모르지.”

백상의 추측은 허황한 것이 아니었다.

적어도 적천강으로부터 전해 들은, 내가 지금껏 보고 겪은 야수묘왕이라면 충분히 그러고도 남을 사람이다.

최악의 상황에서 한 번쯤은 구원의 동아줄을 내밀어 줄 사람.

하지만 나는 곧이곧대로 고개를 끄덕이는 멍청한 짓은 하지 않았다.

어쩌면 이미 늦었을지도 모르지만, 백상의 앞에서 그 사실을 순순히 시인하면 야수묘왕에 대한 경계가 더욱 심해질 테니까.

“글쎄, 난 잘 모르겠던데. 사실 별로 친하지도 않고.”

“제법 머리를 굴리는군. 하지만 아직 한참 미숙해.”

“뭐 믿건 말건 그쪽 마음이고. 당장 노야가 없는 걸 다행으로 여겨라. 한 두세 달 후면 니 머리통이 여기 굴러다니고 있을걸.”

“확실히 치기를 벗어나지 못한 어린아이이기도 하고.”

나는 피식 웃었다.

“아가리에서 똥내가 풀풀 풍기네. 암천 뒷구멍이나 작작 빨아. 적어도 나는 내 사람들을 지키기 위해 여기 있는 거다.”

“…….”

“아무도 없으니까 솔직하게 말하자고. 당신도 알잖아. 지금 스스로 무슨 짓을 하고 있는지.”

이번에 입을 다문 건 백상이었다.

당연히 그럴 수밖에 없었을 것이다. 그가 암천과 협력한다는 건, 남만을 통째로 들어 천주에게 가져다 바치는 꼴이니까.

“수십 년을 함께한 의형도 배신하고. 서른 명이 넘는 부족장과 수많은 남만인들도 속였지. 어떤 변명을 해도 그게 정당화될 수는 없어.”

그 순간, 심유한 눈빛으로 나를 응시하던 백상이 불쑥 입을 열었다.

“이틀.”

“뭐?”

“이틀이다. 이틀 뒤 정오. 넌 모두가 보는 앞에서 사형당할 것이다.”
```

## Final English reading copy

```markdown
# Chapter 660

“We’ve subdued them all. I struck their Sleep Acupoints as well, so they won’t regain consciousness for at least a day.”

“…Good work.”

Chief Jang nodded with a troubled expression as he listened to his warrior’s report.

Song Ilseom and Hyuk Mujin lay motionless, and their figures were reflected in his eyes.

“We don’t know what might happen, so keep a close watch on them. We’ll move again after resting for two shichen.”

“Does that mean…?”

“Yes. We’ll be traveling with them.”

“Chief… Forgive me for speaking out of turn, but wouldn’t it be better to select a few warriors and escort the prisoners to the Inner Palace separately?”

The warrior who had gathered up the courage to ask immediately regretted it. Chief Jang was staring at him without saying a word.

“I’ll carry out your orders.”

After answering hurriedly, the warrior turned and left.

Chief Jang watched him go, then suddenly let out a sigh. The contents of the letter delivered by messenger eagle had come back to him once more.

*Heugung and Yohi, two great chieftains, have gone missing, and the Western Yao Estate has been wiped out. And now they’re saying Jin Taekyung was responsible?*

He had reread it several times because he could not believe what he was seeing.

But the writing in the missive did not change, and Chief Jang had been left with only one choice.

*I’m sorry, everyone.*

Chief Jang repeated the apology silently, knowing it would never reach them. But they would understand soon enough. They would come to know that, under the circumstances, this had been the best course of action.

*This was a thoroughly prepared plot. He was merely caught up in it unexpectedly.*

Chief Jang did not believe the contents of the missive.

Everything Jin Taekyung had shown until now resembled what the Han Chinese of the Central Plains called a Great Hero. If he had not risked his life fighting in the Poisonblood Grounds, more than two hundred warriors would never have returned to their families.

Among those who had made it back alive were the warriors of the Zang people under Chief Jang’s command—and his own blood relatives.

*And regardless of the debt I owe him, there isn’t even a proper justification for this.*

Although Nanman and the Central Plains had fallen out after the Great Faction War, it was closer to one-sided hostility born from the immense sacrifices of that conflict.

So what possible reason could Jin Taekyung, who had been sent to Nanman as the representative of the Murim Alliance, have had for causing such a tragedy?

*Unless he intends to turn Nanman against him as well, on top of Dark Heaven…*

But there was nothing he could do. The course of this incident had already fallen into Baeksang’s hands and those who followed him.

However, the Palace Lord, the Beast Miao King, had secretly conveyed his intentions through a messenger eagle.



> Hold the Han Chinese within the reconnaissance squad, but do not escort them to the Inner Palace.



Chief Jang understood exactly what the Beast Miao King meant.

*If we escort them to the Inner Palace, they’ll undoubtedly become hostages.*

Fortunately, Chief Go, who was leading the reconnaissance squad alongside him, also followed the Beast Miao King. Since the two men shared the same opinion, they had their warriors subdue the three of them.

Not as hostages, but so they could keep them in their hands and protect them somehow.

The circumstances had also worked in their favor. They were already traveling to keep watch for an old monster known as the Blood Monk.

Since it was effectively a wartime situation, even if Baeksang’s faction learned about this, there was nothing they could use against them.

*So please bear with it for a little while. At least until everything is resolved.*

Chief Jang muttered inwardly and stepped toward the two men who were being carried away by the warriors, unconscious.

He intended to loosen their bindings a little, as an apology.

“Stop for a moment. Aren’t those ropes tied too tightly?”

“Chief! You can’t!”

“What do you mean, I can’t? It’s fine—”

Squelch.

Ignoring the warriors’ cries, Chief Jang reached behind Hyuk Mujin’s back, then suddenly frowned.

*What is this?*

A damp, sticky sensation.

Then came a foul stench, followed by a warrior’s voice.

“Uh. There was… feces on his back.”

“…!”

“That’s why we told you not to come any closer…”

The warrior’s voice trailed off. Chief Jang silently looked back and forth between his hand and Hyuk Mujin, then spoke in a low voice.

“The prisoner might shit more—no, escape. Tighten the ropes.”

“Yes, Chief.”

* * *

In the modern world, I had been a model citizen with a strong sense of civic duty.

Until middle school, whenever the traffic light turned green, I would raise my hand high and cross the street. After becoming a Hunter, I paid all my insurance premiums and taxes on time, without ever delaying a payment or evading a cent.

I did not even complain much about the national pension, despite how little I would receive by the time I grew old.

*In short, prison and I had never had anything to do with each other.*

And yet, why was it that in the Murim, I had grown increasingly familiar with a place called an underground prison despite never committing a crime?

It had been the same at the Jin Family of Taiyuan when I was still an aspiring martial artist. At the Sichuan Tang Clan, I had even spent several days there to stand guard beside Jeok Cheongang.

This was my third visit to an underground prison, but it was quite different from the previous two.

*At the Jin Family of Taiyuan, it was practically a training hall rather than a prison. At the Sichuan Tang Clan, I was there to care for Jeok Cheongang.*

This time was different.

Not only was I imprisoned against my will, but anyone would have thought as I did if iron balls weighing more than a thousand geun each were hanging all over their body like accessories.

Clank.

“…Fuck, this is heavy.”

I muttered a curse. The enormous chains binding my limbs and the iron balls attached to them were unbelievably heavy.

Even I, who possessed Strength far beyond human limits, could barely move.

*If I could only use my internal energy, I might be able to think of some way out of this…*

Maybe I shouldn’t have punched him at the end.

I felt a pang of regret, but if Baeksang had been that easy to deal with, I would have been in my quarters instead of an underground prison by now.

Besides, even after taking a punch to the face hard enough to break his nose, Baeksang had personally bound me as I stood there without so much as batting an eye or resisting, then issued this order to the tribal chieftains under his command:



*“Lock the Han Chinese Jin Taekyung in the underground prison and bind him with ten thousand geun of weight.”*



And this was the result.

I had been thrown into the deepest part of the Nanman Beast Palace’s underground prison, then given a special pill that left me unable to use my internal energy for several days.

*At least I should be grateful they didn’t use a Pressure-Point Strike on me.*

The reason they had been unable to strike my acupoints was simple.

They kept coming undone.

My perfect body, which had been recognized as a Heavenly Martial Physique by countless powerful masters, had simply performed its function to the fullest.

Of course, that did not mean my attempts to raise my internal energy had succeeded.

“Ungh.”

I poured all my strength into my body, then took a deep breath and focused my mind on my lower dantian, just as I had done hundreds and thousands of times before.

The next moment, the System alert I had been forced to hear repeatedly for the past half a day pierced my ears again.

Beep.



> **System**
>
> - The energy of the **Force-Sealing Pill** is blocking your dantian!
> - You cannot use **internal energy**!



“Ah.”

I had lost track of how many times I had failed.

After passing fifty attempts, I had given up counting.

“…Damn it.”

Just as I let my body sag with a curse mixed into my sigh, someone’s footsteps began approaching from far away.

Step. Step.

The sound echoed through the damp, dark space.

The Force-Sealing Pill kept me from using my internal energy for the moment, but my physical senses remained as sharp as ever.

I raised my head and looked toward the murky darkness beyond the bars.

Splash.

The footsteps stopped in front of the iron bars. At the same time, the filthy water pooled on the floor splashed against my knees.

There was not a single light in the darkness, but my eyesight—good enough to rival a Mongolian’s—was more than sufficient to identify the other person.

“What is it? Are you a new jailer?”

“…”

“You’ve got no basic manners. You splash dirty water on someone the moment you arrive, then don’t even answer when spoken to.”

The unwelcome visitor looking down at me in silence, Baeksang, replied in a low voice.

“For a criminal, you complain quite a lot.”

“Well, this much is practically cute.”

I tried to shrug, then flinched at the weight of the iron balls before continuing.

“Somebody’s nose bone collapsed, and he still held out pretty well. Wouldn’t you say?”

I could see Baeksang’s brow furrow in the darkness. The bandage wrapped around his straight, prominent nose was visible as well.

“That must have hurt quite a bit. You took it better than I expected. Honestly, you shed a single tear after sending me to prison, didn’t you?”

But his agitation lasted only a moment. Baeksang’s calm voice returned.

“It tickled. Perhaps because I sensed fear in your punch.”

“What?”

“It contained no internal energy, and it was not a full-force blow. It was nothing more than a child’s fit of frustration.”

“…”

“I understand. You must have been afraid. If you had given it everything you had, neither you nor your subordinates would have remained unharmed.”

*Damn. I got absolutely screwed in that exchange.*

His one sentence had struck the exact center of the target. I had been about to say something in reply, but I closed my mouth.

Baeksang’s eyes remained as calm and unwavering as ever as he watched me.

“Why didn’t you leave that place? If you had fled alone, you might have survived.”

I answered with an incredulous expression.

“You said you’d cast a net over heaven and earth, you bastard.”

“Of course, I would have done so. But there was still a sufficient possibility. At the very least, the Palace Lord would not have pursued you. No—he might even have interfered.”

Baeksang’s guess was not baseless.

Judging from everything I had seen and experienced of the Beast Miao King, and from what I had heard directly from Jeok Cheongang, he was more than capable of doing exactly that.

He was the kind of person who would throw out a lifeline at least once in the worst possible situation.

But I did not foolishly nod along.

It might already have been too late, but if I readily admitted that fact in front of Baeksang, his wariness toward the Beast Miao King would only grow stronger.

“I don’t know. I didn’t get that impression. We aren’t even particularly close.”

“You’re putting that head of yours to work. But you’re still far too green.”

“Whether you believe me or not is up to you. Be grateful Old Master isn’t here right now. In two or three months, your head will be rolling around here.”

“You really are still a child who hasn’t outgrown his impetuousness.”

I let out a short laugh.

“Your mouth reeks of shit. Stop sucking Dark Heaven’s asshole. At least I’m here to protect my people.”

“…”

“No one else is around, so let’s be honest. You know too, don’t you? You know what you’re doing right now.”

This time, Baeksang was the one who fell silent.

Of course, he had no choice. Cooperating with Dark Heaven meant taking all of Nanman and offering it up to the Lord of Heaven.

“You betrayed even your sworn brother of several decades. You deceived more than thirty tribal chieftains and countless Nanman people. No matter what excuse you make, none of this can be justified.”

At that moment, Baeksang, who had been watching me with a deep, unreadable gaze, suddenly spoke.

“Two days.”

“What?”

“Two days. At noon, two days from now. You will be executed in front of everyone.”
```

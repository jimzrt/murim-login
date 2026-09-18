<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0371.txt",
      "sha256": "4a8c6a23a2db3a5b655b166bfbfb87467d00d0f82f499a76c629ea422434faa0",
      "bytes": 13871
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a402cbe0270527590353dbb67072abac4aaddb40d56fd9ae5d9de03511ee37b7",
      "bytes": 2422
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "9630a8fee06d4da6f6762f1f9bc8c6aac2ec24b3b450ed42332484cbd386923b",
      "bytes": 129590
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "d5f74d602368733750251f39cd09ded5e54aa3b1a001ced37da255ce3efb6af9",
      "bytes": 803
    },
    {
      "path": "characters/Cheongpung the Ancient Sword.md",
      "sha256": "98c7ec6ec4f5e78dde1c0872ec1b4973dd1ee82fbbb1b07ef950ddb6ed887dc0",
      "bytes": 683
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "5454177ddcd4afb1b671bb873573dad7251659ac41c8aaa57f70ed1cc7d5f750",
      "bytes": 894
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cc35d701ebcecacc65a26cee71518610d8a1c28a1d2440f64796b24157ef8d7e",
      "bytes": 570
    },
    {
      "path": "characters/Extinction Divine Nun.md",
      "sha256": "8310d761da7dab76edd38dea974fa3ef163706f79f04ab7831d9fed79eeddf61",
      "bytes": 656
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "b38ec56d6ae8fddebaf3817c841f8c57bb1c62a2b5ecd367e80654e422667f05",
      "bytes": 609
    },
    {
      "path": "characters/Heaven-Shaking Venerable Nun.md",
      "sha256": "bb2ced14cc4f73fe80f21fafc92d294bbe84324a1e46280886140ae2e4432bb4",
      "bytes": 510
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "547f818cd7ed69c21a84f82fef7ae746cf461754558cae58c2a784c43d5aae92",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f867c592278e6489150030cd016451fa1ab64d56d04d4f5df16741a1c50d22f8",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "30014c8395d8ad69a84b609150dc37533e77e2929c8ec1b0f2de084e615b442d",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3e3eab5fd87fc7d40cdf9216c63e02e4595323ca28b1683375ceae9a7fec3c48",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "2575f96e3361f29cb311f6ce015a2fb01140b4b61c58e450985ef660d982486d",
      "bytes": 655
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "d3a2777c6b94e2d4c2a6378e553f197ab9b615bb1f2162199f666af240630314",
      "bytes": 771
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "83a3e21622d186998973a3f56b57e200d884e1d1d0da496201edde850c43ca75",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8cf735a32ac7c023d2d3c6b9839fc8125e46ade1b1071070190d7af573f37f89",
      "bytes": 98334
    }
  ],
  "estimated_tokens": 14700
}
-->

# Durable State Update — Chapter 371

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 371. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 371. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings (Arabic digits allowed in titles such as 1팀장; do not romanize). At
least one endpoint must occur in the source. The controller drops pairs already
in the address ledger. Do not invent risk-register rows. Beat plot paragraphs
are plain strings; continuity and translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 371,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 371,
    "continuity_sources": [371],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; the Third Fiend has been captured by an unidentified figure, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is awake after exhausting himself, has reached the Supreme Peak realm and manifested Force, and has received the sobriquet Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang; the Divine Physician is Mungyeong's Master.",
    "Mungyeong is the Slaughter Saint and Dong Feng's Disciple; he told the companions that Jin ordered the rescue of Emei.",
    "Hyuk Mujin and Gung Gibang are badly wounded after fighting the Third Fiend, and the Seven Fairies intervened to save Hyuk Mujin from being torn apart.",
    "Cheongpung remains a Supreme Peak master and is at the Sichuan Tang Clan with the Thousand-Year Poison Horned Snake Mimi.",
    "Tang Sadok remains among the critically wounded patients at the Sichuan Tang Clan.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring remains in Jin Taekyung's possession and cannot be appraised by the System."
  ],
  "continuity_sources": [
    370
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why did Mungyeong tell the companions that Jin Taekyung ordered the rescue of Emei?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What is the full nature of the Slaughter Saint's connection to the identity or name Mungyeong?",
    "How will Dark Heaven respond to the failed Three-Gate Bloodbath?"
  ],
  "safe_through": 370,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Render 참이슬 as Chamisul and preserve the Korean soju-brand joke in a footnote.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩.",
    "Use Third Fiend for singular 삼괴 references and Three Fiends for collective references."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 신법     | **movement technique**                           |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 스킬               | **Skill**                      |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 청풍고검 | **Cheongpung the Ancient Sword** | Alias of the Qingcheng Sect's Sect Leader; distinct from Cheongpung. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 멸절신니 | **Extinction Divine Nun** | Presumed-dead Supreme Peak master and Heaven-Shaking Venerable Nun’s only Senior Aunt. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 경천신니 | **Heaven-Shaking Venerable Nun** | Former Emei Sect Leader and sole Supreme Peak master; killed on Mount Emei. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 열화동 | **Fire Gate Cavern** | Ancestral cavern where the Fire Gate Clan began and its legacy continues. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 삼도천 | **Sanzu River** | Buddhist river associated with the boundary between life and death; footnote on first use. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 기문진 | **Mystic Gate Formation** | Formation concealing Dong Feng's clinic in Sichuan. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |

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
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 청풍 | 당사독 | young_martial_artist_to_Sichuan_Tang_Family_Head | Family Head | formal-deferential | Cheongpung addresses Tang Sadok as 가주님 while appealing for help. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 당사독 | 문경 | Family Head to visiting medical apprentice | you | blunt and probing | Asks whether Mungyeong is the Divine Physician's Disciple. |
| 서천마군 | 당사독 | hostile_opponents | you | calm and taunting | The Western Heaven Demon Lord uses 자네 while answering Tang Sadok's question. |
| 당사독 | 서천마군 | hostile_opponents | you bastard | hostile and threatening | Tang Sadok uses 네놈 after recognizing the disguised infiltrator. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 당사독 | 청풍 | family_head_to_younger_ally | greenhorn | blunt and protective | Tells Cheongpung not to interfere while calling him a 핏덩이. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 364
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Cheongpung the Ancient Sword.md

# Cheongpung the Ancient Sword (청풍고검)

- **Safe through:** Chapter 338
- **Aliases:** None
- **Role:** Sect Leader of the Qingcheng Sect and a Supreme Peak martial artist who mobilizes the sect to help Jin Taekyung find the Divine Physician at Mae Jonghak's request.
- **Personality:** Straightforward, genial, and willing to help with matters he considers worthwhile.
- **Voice:** Warm, plainspoken, and good-humored.
- **Relationships:** Mae Jonghak specifically asked him to assist Jin Taekyung, and he commits the Qingcheng Sect and its wider lay-disciple network to the search for the Divine Physician.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 370
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 370
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is the legendary physician also known as Dong Feng and Mungyeong's Master, whose dantian and martial arts were destroyed while shielding Jeok Cheongang.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** The Slaughter Saint is his Master, and Mungyeong is his Disciple.

### Extinction Divine Nun.md

# Extinction Divine Nun (멸절신니)

- **Safe through:** Chapter 369
- **Aliases:** None
- **Role:** Presumed-dead Emei Supreme Peak master and the only Senior Aunt of Heaven-Shaking Venerable Nun, whose reappearance forced the Third Fiend to flee.
- **Personality:** Not established beyond the fear and shock her sudden reappearance caused among the Emei disciples and the Third Fiend.
- **Voice:** Not established.
- **Relationships:** She is Heaven-Shaking Venerable Nun’s only Senior Aunt and was believed to have died after withdrawing from worldly affairs thirty years earlier.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 370
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Heaven-Shaking Venerable Nun.md

# Heaven-Shaking Venerable Nun (경천신니)

- **Safe through:** Chapter 369
- **Aliases:** Blood Rakshasa
- **Role:** Former Emei Sect Leader and the sect's sole Supreme Peak master, killed on Mount Emei by a one-armed middle-aged man.
- **Personality:** Forthright and fearless against enemies.
- **Voice:** Not established.
- **Relationships:** Respected leader of the Emei Sect; she and three Emei Elders were killed in the same attack.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 370
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 370
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 370
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 370
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 370
- **Aliases:** None
- **Role:** Mungyeong is a young medical apprentice and Disciple of Dong Feng who is secretly the Slaughter Saint.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** Initially timid and deferential, he becomes clear, composed, and eloquent when arguing for mercy and justice.
- **Relationships:** Dong Feng is his Master; Jeok Cheongang recognizes him as the Slaughter Saint, and he has now disguised himself as First Fiend to intercept the fleeing Third Fiend.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 370
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded after being forced to watch the clan’s destruction but still alive and receiving treatment from Cheongpung.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor as Family Head, his unnamed nephew serves as Master of the Gatekeeper Pavilion, and the Thousand-Year Poison Horned Snake was his father's final gift and is his cherished companion.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 368
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃371화



“열화신룡(烈火神龍) 진태경 대협을 뵙습니다!”

경외를 담은 외침이 사천당문의 경내에 울려 퍼진 그 순간, 전율을 느낀 것은 진태경 한 사람뿐만이 아니었다.

멀리서 모든 광경을 지켜보던 늙은 스승은 벅차오르는 감정을 숨기기 위해 안간힘을 써야 했다.

‘녀석…….’

적천강은 진태경을 처음 만난 날을 또렷이 기억하고 있었다.

변방 무가의 삼공자. 이제 갓 산서 땅에서 이름을 알리기 시작했던 어린 청년은 잠룡이 되었고, 마침내 날개를 활짝 펴고 푸른 하늘로 비상하고 있었다.

‘그래, 네 녀석이야말로 신룡(神龍)이요, 대협(大俠)이다.’

눈이 마주치자 씩 웃는 진태경의 얼굴이 보인다. 창밖으로 상반신을 내민 그가 두 손을 미친 듯이 휘저었다.

“내 이름이 뭐라고?”

“진태경!”

“별호는 뭐라고!”

“열화신룡!”

“더 크게 소리 질러-!”

“와아아아아!”

엄숙하던 장내가 한 번에 뒤집어지며 광란의 도가니로 변하는 광경에, 적천강은 참았던 웃음을 터트렸다.

“으하, 으하하하!”

시원한 웃음소리와 함성이 뒤섞인다. 바람은 시원했고 하늘은 맑았다.

바야흐로 난세(亂世)의 시작이었으나, 새로운 영웅이 태동하던 그 날은 따스한 봄이었다.



* * *



적천강이 나타난 것은 광란의 도가니가 가라앉은 직후였다.

“좁쌀만 한 방에 많이도 모여 있구나.”

“어? 하나도 안 좁은데요?”

“적 대협, 저쪽에 빈자리가 있습니다.”

눈치라고는 죽었다가 깨어나도 없는 청풍이나 혁무진과는 달리, 뼛속까지 성골 거지인 궁기방은 즉각 움직였다.

“어이구, 그러고 보니까 좁아서 미어터질 것 같네요. 저는 나가 있겠습니다.”

청풍과 혁무진이 손을 흔들어 주었다.

“잘 가요, 궁 소협.”

“저 양반 드디어 가네. 조장, 아까부터 어디서 똥개 궁둥이 냄새 나지 않았습니까?”

나는 조심스럽게 고개를 끄덕였다.

“어, 조금 심하게 나긴 하더라…….”

“개소리 그만하고 둘 다 나와!”

“아니, 진짜 났다니까…….”

“알겠어요. 그렇게 화내지 마세요, 궁 소협.”

벌컥 성을 내는 궁기방의 모습에 청풍이 시무룩한 얼굴로 고개를 숙였다.

“미미. 회오리 치기 하면서 인사.”

취릭. 취리리릭!

“……뭐여, 시벌.”

그사이 스킬이 늘었네. 화려한 퍼포먼스를 보여 준 청풍이 마지막으로 방을 나서자 적천강이 입을 열었다.

“천둥벌거숭이 같으니. 아주 한바탕 난리를 치더구나.”

굳은 얼굴과 착 가라앉은 목소리. 참 여전하다. 평소의 적천강 같아서 왠지 웃음이 나왔다.

“웃어?”

“그럼 웃지, 웁니까?”

“허, 이놈 보게나. 사람들 앞에서 추태를 부려 본문의 명성에 먹칠을 해 놓고도 그런 말이 나오느냐?”

“그렇게 생각하신 것치고는 엄청 크게 웃으시던데.”

“……!”

“다 봤어요.”

애써 유지하던 굳은 표정이 와르르 무너졌다. 적천강의 고개가 슬그머니 창밖을 향해 돌아갔다.

“크흠. 보긴 뭘 봤단 말이더냐.”

“저 말고도 오십 명쯤은 봤을걸요. 입꼬리에서 피 나시는 줄.”

거의 차이나 조커 수준이었지.

도무지 빠져나올 틈을 주지 않는 내 확인 사살에, 한참이나 머뭇거리며 말을 잇지 못하던 적천강이 한마디를 툭 내뱉었다.

“……했다.”

“예?”

“아, 잘했다고!”

벌겋게 달아오른 얼굴로 외친 적천강이 작게 툴툴거린다.

그 모습에 내 입가에 맺힌 웃음이 더욱 짙어졌다. 그래, 그 한마디면 충분하다.

“감사합니다. 전부 노야 덕분이에요.”

“…….”

뭐지? 어째 표정이 심상치 않다.

섭섭함마저 느껴지는 눈빛에 황당해진 내가 물었다.

“이번엔 또 왜요?”

“아니다. 아무것도.”

“그런 것치곤 표정이 어째 좀…….”

“아니라니까!”

“아니, 왜 소리를 지르고 그러세요? 오랜만에 분위기 훈훈하고 좋았는데.”

“거, 아니라면 아닌 줄 알 것이지. 네 녀석이 자꾸 꼬치꼬치 캐물으니까 이러는 것 아니냐!”

“어어, 점점?”

이 양반 갑자기 왜 이래. 내가 무슨 실수라도 했나?

어리둥절해서 고개를 갸웃거리던 그때였다.

스슥.

계단을 올라오는 두 개의 인기척.

벽을 넘어서며 한층 더 예민해진 감각이 아니었다면 쉽게 알아차리지 못했을 만큼, 그들의 걸음은 가볍고 표횰했다.

‘둘 다 엄청난 고수들이다.’

갑자기 초절정의 고수가 둘씩이나?

최근 들어 많은 위기를 겪은 탓에 이제는 몸이 저절로 움직였다.

그런데 적천강이 주먹을 말아쥐는 나를 눈짓으로 만류하더니 손을 내저었다. 한 줄기의 열풍이 닫혀 있던 문을 부드럽게 열어젖혔다.

“다들 성질도 급하군. 일각도 못 기다리고 우르르 몰려와?”

적천강의 불퉁한 목소리에 늙은 여승과 도사가 차례대로 대답했다.

“성질이 급하다니. 시주에게 들으니 기분이 참 묘해지는구려.”

“후배가 결례를 저질렀습니다. 다만 사안이 사안인지라.”

쪼글쪼글한 주름이 가득한 늙은 여승은 초면이었지만, 도사가 누군지는 금방 알아볼 수 있었다.

나는 노고사를 향해 포권을 취했다.

“안녕하십니까. 진인(眞人).”

“다시 보니 반갑네. 진 도우.”

노도사의 정체는 일전에 신의를 찾기 위해 도움을 청하러 간 청성파의 장문인인 청풍고검(淸風高劍)이었다.

‘그럼 이 여승이 아미파의 장문인일 텐데…… 누구지?’

나도 이제 무림 짬밥이 좀 되다 보니 유명한 고수에 관한 것들은 어느 정도 알고 있는데, 남의 문파 사정까지 속속들이 꿰고 있을 정도는 아니었다.

경천신니의 죽음 이후 새로 취임한 장문인의 경우에는 더더욱.

내 생각을 읽은 듯, 적천강이 넌지시 전음을 보냈다.

- 그 할망구는 아미파의 멸절신니(滅絶神尼)다. 보기에는 인자해 보여도 한 번 눈이 뒤집히면 나찰이 따로 없으니 언행에 특별히 신경 써라. 특히 나이에 관해서는 입도 벙긋하지 말고.

나도 조심스럽게 전음으로 응수했다.

- 춘추가 어떻게 되시길래.

- 노부보다 많다. 경천신니의 사고이기도 하지.

- 아.

적천강의 정확한 나이는 모르지만, 백 세를 넘겼다는 것만은 안다. 거기에 더해 별호에서 느껴지는 포스까지.

나는 보쌈집 회장님 같아 보이는 왕 할머니에게 넙죽 허리를 숙였다.

“안녕하십니까! 진태경이라고 합니다!”

“반갑네, 진 시주.”

묘한 눈빛으로 나를 응시하던 멸절신니가 고개를 끄덕였다.

“소문대로군. 아니, 그 이상이야.”

청풍고검이 희미하게 웃으며 말을 받았다.

“실로 놀랍지 않습니까.”

“장강후랑추전랑(長江後浪推前浪). 장강의 뒷물결이 이 늙은이들까지 밀어내려 하는구려. 이토록 어린 나이에 벽을 넘어서다니…….”

“그뿐만이 아닙니다, 신니. 청풍이라는 젊은이도 있지요.”

“아, 그 검성의 후인이라는?”

“예. 빈도가 부족한 탓에 우열을 가릴 수는 없겠으나, 두 젊은이 모두 하늘이 내린 인물들이 확실합니다. 무림의 큰 흥복이지요.”

“호오…….”

피곤함이 묻어나던 두 사람의 얼굴 위로 흥미와 놀라움이 스친다.

어쩐지 민망해져서 눈동자만 굴리고 있던 그때, 적천강이 내 앞을 슥 가로막았다.

그래 봤자 키 차이가 워낙 나서 달라질 것도 없었지만.

“애 얼굴 닳겠소. 할 말이나 후딱 하고 가.”

퉁명스러운 말에 머쓱해진 두 장문인이 본론을 꺼내 들었다.

“문제가 생겼네. 두 사람 모두 잠시 동행해 줄 수 있겠나?”

“오래 걸리지 않을 겁니다. 약속드리지요.”

“동행? 지금 당장?”

탐탁지 않은 목소리로 되물은 적천강이 돌아서며 내게 물었다.

“어찌하겠느냐?”

“…….”

구파일방의 두 장문인이 부탁하는데 나보고 뭘 어쩌라고.

“가겠습니다.”

어차피 몸도 가뿐하겠다, 동행하면서 지금까지의 전후 사정을 들을 수 있을 테니 딱히 거절할 이유가 없었다.

내 흔쾌한 대답에 두 장문인이 앞장서서 걸음을 떼는데, 적천강이 불쑥 입을 열었다.

“그런데, 한 놈은 왜 안 보여?”

“아래에서 기다리고 있다네.”

“다른 사람들 눈에 띄기 싫다 하시더군요.”

한 놈? 이 멤버에 낄 정도면 당문의 가주인 당사독인가?

‘뭐, 누구건 곧 보게 되겠지.’

하지만 내 궁금증은 전각을 나서자마자 마주친 한 사람에 의해 씻은 듯이 사라졌다.

낯익은 얼굴을 보자 절로 반가움이 담긴 외침이 터져 나왔다.

“야, 인마! 문경!”

문경은 사천당문을 떠나기 전의 모습 그대로였다.

안 그래도 녀석이 떠난 지 얼마 되지 않아 암천이 쳐들어온 탓에 걱정이 들었는데, 길이 엇갈렸는지 용케도 다치지 않았다.

“언제부터 와 있었어? 이 자식 이거, 못 본 사이에 키가 더 커진 것 같네. 요즘 성장기냐?”

“…….”

“왜 이렇게 말이 없어. 기분 안 좋아? 혹시…….”

문경의 머리를 쓱쓱 헤집던 나는 숨죽여 속삭였다.

“아침에 몽정했냐?”

“……!”

“했네. 했어.”

짜식, 부끄러워서 아무 말도 안 하는 것 봐라.

나는 흐뭇하게 웃었다.

원래 저 나이대에는 종종 있는 일이다. 이참에 이 케케묵은 무림에 올바른 성 지식을 전파하는 것도 좋겠지.

“이 형님이 신세계를 알려 주마. 앞으로 진성애 선생님이라고 불러라.”

구성애 선생님. 보고 계십니까. 당신의 지식이 시공을 넘어 전해지고 있습니다.

뿌듯한 감정을 느끼며 문경의 어깨를 탁탁 두드리던 그 순간이었다.

“어…….”

“그…….”

“허어…… 저걸 말 안 해 줬네.”

말 안 해 주다니. 뭘?

등 뒤에서 들려오는 세 사람의 장탄식. 동시에 문경의 입술 사이로 무미건조한 음성이 흘러나왔다.

“손. 치워라.”

“……어?”

“그리고 몽정은 오래전에 끝났다.”

“그건 좀 문제가 있는데, 왜냐하면 네가 아직 이차 성징이 완전히 안 끝났……이 아니라.”

나는 침을 꼴깍 삼켰다.

문득, 어떤 무서운 상상이 뇌리를 스쳤기 때문이었다.

“누구……세요?”

엄마, 나 무서워.



* * *



“……해서, 이렇게 된 걸세.”

“참으로 해괴한 일이지.”

엄청난 속도로 신법을 발휘하는 와중에도 두 장문인의 목소리는 흔들리지 않았다.

대답을 요구하는 눈빛에, 나는 힘겹게 입술을 뗐다.

“아, 예. 그래서 지금 가는 곳에 그 뭐냐. 요상한 진법이 있다는 거죠?”

“삼괴(三怪)를 붙잡아 심문한 바에 의하면 그렇다네. 한데 그 진법이라는 것이 워낙 기이해서 말이지.”

적천강이 퉁명스러운 목소리로 대꾸했다.

“노부나 이놈이나, 진법에는 영 젬병이라 봐 봤자 몰라.”

동감이다. 구화산의 열화동은 대단한 기문진식이 설치되어 있지만, 그렇다고 해서 우리가 능통한 것은 아니니까.

‘차라리 제갈세가 같은 곳을 불러야지.’

하지만 제갈세가가 오려면 상당한 시일이 소요될 것이다.

왜인진 몰라도 두 장문인은 우리에게 상당한 기대를 하고 있는 모양이었다. 그중에서도 특히 내게.

“진 도우. 그자에게서 더 이상한 점을 느끼지 못했나? 어떤 언행이라든지.”

“말씀드린 게 전붑니다. 그리고 제가 느끼기에…… 거기서 더 이상해질 것도 없어요.”

암천은 존재 자체가 이상한 놈들이다. 천주라는 존재를 거의, 아니 그냥 신으로 떠받드는 광신도들.

혈주나 서천마군이 보여 준 힘과 기이한 능력들 역시 마찬가지다.

‘인간 트롤마냥 재생하지를 않나, 팔에 양면테이프라도 붙였는지 뗐다 붙이고. 마지막에는 빙의까지 했지.’

생각할수록 기적이다. 그런 놈들을 상대로 싸워서 이겼다는 게.

“으음. 우선 자네가 깨어나기 전 적 시주에게 대략적인 상황은 모두 들었네. 하남으로 보낸 전서응이 답신을 갖고 돌아오면 방향이 잡히겠지.”

“혹시 모르니 진법을 보고 이상한 점이 있다면 알려 주게.”

“예.”

나는 대답하면서 힐끔 저 멀리 앞서나가는 신형을 바라보았다.

문경, 아니 살성(殺聖)이라는 별호를 가진 그를.

‘시벌, 살성이 여기서 왜 나와.’

솔직히 말해서 오줌 쌀 뻔했다.

삼도천 계곡에서 반나절쯤 물놀이 하다가 고기까지 구워 먹고 와도 이 정도는 아닐 거다.

‘문경이 살성이었다니. 내가 살성한테 몽정했냐고 물어봤다니!’

구성애 선생님. 선생님 때문에 뒤질 뻔했습니다.

남몰래 안도의 한숨을 내쉬던 바로 그때, 울창하던 주위의 풀숲이 사라지고 높이 솟은 절벽이 보이기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 371

“I pay my respects to Great Hero Jin Taekyung, the Blazing Flame Divine Dragon!”

At the moment that awe-filled cry rang throughout the grounds of the Sichuan Tang Clan, Jin Taekyung was not the only one who felt a shiver run through him.

The old master watching everything from a distance had to struggle to hide his swelling emotions.

*You rascal…*

Jeok Cheongang remembered the day he had first met Jin Taekyung as clearly as if it had happened yesterday.

The Third Young Master of a frontier martial family. The young man who had only just begun making a name for himself in Shanxi had become a Hidden Dragon, and at last, he had spread his wings wide and soared into the blue sky.

*Yes. You are the Divine Dragon, and the Great Hero.*

Their eyes met, and Jeok saw Jin Taekyung grin. Leaning his upper body out the window, he waved both hands wildly.

“What’s my name?”

“Jin Taekyung!”

“And my sobriquet?”

“Blazing Flame Divine Dragon!”

“Louder—!”

“Waaaaaaaah!”

The solemn gathering flipped over all at once and became a cauldron of madness.

Jeok Cheongang burst into the laughter he had been holding back.

“Ha! Ha-ha-ha!”

His refreshing laughter mixed with the cheers. The breeze was cool, and the sky was clear.

It was the beginning of an age of turmoil, but the day a new hero was born was warm with spring.

* * *

Jeok Cheongang appeared just after the cauldron of madness had settled down.

“So many people crammed into a room as small as a grain of millet.”

“Huh? It’s not cramped at all.”

“Great Hero Jeok, there’s an empty seat over there.”

Unlike Cheongpung and Hyuk Mujin, who would have to die and come back to life before they learned to read the room, Gung Gibang was a pure-blooded beggar to the bone and moved immediately.

“Oh my, now that you mention it, it does look cramped enough to burst. I’ll step outside.”

Cheongpung and Hyuk Mujin waved at him.

“Goodbye, Young Hero Gung.”

“That fellow is finally leaving. Captain, haven’t you noticed the smell of a stray dog’s backside around here?”

I carefully nodded.

“Yeah. It was a little strong…”

“Stop talking crap and both of you get out!”

“No, I’m telling you, it really did smell…”

“Fine, fine. Don’t get so angry, Young Hero Gung.”

At Gung Gibang’s furious outburst, Cheongpung lowered his head with a dejected expression.

“Mimi. Say hello while doing a whirlwind.”

Sssrrk. Sssrrrkk!

“…What the fuck.”

Looks like Mimi had picked up some new tricks in the meantime. After putting on that flashy performance, Cheongpung was the last to leave the room.

Jeok Cheongang finally spoke.

“You reckless little brat. You certainly made quite a ruckus.”

His face was stern, and his voice was low and calm.

He really hadn’t changed at all. Seeing Jeok Cheongang act just like his usual self made me want to laugh for some reason.

“You laughing?”

“Of course I’m laughing. What else should I do, cry?”

“Hah, look at this brat. You made a spectacle of yourself in front of everyone and dragged our sect’s reputation through the mud, yet you still have the nerve to say that?”

“You were laughing pretty loudly for someone who thought that.”

“…!”

“I saw everything.”

The stern expression he had been struggling to maintain collapsed all at once. Jeok Cheongang’s head slowly turned toward the window.

“Ahem. What exactly do you claim to have seen?”

“About fifty people besides me probably saw it too. For a moment, I thought your smile had split your mouth open and you were bleeding from the corners.”

It was practically the Chinese Joker.

My finishing shot left him no room to escape. Jeok Cheongang hesitated for a long while, unable to continue, before finally muttering one word.

“…Did.”

“Huh?”

“I said you did well!”

Jeok Cheongang shouted with his face bright red, then grumbled under his breath.

The sight made the smile at my lips deepen.

Yes. That one sentence was enough.

“Thank you. It was all thanks to you, Old Master.”

“…”

What was this? His expression seemed strangely off.

His eyes even looked almost hurt. I asked, baffled,

“What’s wrong this time?”

“Nothing. It’s nothing.”

“Your expression doesn’t really look like nothing…”

“I said it was nothing!”

“Why are you shouting? The mood was finally warm and pleasant for once.”

“If I say it’s nothing, then take it as nothing! You keep prying and asking questions, so this is happening!”

“Uh-oh. It’s getting worse?”

What was wrong with this man all of a sudden? Had I made some kind of mistake?

It was just as I tilted my head in confusion.

Ssssh.

Two presences were coming up the stairs.

Their footsteps were so light and graceful that I might not have noticed them if my senses had not grown even keener after crossing the threshold.

*They’re both incredible masters.*

Two Supreme Peak masters, just like that?

After everything I had been through lately, my body moved on its own.

But when I clenched my fists, Jeok Cheongang stopped me with a glance and waved his hand.

A thin stream of hot air gently pushed open the closed door.

“You people are impatient. Couldn’t you wait fifteen minutes before coming swarming in?”

An old Buddhist nun and a Daoist answered Jeok Cheongang’s gruff voice in turn.

“Impatient? Hearing that from a lay devotee gives this poor nun a rather strange feeling.”

“This junior was discourteous. However, given the circumstances…”

The old nun had a face covered in fine wrinkles, and I had never met her before. But I immediately recognized the Daoist.

I cupped my hands toward him.

“Greetings, Perfected One.”

“It’s good to see you again, Fellow Daoist Jin.”

The old Daoist was Cheongpung the Ancient Sword, the Sect Leader of the Qingcheng Sect whom I had once visited to ask for help in finding the Divine Physician.

*Then this nun must be the Sect Leader of Emei Sect… Who is she?*

I knew a fair amount about famous masters by now, but I wasn’t familiar enough with the internal affairs of every sect to know them in detail.

Especially not a Sect Leader who had only recently taken office after the death of the Heaven-Shaking Venerable Nun.

As though he had read my thoughts, Jeok Cheongang sent me a quiet message through Sound Transmission.

*That old hag is the Extinction Divine Nun of Emei Sect. She looks kind enough, but the moment she loses her temper, she’s a rakshasa incarnate. Watch what you say. And don’t even open your mouth about her age.*

I replied cautiously through Sound Transmission.

*Just how advanced in years is she?*

*Older than this old man. She was also the Heaven-Shaking Venerable Nun’s Senior Aunt.*

*Oh.*

I didn’t know Jeok Cheongang’s exact age, but I did know he was over a hundred years old. Add in the force suggested by her sobriquet…

I bowed deeply to the old woman who looked like the owner of a bossam restaurant.[^1]

“Greetings! My name is Jin Taekyung!”

“Good to meet you, Benefactor Jin.”

The Extinction Divine Nun studied me with a strange look in her eyes, then nodded.

“So the rumors were true. No—in fact, you’re even more than they said.”

Cheongpung the Ancient Sword smiled faintly and continued,

“Isn’t it truly astonishing?”

“The waves behind push the waves ahead on the Yangtze. It seems the younger generation intends to push even old people like us aside. To cross the threshold at such a young age…”

“It isn’t only him, Venerable Nun. There is also a young man named Cheongpung.”

“Ah, you mean the Sword Saint’s successor?”

“Yes. This poor Daoist lacks the ability to judge which of the two is superior, but both young men are unquestionably heaven-sent. They are a great blessing to the Murim.”

“Oh…”

Interest and surprise flickered across the two faces marked by fatigue.

Feeling awkward, I rolled my eyes around. That was when Jeok Cheongang stepped in front of me.

It didn’t make much difference, considering the enormous difference in our heights.

“You’re going to wear out the boy’s face. Say what you came to say and hurry up.”

The two Sect Leaders looked embarrassed by his blunt words and finally got to the point.

“A problem has arisen. Could the two of you accompany us for a while?”

“It won’t take long. You have my word.”

“Accompany you? Right now?”

Jeok Cheongang asked in a displeased voice as he turned toward me.

“What will you do?”

“…”

Two Sect Leaders from the Nine Sects and One Gang were asking for my help. What exactly was I supposed to do?

“I’ll go.”

I felt light enough on my feet, and accompanying them would let me hear what had happened so far. I had no particular reason to refuse.

At my ready agreement, the two Sect Leaders took the lead and started walking.

Then Jeok Cheongang suddenly spoke.

“But why isn’t one of them here?”

“He’s waiting below.”

“He said he didn’t want to attract the attention of the other people.”

One of them? If he was important enough to be part of this group, was it Tang Sadok, the Family Head of the Tang Clan?

*Well, whoever it is, I’ll see him soon enough.*

But my curiosity vanished without a trace the moment we left the pavilion and ran into one person.

The familiar face immediately drew a delighted shout from me.

“Hey, you bastard! Mungyeong!”

Mungyeong looked exactly as he had before leaving the Sichuan Tang Clan.

Dark Heaven had invaded not long after he left, so I had been worried. Yet, perhaps our paths had simply missed each other, because he had somehow escaped without a scratch.

“When did you get here? You look taller than before. Are you going through a growth spurt?”

“…”

“Why are you so quiet? Are you in a bad mood? Maybe…”

I ruffled Mungyeong’s hair, then leaned in and whispered,

“Did you have a wet dream this morning?”

“…”

“You did. You totally did.”

The little brat. Look at him saying nothing because he’s embarrassed.

I smiled with satisfaction.

It was something that happened from time to time at that age. This would be a good chance to spread some proper sex education through this dusty old Murim.

“Your hyung here is going to show you a whole new world. From now on, call me Teacher Jin Seong-ae.”[^2]

Teacher Gu Seong-ae, are you watching? Your knowledge is crossing space and time to reach the next generation.

I was patting Mungyeong’s shoulder with a proud smile when—

“Uh…”

“Um…”

“Oh dear… We forgot to tell him that.”

Forgot to tell me what?

Three deep sighs came from behind me. At the same time, a flat voice emerged from between Mungyeong’s lips.

“Take your hand off.”

“…Huh?”

“And wet dreams ended a long time ago.”

“That’s a little problematic, because your secondary sexual development hasn’t completely finished ye—no, that’s not what I mean.”

I swallowed hard.

A terrifying possibility had suddenly flashed through my mind.

“Who… are you?”

Mom, I’m scared.

* * *

“And that is how things came to this.”

“It truly is a bizarre matter.”

Even while the two Sect Leaders used their movement techniques at tremendous speed, their voices did not waver.

They looked to me for an answer, and I forced my lips apart.

“Oh, right. So there’s some weird formation at the place we’re going?”

“According to the Third Fiend, whom we captured and interrogated, that appears to be the case. But the formation itself is so strange…”

Jeok Cheongang replied in a gruff voice.

“This old man and this brat are both hopeless at formations. We wouldn’t understand anything even if we looked at it.”

I agreed. The Fire Gate Cavern on Mount Jiuhua had a formidable Mystic Gate Formation installed inside it, but that didn’t mean we were experts in formations.

*We should call in someone like the Zhuge Clan instead.*

But it would take a considerable amount of time for the Zhuge Clan to arrive.

For some reason, the two Sect Leaders seemed to have high expectations of us.

Especially me.

“Fellow Daoist Jin, did you notice anything else strange about that man? Anything he said or did?”

“I’ve told you everything. And from what I could tell… I don’t think he could get any stranger than that.”

Dark Heaven was strange by nature. They were fanatics who worshiped the Lord of Heaven as almost—no, simply—as a god.

The powers and bizarre abilities shown by the Blood Lord and the Western Heaven Demon Lord were no different.

*Regenerating like a human Troll, taking an arm off and sticking it back on as if it had double-sided tape on it—and finally, even possession.*

The more I thought about it, the more miraculous it seemed.

The fact that we had fought those people and won.

“Before you woke up, we heard the general situation from Benefactor Jeok. Once the messenger eagle we sent to Henan returns with a reply, we should have a better idea of how to proceed.”

“If you notice anything strange when you inspect the formation, be sure to tell us.”

“Yes.”

As I answered, I glanced toward the figure moving far ahead of us.

Mungyeong.

No—the man known by the sobriquet Slaughter Saint.

*Fuck. Why is the Slaughter Saint here?*

To be honest, I almost pissed myself.

*Even if I spent half a day swimming in the Sanzu River valley, grilled meat, and came back, it wouldn’t be this bad.*[^3]

*Mungyeong was the Slaughter Saint. And I asked the Slaughter Saint if he’d had a wet dream!*

Teacher Gu Seong-ae, I nearly died because of you.

I was secretly letting out a sigh of relief when the dense undergrowth around us began to disappear, revealing towering cliffs ahead.

[^1]: Bossam is boiled pork commonly wrapped in salted napa cabbage and served with condiments; a bossam restaurant owner is a familiar image of a hearty Korean neighborhood eatery.

[^2]: Gu Seong-ae is a Korean sex educator. Taekyung is parodying her name by replacing Gu with Jin.

[^3]: In Buddhist tradition, the Sanzu River is associated with the boundary between life and death.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0376.txt",
      "sha256": "238732649bf11ec07be4eca4ea6ae273f76eedcf8ee82579ec8256b63ebca2e1",
      "bytes": 14344
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "748c073c8fcd79321b50b94920935f3c6cc8ba8b9a4ed5cd406ccc100955fa50",
      "bytes": 2878
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0ef527fb5a5da59c9dc7fe5ccbd0cb9f274c29c2598a7f9c7753eb48c05ca15e",
      "bytes": 130539
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "bca1162a55b9640aeaa3cbbc85646d2d14db4861eb5ff646f7bb18c1c95bd147",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fa4432f2bd43616d48480c52201ec7a0ce9a9229033447bfa1aeb6bba869712e",
      "bytes": 570
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "98a10b24b5392da8babf3fe7814654d5e5f9c8f962ea03c5251f1b159d8da857",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "786f31d42bf22fef3fe686b40265f11f980ee8a4f22c8ed7dcdee73f79480426",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c14a749d535b372f8214d092762902e5050ed0864f6711bab3b6ee73e6c7556f",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "88c233389b5ecd5f95d9b9c57957010f1e8e1603c8afe1aed93c5cff0b9a9b18",
      "bytes": 1129
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "2828c291edfa6753a57ad6b0fa76d2e68dc44ee854300ce8ac435bc1ad46ea7a",
      "bytes": 1239
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "929ec2041d01cce2b417a7e7b6152b384cf27a9e15001b77bd70725fca82e047",
      "bytes": 622
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "b4bbf193b2d7078d555abb1a01ea13abc4cc2f558290d1d61703e415eb2faccd",
      "bytes": 792
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "c303f40ee9ef9c5b028dd85f9b2786fb0520069f173973a0df686b930fd355fd",
      "bytes": 710
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "69211e21c479772fc7074e7f4bc5fd93cac5d983af8c27db6f56203a6546494c",
      "bytes": 100490
    }
  ],
  "estimated_tokens": 13594
}
-->

# Durable State Update — Chapter 376

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 376. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 376. Profile updates may replace only one
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
  "chapter": 376,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 376,
    "continuity_sources": [376],
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; Mungyeong captured the Third Fiend in the hidden cavern, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is awake, has reached Level 120 and the Supreme Peak realm, manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang; the Divine Physician is Mungyeong's Master.",
    "Mungyeong is the Slaughter Saint and Dong Feng's Disciple; he has sworn never to kill again and intends to live as a medical apprentice.",
    "Hyuk Mujin and Gung Gibang remain badly wounded after fighting the Third Fiend.",
    "Cheongpung remains a Supreme Peak master at the Sichuan Tang Clan with Mimi and is now Mimi's temporary guardian.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring is now bound to Jin Taekyung, alongside White Flame and one unnamed bound item.",
    "A hidden cavern near Chengdu contains the inactive Moving Formation used by Dark Heaven; the Slaughter Saint identifies Dark Heaven as the successor to the Demonic Cult.",
    "Tang Sadok is awake but gravely wounded, has forgiven and received forgiveness for his betrayal, and has entrusted Mimi temporarily to Cheongpung while the Tang Clan's future is uncertain."
  ],
  "continuity_sources": [
    375
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why did Mungyeong tell the companions that Jin Taekyung ordered the rescue of Emei?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "What does the Divine Physician want to ask Jin Wikyung before the party leaves, and what path will the Sichuan Tang Clan take next?"
  ],
  "safe_through": 375,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, and 신니 as Venerable Nun in forms of address.",
    "Render 환영진 as illusion formation and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion and 가주 대행 as Acting Family Head."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 동봉 | **Dong Feng** | Personal name of the Divine Physician and Mungyeong's Master. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
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
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 진태경 | 동봉 | visitor_to_divine_physician | Old Man Dong | formal-polite and deferential | Adopts Dong Feng's requested address after learning his personal name. |
| 청풍 | 동봉 | newly_met_young_martial_artist_to_older_friend | Old Man Dong | casual and cheerful | Accepts Dong Feng's invitation to regard him as an older friend. |
| 문경 | 동봉 | disciple_to_master | Master | deferential and apologetic | Reveals Dong Feng's identity and apologizes for bringing the party without permission. |
| 동봉 | 진태경 | physician_to_visiting_young_martial_artist | Young Master Jin | formal-polite and gentle | Uses 진 공자 while welcoming and speaking with Taekyung. |
| 동봉 | 문경 | master_to_disciple | Gyeong | familiar-commanding | Dong Feng tells Mungyeong to remain at the clinic and care for the patients. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 375
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 375
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is the legendary physician also known as Dong Feng and Mungyeong's Master, whose dantian and martial arts were destroyed while shielding Jeok Cheongang.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** The Slaughter Saint is his Master, and Mungyeong is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 371
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 375
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 375
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 371
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 375
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 371
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 334
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** He has carried Jin Taekyung's party and Mungyeong from Guang'an to Chengdu and agreed to send subordinates to help them return.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 373
- **Aliases:** None
- **Role:** Mungyeong is a young medical apprentice and Disciple of Dong Feng who is secretly the Slaughter Saint, a legendary assassin who has sworn never to kill again.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Master, Jeok Cheongang recognizes his Slaughter Saint identity, and Jin Taekyung, Cheongpung, and the two Sect Leaders know it as well.

## Korean source

```text
＃376화



인산인해(人山人海).

그렇게밖에 표현할 수 없는 광경이었다.

산서잠룡, 아니 열화신룡 진태경과 화산신룡 청풍이 떠난다는 소식을 들은 사람들이 구름처럼 모여들었기 때문이었다.

비단 무림인뿐만 아니라 겁 없는 양민들까지 더해지니, 배웅에 나선 인파는 꼬리에 꼬리를 물고 늘어져 셀 수가 없었다.

“잘 가시오! 열화신룡!”

“사천 무림은 그대들을 잊지 않을 거요!”

“뿔 달린 뱀이다! 화산신룡이 뿔 달린 뱀을 갖고 있다!”

“헉, 뱀이 공중제비를 돌았다!”

“화왕! 화왕이 뱀을 붙잡아서 태우려고 하고 있다!”

웅성거리는 소음이 행렬을 따라 서서히 멀어져 간다.

그리고 아무도 찾지 않는 언덕 위, 나무 그루터기에 앉아 모든 광경을 지켜보고 있던 소년이 문득 입을 열었다.

“멀리도 왔구나.”

“그러게 말입니다. 힘이 드는군요.”

거친 숨소리와 함께 풀밭에 털썩 주저앉는 늙은 제자의 모습에 소년, 문경은 중얼거렸다.

“……참으로 멀리도 왔어.”

거리를 말하는 것이 아니다. 지금 문경은 지나온 세월을 이야기하고 있었다.

“우리가 처음 만났던 때를 기억하느냐?”

“어찌 잊을 수 있겠습니까.”

늙은 제자는 이마에 맺힌 땀을 훔쳤다. 마치 그날의 따가운 햇볕이 자신에게 내리쬐고 있는 것처럼.

“홍무(洪武) 일 년. 유난히도 무더웠던 그해 여름을.”

황위를 둘러싼 내전이 끝나고 새로운 천자가 즉위한 해였다.

젊고 야심만만한 황제는 연호(年號)를 바꾸고 개혁을 꾀했으나, 기나긴 내전으로 피폐해진 백성들은 천자의 뜻을 받들어 개혁에 동참하기에는 너무나 지쳐 있었다.

“천하 각지에서 반란이 일어나고, 도적이 들끓었지.”

“가뭄이 들고 메뚜기 떼가 평야를 휩쓸었습니다. 관군과 반란군의 시신이 도처에 가득하니 역병이 창궐했지요.”

“그래, 실로 난세(亂世)였다.”

죽음은 또 다른 죽음을 낳았고 이내 대륙을 집어삼켰다.

동씨 성을 쓰는 젊은 목수 역시 천하에 드리워진 어두운 그림자를 피할 수는 없었다.

“지금도 가끔 그때를 생각하고는 합니다.”

수십 년의 세월이 바꿔 놓은 것은 강산뿐만이 아니다. 사랑하는 두 아이와 아내를 역병으로 잃어야 했던 젊은 목수는 어느덧 늙은 의원이 되어 있었다.

“제가 조금만 빨랐더라면, 더 빨리 스승님을 찾았다면 가족들을 살릴 수 있지 않았을까 하는 생각 말입니다.”

“후회하느냐?”

“예.”

하늘과 가까운 언덕에 앉아, 떠다니는 조각구름을 바라보는 늙은 의원의 눈동자는 어느새 젊은 목수의 그것으로 돌아가 있었다.

“이 숨이 붙어 있는 한 평생토록.”

고작 하루 차이였다.

목수가 역병에 걸린 몸을 이끌고 화전민촌에 머무르던 이름 모를 노의원을 데려왔을 때는 모든 것이 늦은 후였다.

그는 꼬박 하루를 울었고 가족들을 묻기 위한 구덩이를 팠다. 그리고 자신이 데려온 의원에게 한 가지 부탁을 했다.

“함께 묻어 주십시오. 제가 그리 청했지요.”

문경이 무뚝뚝한 목소리로 말을 받았다.

“그래서 나는 네 뺨을 때려 주었지.”

“많이 아팠습니다. 죽고 싶을 정도로.”

아팠다. 목숨을 좌지우지하는 고통보다는 사랑하는 아내와 아이들을 더 이상 볼 수 없다는 사실 때문에.

“그런 저를 스승님께서 일으켜 세워 주셨습니다.”

문경은 고개를 저었다.

“손을 내밀었을 뿐이다. 그 손을 붙잡고 일어난 것은 네 의지였어.”

“살아야 했습니다. 해야 할 일이 생겼으니까요.”

본래대로라면 목수 역시 역병으로 죽었어야 할 몸이었다.

그러나 의원은 지금껏 본 적 없는 의술로 그를 완치시켰고, 목수는 처음으로 하늘이 정한 생로병사(生老病死)를 한낱 인간 역시 바꿀 수 있음을 깨달았다.

“아직도 눈앞에 선하구나. 제자로 받아 달라며 무릎을 꿇던 네 모습이.”

“이 제자가 기억하는 것과는 다르군요. 저는 따라오라며 손짓하시던 스승님의 모습이 떠오릅니다.”

그렇게 가족을 잃은 젊은 목수는 새로운 목표를 찾았고, 천하를 주유하며 힘없고 가난한 병자를 보살피던 늙은 의원은 새로운 제자를 얻었다.

이제는 의원이 된 목수, 동봉(童奉)이 스승의 진정한 정체를 알게 된 것은 그로부터 오랜 시간이 흐른 뒤였다.

“살성(殺星)…… 실로 무시무시한 별호입니다. 그때 처음으로 스승님이 낯설게 느껴졌지요.”

문경은 무감각한 시선으로 저 너머를 바라봤다.

지금부터 하려는 말은 그가 자신의 제자에게 단 한 번도 묻지 않았던 내용이었다.

“왜 떠나지 않았느냐?”

“제가 스승님을 떠날 것이라 생각하셨습니까?”

“나는 지금까지 헤아릴 수 없이 많은 목숨을 해쳤다. 과거를 숨긴 추악한 살귀(殺鬼)에 불과했지. 네가 떠난다 해도 이해했을 것이다.”

“정말 그랬을지도 모르지요. 하지만 저는 스승님이 어떤 사람인지 너무나도 잘 알고 있었습니다.”

다음 순간, 나지막한 목소리가 이어졌다.

“신의(神醫). 제 스승님은 신의라 불리는 분입니다. 이유 없는 살생을 저지르실 분이 아닙니다.”

“……!”

문경의 눈동자가 파르르 떨렸다. 그건 지금껏 아무에게도 말하지 않았고, 아무도 인정하지 않으려 했던 사실이었다.

그는 살수로 살아오며 정(正), 사(邪), 마(魔)를 가리지 않고 숱한 목숨을 직접 거둬들였다. 그리고 그들은 하나같이 죽어야 할 이유가 있는 자들이었다.

공명정대함으로 이름 높은 정파의 대협은 여인을 간살하는 취미가 있었고, 어느 사파의 고수는 재미 삼아 촌락 하나를 몰살시켰다.

중원을 침공한 마교의 군세가 닥치는 대로 사람들을 죽이고 파괴를 일삼지 않았다면, 보다 못한 천하제일의 살수가 나서서 악명 높은 마두들을 죽이지 않았다면 그는 살성(殺星)이라 불릴 수 없었을 것이다.

“내가 마교와 싸우지 않았다면, 온 천하가 나를 손가락질했을 것이다. 지금껏 그래 왔던 것처럼.”

살성이라는 별호는 천하 무림의 주인이 된 정파가 그에게 내리는 면죄부이자 강자에 대한 찬사일 뿐이었다.

문경은 늘 문경이었음에도, 사람들은 그 이면에 숨겨진 진실을 알지 못했고 알려고도 하지 않았다.

“어째서 알리지 않으셨습니까?”

“모두 지난 일이다. 나는 무림을 떠나고자 했고, 뜻한 바에 따라 의원이 되었지. 그리고 앞으로도 그럴 것이다.”

문경은 천천히 몸을 일으켰다. 어느새 사천당문을 빠져나간 기나긴 행렬은 저 너머로 사라진 후였다.

“이만 내려가자. 우리를 기다리는 병자들이 있다.”

건조한 목소리와 함께 걸음을 뗀 그 순간이었다.

“곧 거대한 전란(戰亂)이 일어날 것입니다.”

문경의 발걸음이 우뚝 멈췄다. 그의 등 뒤로 늙수그레한 제자의 목소리가 이어졌다.

“그때와 같은 일이 반복될 것입니다. 수많은 이들이 죽고 다치겠지요. 부모와 자식을 잃은 자들이 넘쳐나고, 비명과 죽음이 끊이지 않을 겁니다.”

“……많이 바빠지겠군. 준비를 해 둬야겠어.”

“제가 무슨 말을 하려 하는지, 스승님께서는 알고 계시지 않습니까.”

“알고 싶지 않다.”

“스승님.”

“나는 의원이다. 비록 스스로 약속한 바를 깨고 어쩔 수 없이 살생을 저질렀으나, 두 번 다시 그런 실수는 없을 것이다.”

문경은 천천히 말을 이었다.

“싸우는 것은 저들의 몫이고, 병자를 치료하는 것은 우리의 몫이다. 내 뜻은 이미 무림을 떠난 지 오래다.”

“그렇다면 어찌하여 무공을 놓지 않으셨습니까.”

“……!”

문경은 말문이 막혔다.

그건 스스로가 오랫동안 품고 있던 의문이었다. 살생이 싫어 무림을 떠나고자 했다면, 살생을 위한 수단인 무공 역시 전폐해야 맞았다.

그러나 오히려 그의 무공은 한층 진일보했다. 무공에 대한 끈과 미련을 놓지 못했다는 증거다.

‘그것은 어째서인가.’

짧은 상념을 깨트린 것은 늙은 제자의 목소리였다.

“스승님께서는 수백, 수천의 병자를 치료하실 수 있으십니다. 동시에 수만의 인명을 구할 수 있는 분이기도 하지요.”

“…….”

“살성(殺星)이 아닌 신의(神醫)로서 전란을 막아 주십시오. 이 제자는 이곳에서 병자들을 보살피겠습니다.”

문경은 문득 고개를 들어 하늘을 바라봤다.

맑고 푸르르다. 사천당문이 피로 물들었던 칠 주야 전의 하늘은 먹구름으로 가득했었다.

“하늘이 맑구나.”

무뚝뚝한 목소리와 함께 멈춰 있던 발걸음이 앞으로 나아갔다.

“이만 병자들을 살피러 가 보아야겠다. 천천히 내려오너라.”

언덕을 내려가는 그의 등 뒤로 동봉의 목소리가 흩어졌다.

“술시(戌時). 성도의 서쪽 항구에서 출발한다고 했습니다.”

“부질없는 짓. 내가 있어야 할 곳은 무림이 아니다.”

그러나 서서히 멀어지는 스승의 뒷모습을 바라보는 늙은 제자의 입가에는 희미한 웃음이 맺혀 있었다.

“부디…… 강녕하십시오.”

휘이이잉.

어디선가 불어온 바람이 두 사람의 사이를 스쳐 지나갔다.



* * *



“뭘 그렇게 보고 계세요?”

혁무진의 물음에, 항구를 에워싼 인파를 바라보고 있던 나는 고개를 돌렸다.

“별거 아니다. 그냥 혹시나 해서.”

“그러니까 뭘요?”

“이 자식이, 왜 이렇게 꼬치꼬치 캐물어? 그렇다면 그런 줄 알지.”

내 대답에 혁무진이 의미심장하게 웃었다.

“사실 다 알고 있습니다. 조장님께서 왜 그러시는지.”

“……?”

순간 멈칫했다. 이 자식이 어떻게 그걸 알지? 나와 신의가 나눈 대화는 청풍도 듣지 못했는데.

‘이 녀석 눈치가 이렇게 빨랐나.’

의아해하던 그때, 녀석이 작게 속삭였다.

“저기 앞줄 우측 네 번째에 서 있는 소저를 보고 계셨던 거 아닙니까?”

“…….”

“확실히 예쁘긴 하네요. 제법 있는 집 규수 같아 보이는데. 조장님께서 허락하신다면 오른팔인 제가 슬쩍 가서 따로 자리를…….”

“무진아.”

“예? 아, 혹시 자연스러운 만남을 추구하시는 쪽입니까? 그렇다면…….”

“장강 밑바닥에 가라앉고 싶니?”

“……!”

“개소리하지 말고 계속 거기 누워 있어. 나중에 멀미 난다고 토하지나 말고.”

“……옙.”

조용히 찌그러지는 혁무진의 모습에 궁기방이 킬킬거렸다.

“멍청한 작자 같으니. 우측 네 번째가 아니라 좌측 세 번째 여인이다. 누가 봐도 훨씬 미인인데 눈깔이 삐었군.”

“눈깔 삐꾸 만들어 줘?”

“……미안하다.”

“사람답게 살자. 사람답게.”

한숨과 함께 고개를 내저은 나는 마지막으로 구름처럼 모여 있는 사람들을 쭉 훑었다.

확실히 둘 다 예쁘긴 하지만 궁기방이 말한 좌측 세 번째가 내 스타일…… 아, 이게 아니지.

‘아 씨, 저 자식들이 떠들어 댄 것 때문에 괜히 자꾸 보게 되네.’

그런 생각을 하고 있을 때, 구릿빛 체구의 거한이 내게 다가와 말을 건넸다.

“이보게, 후배. 아니 후배가 아니라 진 소협, 아니 대협.”

뭐야, 버퍼링이야?

나는 번개에 콩 볶듯 호칭을 바꿔 대는 선화아(船火兒) 무송에게 해결책을 제시해 주었다.

“그냥 후배라고 하시죠.”

“커흠. 그, 그래도 되겠나?”

“안 될 건 뭡니까. 전에는 잘만 하시더니.”

“그래도 그, 자네가 워낙 큰일을 해내지 않았나.”

그렇긴 하다. 산서잠룡이라는 지역구 후기지수에서 이제는 전국구 유명인사가 되었으니까.

“그리고 적 대협께서도 나를 좀 별로 마음에 안 들어 하시는 것 같길래…….”

“괜찮아요. 애초에 물을 별로 안 좋아하셔서.”

무송이 힐끔거리는 곳에는 잔뜩 성난 얼굴의 적천강이 있었다.

바로 옆에는 진위경이 뭔지 모를 죽간을 들여다보고 있고, 청풍은 미미에게 새로운 기술을 연습시키고 있었다.

“미미, 파도타기!”

취릭, 촤아아악!

……저거 물뱀이었나.

좀처럼 보기 힘든 진귀한 광경에 잠시 시선을 뺏겼던 무송이 떨떠름하게 입을 열었다.

“어쨌든, 출항 준비는 이미 끝마쳤는데 언제쯤 출발하면 되겠나?”

“혹시 지금 시간이?”

“자네가 말했던 술시가 지났네. 더 어두워지기 전에 출발하는 것이 좋아.”

“……음.”

“혹시 더 올 사람이라도 있는 건가?”

무송의 질문에 잠시 고민하던 나는 고개를 저었다.

“아뇨. 없어요.”

“그럼 출발해도 되겠군.”

“그렇게 하시죠.”

“알겠네.”

무송이 손을 번쩍 치켜올리자 이미 모든 준비를 끝마친 수적들이 일사불란하게 움직였다.

환송을 위해 모여 있던 사람들이 우리를 향해 손을 흔들던 바로 그 순간이었다.

“잠깐, 잠깐만요!”

“정지, 정지!”

항구에서 떨어지려던 쾌조선의 뱃머리가 흔들렸다.

나는 저 멀리, 사람들 사이를 해치며 다가오는 한 소년을 발견하고 피식 웃었다.

“한 사람만 더 태우고 가죠.”
```

## Final English reading copy

```markdown
# Chapter 376

A sea of people.

That was the only way to describe the scene.

After hearing that the Sleeping Dragon of Shanxi—no, the Blazing Flame Divine Dragon Jin Taekyung—and the Huashan Divine Dragon Cheongpung were leaving, people had gathered like clouds.

Not only martial artists, but also fearless ordinary citizens had come to see them off. The crowd stretched endlessly, one person after another, until it was impossible to count them.

“Safe travels, Blazing Flame Divine Dragon!”

“Sichuan Murim will never forget you!”

“It has horns! The Huashan Divine Dragon has a horned snake!”

“Whoa, the snake just did a flip in midair!”

“Fire King! The Fire King is grabbing the snake and trying to roast it!”

The murmuring noise gradually faded into the distance as the procession moved away.

On a deserted hill, a boy sat on a tree stump watching the entire scene. Then he suddenly spoke.

“We’ve come a long way.”

“Indeed. I’m getting tired.”

At the sight of his old Disciple dropping heavily onto the grass with ragged breaths, Mungyeong muttered,

“…We really have come a long way.”

He wasn’t talking about distance. Mungyeong was speaking of the years they had traversed.

“Do you remember when we first met?”

“How could I forget?”

The old Disciple wiped the sweat from his brow, as though the scorching sunlight from that day were still beating down on him.

“The first year of Hongwu.[^1] That particularly hot summer.”

It was the year the civil war over the imperial throne ended and a new Son of Heaven ascended.

The young, ambitious emperor changed the era name and sought to introduce reforms, but the people, exhausted by the long civil war, were far too weary to heed the Son of Heaven’s will and take part in them.

“Rebellions broke out across the land, and bandits ran rampant.”

“There was a drought, and swarms of locusts swept across the plains. The corpses of government soldiers and rebels filled every corner, and epidemics raged.”

“Yes. It was truly a time of turmoil.”

Death begot more death, and before long, it swallowed the continent whole.

A young carpenter surnamed Dong could not escape the dark shadow that had fallen over the land.

“Even now, I sometimes think about those days.”

The decades had changed more than just the mountains and rivers. The young carpenter who had lost his beloved wife and two children to the epidemic had eventually become an old physician.

“I sometimes wonder whether I could have saved my family if I had been a little faster, if I had found you sooner.”

“Do you regret it?”

“Yes.”

Sitting on a hill close to the heavens and gazing at the drifting scraps of cloud, the old physician’s eyes had returned to those of the young carpenter.

“For the rest of my life, as long as I draw breath.”

It had been a difference of only one day.

By the time the carpenter dragged his plague-stricken body to bring back the unnamed old physician who had been staying in a slash-and-burn settlement, everything was already too late.

He had cried for an entire day, dug a pit to bury his family, and then made one request of the physician he had brought.

“Please bury me with them. That was what I asked.”

Mungyeong replied in his blunt voice.

“That was why I slapped you across the face.”

“It hurt. So much that I wanted to die.”

It had hurt—not because of any pain that could decide life or death, but because he could no longer see his beloved wife and children.

“You were the one who helped me stand again.”

Mungyeong shook his head.

“I only held out my hand. You were the one who grasped it and got back up.”

“I had to live. I had something I needed to do.”

Under normal circumstances, the carpenter should have died from the epidemic as well.

But the physician cured him with medical arts unlike anything he had ever seen, and for the first time, the carpenter realized that even a mere human being could alter the cycle of birth, aging, sickness, and death ordained by Heaven.

“I can still see it clearly. You kneeling before me and begging me to accept you as my Disciple.”

“That is different from what this Disciple remembers. I remember you beckoning for me to follow you.”

The young carpenter who had lost his family found a new goal, while the old physician who roamed the land tending to poor and helpless patients gained a new Disciple.

It was only after many years had passed that the carpenter, now a physician—Dong Feng—learned his Master’s true identity.

“The Slaughter Saint… It is a truly terrifying sobriquet. That was when you first seemed like a stranger to me, Master.”

Mungyeong gazed into the distance with an impassive expression.

What he was about to ask was something he had never once asked his Disciple.

“Why did you not leave?”

“Did you think I would leave you, Master?”

“I have harmed countless lives. I was nothing more than an ugly killing fiend hiding his past. I would have understood if you had left.”

“Perhaps I really would have. But I knew all too well what kind of person you were, Master.”

The next words came in a low voice.

“You are the Divine Physician. My Master is known as the Divine Physician. You are not someone who would kill without reason.”

“...!”

Mungyeong’s eyes trembled.

It was something he had never told anyone, and something no one had ever wanted to acknowledge.

He had lived as an assassin and personally taken countless lives, whether they belonged to the orthodox faction, the unorthodox faction, or the Demonic Cult. Every one of them had been someone with a reason to die.

A Great Hero of the orthodox faction, renowned for his fairness and integrity, had a habit of raping and murdering women. A master of an unorthodox faction had wiped out an entire village for fun.

If the Demonic Cult’s army invading the Central Plains had not killed and destroyed indiscriminately, if the greatest assassin under Heaven had not stepped forward when he could no longer stand by and killed the notorious fiends, he could never have been called the Slaughter Saint.

“If I had not fought the Demonic Cult, the entire world would have pointed fingers at me. Just as it always had.”

The sobriquet Slaughter Saint had been both the absolution bestowed upon him by the orthodox faction that ruled Murim and praise for a powerful man.

Though Mungyeong had always been Mungyeong, people neither knew nor tried to learn the truth hidden behind him.

“Why did you never tell anyone?”

“It is all in the past. I wanted to leave Murim, and I became a physician as I had intended. I will continue to do so.”

Mungyeong slowly rose to his feet. By then, the long procession that had left the Sichuan Tang Clan had already disappeared into the distance.

“Let us go down. There are patients waiting for us.”

The instant he started walking, his Disciple spoke.

“A great war will break out soon.”

Mungyeong’s footsteps stopped abruptly. Behind him, the old Disciple’s voice continued.

“The same thing that happened back then will happen again. Countless people will die and be wounded. There will be countless people who have lost their parents and children, and the screams and deaths will never cease.”

“…We will be very busy. I should make preparations.”

“You know what I am trying to say, Master.”

“I do not want to know.”

“Master.”

“I am a physician. Though I broke the promise I made to myself and was forced to kill, I will not make the same mistake again.”

Mungyeong continued slowly.

“Fighting is their responsibility, and treating the sick is ours. My heart left Murim long ago.”

“Then why did you never give up martial arts?”

“...!”

Mungyeong was left speechless.

It was a question he had carried inside himself for a long time. If he had wanted to leave Murim because he hated killing, then it would have made sense to abandon martial arts as the means of killing as well.

Yet his martial arts had instead advanced another step. It was proof that he had been unable to let go of his attachment to them.

*Why is that?*

The voice of his old Disciple broke through his brief thoughts.

“You can treat hundreds, even thousands of patients, Master. At the same time, you are someone capable of saving tens of thousands of lives.”

“…”

“Please prevent the war as the Divine Physician, not the Slaughter Saint. This Disciple will care for the patients here.”

Mungyeong suddenly raised his head and looked at the sky.

It was clear and blue. Seven days earlier, when the Sichuan Tang Clan had been stained with blood, the sky had been filled with dark clouds.

“The sky is clear.”

With his blunt voice, Mungyeong’s halted footsteps began moving forward again.

“I should go tend to the patients. Come down slowly.”

From behind him, Dong Feng’s voice scattered into the air.

“The Hour of the Dog.[^2] They said the ship would depart from Chengdu’s western harbor.”

“Pointless. The place I should be is not Murim.”

Yet a faint smile formed at the corner of the old Disciple’s mouth as he watched his Master’s back slowly recede.

“Please… stay well.”

Whoooosh.

A wind that had come from somewhere swept between the two of them.

* * *

“What are you looking at so intently?”

At Hyuk Mujin’s question, I turned away from the crowd surrounding the harbor.

“It’s nothing. I was just checking something.”

“Checking what?”

“You little pest, why are you prying into every little thing? If I say it’s nothing, then take it as nothing.”

Hyuk Mujin gave me a meaningful smile.

“I actually know why you are doing that, Captain.”

“…?”

I froze for a moment. How the hell did he know? Even Cheongpung hadn’t heard the conversation between the Divine Physician and me.

*Was this guy always this perceptive?*

Just as I was wondering, he whispered,

“Weren’t you looking at the Young Lady standing fourth from the right in the front row?”

“…”

“She is definitely pretty. She looks like the daughter of a fairly wealthy family, too. If you permit it, Captain, I could go over there as your right-hand man and arrange for the two of you to meet privately…”

“Mujin.”

“Yes? Ah, do you prefer natural meetings? If so…”

“Do you want to sink to the bottom of the Yangtze?”

“...!”

“Stop spouting bullshit and keep lying there. And don’t go vomiting later because you get seasick.”

“…Yes, sir.”

As Hyuk Mujin quietly crumpled into silence, Gung Gibang snickered.

“You idiot. It wasn’t the fourth from the right. It was the third woman from the left. Anyone can see she is much prettier. Your eyes are screwed up.”

“Want me to screw up your eyes for you?”

“…Sorry.”

“Let’s try to live like decent human beings. Decent human beings.”

With a sigh, I shook my head and gave the cloud-like crowd one final sweep.

Both of them were definitely pretty, but the third woman from the left was more my type…

No. That wasn’t it.

*Damn it. Those bastards kept going on about it, so now I keep looking at her.*

As I was thinking that, a huge man with a copper-colored complexion approached me and spoke.

“Hey, Junior. No, not Junior. Young Hero Jin. No, Great Hero.”

*What is this, buffering?*

The man cycling through forms of address at lightning speed was Ship-Fire Boy Mu Song. I offered him a solution.

“Just call me Junior.”

“Ahem. Would that really be all right?”

“Why wouldn’t it be? You did just fine before.”

“Still, you have accomplished something so great.”

That was true. I had gone from being a regional young prodigy known as the Sleeping Dragon of Shanxi to a nationally famous figure.

“And Great Hero Jeok seems not to like me very much, either…”

“It’s fine. He was never very fond of water in the first place.”

Where Mu Song was glancing stood Jeok Cheongang, his face thoroughly incensed.

Right beside him, Jin Wikyung was examining a bamboo slip whose purpose I couldn’t identify, while Cheongpung was teaching Mimi a new technique.

“Mimi, ride the waves!”

Sssrik, shaaaash!

*Was that a water snake?*

Mu Song had briefly been distracted by the rare sight—one that was difficult to see anywhere else—before opening his mouth with an awkward expression.

“Anyway, we have finished preparing for departure. When should we leave?”

“What time is it now?”

“The Hour of the Dog you mentioned has passed. It would be best to leave before it gets any darker.”

“…Hmm.”

“Are we waiting for anyone else?”

I thought about Mu Song’s question for a moment before shaking my head.

“No. No one else.”

“Then we can depart.”

“Let’s do that.”

“Understood.”

When Mu Song raised his hand high, the river pirates who had already finished preparing moved in perfect unison.

It was at that exact moment, as the people gathered to see us off waved in our direction, that—

“Wait! Wait just a moment!”

“Stop! Stop!”

The bow of the fast ship pulling away from the harbor shook.

Far off in the distance, I spotted a boy forcing his way through the crowd. I let out a short laugh.

“Let’s take one more person aboard before we go.”

[^1]: Hongwu was the reign name of Zhu Yuanzhang, the founding emperor of China’s Ming dynasty.

[^2]: The traditional Hour of the Dog lasted roughly from 7 to 9 p.m.
```

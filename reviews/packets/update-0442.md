<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0442.txt",
      "sha256": "66f38e8ac8472a5507384869ccbdec4ba7f012db2e417575ca17797dd57960f5",
      "bytes": 13200
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4ba49f5070da05004a6dfa39739e551d1e3e02b178d8ad069fd4b064255fea55",
      "bytes": 2388
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "43533811badb3beeb5945e723b2b473a7c759b00647dc17e216bbc011adaff72",
      "bytes": 144378
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "3443a5f40b34c3c3fbb5017813072fe8a1822818aefaf86ba29ea1f24dd10f26",
      "bytes": 803
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d6dafe55f68af5e2e7ff160be5cfcaf8d5b42e1e93d030b5dd3aae8fd21fe259",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7f31b7ae39578f08a956733f08563902ab09e95a9564be503c5fccf910675cde",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "ce0ca322175b3856c15fab21091dfa71f57070b596dcfe5a2ac9f1dd1be49618",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ca411750d3aebc9be0dc37cf11150962d2aa43dfb1ed69cfe9deac0e832fa33b",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2a7eaeff7b3798b09032413702adfc7ee5ab54a0ef9f92ed992db6df45f3e9a2",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fa5f8cab5b117133d2435121f6186868e7dbe823b99fa12c862620548105290e",
      "bytes": 1526
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1489e917762c978579f778d191a7774144cb7ff2a1952efdeb43ab34d49a6145",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "2436dbef8e9f582321fb451187ebc6225a63b46893d4e4aa33d55c986a3c07ae",
      "bytes": 1182
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "01623507eb9338e686c51849bf652b6401ee23a2ba1dec575acfddb2e17a5294",
      "bytes": 686
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "555daf074d4a13d8e280a2bcaec91bc0de15bb4ad42b793591cb1945bf6011e4",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fd607b1d31fc804def3ff7ececdefae938e4f4547a807dba3bb439da4405549d",
      "bytes": 138961
    }
  ],
  "estimated_tokens": 13485
}
-->

# Durable State Update — Chapter 442

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 442. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 442. Profile updates may replace only one
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
  "chapter": 442,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 442,
    "continuity_sources": [442],
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
    "Jin Taekyung has returned to Korea and received a globally broadcast welcome and car parade at Incheon attended by hundreds of thousands.",
    "Taekyung's public image now includes the nicknames King Taekyung, Lord Fuck, and Lord Sibu-leol.",
    "Taekyung's family was present for his return, and he is resolved to protect them from the dangers he has faced.",
    "Taekyung and Team Leader Choi have reaffirmed their ongoing cooperation and mutual support.",
    "The Skeleton King's undead identity remains concealed from the public, and he was hidden in Inventory during the parade.",
    "Taekyung has ordered the Skeleton King to join Peace Guild under an already prepared contract.",
    "Magic Johnson has publicly announced that he is pursuing an agreement with Peace Guild.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Go Jun's hatred of Jin Taekyung is overshadowed by fear and helplessness caused by their confrontation.",
    "Taekyung is training aboard the Water Dragon Stronghold to adapt to his opened Middle Dantian.",
    "Cheongpung is participating in Taekyung's training under Jeok Cheongang's supervision."
  ],
  "continuity_sources": [
    441
  ],
  "open_questions": [
    "Why does Mungyeong continue accompanying Jin Taekyung's group despite being unable to explain the impulse?",
    "How did Jin Taekyung actually open his Middle Dantian?",
    "What confidential matter is Jin Wikyung withholding?",
    "Are Taekyung's suspicions about the mysterious patterns and symbols found in both worlds correct?",
    "What agreement is Magic Johnson pursuing with Peace Guild, and what evidence is contained in Lee Jungryong's holographic recorder?"
  ],
  "safe_through": 441,
  "temporary_decisions": [
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi” and 진태경 씨 as “Mr. Jin Taekyung.”",
    "Keep Peace Guild, guild house, Inventory, and Magic Johnson as established terms.",
    "Render 명경지수 as “clear as a mirror and still as water” and 탄지 as “finger flick.”"
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
| 이정룡    | **Lee Jungryong** |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 화신귀무   | **Dance of the Fire God and Demon** |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 로그아웃             | **Logout**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 길드      | **Guild**             |
| 사천     | **Sichuan**            |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 산음 | **Saneum** | Jin Family branch location |
| 평화 | **Peace Guild** | Guild name. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 여사 | **Lady** | Taekyung's joking sobriquet for Kim Jeonghee. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |

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
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
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
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 430
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He and the Western Heaven Demon Lord serve the same master; he now seeks to personally kill Cheongpung, Jeok Cheongang, and Jin Taekyung, while his former contact Han Su is dead.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 441
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 441
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 436
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 436
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 441
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 441
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is Korea's publicly recognized representative S-rank Hunter.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 441
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 441
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 438
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 430
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃442화



도도하게 흐르는 장강의 강물처럼, 시간도 느리지만 꾸준히 흘렀다.

무림의 시간으로 사천을 떠난 지 나흘째에 접어든 늦은 오후. 갑판에 앉아 있던 내게 익숙한 인기척이 다가왔다.

“뭐 하십니까?”

발소리만 들어도 아는 놈이다.

나는 장강에서 눈을 떼지 않으며 대답했다.

“뭐 하는 것 같은데?”

절뚝거리며 다가온 혁무진이 망설임 없이 대답했다.

“그냥 앉아 계신 것 같은데요.”

“생각 중이야.”

“무슨 생각이요?”

“무림의 평화에 관한 생각.”

잠깐의 침묵이 흐른 뒤, 시원한 웃음이 터져 나왔다.

“푸하하! 올해 들은 농담 중에 제일 웃겼습니다. 역시 조장님.”

“아니다. 취소. 방금 다른 생각이 떠올랐다.”

“뭔데요?”

“내 말을 항상 개똥으로 알아듣는 놈이 하나 있거든? 근데 요즘 몸이 좀 나아져서 그런지 주둥이가 자제가 안 되는 것 같아. 그래서 몇 대 때려 줄까 고민 중인데, 넌 어떻게 생각하냐?”

잠시 고민하던 혁무진이 물었다.

“혹시 제가 생각하고 있는 그 사람은 아니죠?”

“맞을걸.”

“누군데요?”

“있어. 혁무진이라고.”

“…….”

“조용히 해라. 다시 찍먹 당하고 싶지 않으면.”

혁무진이 거의 경기를 일으키며 미친 듯이 고개를 끄덕였다.

“제발 그것만은……!”

며칠 전, 내가 장강 찍먹 형벌을 내린 뒤 곧바로 로그아웃한 덕분에 장장 한 시진 동안 장강 아쿠아리움을 구경한 혁무진이다.

문경의 뛰어난 의술로 몸이 어느 정도 회복되자마자, 그때 자신의 코를 깨문 놈들을 모조리 잡아 회를 쳐 버리겠다며 낚싯대를 드리우기도 했다.

“알겠으니까 진정하고. 왜 왔어?”

“예?”

“용건이 뭐냐고. 이유가 있을 거 아냐.”

혁무진이 섭섭함이 가득한 목소리로 물었다.

“아니, 우리 사이에 꼭 용건이 있어야 되는 겁니까?”

“없으면 찍먹.”

“있습니다! 있어요!”

“씨부려 봐.”

“이건 그냥 제 느낌일 수도 있는데…….”

혁무진이 우물쭈물 말을 이었다.

“요즘 무슨 고민이라도 있으세요?”

“왜?”

“그냥요. 근래에 조장님을 보고 있으면 고민이 많아 보이셔서.”

“내가?”

“네. 그리고 뭐랄까, 솔직히 말씀드리면 요즘은 전에 비해 별다른 일이 없는데. 희한하게 조장님만 혼자 지치고 바쁘신 느낌이라고 해야 하나?”

“……흠.”

“잠도 자주 주무시는 것 같고요.”

이 자식이 눈치가 언제 이렇게 늘었지?

묘한 내 시선에 혁무진이 뒤통수를 긁적였다.

“뭐, 그냥 그런 생각이 들었다고요. 아닙니까?”

“어. 아니야.”

당연히 내 대답은 거짓말이었고, 혁무진의 짐작은 정확했다.

처음으로 무림에 발을 디딘 이래, 요즘처럼 두 세상을 자주 오간 적은 없었다.

‘돌이켜보면 전부 다 내 선택이었지만.’

때로는 퀘스트가 로그아웃 기능을 막아 버리기도 했으나, 대부분은 나 스스로 내린 결정이었다.

살얼음판 위를 걷는 상황에서 다른 한 세상으로 넘어가 시간을 보냈다면 긴장감이 무너져 위기를 극복하지 못했을 테니까.

그러던 차에 상황이 변한 것은 최근의 일이었다.

‘현대도, 무림도 산 하나를 넘었지.’

두 세상이 동시에 조용해진 것이 얼마 만인가 싶다.

무림이야 처음부터 평지풍파가 끊이지 않는 지뢰밭이었고, 그나마 조용하던 현대에서도 이정룡과 갈등을 빚으며 시끄러워지기 시작했으니까.

실로 오랜만에, 아니 시스템을 얻은 이래 처음으로 찾아온 두 세상의 평화.

하지만 나는 내심 확신에 가까운 짐작을 하고 있었다. 지금의 평화는 오래가지 않으리라는 것을.

폭풍전야(暴風前夜). 내게 주어진 잠깐의 평화는 폭풍이 몰아치기 전날 밤의 고요함과 같다.

그렇기에 두 세상을 바쁘게 오가며 곧 들이닥칠 폭풍에 대비하는 것이고, 그것이 기가 막힌 장강의 절경을 눈앞에 두고도 풀리지 않는 수수께끼를 붙잡은 채 끙끙거리는 이유다.

‘도대체 이것의 정체가 뭘까.’

나는 손에 쥐어진 종이를 빤히 노려보았다.

그다지 질이 좋지 않은 화선지에는 내가 직접 그려 넣은 알 수 없는 문양과 기호로 가득했다.

종류도 다양하고, 형태도 미세하지만 제각각인 그것들은 추리소설에서나 보던 수수께끼 문자 같았다.

아니, 차라리 그랬으면 좋겠다. 이렇게 신경 쓸 일도 없을 테니까.

“그게 뭡니까?”

“폭풍.”

“예?”

“사실 나도 잘 몰라.”

아니, 이미 알고 있지만 믿고 싶지 않은 걸지도.

이 문양과 기호들은 시간의 흐름도, 역사도, 문화도 다른 두 세상의 유일한 교집합이다.

현대에서는 아크 리치의 마법진에서, 무림에서는 암천의 진법에서 발견되었다.

그리고 지금, 나는 마음 깊숙한 곳에서 한 단어를 만지작거리고 있었다.

‘흑마법.’

무림에서 말하는 사마외도(邪魔外道)의 무공. 흔히들 마공(魔功)이라 부르는 그것이 얼마나 괴이하며 광활한지 나는 모른다.

다만 돌이켜볼수록 내가 지금까지 직접 보고 겪었던 것들은 흑마법과 닮아 있었다.

‘혈주, 서천마군, 동굴에서 발견된 진법까지.’

적천강이 펼친 화신귀무에서 회복하는 혈주의 모습은 인간이 아닌 트롤과도 같았고, 서천마군이 숭배해 마지않던 암천의 천주(天主)는 이미 숨이 끊긴 수하의 몸을 빌려 나와 마주했다.

거기에 더해 각자의 우두머리들을 따라 소림과 사천을 피로 물들였던 흑의인들이 이용한 진법은 현대에서 워프 게이트(Warp Gate)라 부르는 그것과 놀랍도록 흡사하다.

‘이쯤 되면 의심이 들지 않는 게 이상할 정도지.’

동시에…… 쉽게 믿고 싶지 않은 것이 내 현실이었다.

무림에 흑마법이라니.

이건 마치 짝사랑하는 여사친이 집 화장실을 썼는데, 변기 커버가 올라가 있는 것보다 심각한 상황이다.

‘도대체 어디서, 어떻게, 왜?’

머릿속에는 물음표로 가득했다. 현대에서는 이미 조사가 진행 중이지만, 나는 끝이 보이지 않는 안개 속에서 헤매는 기분이었다.

그리고 그보다 더 두려운 것은, 아직 모습을 나타내지 않은 채 안개 너머에 도사리고 있는 정체 모를 무언가였다.

만약 내가 생각하는 모든 불안감이 모두 사실이라면, 그때는…….

“뭘 그렇게 열심히 보고 있는 거지?”

순간, 깊은 상념을 깨트리는 목소리에 정신을 차린 나는 눈살을 찌푸렸다.

생각이 끊겨서가 아니라 코를 찌르는 쉰내 때문이었다.

본능적으로 올라오는 헛구역질을 참으며 물었다.

“너, 또 안 씻었냐?”

은근슬쩍 옆자리에 엉덩이를 붙인 궁기방이 고개를 끄덕였다.

“거지가 안 씻는 건 당연한 이치인데, 무슨 문제라도?”

혁무진이 메슥거리는 표정으로 입을 열었다.

“궁 소협, 혹시 독인(毒人)입니까? 반경 삼 장 안으로 들어오자마자 머리가 핑 돌고 헛구역질이 나요.”

“개방도는 살면서 단 세 번만 씻는다. 태어났을 때, 개방에 입문했을 때, 그리고 죽었을 때.”

나는 개소리를 지껄이는 궁기방을 향해 말했다.

“그럼 당장 죽여 버리기 전에 빨리 강물에 몸 한번 담그고 와. 기왕 하는 거 때도 좀 밀고.”

“싫다. 물이라면 질색이야. 특히 그날 이후로는.”

아. 저놈도 찍먹 피해자였지, 참.

정색한 얼굴로 대답한 궁기방이 내가 들고 있는 종이를 힐끔거렸다.

“또 그걸 보고 있었나?”

“또? 궁 소협은 알고 계셨어요?”

혁무진의 물음에 궁기방이 고개를 끄덕였다.

“당연하지. 며칠 전에 갑자기 따라오라더니 보여 주던데. 혹시 어디서 본 적 있냐고. 물론 난생처음 본다고 했지.”

“조장님. 이런 식으로 사람 차별하기 있습니까?”

나는 섭섭해하는 혁무진에게 따뜻한 미소를 지어 주었다.

“응. 있어.”

“…….”

“후개라서 보여 줬다. 혹시 알까 싶어서. 됐냐?”

혁무진을 놀릴 거리를 잡은 궁기방이 낄낄거리며 말했다.

“문경. 그 녀석한테도 보여 주던데?”

“야, 그건…….”

막상 입을 열긴 했는데, 문경의 정체를 까발릴 수는 없는 노릇이라 입을 다물었다.

몇 장 떨어진 곳에서 이쪽을 바라보며 의미심장하게 대침을 쓰다듬는 문경의 모습을 봤기 때문만은 아니다.

……진짜로.

“봐라, 혁가 놈아. 이게 네 녀석의 위치다. 심장이 아니라 새끼발가락, 어억!”

덥석, 후웅!

듣고 있자니 시끄러워서 귀가 아플 지경이라, 궁기방의 멱살을 붙잡아 난간 밖으로 내던졌다. 허공을 허우적거리던 녀석은 외마디 비명과 함께 강물에 처박혔다.

풍덩!

제법 강하게 떨어졌는지, 물보라가 배 난간까지 튀었다.

그리고 다음 순간, 깜짝 이벤트에 까르륵 웃고 있던 청풍이 돌연 비명을 내질렀다.

“안 돼! 미미야!”

뭔데, 또.

무슨 일인가 싶어 자세히 바라본 나는 내 눈을 의심했다.

머리부터 꼬리까지 온통 새하얀, 뿔 달린 뱀 한 마리가 지랄 발광을 떨면서 이쪽을 향해 필사적으로 헤엄치는 중이었다.

맑은 장강의 강물은 궁기방의 몸을 중심으로 시커멓게 오염되고 있었고, 인근을 평화롭게 헤엄치던 물고기 몇 마리가 배를 까뒤집고 둥둥 떠다녔다.

“……뭐여, 시벌.”

천년 독각사까지 저런 반응이라니. 혁무진 말대로 진짜 독인인가.

이 말도 안 되는 수질 오염 광경을 실시간으로 목격한 수적들은 심각한 표정으로 궁기방의 소속이 개방인지 사천당문인지 토의를 벌였다.

깊은 한숨을 내쉰 내가 그들을 향해 손짓했다.

“빨리 건져요. 앞으로도 계속 장강에서 수적질 하고 싶으면.”

생활 터전이 위협받고 있다는 걸 깨달은 수적들은 부산스럽게 움직였다.



* * *



나는 그 후에도 하루에 한 번, 혹은 몇 번씩 현대와 무림을 오고 가며 해야 할 일을 처리하고 조사를 이어 나갔다.

내가 소속된 평화 길드와 매직 존슨이 이끄는 위저드(Wizard) 길드가 모종의 협약을 맺었다는 이야기는 전 세계의 헌터들 사이에서 상당한 화제가 되었다.

그러나 일반인들에게 있어 더욱 큰 사건은 역시 바로 나, 진태경이라는 개인에 관한 것이었다.



[세계 헌터 협회, “진태경은 누구도 부정할 수 없는 S급 헌터이자 수많은 인명을 구한 영웅. 그런 그가 아직도 A급 헌터라는 건 어불성설.” 협회 본부에 방문하여 간략한 테스트 후 S급 헌터 라이센스 발급 예정. 세계 헌터 협회의 진한 러브 콜!]

[속보) 진태경, 협회의 제안을 단칼에 거절. “지금은 사정이 있어 가기 어렵다. 나중에 시간 나면 들르겠다.” 당황한 세계 헌터 협회.]

[세계 헌터 협회, 새로운 입장 발표. “이는 전례 없는 일이다. S급 헌터의 테스트와 발급은 항상 협회 본부에서 치러졌다.”]

[진태경, “테스트를 안 받겠다는 게 아니라, 나중에 간다고 했다. 그리고 한국에서 테스트받으면 되는 건데 뭐가 문제냐. 전례 따지기 전에 좀 효율적으로 하자.]

[자존심 상한 헌터 협회 고위 간부의 으름장. “그럼 S급 헌터 라이센스를 발급할 수 없다.”]

[긴급 속보) SNS로 올라온 짤막한 글. “그럼 하지 말든가. 어디서 협박질이야. 시부럴 거.” 알고 보니 진태경의 공식 SNS로 밝혀져…… 대중들의 반응은? ‘완전 사이다.’, ‘천리행군 때 마셨던 탄산음료보다 시원하다.’]

[세계 헌터 협회, “해당 간부의 발언은 단체가 아닌 개인의 실언. 사과드린다.” 진태경을 위해 한국으로 테스트팀 파견 최종 결정.]

[日고이즈미 총리. “진태경은 펀하고 쿨하며 섹시하다. 반드시 그를 일본으로 귀화시키겠다. 그것이 ‘약속’이니까…….”]



나를 둘러싼 수많은 사건과 말들을 뒤로하고, 나는 다시 무림으로 돌아왔다.

그리고…….

“이제야 좀 살겠군. 염병할 장강.”

속 시원한 적천강의 말과 함께, 장장 열흘에 가까운 항해를 이어간 쾌조선의 뱃머리가 호북성에 접어들었다.
```

## Final English reading copy

```markdown
# Chapter 442

Like the Yangtze flowing majestically onward, time passed slowly but steadily.

It was late afternoon on the fourth day since we had left Sichuan by Murim reckoning. As I sat on the deck, a familiar presence approached.

“What are you doing?”

I knew who it was just from the footsteps.

Without taking my eyes off the Yangtze, I answered,

“What does it look like I’m doing?”

Hyuk Mujin approached with a limp and answered without hesitation.

“Looks like you’re just sitting there.”

“I’m thinking.”

“About what?”

“About the peace of Murim.”

After a brief silence, a hearty laugh burst out.

“Pfft-hahaha! That’s the funniest joke I’ve heard all year. Just like you, Captain.”

“No. I take it back. I just thought of something else.”

“What?”

“There’s a certain bastard who always takes everything I say for dog shit. But maybe because he’s been feeling better lately, he doesn’t seem able to control his mouth. So I’m wondering whether I should beat him a few times. What do you think?”

Hyuk Mujin thought for a moment before asking,

“It isn’t the person I’m thinking of, is it?”

“Probably.”

“Who is it?”

“There is someone. A man named Hyuk Mujin.”

“…”

“Be quiet unless you want another taste of the Yangtze.”

Hyuk Mujin nodded frantically, practically having a seizure.

“Please, anything but that…!”

A few days earlier, after sentencing him to the Yangtze-dipping punishment, I had immediately logged out, leaving Hyuk Mujin to spend an entire shichen sightseeing at the Yangtze Aquarium.

The moment Mungyeong’s superb medical skills had restored him to a reasonable condition, he had even cast out a fishing line, declaring that he would catch every last one of the bastards who had bitten his nose and turn them into sashimi.

“Fine, calm down. Why are you here?”

“Huh?”

“I’m asking what you want. You must have a reason.”

Hyuk Mujin asked in a wounded voice,

“Do I really need a reason to come see you? Between us?”

“If you don’t have one, you get a taste of the Yangtze.”

“I do! I have one!”

“Then spit it out.”

“This might just be my impression, but…”

Hyuk Mujin continued hesitantly.

“Have you been worried about something lately?”

“Why?”

“Just because. Recently, whenever I look at you, you seem like you have a lot on your mind.”

“I do?”

“Yes. And, well… To be honest, nothing particularly significant has happened lately compared to before. But somehow, you’re the only one who seems tired and busy. That’s the best way I can put it.”

“…”

“You also seem to be sleeping more often.”

When had this bastard gotten so perceptive?

Under my strange gaze, Hyuk Mujin scratched the back of his head.

“Well, that’s just the impression I got. Am I wrong?”

“Yeah. You are.”

Naturally, my answer was a lie, and Hyuk Mujin’s guess was exactly right.

Since first setting foot in Murim, I had never gone back and forth between the two worlds as often as I had recently.

*Looking back, every one of those trips was my own choice.*

Sometimes a Quest had blocked the Logout function, but most of the time, I had made the decision myself.

If I had crossed over to the other world and spent time there while walking across thin ice, my tension would have collapsed, and I would have been unable to overcome the crisis.

But recently, the situation had changed.

*Both the modern world and Murim have made it over one mountain.*

How long had it been since both worlds had grown quiet at the same time?

Murim had been a minefield where disturbances never stopped from the beginning, while even the relatively peaceful modern world had begun to grow chaotic after my conflict with Lee Jungryong.

For the first time in a long while—or rather, for the first time since I had obtained the System—I had found peace in both worlds.

But deep down, I had a suspicion bordering on certainty.

The current peace would not last long.

The calm before the storm. The brief peace I had been given felt like the stillness on the night before a storm broke.

That was why I was busily traveling between the two worlds to prepare for the storm that would soon arrive. It was also why, even with the spectacular Yangtze scenery spread out before me, I was hunched over a mystery that refused to yield.

*What the hell is this, anyway?*

I stared intently at the paper in my hand.

The not particularly high-quality xuan paper was covered with strange patterns and symbols I had drawn myself.

They came in various types and forms. Though each differed only slightly, they looked like mysterious letters from a detective novel.

No. I would almost prefer that to be the case. Then I wouldn’t have to worry about them this much.

“What is that?”

“A storm.”

“Huh?”

“To be honest, I don’t really know either.”

No, perhaps I already knew and simply did not want to believe it.

These patterns and symbols were the only common ground between two worlds whose flow of time, history, and culture were all different.

In the modern world, they had been found in the Arch Lich’s magic circle. In Murim, they had appeared in Dark Heaven’s formations.

And now, deep in my heart, I was turning over a single word.

*Black magic.*

The martial arts of those Murim deemed demonic and heterodox—what people commonly called demonic martial arts. I had no idea how bizarre or far-ranging they could be.

But the more I looked back on everything I had personally seen and experienced, the more it resembled black magic.

*The Blood Lord, the Western Heaven Demon Lord, even the formation found in the cave.*

The way the Blood Lord recovered from Jeok Cheongang’s Dance of the Fire God and Demon was like that of a Troll, not a human. The Lord of Heaven worshiped by the Western Heaven Demon Lord had appeared before me by borrowing the body of a subordinate who was already dead.

On top of that, the formations used by the black-robed men who had stained Shaolin and Sichuan with blood in service to their respective leaders were astonishingly similar to what the modern world called a Warp Gate.

*At this point, it would be strange not to have suspicions.*

At the same time… the fact that I did not want to believe it easily was my reality.

Black magic in Murim.

It was more serious than discovering that a female friend I had a crush on had used the bathroom in my house and left the toilet seat up.

*Where? How? Why?*

My head was full of question marks. An investigation was already underway in the modern world, but I felt like I was wandering through fog with no end in sight.

And even more frightening was the unknown something waiting beyond that fog, still refusing to reveal itself.

If every one of my fears turned out to be true, then…

“What are you looking at so intently?”

The voice shattered my deep thoughts and brought me back to reality. I frowned.

Not because my train of thought had been interrupted, but because of the sour stench stabbing at my nose.

Suppressing the nausea rising instinctively, I asked,

“Did you not wash again?”

Gung Gibang, who had subtly pressed his butt against the spot beside me, nodded.

“It’s only natural for a beggar not to wash. Is there a problem?”

Hyuk Mujin opened his mouth with a queasy expression.

“Young Hero Gung, are you perhaps a poison human? The moment you came within three jang of me, my head started spinning and I began dry-heaving.”

“A Beggars’ Sect disciple washes only three times in his life: when he is born, when he enters the Beggars’ Sect, and when he dies.”

I spoke to Gung Gibang, who was spouting bullshit.

“Then go dunk yourself in the river before I kill you right now. And since you’re doing it anyway, scrub off some of that grime while you’re at it.”

“No. I hate water. Especially since that day.”

Ah. Right. He was a victim of the Yangtze, too.

Gung Gibang answered with a severe expression, then glanced at the paper in my hand.

“Were you looking at that again?”

“Again? Young Hero Gung, you knew about it?”

At Hyuk Mujin’s question, Gung Gibang nodded.

“Of course. A few days ago, he suddenly told me to follow him and showed it to me. He asked whether I had ever seen it somewhere before. Naturally, I told him I was seeing it for the first time.”

“Captain, is this how you discriminate between people?”

I gave the wounded Hyuk Mujin a warm smile.

“Yes. It is.”

“…”

“I showed it to you because you’re the Successor Beggar. I thought you might know something. Satisfied?”

Gung Gibang, who had found something to tease Hyuk Mujin about, snickered.

“He showed it to Mungyeong, too.”

“Hey, that’s…”

I had opened my mouth, but I could not reveal Mungyeong’s identity, so I shut it again.

It wasn’t only because I saw Mungyeong several jang away, watching us as he pointedly stroked a large acupuncture needle.

*Seriously.*

“Look, you Hyuk bastard. This is where you stand. Not in the heart, but in the little toe. Ow!”

*Grab—whoosh!*

Listening to him had become so irritating that my ears hurt. I grabbed Gung Gibang by the collar and threw him over the railing.

He flailed in midair, then crashed into the river with a single shriek.

Splash!

He must have hit the water fairly hard, because the spray reached the ship’s railing.

Then, in the next moment, Cheongpung, who had been giggling at the surprise event, suddenly screamed.

“No! Mimi!”

What now?

Wondering what had happened, I looked more closely and doubted my eyes.

A horned snake, pure white from head to tail, was swimming desperately toward us while thrashing around like a lunatic.

The clear waters of the Yangtze were turning pitch-black around Gung Gibang’s body, and several fish that had been swimming peacefully nearby were floating belly-up.

“…What the fuck?”

Even the Thousand-Year Poison Horned Snake was reacting like that. Was Hyuk Mujin right? Was Gung Gibang really a poison human?

The river bandits who witnessed this utterly absurd water-pollution spectacle in real time began seriously debating whether Gung Gibang belonged to the Beggars’ Sect or the Sichuan Tang Clan.

I let out a deep sigh and gestured toward them.

“Get him out quickly. If you want to keep working as river bandits on the Yangtze.”

The river bandits realized that their livelihood was under threat and began bustling about.

* * *

After that, I continued traveling between the modern world and Murim once or several times a day, taking care of what needed to be done and continuing my investigation.

News that my Peace Guild and the Wizard Guild led by Magic Johnson had entered into some sort of agreement became a major topic of conversation among Hunters around the world.

But to ordinary people, the bigger story was still about me, the individual named Jin Taekyung.

> World Hunter Association: “Jin Taekyung is an undeniable S-rank Hunter and a hero who has saved countless lives. It is absurd that he is still only an A-rank Hunter.” He is scheduled to visit the Association headquarters for a brief test, after which his S-rank Hunter license will be issued. A passionate personal invitation from the World Hunter Association!

> Breaking News: Jin Taekyung flatly rejects the Association’s offer. “I have circumstances that make it difficult to go right now. I’ll stop by when I have time.” The World Hunter Association is thrown into confusion.

> World Hunter Association issues a new statement: “This is unprecedented. S-rank Hunter testing and licensing have always been conducted at the Association headquarters.”

> Jin Taekyung: “I didn’t say I wouldn’t take the test. I said I’d go later. And I can take the test in Korea, so what’s the problem? Before you start talking about precedent, let’s try doing things efficiently.”

> A senior Hunter Association official, wounded in his pride, issues a threat: “Then we cannot issue you an S-rank Hunter license.”

> Urgent Breaking News: A brief post uploaded to social media reads, “Then don’t. Where do you get off threatening me? Sibu-leol.” The account is revealed to be Jin Taekyung’s official social-media account… How is the public reacting? “That’s so satisfying.” “Cooler than the soda we drank during the Thousand-Li March.”

> World Hunter Association: “The official’s statement was a personal slip, not the position of the organization. We apologize.” Final decision made to dispatch a testing team to Korea for Jin Taekyung.

> Japanese Prime Minister Koizumi: “Jin Taekyung is fun, cool, and sexy. I will definitely have him naturalized as a Japanese citizen. Because that is my ‘promise’…”

Leaving behind the countless incidents and remarks surrounding me, I returned to Murim.

And then…

“I can finally breathe again. Damn Yangtze.”

Alongside Jeok Cheongang’s heartfelt exclamation, the bow of the fast ship that had continued its voyage for nearly ten full days entered Hubei Province.
```

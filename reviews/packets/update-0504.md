<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0504.txt",
      "sha256": "2b7bf85964fee7cb70ad8c1b3dff0aa6462fcf749cfe894f2f92bb789a7f81d8",
      "bytes": 13356
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "154aa25facfa3b583d3cf4ff37c73593dac45824ec6b2402d449aaa582d3a566",
      "bytes": 5594
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f540186e8a90a2365e166db3d9158c7729a3d7f452dbe7883ad442de846bfb11",
      "bytes": 160679
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "eaba11428929a7c7b9eb95d1ff6b35ebde728e7688d0e87c9a3aea342529d215",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "7e861e915b3eaef36497bf80b2d9896c3602c623b6bee6c880293dead4ec08cd",
      "bytes": 686
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "adda427e9d31b0e2a74324fd9544991db9803dcc5fc1bd6cc67ef8e7548650b8",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "0456eb089952d62acf63b7a03a0cdcfcf94ea4186379c06b9bb423fcd0871d24",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b6adc5d458cf281c5117cc4f2cf4ba585dac16d1024b60ae426623d65de72473",
      "bytes": 1777
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "03d104a088ac93df12a135207f42e20d46d0a604b60c798e4511bd32e3b97ca3",
      "bytes": 1210
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "28ecd7ec4c920677357e30d77e4923c51c3119a41c7d55f14b7c4bee6abae8ed",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "748c60ad6275677a0889e320759d914aedc9bee54af2bdf8d93db78d1e52bd06",
      "bytes": 916
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "0baee639f59168a7c74ad8572bb370eab2c56b3d24dfb9250930f985e2a20852",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "eebb6a55d417a0bf58918cb43c8dd3bd0a4d194812edee7631ef94a7e3eedbb2",
      "bytes": 153941
    }
  ],
  "estimated_tokens": 14156
}
-->

# Durable State Update — Chapter 504

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 504. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 504. Profile updates may replace only one
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
  "chapter": 504,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 504,
    "continuity_sources": [504],
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
    "Jeok Cheongang's infirmities of old age began immediately after he left Sichuan; his leaking innate qi causes progressive memory and time loss, with seven external days experienced as five days by Jeok in this episode.",
    "Jeok Cheongang is pursuing enlightenment through secluded meditation because acquired qi from elixirs cannot restore the balance disrupted by his leaking innate qi.",
    "Mungyeong indirectly rejects Jeok Cheongang's plan to leave Jin Taekyung, and Jeok recognizes the plan as proud self-denial rather than a pure effort to protect his Disciple.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master whose assassin instincts remain formidable despite decades spent living as a medical apprentice.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun, and the New Murim Alliance is scheduled to be founded at Mount Song in one month, with Taekyung believing Dark Heaven deliberately planned the Gate incident.",
    "Jin Wikyung proposed the Hubei political arrangement through Hongcheon, the new Provincial Administration Commissioner and Prince Shangshan's hidden loyal retainer; the purge of Hubei's dark-path figures was intended to create an opportunity for rival unorthodox factions while warning them.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has broken free of those chains and risen with wind surging outward around him."
  ],
  "continuity_sources": [
    503,
    502
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the fractured unorthodox factions accept the New Murim Alliance's invitation instead of joining Dark Heaven?",
    "What lasting change will follow Jeok Cheongang's apparent breakthrough after his Heart Demon was expelled?"
  ],
  "safe_through": 503,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher’s Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, 변이된 송사리 as Mutated Minnow, 왜국 as Wa Kingdom, 인자 as ninja, and 절강 as Zhejiang; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, 천기 as heavenly patterns, and 후천지기 as acquired qi.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, 진룡 as Jin Dragon, 마봉진 as Demon-Sealing Formation, 철기당 as Ironcraft Hall, 철기당주 as Master of Ironcraft Hall, 신룡 as Divine Dragon, 신(新) 무림맹 as New Murim Alliance, 면벽수련 as secluded meditation, 호법 as stand guard, 한나절 as half a day, 일다경 as the time it takes to drink a cup of tea, 촌각 as moments, 진맥 as take one's pulse, 은영술 as concealment techniques, 표창 as throwing blades, and 철구 as iron balls."
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
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 평화 | **Peace Guild** | Guild name. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 궁기방 | 진위경 | martial_companion_to_family_head | Great Hero Jin | familiar and polite | Asks Jin Wikyung not to exclude the Beggars' Sect from the defense. |
| 제갈풍 | 진위경 | Zhuge Clan Family Head to Jin Family Lesser Family Head | Lesser Family Head | formal and conciliatory | Uses 소가주 while trying to secure Jin Wikyung's support during the settlement. |
| 진위경 | 제갈풍 | Jin Family Lesser Family Head to Zhuge Clan Family Head | Sir Zhuge | formal with deliberate comic deference | Uses 제갈 대협 while theatrically scolding Taekyung to force Zhuge Feng to concede. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 503
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 498
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 501
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 503
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 503
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 501
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung's eldest brother and future Family Head who protects and mentors him, commands Wipeng and the Jin Family's forces, has worked with Jeok Cheongang, and maintains a political connection with Hongcheon, Prince Shangshan's hidden loyal retainer; Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 503
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 503
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, and Mungyeong has completed his poisoned tests of Taekyung’s basics without a formal Master-Disciple relationship and intends to teach him secret martial arts.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 501
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃504화



깨달음은 생각지도 못한 순간에 찾아온다.

주위의 모든 것을 잊은 무아(無我)의 상황에서, 죽음을 코앞에 둔 절박한 상황에서, 혹은…… 수십 년간 심신을 옥죄고 있던 사슬을 벗어던졌을 때.

그렇게 깨달음은 찾아온다.

콰아아아아!

한 사람으로부터 흘러나온 기의 바람이 사방을 휩쓸었다.

빛이 들어오지 않아 컴컴한 동굴 내부는 어느덧 빛무리로 환하게 밝혀져 있었다.

그 기이한 광경을 말없이 바라보던 소년, 문경의 입술 사이로 나직한 목소리가 흘러나왔다.

“마침내…… 심마(心魔)에서 벗어났는가.”

처음부터 의도했던 일은 아니었다. 단지 알려 주고 싶었을 뿐이었다.

적천강은 혼자가 아니라는 사실을. 모든 고민과 부담을 떠안은 채 스스로를 고립시킬 필요는 없다는 것을.

그리고 그 결과는 생각했던 것 이상이었다.

화왕(火王)이라 불리는 초절정 고수는 오랜 세월 자신을 옥죄고 있던 사슬을 깨트리고, 새로운 경지로 발돋움하고 있었다.

“괜한 오지랖은 아니었던 모양이군.”

낮게 뇌까리는 문경의 눈빛에는 복잡한 감정이 뒤섞여 있었다.

어찌하여 자신이 적천강을 찾아왔는지, 별다른 친분도 없는 그를 도왔는지 모를 일이었다.

아니, 설령 알았다 하더라도 모르는 척했을 것이다. 그는 그런 사람이었으니까. 일평생을 그렇게 살아왔으니까.

하지만…….

‘썩 나쁘지 않은 기분이야.’

문경은 알지 못했다. 자신도 모르는 사이에 희미한 웃음이 입가를 스쳤다는 것을.

그리고 이런 일이 며칠 전에도 한 번 있었다는 사실을.

그건 문경이 인식하지 못할 만큼 짧은 순간 일어난 일이었고, 이내 천천히 돌아선 그는 비좁은 동굴 밖 세상으로 발을 내디뎠다.

솨아아아.

때마침 불어온 바깥의 바람이 머리카락을 흔들고 코를 간지럽힌다.

동굴 주변에 무성하게 자라난 잡초와 꽃. 그리고 어느새 모여든 들짐승들을 말없이 바라보던 문경이 문득 입을 열었다.

“호법(護法)이 필요하겠군. 아무것도 모르는 들짐승들이 동굴 안으로 들어간다면 애써 얻은 깨달음도 허사가 될 테니까.”

꾸익?

잠든 어미 곁에서 풀을 뜯고 있던 새끼 노루가 귀를 쫑긋 세웠다.

경계와 호기심이 뒤섞인 짐승들의 시선 속, 문경은 고개를 들어 푸른 하늘을 바라보았다.

“좋은 날이다. 이런 날씨에 동굴 안에 처박혀 있을 수는 없지.”

저벅.

혼잣말처럼 중얼거린 문경은 빠르지도, 느리지도 않은 걸음으로 걷기 시작했다.

동굴을 뒤로한 채 어딘가로 사라지는 그를 배웅하듯 다시 한번 바람이 불어왔다.

솨아아아.

구름 한 점 없이 청명한 하늘, 시원한 바람. 평화로운 자연과 풀꽃들 사이에 누워 다 함께 햇빛을 즐기는 들짐승들.

그리고…… 차마 안으로 들어오지 못하고 밖을 서성이던 누군가.

‘스승이나, 제자나.’

아무리 생각해도 닮았다. 저 두 사람은.

소리 없이 웃는 문경의 어깨 위에 나풀거리며 날아온 나비 두 마리가 내려앉았다.

참으로 좋은, 어느 날이었다.



* * *



태어난 지 얼마 되지 않은 새끼 노루는 호기심이 많았다.

나비를 쫓아 폴짝폴짝 뛰기도 하고, 무성하게 자라난 풀과 꽃에 까만 코를 들이밀고 킁킁 냄새를 맡기도 했다.

그리고 언제나 그렇듯, 금세 호기심을 잃어버리고 다음 할 일을 찾아 서성거리고는 했다.

꾸익?

하지만 이번에는 달랐다.

새카만 동혈(同穴)의 입구는 빨려 들어갈 것처럼 매혹적이었고, 육아 활동으로 지친 어미는 잠들어 있었다.

그리고 결정적으로, 난생처음 보는 괴상한 두 발 짐승은 어느새 저 멀리 사라진 후였다.

꾸익.

저긴 뭘까. 들어가고 싶은데.

꾸익!

그래, 가 보자!

그러나 새끼 노루의 굳은 결심은, 불과 풀 몇 번 뜯을 만큼 짧은 시간 만에 좌절되고 말았다.

저벅.

갑작스럽게 들려온 인기척과 함께 동그란 머리 위로 드리워진 그림자.

화들짝 놀라 뒷걸음질 친 새끼 노루의 검은 눈동자에 커다란 인영이 비쳤다.

“지금은 안 돼. 나중에 들어가자.”

겁먹은 새끼 노루의 머리를 슥슥 쓰다듬은 인영은 새카만 동혈을 물끄러미 바라보았다.

본능적으로 어미를 깨우려던 새끼 노루가 울음소리를 삼킬 만큼, 낯선 이방인의 눈빛은 깊게 가라앉아 있었다.

꾸이익.

“그래, 착하지. 이제 어미 곁으로 가라.”

고개를 갸웃거린 새끼 노루가 잠든 어미에게 다가가는 것을 지켜본 인영이 굽혔던 허리를 폈다.

이내 동굴을 향해 내디딘 그의 발걸음은 곧았고, 바람에 섞여든 목소리는 흐릿했다.

“이제…… 나도 가 봐야겠다.”

동굴까지 가는 길은 멀었다.

노인과 청년이 처음으로 만났던 그 날로부터 일 년 하고도 수개월.

먼 길을 돌아 그들은 마침내 다시 만날 수 있었다.

앞과 뒤가 아닌, 그저 어깨를 맞대고 나란히.



* * *



“진태경, 이놈은 도대체 언제 오는 거야?”

짜증 섞인 표정으로 투덜거리는 궁기방의 모습에, 혁무진이 혀를 찼다.

“쯧쯧. 성질이 그리 급해서 구걸이나 하겠습니까? 좀 진득하게 기다려 보십쇼.”

“혁가 새끼 말하는 본새 보게. 거지는 성격도 급하면 안 되냐?”

“인내심을 가져야 철전 하나라도 적선 받을 것 아닙니까.”

“혁가 포목점이라고 했나. 십만 개방도가 찾아가서 똥 한 번씩 싸질러 줘?”

“……가족은 건드리지 맙시다.”

“그럼 주둥이 조심해. 우리 애들이 돈이 없지, 똥이 없는 줄 알아?”

혁무진이 혐오 섞인 표정으로 궁기방을 바라보았다.

“미치겠네. 막 밥 먹었는데 더럽게 왜 똥 싸는 얘기를 해요. 곧 배도 타야 하는데.”

“그러니까 혁가 포목점이 똥 범벅되기 전에…….”

“아, 그만하시라니까! 똥 먹은 다음에 밥 얘기 들으면 속 안 좋아진다고요!”

“……?”

“……?”

뭔가 이상함을 느낀 두 사람이 고개를 갸웃거리는 사이, 진위경은 한 사람을 향해 묻고 있었다.

“이보게, 곧 오는 것이 확실한가?”

신의의 제자로 알려진 소년 의생, 문경이 공손하게 고개를 숙였다.

“예. 진 공자님께서 분명 그리 말씀하셨습니다.”

“해가 지기 전에는 출발해야 할 터인데…….”

진위경은 서서히 붉게 물들어가는 하늘을 바라보며 중얼거렸다.

하남에서 있을 신(新) 무림맹 선포식이 고작 달포 뒤다. 도중에 일어날 만일의 사태를 염두에 둔 채 지금부터 부지런히 가야 시일에 맞출 수 있었다.

‘아니지. 그나마 적 대협을 모시고 가게 되었으니 다행으로 생각해야지.’

벌써 칠주야 동안 두문불출한 적천강에 대해서는 여러 가지 소문들이 무성했다.

마침내 깨달음의 단초를 얻었다는 희망찬 이야기부터 혹 건강에 문제가 생긴 게 아니냐는 불경한 말도 있었고, 별다른 이유 없이 그냥 모습을 드러내지 않는 거라고 주장하는 사람도 있었다.

셋 중 어느 것이 진실인지는 진위경도 알 수 없었지만, 그가 남몰래 마음을 졸였던 것은 틀림없는 사실이었다.

‘만에 하나 무림맹에 참여하지 않겠다고 하시면 어쩌나 했는데…… 막내가 잘 설득한 모양이로군.’

대부분의 정파 무림인들이 잊고 있던 사실이나, 화왕 적천강은 본래 정사마(正邪魔) 어디에도 속해 있지 않은 정사지간의 무림인이었다.

이는 수백 년간 일인전승으로 명맥을 이어 온 열화문의 근간이기도 했으며, 역대 문주들은 어디에도 속하지 않은 중도의 자세를 강대한 무위로 지켜 냈다.

‘하물며 바로 그 적 대협이니.’

화왕 적천강이 정파를 도와 정마대전을 승리로 이끌었다는 사실은 코흘리개도 아는 사실이다.

하지만 이 전전대의 초절정 고수가 정마대전 중에도, 그리고 후에도 정파에 적잖은 실망을 했다는 건 잘 알려지지 않은 이야기였다.

“그러고 보니 문득 조부님께서 적 노선배에 대해 하셨던 말씀이 떠오르는구려.”

배웅을 위해 나와 있던 제갈풍의 말에, 진위경의 귀가 움찔거렸다.

“적 대협에 대해 말입니까?”

“그렇소.”

“전대 가주께서는 지혜롭고 뛰어난 통찰력을 지니신 분이었다고 들었지요. 혹 그분께서 무슨 말씀을 하셨는지 여쭈어도 되겠습니까?”

“그게 그러니까, 본인이 열세 살 때 가주 전에서 들었던 이야기였소.”

“그렇군요. 그래서 무슨 말씀을…….”

“똑똑히 기억나는군. 그때 조부님께서 정마대전 당시의 일을 이야기 중이었는데. 아, 혹시 사천에서 벌어진 대혈전에서 본가의 식솔들이 크게 활약한 이야기를 들어 보았소?”

우드득.

느긋하게 부채질을 하던 제갈풍이 멈칫했다.

힘껏 쥐어진 진위경의 주먹과 벌겋게 달아오른 얼굴을 번갈아 바라보던 그가 슬그머니 부채를 내렸다.

무공이야 전혀 꿇릴 게 없지만, 진위경은 겉모습 자체만으로도 인간 흉기나 다름없었다.

게다가 무가지보(無價之寶)이라 할 수 있는 수신룡의 사체를 양손에 틀어쥔 절대 갑이 아닌가.

슬쩍 눈치를 살핀 제갈풍은 헛기침과 함께 입을 열었다.

“크흠. 어쨌건 그때 본인이 먼저 여쭤보았소. 조부께서 생각하시기에, 가장 처음 정파로 승기가 기울기 시작한 것이 언제냐고.”

진위경이 착 가라앉은 목소리로 물었다.

“혹시 사천에서 벌어진 대혈전에서 제갈세가의 식솔들이 큰 역할을 했기 때문입니까?”

“아니, 그게 아니오! 정말 아니오!”

“그거 다행이군요. 계속 들려 주시지요.”

제갈풍은 불끈 쥐어진 주먹을 곁눈질하며 말문을 열었다.

“조부께서 그리 고민하시는 모습은 그것이 처음이자 마지막이었소. 한참을 생각한 끝에 하신 말씀이 뭔지, 소가주는 짐작 가는 바가 있소?”

“앞서 가주께서 적 대협과 연관이 있다 하셨으니…… 아무래도 과거 섬서에서 벌어졌던 대전(大戰)이 아니겠습니까. 다른 대선배들께서도 큰 활약을 하셨지만, 적 대협께서 세우신 전공은 그야말로 엄청났다고 들었습니다.”

방금 진위경이 말한 섬서에서의 일은 피로 얼룩진 정마대전의 숱한 전투 중에서도 유독 빛나는 승리였다.

진위경으로서는 나름 고민한 끝에 나온 대답이었으나, 제갈풍은 피식 웃으며 고개를 저었다.

“틀렸소.”

“그럼 무엇입니까?”

“안휘성(安徽省).”

“안휘성이라면…… 혹시 그?”

“맞소. 안휘성을 가로지르던 마교의 정예, 흑풍단(黑風團) 일천 명이 단 한 사람의 손에 의해 전멸할 줄은 그 누구도 예상치 못했소. 심지어는 내 조부께서도 마찬가지셨지.”

진위경이 고개를 끄덕였다.

구화산이 화마에 휩싸인 그 날, 초야에 묻혀 살아가던 이름 모를 노인은 화왕(火王)이라 불리게 되었고 마교는 정마대전의 개전(開戰)이래 숱한 전공을 쌓아올린 정예 타격대를 잃었다.

“그것이라면 수긍이 가는군요. 아무래도 적 대협께서 처음 세상에 나왔을 때의 일이니.”

“하지만 지혜롭고 현명하신 조부님의 판단이 아니었다면, 흑풍단의 궤멸은 물론 적 노선배께서도 화왕이라는 별호를 얻지 못했을 거요.”

“그게 무슨…….”

주위를 둘러본 제갈풍이 한껏 목소리를 죽였다.

“당시 흑풍단에게는 안휘의 모든 길이 열려 있었소. 굳이 구화산을 지나쳐 올 필요가 없었단 말이지.”

“잠깐. 그럼 혹시?”

“조부님께서는 한 번 본 것은 잊으시는 법이 없었소. 자그마치 백여 년 전의 일이 적힌 본가의 문헌에서, 어느 일인 문파에 관한 기록을 떠올리신 것도 마찬가지였지.”

“……!”

“후후, 과감한 모험이었지만 결국 성공했지. 실로 제갈무후 뺨치는 계책 아니오?”

아무렇지 않게 가문 선조의 뺨을 후려치는 제갈풍의 귓가에, 묵직하게 가라앉은 누군가의 목소리가 파고들었다.

“그래. 그랬단 말이지.”

“……어?”

어리둥절하게 고개를 돌린 제갈풍은 볼 수 있었다.

“제갈세가, 집합.”

도저히 들릴 수 없는 거리에서 다가오는 중년인을. 그리고 그 옆에 나란히 걷고 있는 한 청년을.
```

## Final English reading copy

```markdown
# Chapter 504

Enlightenment comes when you least expect it.

It comes when you have forgotten everything around you and entered a state of selflessness, when death is right before your eyes, or when you finally cast off the chains that have bound your body and mind for decades.

That was how enlightenment came.

Fwoooooosh!

A wind of qi flowing from a single person swept in every direction.

The cave interior was dark, deprived of even a ray of light, but it was now brightly illuminated by a halo of light.

The boy who had been silently watching the strange sight spoke in a quiet voice.

“Have you finally escaped your Heart Demon?”

It had not been intentional from the beginning. Mungyeong had only wanted to tell him something.

That Jeok Cheongang was not alone. That he did not need to isolate himself while carrying every worry and burden on his own shoulders.

And the result had been greater than Mungyeong expected.

The Supreme Peak master known as the Fire King had broken the chains that had bound him for so many years and was stepping into a new realm.

“Seems I wasn’t meddling for nothing after all.”

A complicated mixture of emotions swirled in Mungyeong’s eyes as he murmured under his breath.

He did not know why he had sought out Jeok Cheongang or why he had helped a man with whom he had no particular relationship.

No—even if he had known, he would have pretended not to. That was the kind of person he was. That was how he had lived his entire life.

But…

*It doesn’t feel so bad.*

Mungyeong did not realize that, without his knowledge, a faint smile had brushed across his lips.

Nor did he know that something similar had happened once a few days earlier.

It had happened so briefly that Mungyeong had not noticed. Soon afterward, he slowly turned and stepped out of the cramped cave into the world beyond.

Whoosh.

As if on cue, a breeze from outside blew past, stirring his hair and tickling his nose.

Mungyeong silently gazed at the tall grass and flowers growing thickly around the cave—and the wild animals that had gathered there before suddenly speaking.

“I suppose someone will have to stand guard. If those ignorant wild animals go into the cave, all the enlightenment he worked so hard to attain will be wasted.”

Squeak?

A fawn grazing beside its sleeping mother pricked up its ears.

Amid the wary, curious gazes of the animals, Mungyeong raised his head and looked up at the blue sky.

“It’s a beautiful day. I can’t stay cooped up in a cave in weather like this.”

Step.

Mungyeong muttered as though speaking to himself, then began walking at neither a fast nor a slow pace.

As though bidding farewell to him while he disappeared somewhere with the cave at his back, the wind blew once more.

Whoosh.

A clear sky without a single cloud. A refreshing breeze. Wild animals lying among peaceful nature and wildflowers, all enjoying the sunlight together.

And…

Someone who could not bring himself to enter and was lingering outside.

*Master and Disciple alike.*

No matter how he thought about it, those two really were alike.

Two butterflies fluttered down and landed on Mungyeong’s shoulder as he smiled without a sound.

It was truly a beautiful day.



* * *



The fawn had not been alive for very long, and it was curious about everything.

It sometimes chased butterflies with little bounding hops. It also buried its black nose in the tall grass and flowers, sniffing at their scents.

And as always, it soon lost interest and wandered around looking for something else to do.

Squeak?

But this time was different.

The pitch-black entrance to the cave was strangely alluring, as though it were sucking everything inside, while its mother was asleep after being worn out by raising it.

Most importantly, the strange two-legged animal it had never seen before had disappeared into the distance.

Squeak.

*What’s in there? I want to go inside.*

Squeak!

*All right. Let’s go!*

But the fawn’s firm resolve was crushed in less time than it took to pull at the grass a few times.

Step.

Along with the sudden sound of someone approaching, a shadow fell over its round head.

The startled fawn stumbled backward. Reflected in its black eyes was the silhouette of a large figure.

“Not right now. We’ll go in later.”

The figure gently rubbed the frightened fawn’s head and stared at the pitch-black cave.

The stranger’s gaze was so profoundly somber that the fawn, which had instinctively been about to wake its mother, swallowed its cry.

Squeeeeeak.

“That’s right. Good. Now go back to your mother.”

The figure watched the fawn tilt its head and approach its sleeping mother, then straightened from his bent posture.

He walked toward the cave with steady steps, his voice blurred by the wind.

“Now… I suppose I should go, too.”

The path to the cave was long.

A year and several months had passed since the day the old man and the young man first met.

After taking the long way around, they could finally meet again.

Not one before the other or one behind the other, but side by side, shoulder to shoulder.



* * *



“When the hell is Jin Taekyung coming?”

At Gung Gibang’s irritated complaint, Hyuk Mujin clicked his tongue.

“Tsk, tsk. With a temper that impatient, how are you ever going to beg? Try waiting patiently for once.”

“Listen to the way that Hyuk bastard talks. Are beggars not allowed to be impatient?”

“You need patience if you want to receive even a single iron coin in alms.”

“Did you say the Hyuk Family Textile Shop? Should we send a hundred thousand Beggars’ Sect disciples over there to take a shit each?”

“…Let’s leave family out of this.”

“Then watch your mouth. You think my children don’t have money, but don’t have shit?”

Hyuk Mujin looked at Gung Gibang with disgust.

“I’m going insane. I just ate, so why the hell are you talking about shit? We have to board the ship soon, too.”

“That’s why, before the Hyuk Family Textile Shop gets covered in shit—”

“Ah, I said stop! Hearing about food after talking about eating shit is making my stomach turn!”

“……?”

“……?”

While the two men tilted their heads, sensing that something was wrong, Jin Wikyung was asking someone else a question.

“Tell me, are you certain he will be arriving soon?”

Mungyeong, the young medical apprentice known as the Disciple of the Divine Physician, bowed politely.

“Yes. Young Master Jin definitely said so.”

“We will have to set out before sunset…”

Jin Wikyung murmured as he gazed at the sky slowly turning red.

The declaration ceremony for the New Murim Alliance in Henan was only about a month away. They had to leave diligently from this moment onward to arrive on time while allowing for any unforeseen circumstances along the way.

*No. I should consider us fortunate that we get to travel with Great Hero Jeok.*

Many rumors had already spread about Jeok Cheongang, who had secluded himself for seven days and nights.

Some were hopeful stories claiming that he had finally found the beginnings of enlightenment. Others were impious suggestions that perhaps something had gone wrong with his health. Still others insisted that he had simply chosen not to show himself for no particular reason.

Jin Wikyung did not know which of the three was true, but there was no doubt that he had secretly been worried.

*I was afraid he might say he would not participate in the Murim Alliance… It seems the youngest managed to persuade him.*

Most orthodox Murim practitioners had forgotten this fact, but the Fire King Jeok Cheongang was originally a martial artist who belonged to neither the orthodox, unorthodox, nor Demonic factions—a martial artist who stood between the orthodox and unorthodox factions.

That was also the foundation of the Fire Gate Clan, which had maintained its lineage through one-person succession for hundreds of years. Its successive Sect Leaders had defended their position outside every faction through overwhelming martial might.

*Especially since it was Great Hero Jeok.*

Even a child with a runny nose knew that the Fire King Jeok Cheongang had helped the orthodox faction and led it to victory in the Great Faction War.

But few people knew that this Supreme Peak master from two generations ago had been deeply disappointed by the orthodox faction both during and after the war.

“Now that I think about it, I suddenly remember something my grandfather once said about Senior Jeok.”

Zhuge Feng had come out to see them off. Jin Wikyung’s ear twitched at his words.

“About Great Hero Jeok?”

“Yes.”

“I’ve heard that the previous Family Head was a wise man with remarkable insight. May I ask what he said?”

“Well, it was something I heard in the Family Head’s hall when I was thirteen.”

“I see. And what did he say…?”

“I remember it clearly. At the time, my grandfather was talking about what happened during the Great Faction War. Ah, have you heard about how the members of our family played a major role in the great battle that took place in Sichuan?”

Crack.

Zhuge Feng, who had been leisurely fanning himself, suddenly stopped.

He glanced back and forth between Jin Wikyung’s tightly clenched fist and his flushed face, then slowly lowered the fan.

Jin Wikyung’s martial arts were in no way inferior, but even his appearance alone made him little different from a human weapon.

Besides, with the priceless Water God Dragon’s corpse in his hands, was he not the one holding all the cards?

Zhuge Feng discreetly gauged the mood, cleared his throat, and continued.

“Ahem. In any case, I asked him first. I asked when he thought the tide had first begun to turn in favor of the orthodox faction.”

Jin Wikyung asked in a low, level voice,

“Was it because the members of the Zhuge Clan played such an important role in the great battle in Sichuan?”

“No, that wasn’t it! Absolutely not!”

“That is a relief. Please continue.”

Zhuge Feng began speaking while glancing sideways at the clenched fist.

“It was the first and last time I ever saw my grandfather deliberate so deeply. After thinking for quite some time, he finally answered. Can you guess what he said, Lesser Family Head?”

“You just said it was connected to Great Hero Jeok… Then perhaps it was the great battle in Shaanxi. I’ve heard that although the other Seniors also distinguished themselves, Great Hero Jeok’s achievements were truly astounding.”

The battle in Shaanxi that Jin Wikyung had mentioned was one of the particularly brilliant victories among the countless battles of the blood-soaked Great Faction War.

It was an answer Jin Wikyung had reached after giving the matter some thought, but Zhuge Feng gave a quiet laugh and shook his head.

“Wrong.”

“Then what was it?”

“Anhui.”

“Anhui… You mean that?”

“That’s right. No one could have expected the Demonic Cult’s elite Black Wind Corps, a thousand men strong, marching across Anhui, to be annihilated by a single person. Not even my grandfather.”

Jin Wikyung nodded.

On the day Mount Jiuhua was engulfed in flames, an unknown old man living in obscurity became known as the Fire King, while the Demonic Cult lost an elite strike force that had accumulated countless achievements since the beginning of the Great Faction War.

“That makes sense. It was when Great Hero Jeok first entered the world.”

“But if not for my wise and perceptive grandfather’s judgment, not only would the Black Wind Corps not have been annihilated, Senior Jeok would never have gained the title of Fire King.”

“What do you mean…?”

Zhuge Feng looked around, then lowered his voice as much as possible.

“At the time, every road through Anhui was open to the Black Wind Corps. They had no need to pass through Mount Jiuhua.”

“Wait. Then could it be…?”

“My grandfather never forgot anything he had seen once. This was no different. He remembered a record about a one-person sect in our family’s archives, one describing events from more than a hundred years ago.”

“……!”

“Heh heh. It was a bold gamble, but it worked. It was a stratagem that would put even Zhuge Wuhou to shame, wouldn’t you say?”

As Zhuge Feng casually put his own clan’s ancestor to shame, a deep voice reached his ear.

“Is that what happened?”

“…Huh?”

Zhuge Feng turned around in bewilderment.

He saw a middle-aged man approaching from a distance far too great for his voice to have carried.

“Zhuge Clan, assemble.”

And walking beside him, shoulder to shoulder, was a young man.
```

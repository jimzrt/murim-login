<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0484.txt",
      "sha256": "24358bc891dacc42ed9d7e42be663f7a47266153bbff9722d744b1203a08a3dd",
      "bytes": 13417
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6e906f641006a8448d8763b62d32eee63a59204175c5d645e4c286e2b97ee9c3",
      "bytes": 3234
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "99d01cea0f3a836b7a9bafb8ca912256d160fae612ec074bf704de80c3a7daa0",
      "bytes": 154716
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "694e7700092853e1a86c9b0d5e5764cb81f7147df0576d2183321758afb44e20",
      "bytes": 1006
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "fa0cde37c34a0c067a16b4a1184d444402d7fdf92c8b41dc2c55762e8c14d49c",
      "bytes": 686
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "faf88dceb5dfdc81dc50aa928115ccf78323d26886eceec4faf0e8ce2af93262",
      "bytes": 1001
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "7df106dee92d6514f58568a1c4dd64ff4ed4a18a3308565466f9fbb2cf8c0ff1",
      "bytes": 735
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "490a0f6d5cad171bcdb1ba961c2123d97bbfc53647e0cac662ca0db9b2464b13",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "dca32945ac0b42fdd455489ee82b33b68ec5cc33225c66419ee1396444f3ff15",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "574c58822034006f352463e9f0271f56340528a477dcdf56e22bf8baeb4a9055",
      "bytes": 1239
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "6bb60981459df11133e03e95b1e74731319b3bdcb5e7b3830b6218b765768361",
      "bytes": 786
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "709cf1339869a6ffbcfe2e8a43cbab31ca127a64fad0cb8aad3c2ca6f5457040",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4f9a2b6f44f23a401944cbb3ff87467abd5f25164948ba8ba22aebcefbbab70a",
      "bytes": 151253
    }
  ],
  "estimated_tokens": 13144
}
-->

# Durable State Update — Chapter 484

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 484. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 484. Profile updates may replace only one
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
  "chapter": 484,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 484,
    "continuity_sources": [484],
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
    "The Water God Dragon died after regaining its reason and giving Taekyung its purified Origin Essence, which humans call an inner core.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "Honglan can enthrall people by seizing their emotions and souls, and she can now speak remotely through a controlled person's body.",
    "Honglan escaped from the military vessel last associated with her at Red Cliffs; ninety-four passengers and crew members died by mass suicide, while the surviving officer Song Ho remains incapacitated.",
    "Honglan identifies herself as the Southern Heaven Demon Empress and confirms that Dark Heaven has many eyes and ears, including Blood Lord's reports.",
    "The Southern Heaven Demon Empress serves Lord of Heaven and claims that no one can know his will.",
    "The Gate or rift that corrupted the Water God Dragon remains connected to unresolved questions involving demonic qi and Dark Heaven.",
    "The Dongting Fisherman is alive but severely injured, with crushed limbs, substantial Internal Injury, and serious Fear exposure after encountering the Water God Dragon at Donghu Stronghold.",
    "Gung Gibang has traced the vessel connected to Honglan to Red Cliffs.",
    "Cheongpung reports that Zhuge Feng has found the Gate site from the Water God Dragon's memories.",
    "Jin Wikyung and Gung Gibang have pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths."
  ],
  "continuity_sources": [
    482,
    483
  ],
  "open_questions": [
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "Who created or controlled the Gate that corrupted the Water God Dragon, what is its purpose, and how is that power related to Dark Heaven?"
  ],
  "safe_through": 483,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, established renderings of live-fish sashimi and bone-in sashimi, and gukbap with an explanatory footnote.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 원정 as Origin Essence, 내단 as inner core, 꽃뱀 as flower snake, 산재처리 as workers’ compensation, 거열형 as tearing apart by chariots, 섭혼술 as Soul-Seizing Technique, 남천마후 as Southern Heaven Demon Empress, 묘족 as Miao people, and 페미비수타 as femibista."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 굉도     | **Hong Dao**       |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무당파    | **Wudang**                       |
| 암천     | **Dark Heaven**                  |
| 제갈세가   | **Zhuge Clan**                   |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 신법     | **movement technique**                           |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 마교     | **Demonic Cult**                                 |                                                       |
| 가주     | **Family Head**                              |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 등평도수 | **Rising on Duckweed, Crossing Water** | Comparable movement feat for walking across water. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 현공진인 | 제갈풍 | senior Wudang master to Zhuge Clan Family Head | Family Head Zhuge | formal-respectful | Uses 제갈가주 while discussing the fast ship and the route. |
| 제갈풍 | 현공진인 | Zhuge Clan Family Head to senior Wudang master | Perfected Being Hyeongong | formal-deferential | Addresses Hyeongong with marked respect and calls his presence a great reinforcement. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |
| 청풍 | 제갈풍 | young_martial_artist_to_family_head | Great Hero Zhuge Feng | cheerful and polite | Cheongpung addresses Zhuge Feng as 제갈풍 대협, but deliberately mispronounces the name once as 제갈퐁 for comic effect. |
| 제갈풍 | 청풍 | family_head_to_younger_martial_artist | you | familiar and polite | Zhuge Feng uses 자네 while instructing Cheongpung and responding to his advice. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 궁기방 | 진위경 | martial_companion_to_family_head | Great Hero Jin | familiar and polite | Asks Jin Wikyung not to exclude the Beggars' Sect from the defense. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 483
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 483
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 463
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed and used his final words to warn Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff; sends Unnamed to bring the Master of Morning Star to Shaolin.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 468
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge while carrying the authority of an experienced senior master.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 482
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 483
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 483
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 483
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a former assassin who passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 483
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical and disarmingly casual, he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃484화



목적지를 찾아가는 것은 그리 어렵지 않았다. 이미 한차례 오가며 물길을 익힌 수부들은 능숙하게 선박을 몰아 나아갔다.

촤아아아.

불과 이틀 전 폭풍우가 일었다는 사실이 믿기지 않을 만큼, 강물은 잔잔하고 바람은 시원했다.

뱃머리에 앉아 머리 위로 내리쬐는 햇빛을 받고 있던 나는 스쳐 지나가는 주위 풍경 속에서 익숙함을 발견할 수 있었다.

‘맞아, 분명 이쯤이었지.’

[기억의 파편]은 수신룡의 뇌리에 남은 기억들이었고, 나는 그의 시야에서 모든 것을 보고 느꼈다.

당연히 ‘그곳’으로 향하는 길 역시 모를 리 없었다.

“잠깐. 청 소협, 여기로 가는 거 맞아?”

문득 던진 내 물음에 청풍이 고개를 갸웃거렸다.

“맞는데, 왜 그러세요?”

“아니. 내가 기억하는 풍경이랑은 조금 다른 것 같아서. 특히 저쪽 절벽이…….”

“아하. 저거요? 사정이 있었어요.”

“무슨 사정?”

“네. 알려 주신 길대로 찾아가긴 했는데, 손만 겨우 들어갈 정도로 틈이 좁았거든요.”

“아.”

오랜 세월 동안 사람의 발길이 닿지 않았던 이유가 있었다. 까마득한 시간이 흐르고 퇴적물이 쌓이다 보니 어느 순간 절벽이 길을 가로막은 것이다.

수신룡이야 뭐, 굳이 절벽을 통과할 필요 없이 밑으로 헤엄쳐서 가면 되니 아무런 문제가 없었겠지만, 사람들은 달랐다.

“그래서?”

“잘랐는데요.”

“……잘라?”

“네. 무당파 할아버지랑 제가 검으로 싹둑싹둑.”

뭔 시벌, 절벽을 종이 오리는 것처럼 말하네.

하지만 종이접기 아저씨, 아니 무당파가 자랑하는 초절정 고수인 현공진인과 청풍이라면 못할 것도 없다.

나만 해도 별 어려움 없이 해낼 수 있는 수준이니까.

“어쨌건 그런 식으로 쭉쭉 뚫었어요. 별로 어렵진 않더라고요. 나머지는 후발대로 온 다른 분들이 다듬으셨다고 들었는데.”

“……어, 그래.”

나도 가끔 깜빡깜빡한다. 주위에 괴물만 득실거린다는 걸. 그리고 나 역시 그중 한 사람이라는 것도.

옆에서 청풍과 내 대화를 듣고 있던 적천강이 문경의 옆구리를 쿡 찔렀다.

“세상이 미쳐 돌아가는 건가? 우리 젊었을 적에는 안 그랬던 것 같은데. 그냥 저놈들이 괴물인 거지?”

“나까지 한 묶음으로 엮지 마라. 기분 나쁘니까.”

“그래서 초절정 고수가 되었을 당시 나이가?”

“……저놈들이 괴물인 거다.”

“그래. 아무래도 그런 거겠지. 허어, 천기가 흐려져서 그런가. 무림도 변했군, 변했어.”

적천강이 한탄하는 사이, 소름이 끼칠 정도로 반듯하게 잘려 나간 절벽 사이를 파고든 선박은 계속해서 나아갔다.

그리고 서서히 모습을 드러내는 새로운 풍경과 새로운 사람들이 있었다.

파팟! 촥!

표횰한 신법. 등평도수(登萍渡水)의 수법으로 강물을 밟으며 내려앉은 절정 고수들이 삼엄한 기세로 선박을 가로막았다.

“정지! 승선한 분들께서는 각자의 이름과 별호를 밝히고, 신분 확인 절차가 끝난 후에…….”

최근 들어 이어지는 물 친화적인 삶에 예민해져 있던 적천강이 악귀 같은 얼굴로 쑥 고개를 내밀었다.

“노부, 화왕.”

“허억!”

“막으면. 뒈짐.”

“예, 옛!”

“기, 길을 열어라! 아무도 막지 마라!”

파팟!

처음 등장했던 속도보다 두 배는 빠르게 사라지는 신형들을 바라본 궁기방이 중얼거렸다.

“무당파의 신법이 이 정도였나. 본 방도 긴장해야겠군.”

아니. 그냥 좆 된 걸 느끼고 죽을힘을 다해 도망간 것 같은데.

어찌 되었건 그 이후로는 일사천리였다. 포악한 불 포켓몬인 적천강이야 말할 것도 없고, 나 역시 모르면 암천 소리가 나올 정도로 얼굴이 알려진 데다 곁에는 청풍과 궁기방까지 있으니까.

“오, 방금 누가 날 알아본 것 같은데?”

“당연하지. 나랑 같이 다니는 거지는 너밖에 없으니까.”

“…….”

“와아, 방금 저도 알아봤어요!”

“당연하지. 뿔 달린 물뱀이랑 다니는 인간은 당신밖에 없으니까.”

“네에.”

나는 시무룩해진 궁기방과 청풍을 무시하며 눈앞의 광경에 집중했다.

까마득한 절벽 위에는 어떻게 올라갔는지 모를 궁수들이 활을 쏠 만반의 준비를 갖추고 있었고, 곳곳에 숨어 있는 고수들의 기척이 느껴졌다.

‘무당파, 제갈세가, 거기에 더해 개방도 온 것 같은데.’

삼엄하기 그지없는 경계 태세.

다만 이번 사안이 갖는 무게와 중요성을 생각하면 당연한 일이기도 했다.

“호북성주는 이 일을 아예 묻어 두기로 한 겁니까?”

내 물음에 진위경이 무겁게 고개를 끄덕였다.

“일단은 그리되었다. 오백 년 묵은 이무기가 미쳐 날뛰었다는 소식을 좋게 받아들일 양민들은 없을 테니까.”

“그건 그렇죠.”

민중의 지지는 양날의 검과 같다.

평상시에는 천자님, 천자님 하면서 떠받드는 순박한 백성들도 홍수나 지진이 일어나면 나라에 망조가 들었다며 혁무진 급 태세 전환을 보여 준다.

거기에 2+1 행사로 역병까지 따라붙는 날에는 밭 갈던 곡괭이로 나라를 갈아엎겠다며 뛰쳐나오는 게 이 시대의 분위기였다.

하물며 수많은 사람이 신령으로 떠받들던 이무기가 어느 날 미쳐서 기천에 달하는 인명을 해쳤다? 호북성주로서는 최대한 숨기고 싶은 진실일 것이다.

“대신 암천이 매우 위험한 집단이라는 것에는 그도 일부분 동의하더구나.”

“……일부분 동의? 이 꼴이 났는데도요?”

방금 했던 말 취소.

수신룡의 존재를 감춘 것까지는 그렇다 치더라도, 이번 일로 죽은 이들이 몇 명인데 일부분 동의라니.

아직 제정신을 못 차린 것이 틀림없다.

“자만심이 낳은 착각이지. 무림은 무림일 뿐, 자신들이 나라를 다스리는 데에는 아무런 문제가 없을 거라 생각하는 거다. 최대한 설득하려 했지만 별 소용 없더구나.”

적천강이 퉁명스러운 목소리로 불쑥 끼어들었다.

“그 머저리 같은 관부 놈들은 변함이 없군. 정마대전 때와 똑같아. 마교 놈들이 사천을 밀고 내려올 때도 두 손 놓고 있더니 양민들의 피해가 커지자 부랴부랴 군사를 끌어모았지.”

“그래서 어떻게 됐는데요?”

“어떻게 되긴. 그때쯤 마교가 패퇴하고 물러서자 대장군이란 놈이 와서 거들먹거렸지. 이게 다 황상 폐하의 은혜니 어쩌니. 어차피 나라의 주인은 천자니까 누가 이겨도 별 상관은 없지만 그래도 그대들의 승리를 축하한다. 뭐 그런 헛소리를 지껄이더구나.”

“잘 참으셨네요. 노야 성격에 그 정도면 거의 부처 수준인데.”

적천강이 무슨 개소리냐는 표정으로 나를 바라보았다.

“노부가 그걸 왜 참아? 때려죽이려고 했지. 굉도, 그 친구가 안 말렸으면 정마대전이 아니라 정관대전, 뭐 그런 게 일어났을걸?”

“……아, 예.”

“뭐 어쨌건 관부 놈들에게 큰 기대는 하지 말아라. 그나마 가만히 있던 흑도 놈들을 암천의 끄나풀로 둔갑시킨 것으로 만족해야지.”

진위경이 씁쓸하게 웃으며 대답했다.

“예. 다행히 그 후로 민중들 사이에서 암천에 대한 분노와 경계심이 하늘을 찌르고 있더군요.”

“이번 일과는 아무런 상관도 없는 놈들이지만 뭐 어쩌겠느냐. 아예 죄 없는 놈들도 아니고 흑도 놈들이니 이참에 뿌리 뽑는 것도 나쁘지 않겠지.”

관부는 무림과의 협의를 통해 민중의 분노를 잠재울 희생양으로 호북성의 흑도를 조졌고, 양 측 모두 원하는 바를 얻었으니 나름대로의 기브 앤 테이크라고 볼 수 있다.

물론, 그 과정에서 나와 일행들의 이름값이 다시 한번 천정부지로 솟구쳤음은 말할 것도 없다.

‘암천이 지금보다 더 날뛰어도 관부가 나설지는 미지수지만.’

그런 생각을 하는 사이, 거침없이 나아가던 선박이 비로소 멈추었다.

절벽에 연결하여 임시로 만든 나루터에 정박한 우리를 향해 사람들이 시선이 쏟아진다.

“적천강 대협이시다.”

“옆에는 후개도 있는데? 화산신룡이 어딜 갔나 했더니.”

“가만. 저기 저 청년은 열화신룡 아닌가?”

“자네 그 얘기 들었나? 수뇌부 사이에서 이무기를 잡은 것이 열화신룡이라는 이야기가…….”

나름 작게 말한다고 하는데, 다 들린다. 이것들아.

수군거리는 목소리들이 거슬린 내가 대놓고 인상을 팍 찡그리자 주위가 삽시간에 조용해졌다.

그리고 다음 순간, 침묵을 깨는 외침이 울려 퍼졌다.

“오, 왔는가!”

진흙과 강물로 흠뻑 젖은 몸. 풀어 헤쳐진 머리카락 사이에는 이름 모를 수초(水草)가 엉겨 있다.

첨벙첨벙 강물을 헤치며 달려오는 중년인의 모습에, 나는 내심 중얼거렸다.

‘저런 양반이 제갈세가의 가주라니.’

새삼스럽게 깨달은 사실이지만, 와룡객(臥龍客) 제갈풍은 확실히 무림에서도 괴짜로 통하는 인물임이 확실했다.

“가주, 다른 때라면 말도 안 하오. 하지만 외인(外人)들도 있는데 체통을 좀…….”

“아, 저리 좀 비키십쇼. 숙부님.”

“가주우!”

체통은 우체통에 처넣고 온 것이 확실하다.

만류하는 집안 어른을 매몰차게 뿌리치고 한달음에 달려온 제갈풍이 잔뜩 상기된 얼굴로 입을 열었다.

“찾았네. 찾았단 말일세!”

“아, 예. 들어서 알고 있습니다. 청 소협이…….”

“처음에는 이게 무슨 개소린가 싶었는데, 정말 자네가 말한 그곳에 떡하니 있더군!”

“…….”

아니, 이건 너무 솔직한 거 아니냐?

그렇게 성심성의껏 설명했는데 개소리로 취급했었다니.

내 표정을 본 제갈풍이 짐짓 진지한 표정으로 말을 이었다.

“본가의 선조이신 제갈무후(諸葛武侯)께서는 돌다리도 두들겨 보고 건너라고 하셨지. 너무 섭섭해하진 말게.”

툭 하면 가문의 선조를 팔아먹는 건 제갈세가의 가훈인가, 아니면 유전인가. 나는 미심쩍은 눈빛으로 제갈풍을 응시했다.

“……진짜 제갈무후가 그런 말을 했어요? 제가 알기로는 그게 다른 나라 속담일 텐데.”

“살면서 한 번쯤은 하셨겠지. 지금 그게 중요한가?”

어이가 없네, 진짜.

저쪽 중국 놈이나 이쪽 중국 놈이나 남의 것 베끼는 솜씨 하나만큼은 아주 기가 막힌다.

하지만 내가 뭐라 할 새도 없이 휙 몸을 돌린 제갈풍은 앞장서서 걷기 시작했다.

“따라오게.”

임시 나루터에나마 발을 디딜 수 있게 되었다는 기쁨에, 몸을 부르르 떨고 있던 적천강이 눈을 치켜떴다.

“따라오게? 그거 지금 노부에게 한 말이냐?”

“……노 선배님께 드린 말씀이 아닙니다.”

“그럼 앞으로 주둥아리 조심하고, 반으로 접어 놓은 혓바닥 빳빳하게 펴라. 반으로 죽이기 전에.”

“옙.”

“그리고 발걸음이 왜 이리 느려 터졌느냐? 네놈보다 노부의 할머니가 더 빠르겠다.”

“악!”

갑자기 기합 왜 저래.

1번 교육생처럼 빠릿빠릿해진 제갈풍은 신법을 발휘하여 달려 나갔고, 얼마 지나지 않아 나는 [기억의 파편]에서도 볼 수 없던 희한한 광경을 마주할 수 있었다.

“저건…….”

“내가 아홉 살 때 고안해 낸 장치일세. 이틀 동안 저거 가져온다고 꽤 고생했지. 어떤가?”

나는 강물 안에 벽처럼 세워진 거대한 석벽을 보며 고개를 끄덕였다.

“어, 끝내주네요.”

“물속에서는 오랫동안 조사를 할 수 없으니, 절벽을 잘라 만든 석재로 사면(四面)을 틀어막고 안의 물을 모두 빼냈지. 아마 평범한 인부들이었다면 족히 몇 달은 걸렸을 거라네.”

제갈풍이 개발했다는 기관 장치의 역할도 컸지만, 무공을 익힌 무림인들이 없었다면 이틀 만에 이런 것을 만들 엄두조차 내지 못했을 것이다.

“모두 잠시 자리를 비워 주겠나?”

석벽 아래로 내려가자마자 제갈풍이 던진 한마디에, 제갈세가의 진법가들로 보이는 이들이 썰물처럼 물러난다.

그리고 나는 비로소 볼 수 있었다. 오랜 세월 한자리에 서 있었을 높은 절벽, 그 중심을 정확히 가로지르는 거대한 틈새를.

스윽.

본능적으로 뻗은 손이 틈새에 닿은 바로 그 순간.

삐빅.

불길하기 짝이 없는 시스템 알림이 귓가를 파고들었다.
```

## Final English reading copy

```markdown
# Chapter 484

It wasn’t difficult to find our destination. The boatmen had already made one round trip and learned the waterways, so they guided the vessel forward with practiced ease.

*Whoosh…*

It was hard to believe that a storm had raged only two days ago. The river was calm, and the breeze was refreshing.

Sitting at the bow and basking in the sunlight pouring down over my head, I spotted something familiar among the passing scenery.

*That’s right. It was around here.*

The *Memory Fragment* contained the memories left in the Water God Dragon’s mind, and I had seen and felt everything from its perspective.

Naturally, I knew the way to *that place* as well.

“Wait. Young Hero Cheongpung, are we sure this is the way?”

At my sudden question, Cheongpung tilted his head.

“It is. Why do you ask?”

“It just looks a little different from what I remember. Especially that cliff over there…”

“Oh, that? There were some circumstances.”

“What circumstances?”

“Yes. We followed the route you told us about, but the gap was so narrow that only a hand could fit through.”

“Oh.”

So that was why no one had set foot there for so many years. As the ages passed and sediment accumulated, the cliff had eventually blocked the passage.

The Water God Dragon had never needed to pass through the cliff. It could simply swim underneath it. Humans, however, were a different story.

“So?”

“We cut through it.”

“…You cut through it?”

“Yes. The Wudang grandpa and I sliced it up with our swords.”

*What the hell? He’s talking about cutting through a cliff like he’s trimming paper.*

But with Origami Man—no, Perfected Being Hyeongong, the Supreme Peak master Wudang was so proud of—and Cheongpung, it was entirely possible.

I could have managed it without much difficulty myself.

“Anyway, we carved straight through it. It wasn’t too hard. I heard the others who came with the second wave polished the rest.”

“…Uh. Right.”

Sometimes I forgot.

I forgot that monsters were everywhere around me.

And that I was one of them.

Jeok Cheongang, who had been listening to Cheongpung and me, poked Mungyeong in the ribs.

“Is the world going mad? I don’t remember things being like this when we were young. Or are those two simply monsters?”

“Don’t lump me in with you. It’s insulting.”

“So how old were you when you became a Supreme Peak master?”

“…”

“They’re the monsters.”

“Yes. That must be it. Hah. Perhaps the heavenly patterns have grown clouded. The Murim has changed. It certainly has.”

While Jeok Cheongang lamented, the vessel continued forward between cliffs that had been cut with such unnerving precision that they looked almost artificial.

Then a new landscape—and new people—gradually came into view.

*Whoosh! Splash!*

Masters who had reached the Peak realm landed on the river after stepping across the water with the movement technique known as Rising on Duckweed, Crossing Water. They blocked the vessel with imposing auras.

“Stop! Everyone aboard must state their names and sobriquets. Once the identity verification process is complete—”

Jeok Cheongang, already sensitive after living a water-friendly life for the past few days, stuck his head out with a fiendish expression.

“This old man is the Fire King.”

“Gasp!”

“If you stop us, you die.”

“Yes, sir!”

“O-open the way! Let no one stop them!”

*Whoosh!*

Gung Gibang watched the figures vanish at twice the speed with which they had first appeared and muttered,

“Was the Wudang Sect’s movement technique always this impressive? Our sect will have to stay on its toes.”

No. They had probably realized they were completely fucked and fled for their lives.

Either way, everything proceeded smoothly after that. The vicious Fire Pokémon Jeok Cheongang needed no explanation, and my face was famous enough that anyone who failed to recognize me might as well have been working for Dark Heaven. Besides, Cheongpung and Gung Gibang were with me.

“Oh, did someone just recognize me?”

“Of course. You’re the only beggar who travels with me.”

“…”

“Wow! Someone recognized me just now, too!”

“Of course. You’re the only human who travels around with a horned water snake.”

“Yes…”

I ignored the dejected Gung Gibang and Cheongpung and focused on the scene ahead.

Archers had somehow climbed to the tops of the impossibly high cliffs and stood ready to fire. I could also sense the presence of masters hiding in various locations.

*Wudang, the Zhuge Clan, and it looks like the Beggars’ Sect came too.*

The security was nothing short of formidable.

But considering the weight and importance of what had happened, it was only natural.

“Did the City Lord of Hubei Province decide to bury this matter completely?”

Jin Wikyung nodded gravely.

“For the time being. No ordinary citizen would take the news well that a five-hundred-year-old imugi had gone berserk.”

“That’s true.”

The people’s support was a double-edged sword.

Under ordinary circumstances, the simple folk who fawned over the Son of Heaven would pull a Hyuk Mujin-level about-face the moment a flood or earthquake struck, declaring it an omen of the nation’s ruin.

And if a plague came along as part of a buy-two-get-one-free deal, the people of this era would grab the pickaxes they had been using to till their fields and charge out to overturn the country.

How much worse would it be if an imugi, worshiped by countless people as a divine creature, suddenly went mad and killed several thousand people?

The City Lord of Hubei Province would want to hide that truth as much as possible.

“He does agree, at least in part, that Dark Heaven is an extremely dangerous organization.”

“…He agrees *in part*? Even after all this?”

I took back what I had said.

I could understand concealing the existence of the Water God Dragon. But how many people had died because of this incident? And he only agreed *in part*?

He clearly still hadn’t come to his senses.

“It is an illusion born of arrogance. He believes the Murim is merely the Murim, and that it will pose no problem for them to govern the country. I tried to persuade him as much as possible, but it was of little use.”

Jeok Cheongang suddenly cut in with a disgruntled voice.

“Those idiot government officials haven’t changed at all. They were exactly the same during the Great Faction War. When the Demonic Cult pushed down through Sichuan, they sat on their hands. Only after the civilian casualties grew did they hurriedly gather troops.”

“What happened then?”

“What do you think happened? By then, the Demonic Cult had already been defeated and withdrawn, and some bastard who called himself a Great General came strutting over and taking credit. He said it was all thanks to His Imperial Majesty’s grace and this and that. Since the Emperor was the master of the country anyway, it didn’t matter who won, but congratulations on your victory. That sort of bullshit.”

“You showed remarkable restraint. For you, Old Master, that was practically the patience of a Buddha.”

Jeok Cheongang looked at me as if I had just said something incomprehensible.

“Why would this old man have put up with that? I tried to beat him to death. If Hong Dao hadn’t stopped me, it wouldn’t have been the Great Faction War. It would have been the Great Government War, or something like that.”

“…Ah. Right.”

“In any case, don’t expect much from the government officials. We should be satisfied that they at least turned the dark-path figures who had been sitting quietly into Dark Heaven’s lackeys.”

Jin Wikyung answered with a bitter smile.

“Yes. Fortunately, since then, the people’s anger and wariness toward Dark Heaven have reached the heavens.”

“They had nothing to do with this incident, but what can we do? They aren’t completely innocent, either. They’re dark-path figures, so it wouldn’t be a bad idea to take this opportunity to uproot them.”

The government had worked with the Murim to crush Hubei Province’s dark-path figures as sacrifices to appease the people’s anger. Since both sides had gained what they wanted, it could be called a form of give-and-take.

Of course, there was no need to mention that my companions’ and my reputations had skyrocketed once again in the process.

*Whether the government would actually act even if Dark Heaven became more aggressive was another question.*

As I thought about that, the vessel that had been charging forward finally came to a stop.

We docked at a temporary pier built against the cliff, and people’s gazes poured toward us.

“That’s Great Hero Jeok Cheongang.”

“The Successor Beggar is beside him, too. I was wondering where the Huashan Divine Dragon had gone.”

“Wait. Isn’t that young man the Blazing Flame Divine Dragon?”

“Did you hear? There’s a rumor among the leaders that the Blazing Flame Divine Dragon was the one who took down the imugi…”

They thought they were whispering quietly, but I could hear every word.

*You idiots.*

I found the muttering irritating and deliberately scowled, causing the surroundings to fall silent in an instant.

Then, the next moment, a shout broke through the silence.

“Oh, you’ve arrived!”

The middle-aged man running toward us was drenched from head to toe in mud and river water. Unfamiliar aquatic plants were tangled in his disheveled hair.

As he came splashing through the river, I muttered inwardly,

*That man is the Family Head of the Zhuge Clan?*

It was something I had only just realized, but Crouching Dragon Guest Zhuge Feng was unquestionably regarded as an eccentric even within the Murim.

“Family Head, I normally wouldn’t say anything, but there are outsiders present. Please show some decorum…”

“Ah, please move aside, Uncle.”

“Family Heaaad!”

He had definitely left his decorum in a mailbox somewhere.

Shrugging off the family elder who tried to stop him, Zhuge Feng ran toward us and opened his mouth with a flushed face.

“We found it. We found it!”

“Yes, I know. Young Hero Cheongpung told me…”

“At first, I thought, *What kind of bullshit is this?* But it was really sitting right there in the place you described!”

“…”

Wasn’t that a little too honest?

I had explained everything so earnestly, and he had dismissed it as bullshit?

Seeing my expression, Zhuge Feng continued with a solemn face.

“Our ancestor, Zhuge Wuhou, once said that one should tap even a stone bridge before crossing it. Don’t take it too personally.”

Was constantly invoking the ancestors of the family a Zhuge Clan motto, or was it hereditary?

I stared at Zhuge Feng suspiciously.

“…Did Zhuge Wuhou really say that? As far as I know, that’s a proverb from another country.”

“He must have said it at least once in his life. Is that important right now?”

*Unbelievable.*

Whether it was the Chinese over there or the Chinese over here, they were both astonishingly talented at copying other people’s work.

But before I could say anything, Zhuge Feng abruptly turned around and started walking ahead of us.

“Follow me.”

Jeok Cheongang, who had been trembling with delight at finally being able to set foot on even a temporary pier, narrowed his eyes.

“‘Follow me’? Was that directed at this old man?”

“…I wasn’t speaking to Senior.”

“Then watch your mouth from now on, and straighten that folded tongue before this old man kills you in half.”

“Yes, sir.”

“And why are you walking so slowly? Even this old man’s grandmother would be faster than you.”

“Ah!”

Why did he suddenly start shouting battle cries?

Zhuge Feng became as brisk and alert as a model trainee and activated his movement technique, racing ahead. Not long afterward, I encountered a bizarre sight that I had never seen in the *Memory Fragment*.

“What is that…?”

“I invented that device when I was nine. It took quite a bit of effort to bring it here over the past two days. What do you think?”

I nodded as I stared at the enormous stone wall standing in the river like a barrier.

“Wow. That’s incredible.”

“It’s impossible to investigate underwater for long, so we used stone taken from the cliff to enclose all four sides and drained out all the water inside. If ordinary laborers had done it, it would have taken several months at least.”

The mechanical device Zhuge Feng had developed had played a major role, but without martial artists who had trained in martial arts, they would never even have considered building something like this in two days.

“Would everyone clear out for a moment?”

The moment we descended beneath the stone wall, Zhuge Feng uttered those words, and the people who appeared to be formation experts from the Zhuge Clan withdrew like the receding tide.

Only then could I see it.

A towering cliff that must have stood in the same place for countless years—and an enormous fissure running precisely across its center.

*Swish.*

The instant my hand stretched out instinctively and touched the gap—

> **System**
>
> *Beep.*

An utterly ominous System notification pierced my ears.
```

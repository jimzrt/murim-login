<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0494.txt",
      "sha256": "1cceec57d95632a540dd5a7516c5ff129c72db300a32cd28586a2252c5c76f2d",
      "bytes": 12809
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c1f2364a2cf9a069a0e78697354b3c8a23882dd287a6e5083ccb8119125d7598",
      "bytes": 4384
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d889a5f6355e2f8e2d2ef27c974938fa77a4b44433b759d896eb4490602296f0",
      "bytes": 157427
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "499ebd12485308fb572824af45ef1838fead424b3da8e87c06953bc581da44a7",
      "bytes": 1006
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "15eefe09481b9be8673750322adc16827123263d8a23c6f1bc019a2f4e2a37e6",
      "bytes": 553
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "730b9d934d6bff154db658f66bf6153e887ee4b82c90a5bf7713b8d98b9b7c38",
      "bytes": 698
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "1d6a80191793d78438ac796ac888b5bf910ddebea450aeb0e9b4112d718a1420",
      "bytes": 768
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "5a95e87cf47790549f79caa600b9860290a455426acf8df277249651186f60cf",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "54626e3cfefc8da7513fc3397361de1e93ade51b38bdf660741493faf8b41289",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "90ce3ec30b98558adcfb0dc322621f0ec92d198db60e2922600907ff97769966",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b735eabf14d7f1de55ed8de83ac24e6f0067969f34f4e1649c5625ebb675eb6b",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "c64316e396998a13d4b0cfc2b783fad4601a527f7d7457ed21d99d63362c926a",
      "bytes": 885
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "75d2fc0e87a4c34f13935fced5c1c68cdcadc831e21af3bd589a931a711c934e",
      "bytes": 153277
    }
  ],
  "estimated_tokens": 13068
}
-->

# Durable State Update — Chapter 494

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 494. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 494. Profile updates may replace only one
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
  "chapter": 494,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 494,
    "continuity_sources": [494],
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
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment, and he has withdrawn from the Water God Dragon expedition.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong has agreed to teach Taekyung his secret martial arts without forming a formal Master-Disciple relationship and is testing him through successive poisoned traps; Taekyung has survived the first night's traps and has now been affected by Potent Energy-Dispersing Poison.",
    "The Water God Dragon's spirit has departed; its enormous corpse at Dongting Lake is being dismantled for distribution, with Hyeongong and Cheongpung performing the sword work."
  ],
  "continuity_sources": [
    493,
    492
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What further poison tests will Mungyeong impose on Taekyung, and what secret martial arts will he teach him?"
  ],
  "safe_through": 493,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, and 이룡 as Two Dragons."
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
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 검법     | **sword technique**                              |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 민첩               | **Agility**                    |
| 태원     | **Taiyuan**            |
| 사천     | **Sichuan**            |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 관세음보살 | **Avalokiteshvara** | Buddhist invocation shouted by Unnamed during his attack. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 태극혜검 | **Taiji Wisdom Sword** | Wudang’s supreme sword technique. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |

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
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |
| 현공진인 | 진태경 | senior Wudang master to younger martial artist | young friend | gentle and polite | Hyeongong uses 진 도우 and 젊은 도우 while greeting and worrying about Taekyung. |
| 진태경 | 현공진인 | younger martial artist to senior Daoist master | Perfected Being | respectful and polite | Uses 진인 while responding to Hyeongong's religious instruction. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 493
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 493
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 374
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 493
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge, carries the authority of an experienced senior master, and openly covets exceptional weapons.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 493
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 491
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 493
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 493
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 493
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, and Mungyeong is currently testing Taekyung before teaching him secret martial arts without a formal Master-Disciple relationship.

## Korean source

```text
＃494화



서걱! 촤촤촤촥!

비늘이 갈라지고, 커다란 살점이 일정한 간격으로 토막 난다.

그 사이로 모습을 드러내는 거대한 뼈는 이래도 되는 건가 싶을 정도로 깔끔했다.

푸푹! 서걱!

그야말로 신기(神奇)에 가까운 솜씨.

그 경이로운 광경을 넋 놓은 시선으로 바라보던 사람들 사이로 작은 수군거림이 흘러나왔다.

“혁가야. 내가 정말 몰라서 묻는 건데, 혹시 태원진가가 어부 집안이었냐?”

“그거 그대로 소가주님께 여쭤봐도 됩니까?”

“당연히 안 되지, 미친놈아. 그런데 저건 진짜 타고나지 않고서야 불가능한 일인데. 혹시 진짜 어부…….”

“소가주님! 방금 궁 소협이 뭐라 했냐면!”

“야, 야!”

“우리 가문의 선조 중에 어부가 계셨나? 막내가 어떻게 저러지?”

“……소가주님?”

“제갈무후(諸葛武侯)께서 보셨다면 놀라 사륜거에서 떨어지셨을 광경이군. 안 그렇습니까, 현공진인.”

“세상에, 무량아멘 관세음보살.”

“……진인?”

이렇게 모두가 태원진가의 뿌리에 대해 의심하고 한편으로는 종교 대통합을 이뤄 나갈 때, 한 사람만큼은 홀로 다른 생각을 하고 있었다.

‘허. 이놈 봐라.’

문경의 투명한 눈동자에 신들린 듯이 베고, 가르는 진태경의 움직임이 고스란히 담겼다.

‘엄청난 힘이군. 그뿐만 아니라 쾌속하고 간결해.’

사소한 움직임 하나만으로도 그 사람의 경지를 알 수 있다.

그런 의미에서 보자면 진태경이 보여 주고 있는 모습은 놀라운 것이었다.

‘대단한 성취다. 이제 갓 약관을 넘긴 핏덩이라고는 믿어지지 않을 만큼.’

진태경이 상식을 아득히 초월한 놈이라는 것은 이미 알고 있었다.

아니, 문경뿐만 아니라 이 풍진 강호에 속한 무림인 모두가 아는 사실이다.

최고의 지원을 받는 구파일방의 후기지수들도 약관에는 절정의 벽을 넘지 못해 허덕이는데, 진태경은 초절정의 경지에 올라 전대, 전전대의 고수들과 어깨를 나란히 하고 있으니까.

그러나 문경이 경탄하는 이유는 그뿐만이 아니었다.

‘노강호처럼 노련하다. 저 나이에 보일 수 없는 힘의 조절까지. 군더더기가 없어.’

푹! 서걱!

작은 움직임 하나조차 효율적이다. 다른 사람의 시선을 의식할 법도 한데, 또래라면 부릴 법한 일체의 겉멋도 들어가 있지 않다.

그저 묵묵하게 가장 빠르고 편한 길을 찾아 이동하는 나그네처럼 베고, 가르고, 분리해 낼 뿐이다.

‘이무기를 상대할 때도 마찬가지였지.’

살수는 주위에서 벌어지는 모든 상황을 담고 분석한다. 어떤 경우에도 표적을 암살하고 퇴로를 찾는 것이 그들의 업이니까.

문경은 그런 살수 중에서도 고금 제일이라 불리는 살성이다.

그는 사천에서부터 지금까지 진태경을 주시해 왔다. 신의가 아닌, 살성의 시선으로.

‘천무지체(天武地體)…… 사실이었나.’

무림을 떠난 지 어언 사십 년. 강산이 네 번이나 바뀔 세월 동안 의생으로 살아온 그다.

수천, 수만에 달하는 환자를 진맥하고 치료하며 수많은 경험을 쌓았다.

그러나 그런 문경에게도 진태경의 신체와 자질은 쉽사리 설명할 수 없는 것이었다.

‘청풍과 비슷하지만, 묘하게 달라.’

문경의 시선이 청풍을 향했다가 이내 떨어졌다.

진태경에 비견할 수 있는 유일한 사람. 아니, 무공에 대한 이해력과 응용 면에서는 오히려 진태경 이상이라고도 할 수 있다.

그런 청풍 역시 문경이 본 적 없을 만큼 대단한 신체를 지녔지만, 진태경만큼은 아니다.

‘청풍이 다듬어졌다면, 진태경은 타고났다.’

근육의 모양와 크기, 골격과 혈도. 모든 것이 완벽하다.

그야말로 천무지체.

진태경을 바라보는 문경의 눈빛이 심유하게 가라앉았다.

‘만약 저 녀석이 내 독문 무공을 완전히 제 것으로 만든다면……?’

순간 머릿속에 떠오른 한줄기 생각을, 문경은 이내 치워 버렸다.

‘말도 안 되는 소릴.’

무공은 끝없이 펼쳐진 산맥과 같다.

산 밑에 있는 무림인 대다수는 문경이 정상에 올랐다고 생각하겠지만, 문경은 또 다른 산을 마주하고 있었다.

무공의 세계는 그만큼 광활하고 아득한 영역에 있는 것.

문경조차 자신이 익힌 독문 무공의 끝을 보지 못했는데, 제아무리 천무지체라 해도 단시일 내에 만족할 만한 성취를 보이는 것은 무리다.

‘지금 같은 경우에는 더더욱.’

전란은 이미 코앞까지 들이닥쳤다.

곧 다가올 숱한 싸움을 생각하면 가장 필요한 것을 가르치는 것이 옳았다. 무엇이든지 과하면 독이 되는 법이니까.

화왕 적천강 역시 그 사실을 알기에 진태경을 자신에게 맡겼을 터였다.

‘그런데…… 도대체 저놈에게 무엇을 가르쳐야 하나.’

문경은 실로 오랜만에 막막함을 느끼며 눈 앞에 펼쳐진 광경을 바라보았다.

“청 소협! 준비됐지?”

“네, 은인!”

“매화검법으로 조져!”

“악!”

“진인! 진인은 어디 계십니까!”

“헛. 여기 있네!”

“왜 작업도 안 하고 거기 계십니까! 저희 일하시는 거 안 보이십니까!”

“자, 잠깐 쉬려던 게 그만…….”

“진인께서는 개인주의십니다! 이렇게 협동심이 없어서야 되겠습니까!”

“미, 미안하네.”

“미안함을 담아 보여 주십시오. 태극혜검, 출발!”

“무, 무량수불!”

서걱! 서걱! 서걱!

실로 엄청난 박력을 뿜어내는 진태경의 진두지휘에 따라 순식간에 해체되는 수신룡의 사체.

감탄을 토해 내는 사람들과 달리 문경의 마음은 답답해져만 갔다.

‘진짜 저놈한테 뭘 어떻게 가르쳐야 하지?’

저 정도면 알아서도 잘 클 놈 같긴 한데…….

갈등하던 문경은 마음을 고쳐먹었다.

아니다. 이렇게 된 이상 끝장을 봐야 한다.

진태경이라는 건방진 놈이 어디까지 가는지, 옆에서 직접 지켜보고 싶은 마음도 있었다.

‘우선 저 안이하기 짝이 없는 정신머리부터 뜯어고치는 게 급선무겠군.’

문경은 넋을 놓은 채 구경 중인 혁무진의 옆으로 슬쩍 다가가 말을 걸었다.

“혁 무사님.”

“와 미친. 저걸 한 번에 잘라 버리, 어. 문경아. 왜?”

“진 공자님께서 많이 지치셨을 텐데, 이 물이라도 좀 가져다드리면 어떨까 싶어서요.”

“허어. 역시 넌 생각하는 것부터가 다르구나. 내 금방 전해드리고 오마.”

“제가 드렸다는 말씀은 하지 말아 주세요. 혁 무사님께서 칭찬받는 것이 제게는 더 기쁜 일입니다.”

“너란 녀석은 정말……!”

뭉클한 눈빛으로 문경을 바라본 혁무진이 수통을 건네받았다.

물론 그 안에는 시원한 물과 함께 일곱 걸음을 걷기도 전에 죽는다는 극독, 칠보추혼산(七步追魂散)이 담겨 있었다.



* * *



“……이거, 뭐냐?”

작업이 끝난 직후, 가죽 수통을 들고 다가온 혁무진이 내 물음에 뿌듯한 표정으로 대답했다.

“물입니다. 조장님께서 힘드실 것 같아서요.”

“네가 이런 센스 있는 짓을 할 리가 없잖아.”

“진짜 제가 손수 떠 온 물입니다! 절 왜 그렇게 못 믿으세요!”

요즘 너무 예민했나. 저렇게 억울해하는 혁무진을 보니 조금이나마 의심했던 것이 미안해진다.

솔직히 작업을 오래 하다 보니 목이 타는 것도 사실이고.

“음. 그래?”

“됐습니다. 이러실 거면 그냥 마시지 마세요! 제가 마시고 말지!”

“야, 야. 알겠으니까 놓고 가. 잘 마실게.”

“됐다니까요!”

“이 절까지만 해. 빡치려고 하니까.”

“……예.”

혁무진을 돌려보낸 나는 조심스럽게 가죽 수통의 마개를 열고 냄새를 맡았다. 음, 스멜.

‘일단 냄새는 정상인데.’

그래도 방심하지 않는다. 나는 매우 신중하게 가죽 수통을 기울였다.

느릿느릿 흘러나온 물 한 방울이 혓바닥 위로 똑, 떨어졌다.

‘그래도 혹시 모르니까 우선 한 방울만…….’

삐빅.



- [강력한 칠보추혼산]에 중독되었습니다!

- [강력한 칠보추혼산]은 단 한 방울로 수십 마리의 황소를 죽일 수 있는 극독입니다!

- 심각한 내상과 장기 손상이 우려됩니다. 매우, 매우 신속한 치료가 필요합니다!



“……혁무진 개새끼야.”

시발, 내가 생각한 한 방울은 이게 아니었는데.

‘인벤토리 오픈, 소환!’

나는 황급히 만독지환을 착용함과 동시에 열양지기를 끌어올려 독기를 몰아냈다.

곧이어 울린 시스템 알림이 해독이 완료되었음을 알렸지만, 그게 끝이 아니었다.

삐빅.



- 빠른 조치, 그러나 극독의 후유증이 남습니다!

- [근맥]이 미세한 손상을 입었습니다!

- [근맥]의 손상에 따라 일부 능력치가 하락합니다!

- [근력]이 5 하락했습니다!

- [민첩]이 5 하락했습니다!

- 상태 이상, [심각한 복통]에 걸렸습니다!

- 상태 이상은 완전히 회복되었을 때 원상 복구되지만, 능력치 하락은 되돌릴 수 없습니다!



“이런 미친.”

아니, 시부럴. 능력치 하락 실화냐.

심지어 1, 2가 아니라 근력과 민첩을 합쳐 자그마치 10포인트나 증발해 버렸다.

‘10포인트면 레벨 업 한 번인데!’

제기랄. 어떤 놈 짓인지 딱 보니 알겠다.

지금껏 온갖 개고생을 하며 올려온 능력치가 허망하게 날아가자, 뱃속 깊은 곳으로부터 뜨거운 분노가 솟구쳤다.

꾸르르륵.

……분노가 아니라 분뇨였나.

하필이면 상태 이상도 거지 같은 걸 걸려 버린 상황.

나는 복통으로 눈앞이 새하얗게 물드는 것을 느끼며 황급히 걸음을 옮겼다.

“이보게, 진 도우. 어디 가나?”

“은인, 어디 가세요?”

“비키세요, 비켜. 어차피 해체는 다 끝났으니까 이제 분류만 해 놓으면 돼요. 일단 저는 잠깐 볼일 좀 보러…….”

“은인, 똥 싸러 가요?”

크게 말하지 마, 미친놈아. 문경이 들으면 어쩌려고.

나는 창백하게 질린 얼굴로 비틀비틀 걸었다. 사람들의 눈에 띄지 않는 곳에 가까워고 나서야 비로소 안도의 감정이 들었다.

‘후, 다행이다.’

서서 똥을 지리는 개망신은 둘째 치고, 문경의 눈에 띄었으면 좋은 꼴은 못 봤을 거다.

다행히 사람들 사이에 보이지 않았으니 지금쯤 다른 곳에 있을…….

‘잠깐만. 다른 곳?’

머릿속에 의문이 떠오름과 동시에 걸음을 내디딘 발이 지면을 밟았다.

그리고 귓가를 파고드는 미세한 소음이 있었다.

저벅, 툭.

순간 등골을 타고 흐르는 서늘한 감각.

나는 본능적으로 신형을 허공으로 띄웠다.

쉬쉬쉬쉭!

바람을 타고 울려 퍼지는 네 줄기의 파공음.

전후좌우에서 날아든 네 자루의 비수가 옷깃을 뚫고 살갗을 아슬아슬하게 스쳐 지나간다.

피하지 않았다면 꼼짝없이 가슴과 등, 팔다리에 박혔을 것이 분명했다.

‘이런 미친……!’

타닥.

신형을 바로 세우며 지면에 착지한 나는, 분노를 담아 십여 장 밖의 암벽을 쏘아보았다.

“적당히 좀 합시다. 예?”

스으윽.

마치 아지랑이처럼 일렁이는 암벽.

곧이어 모습을 드러낸 한 사람이 건조한 목소리로 대답했다.

“분명히 말했다. 수련 방식은 내가 정하는 것이라고.”

“사람을 이 지경으로 만들어 놓고 거기 숨어 있어요? 차라리 정면으로…….”

“숨어 있던 것이 아니라 지켜본 거다.”

“그럼 뭐 합니까. 들켰는데.”

“딱 네놈이 알아챌 만큼 드러낸 것뿐이다. 이 정도도 알아채지 못하면 입에 칼을 물고 죽어야지.”

“당신…….”

“당신?”

문경. 아니 살성의 깊게 가라앉은 눈빛을 마주하자 소름과 함께 뜨거운 분노가 솟구쳤다.

꾸르르르륵. 뿌직.

“…….”

“…….”

그것은 분노가 아니라 분뇨였구요.
```

## Final English reading copy

```markdown
# Chapter 494

Slash! Shhk-shhk-shhk!

Scales split apart, and huge chunks of flesh were cut into evenly sized pieces.

The enormous bones revealed between the chunks were so clean that it hardly seemed possible.

Thud! Slash!

It was a skill bordering on the supernatural.

As everyone stared at the astonishing sight in a daze, a quiet murmur spread through the crowd.

“Hyuk. I’m asking because I genuinely don’t know, but… Was the Jin Family of Taiyuan originally a family of fishermen?”

“Can I ask the Lesser Family Head that exact question?”

“Of course not, you lunatic. But this really is impossible unless he was born with it. Could he actually be a fisherman…?”

“Lesser Family Head! Do you know what Young Hero Gung just said?”

“Hey, hey!”

“Was one of our ancestors a fisherman? How can the youngest one do that?”

“……Lesser Family Head?”

“If Zhuge Wuhou had seen this, he would have been so shocked that he’d have fallen out of his four-wheeled carriage. Wouldn’t you agree, Perfected Being Hyeongong?”

“Good heavens. Infinite Amen, Avalokiteshvara.”

“……Perfected Being?”

While everyone questioned the roots of the Jin Family of Taiyuan and, at the same time, worked toward religious unification, one person alone was thinking about something entirely different.

*Huh. Look at this guy.*

The movements of Jin Taekyung, cutting and slicing as if possessed, were reflected in Mungyeong’s clear eyes.

*What incredible power. And it’s fast and concise, too.*

A person’s realm could be recognized from even the smallest movement.

In that sense, what Jin Taekyung was showing them was astonishing.

*An incredible achievement. It’s hard to believe he’s barely past twenty.*

Mungyeong had already known that Jin Taekyung was a man who far surpassed common sense.

No, it was not only Mungyeong. Every martial artist in this dusty martial world knew it.

Even the young prodigies of the Nine Sects and One Gang, who received the finest support, struggled to break through the Peak realm at twenty. Jin Taekyung, meanwhile, had reached the Supreme Peak realm and stood shoulder to shoulder with masters of the previous and even earlier generations.

But that was not the only reason Mungyeong admired him.

*He’s as seasoned as an old hand in the martial world. And he can even control his strength in a way no one his age should be able to. There’s no wasted movement.*

Thump! Slash!

Even his smallest movements were efficient. He had every reason to be conscious of the people watching him, yet there was none of the flashy affectation that someone his age might have displayed.

He simply cut, sliced, and separated, like a traveler quietly taking the fastest and easiest road.

*He was the same when he fought the imugi.*

An assassin took in and analyzed everything happening around him. Their profession required them to assassinate their target and find an escape route under any circumstances.

And Mungyeong was the Slaughter Saint, called the greatest assassin of all time.

He had watched Jin Taekyung from Sichuan until now—not as the Divine Physician, but through the eyes of the Slaughter Saint.

*The Heavenly Martial Physique… Was it real after all?*

It had been forty years since Mungyeong left Murim. For all that time—long enough for the mountains and rivers to change four times—he had lived as a medical apprentice.

He had examined and treated thousands upon thousands of patients, accumulating countless experiences.

Yet even for Mungyeong, Jin Taekyung’s body and talent were not easily explained.

*He’s similar to Cheongpung, but subtly different.*

Mungyeong’s gaze turned toward Cheongpung, then quickly moved away.

The only person who could be compared to Jin Taekyung. No—in terms of understanding and applying martial arts, one could even say Cheongpung surpassed Jin Taekyung.

Cheongpung, too, possessed an extraordinary body unlike any Mungyeong had ever seen.

But it was not the same as Jin Taekyung’s.

*Cheongpung was refined. Jin Taekyung was born this way.*

The shape and size of his muscles, his skeleton, his acupoints—everything was perfect.

The Heavenly Martial Physique in every sense.

Mungyeong’s gaze sank into deep thought as he looked at Jin Taekyung.

*What if that boy completely made my secret martial arts his own…?*

The thought flashed through his mind, but Mungyeong quickly pushed it aside.

*Ridiculous.*

Martial arts were like an endless mountain range.

Most martial artists at the foot of the mountain probably believed Mungyeong had reached the summit. But Mungyeong was already facing another mountain.

That was how vast and distant the world of martial arts was.

Even Mungyeong had not seen the end of the secret martial arts he had learned. No matter how exceptional Jin Taekyung’s Heavenly Martial Physique was, it was unreasonable to expect him to show a satisfactory level of achievement in such a short time.

*Especially in a situation like this.*

War was already right on their doorstep.

When he considered the countless battles soon to come, it was only right to teach Taekyung what he needed most. Anything in excess became poison.

The Fire King, Jeok Cheongang, must have known that too. That was why he had entrusted Jin Taekyung to Mungyeong.

*But… What on earth should I teach that bastard?*

Feeling truly at a loss for the first time in a long while, Mungyeong watched the scene unfolding before him.

“Young Hero Cheongpung! Ready?”

“Yes, Benefactor!”

“Lay into it with the Plum Blossom Sword Technique!”

“Ah!”

“Perfected Being! Where are you?”

“Oh. Here I am!”

“Why are you standing over there instead of working? Can’t you see the rest of us working?”

“I-I was just about to take a short break…”

“Perfected Being, you’re such an individualist! How can you have no teamwork at all?”

“I-I’m sorry.”

“Show me how sorry you are. Taiji Wisdom Sword, go!”

“I-Infinite Life Buddha!”

Slash! Slash! Slash!

Following Jin Taekyung’s thunderous directions, the Water God Dragon’s corpse was dismantled in an instant.

While everyone else cried out in admiration, Mungyeong’s heart only grew heavier.

*What am I supposed to teach that bastard?*

At this point, he looked like the kind of person who would grow just fine on his own…

After wrestling with his thoughts, Mungyeong changed his mind.

No. Now that things had come to this, he would see it through to the end.

He also wanted to watch from the side and see just how far this arrogant bastard named Jin Taekyung could go.

*First, I need to fix that absurdly complacent head of his.*

Mungyeong quietly approached Hyuk Mujin, who was watching with his mouth hanging open.

“Martial Warrior Hyuk.”

“Wow, that’s insane. He cut through that in one go—oh, Mungyeong. What is it?”

“I thought Young Master Jin must be exhausted. I was wondering if you could take him some water.”

“Good heavens. You really do think differently from the start. I’ll deliver it right away.”

“Please don’t tell him I gave it to you. It makes me happier when you receive the praise.”

“You really are something…!”

Hyuk Mujin looked at Mungyeong with deeply moved eyes and accepted the leather waterskin.

Of course, along with cool water, it contained a deadly poison called Seven-Step Soul-Chasing Powder—an extreme poison that killed its victim before they could take seven steps.

* * *

“……What is this?”

Immediately after the work was finished, Hyuk Mujin approached me with a leather waterskin. He answered my question with a proud expression.

“It’s water. I thought you might be tired, Captain.”

“There’s no way you could do something this considerate.”

“I really fetched this water myself! Why don’t you trust me?”

Had I been too sensitive lately? Seeing how wronged Hyuk Mujin looked, I felt a little guilty for even suspecting him.

To be honest, after working for so long, my throat was genuinely dry.

“Hm. Really?”

“That’s enough. If you’re going to be like this, don’t drink it! I’ll drink it myself!”

“Hey, hey. Fine. Leave it here and go. I’ll drink it.”

“I said forget it!”

“Just stop there. You’re starting to piss me off.”

“……Yes.”

After sending Hyuk Mujin away, I carefully opened the stopper of the leather waterskin and smelled it.

*Mm. Smell.*

*At least the smell seems normal.*

Even so, I did not let my guard down. I tilted the leather waterskin very carefully.

A drop of water trickled out slowly and plopped onto my tongue.

*Still, just in case, I’ll start with one drop…*

> **System**
> - You have been poisoned by **Potent Seven-Step Soul-Chasing Powder**!
> - **Potent Seven-Step Soul-Chasing Powder** is an extreme poison capable of killing dozens of bulls with a single drop!
> - Severe **Internal Injury** and organ damage are likely. Very, very urgent treatment is required!

“……Hyuk Mujin, you son of a bitch.”

Fuck. This wasn’t the kind of one drop I meant.

*Inventory open. Summon!*

I hurriedly equipped the Myriad-Poison Ring and raised my Scorching Yang Qi, driving out the poison.

An instant later, a System notification announced that Detoxification was complete.

But that was not the end.

> **System**
> - Quick action—but the extreme poison has left aftereffects!
> - Your **Sinews and Meridians** have suffered minor damage!
> - Some abilities have decreased due to the damage to your **Sinews and Meridians**!
> - **Strength** decreased by 5!
> - **Agility** decreased by 5!
> - Status abnormality: **Severe Stomachache**!
> - Status abnormalities will return to normal once you have fully recovered, but decreased abilities cannot be restored!

“What the hell?”

No, fuck. Were these stat losses for real?

And not just one or two points. Ten whole points had vanished from my Strength and Agility combined.

*Ten points is one level-up!*

Damn it. I knew exactly whose work this was.

As the stats I had raised through every kind of hell disappeared pointlessly, hot fury surged up from deep in my gut.

Grrrggg.

……Was that fury?

Or was it feces?

As if the situation were not already bad enough, I had been afflicted with a truly shitty status abnormality.

Feeling my vision turn white from the stomachache, I hurriedly started walking.

“Young Friend Jin, where are you going?”

“Benefactor, where are you going?”

“Move, move. The dismantling is finished anyway, so all we need to do now is sort everything. I just need to take care of something…”

“Benefactor, are you going to poop?”

*Don’t say it so loudly, you lunatic. What if Mungyeong hears you?*

I walked unsteadily with a pale face. Only after I reached a place where no one could see me did I finally feel relieved.

*Whew. Thank goodness.*

The humiliation of shitting myself while standing was one thing, but if Mungyeong had seen me, I definitely would not have gotten off easy.

Fortunately, Mungyeong was nowhere among the others, so he must be somewhere else by now…

*Wait. Somewhere else?*

The question surfaced in my mind at the exact moment my foot came down on the ground.

And then I heard a faint noise.

Step. Tap.

A chill ran down my spine.

I instinctively launched my body into the air.

Shhk-shhk-shhk!

Four sounds of air splitting rang out on the wind.

Four daggers flew in from the front, back, left, and right, piercing the edges of my clothes and skimming dangerously close to my skin.

If I had not dodged, they would have been buried in my chest, back, and limbs.

*What the hell…!*

I righted my body and landed on the ground, then glared furiously at the rock wall more than ten zhang[^1] away.

“Can we take it down a notch? Huh?”

The rock wall rippled like a heat haze.

A moment later, a person emerged and answered in a dry voice.

“I told you clearly. I decide the method of training.”

“You put me in this state and then hid over there? You could at least face me directly—”

“I was not hiding. I was watching.”

“What difference does that make? You got caught.”

“I merely exposed myself enough for you to notice. If you can’t notice even this much, you might as well bite down on a blade and die.”

“You…”

“You?”

Mungyeong.

No—the Slaughter Saint.

The moment I met his deeply sunken gaze, a chill ran over my skin, and hot fury surged up again.

Grrrrrrrk. Frrt.

“……”

“……”

It wasn’t fury.

It was shit, actually.

[^1]: A zhang is a traditional East Asian unit of length, roughly 3.3 meters.
```

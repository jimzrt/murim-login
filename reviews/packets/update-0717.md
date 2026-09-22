<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0717.txt",
      "sha256": "1d6dfc287c99d6b7fde5104d66cfd9f4a08b54892f13df916787e0b87f13e8fa",
      "bytes": 12537
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "64246c83f7462ecc486ca4435de420749bd764484dcbac2119b4836224e3dd3e",
      "bytes": 1759
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "253e9b5288386051c82bc2373ba82835eacd1d4a307dbac220c69208d60acf41",
      "bytes": 208264
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "fa99dbc7c6d687492789fcc231e85150b0e64a5e9aca9a1687af8977d89130ea",
      "bytes": 862
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "32d9636165d996aa934434a6adcdaf177dcc5cf79dbc1ee30dbcb8183789b748",
      "bytes": 553
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b976d240a174e8336d59e4c4e4dc11c53d8c18274436087da9d6c2157f026d32",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1b8818e7444d0ddffd7cebf0c147245600fff584f8600fb7feba3607b34aba0b",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b3e589aeb7121c58f1e19c044125ecee3cb5c669648476b12481708446b128e1",
      "bytes": 1787
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1e2bdb85464f9cebac56b90d1fb496b0da0fd7259b8d2b1c7db2b049c347a071",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "4fe0053c401903f77254198b8502c0716d7d2dd641322d69c5c996cb361e3bac",
      "bytes": 937
    },
    {
      "path": "characters/Namho.md",
      "sha256": "3e69fa25fe5d494a0f61b1d07a7ea793e1e1a22944817e8b95fcbb1823478d13",
      "bytes": 843
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "e74eec136b752542653d6d1552b26bae121e7ce846e2f45941ed3cfffc3990a3",
      "bytes": 715
    },
    {
      "path": "characters/Wonhu.md",
      "sha256": "6fa0b4a71b46752495bf74a885b0e1fd76e5abbcd1d873bff11a2ee8730dea16",
      "bytes": 415
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "2d4da3e38a9e5a5429f177c6729d8052c1adfe10cb5db2cc042e29c98c48c8f0",
      "bytes": 925
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ff357bd805d45735129f367b288d5b4fb85de4c748a7007cc6eba222067c2581",
      "bytes": 218760
    }
  ],
  "estimated_tokens": 12723
}
-->

# Durable State Update — Chapter 717

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 717. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 717. Profile updates may replace only one
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
  "chapter": 717,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 717,
    "continuity_sources": [717],
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
    "Jin Taekyung has awakened after seven days and nights and has regained his physical clarity and strength.",
    "Jin remembers the deaths at the Inner Palace and is struggling with survivor's guilt over failing to save everyone.",
    "Jeok Cheongang recognizes Jin's guilt and advises him to value survival and mourn the dead.",
    "Jeok Cheongang remains quietly protective of Jin while hiding concern behind gruff teasing and threats.",
    "The Fire Dragon Pavilion members are reunited around Jin in Nanman.",
    "Ju Hwaran has taken control of the disorder and is fiercely protective of Jin's recovery.",
    "Jeok Cheongang and the Beast Miao King are concealing Jin's System and true condition from the others.",
    "Yohi has voluntarily entered the underground prison after her alliance with Baeksang.",
    "The Nanman Beast Palace is being rebuilt after the destruction of its Inner Palace and damage to its Outer Palace.",
    "Yayul Mok is occupied with restoration work and is rarely seen.",
    "The Beast Miao King has been missing for two days.",
    "Nanman's leadership is in an uproar over the Beast Miao King's disappearance."
  ],
  "continuity_sources": [
    716
  ],
  "open_questions": [
    "Where has the missing Beast Miao King gone, and why?"
  ],
  "safe_through": 716,
  "temporary_decisions": [
    "Retain Old Master for 노야 when Jin addresses Jeok Cheongang.",
    "Retain established renderings of Flame Divine Palm, Flame-Extinguishing Divine Fist, Dance of the Fire God and Demon, Solar Fist, Force, and Skill.",
    "Render 남만당 as Nanman Party.",
    "Render 각주 as Pavilion Master when Taishan addresses Jin.",
    "Render 대마두 as great fiend."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 일신     | **One God**         |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 사제     | **Junior Brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 하남     | **Henan**              |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 원후 | **Wonhu** | Named member of the Beast Miao King's personal guard, the Seven Miao Tigers. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 칠묘호 | **Seven Miao Tigers** | The Beast Miao King's personal guard, composed of elite Miao warriors. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 외궁 | **Outer Palace** | The outer compound of the Nanman Beast Palace. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |

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
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 야율목 | 원후 | Young_Palace_Lord_to_elder_personal_guard | Wonhu | formal-commanding | Calls on Wonhu to open a path through the surrounding guards. |
| 원후 | 진태경 | elder personal guard to trusted ally | you | formal and deferential | Wonhu addresses Jin while entrusting the collapsed Young Palace Lord to him. |
| 야수묘왕 | 원후 | lord to personal guard | monkey | familiar and teasing | The Beast Miao King calls Wonhu a liquor-loving monkey while throwing him his gourd. |
| 원후 | 야수묘왕 | personal guard to lord | you | informal and joking | Wonhu asks the hidden speaker for liquor before recognizing the Beast Miao King's gourd. |
| 진태경 | 부족장 | captor to captured tribal chieftain | tribal chieftain | casual, coercive, and mocking | Jin promises to spare the captured chieftain if he answers questions properly. |
| 부족장 | 진태경 | captured tribal chieftain to overpowering enemy | Jin Taekyung | alarmed and desperate | The chieftain recognizes Jin by name while fleeing and then begs for his life. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 716
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and Great Chieftain of the Miao people; he has been missing for two days while Nanman's leadership searches for him.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 713
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 716
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 716
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 716
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 716
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 716
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 716
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 716
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Wonhu.md

# Wonhu (원후)

- **Safe through:** Chapter 670
- **Aliases:** None
- **Role:** Wonhu is the eldest member of the Seven Miao Tigers, the Beast Miao King's personal guard.
- **Personality:** No personality traits are established.
- **Voice:** No distinctive voice is established.
- **Relationships:** Wonhu serves Yayul Cheok as a personal guard.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 716
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger and speaks Han Chinese haltingly but capably; he is currently occupied with rebuilding the damaged Palace.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

## Korean source

```text
＃717화



칠 주야는 사람에 따라 길다면 길고, 짧다면 짧은 시간이다.

하지만 현재 남만야수궁의 상황을 생각한다면, 그들이 입은 피해를 모두 수복하기에는 턱없이 부족한 시간이기도 했다.

균열에서 흘러나오던 마기(魔氣)가 사라졌다고 한들 그 여파는 아직 또렷이 남아 있으니까.

무수한 이들이 죽음을 맞았고, 누군가는 가족과 집을 잃었으며, 언제 다시 찾아올지 모를 재앙을 두려워하고 있을 것이다.

‘그런데 이런 상황에서 궁주인 야수묘왕이 사라졌다고?’

미간을 좁힌 채 생각에 잠겨 있던 나는 무겁게 입을 열었다.

“더 자세히 읊어 봐.”

혁무진이 뒤통수를 긁적이며 대답했다.

“어, 죄송하지만 제가 아는 게 그렇게 많지는 않아서요. 굳이 덧붙이자면 아까 말씀드렸던 대로 남만 수뇌부가 난리가 나고, 야율 대협을 찾기 위해 천라지망(天羅蜘網)까지 논의가 되었다는 것 정도?”

남만인들 입장에서는 당연한 일이다.

이런 어려운 상황에서 누구보다 구심점이 되어야 할 궁주가 사라졌으니까.

그리고 그들의 우려 속에는 다시 한번 암천(暗天)이 나섰을 가능성도 포함되어 있을 것이다.

‘이를테면 암살. 혹은 납치라든지.’

너무 나갔나 싶지만, 그렇다고 불가능한 일도 아니다.

남천마후와의 일전으로 야수묘왕 역시 적지 않은 부상을 입었다.

워낙 일신의 무위가 뛰어난 데다 늦지 않게 적천강의 도움을 받긴 했지만, 그렇다고 불과 며칠 만에 몸을 털고 일어날 정도는 아니다.

“그래서, 수색 결과는?”

내 물음에 혁무진이 고개를 갸웃거렸다.

“무슨 수색이요?”

“……너 진짜 머리 다친 거 아니냐. 방금 말했던 것도 기억 못 해?”

“아, 천라지망.”

이마를 탁, 친 혁무진이 말을 이었다.

“저는 논의되었다고만 말씀드렸는데요.”

“어?”

“그거 파투 났어요.”

뭐? 파투? 이런 중대 사안이?

잠시 눈을 깜빡이던 내가 물었다.

“혹시 나 잠든 사이에 남만야수궁이 암천에 먹혔냐?”

“수뇌부요? 그건 아닐걸요.”

“아, 그럼 괜히 부족민들한테 불안감 조성하기 싫어서 비밀 수색 작업 중이구나?”

“그것도 아닐걸요.”

“그럼 뭐 하는 새끼들이길래 궁주를 안 찾아.”

“그걸 왜 저한테 물어보세요. 제 궁주도 아닌데.”

빡!

기어코 뒤통수 마일리지를 적립한 혁무진이 소리 없는 비명을 내지르며 쓰러진다.

버둥거리는 녀석을 보며 작게 혀를 찬 남호가 나를 향해 고개를 돌렸다.

“원래대로라면 수뇌부 측에서도 뭐든 했을 거다. 천라지망이건, 비밀리에 전사들을 풀어 수색 작업을 벌이건 간에 말이다.”

나는 주먹을 내리며 대답했다.

“그런데 손을 놨다?”

“정확히는 손을 놓을 수밖에 없었지. 다른 누군가에 의해서.”

“다른 누군가라면…….”

“뭐 어쩌겠느냐. 어디서 굴러먹다 왔는지도 모를 개뼈다귀도 아니고. 천하의 화왕(火王)이 죄다 집어치우라는데.”

“……!”

“이틀 뒤 자정이 지나도 나타나지 않으면 당신이 직접 나설 테니 입 닥치고 민심부터 안정시키라고 했다더군. 고심하던 소궁주도 결국 화왕의 말을 들었지. 다른 부족장들이야 말할 것도 없고.”

적천강에, 야율목까지?

하지만 놀라움은 잠시뿐이었다. 잠깐 생각하던 나는 담담하게 고개를 끄덕였다.

“이틀 뒤 자정이면, 오늘이네요?”

“그렇지.”

“그렇군요.”

“그렇군요? 반응이 그게 전부냐?”

“뭐가 더 필요합니까? 노, 아니 스승님께서 집어치우라고 하셨으면 집어치워야죠.”

말없이 나를 바라보던 남호가 입맛을 다셨다.

“거, 사제 간의 신뢰가 아주 끈끈하구먼.”

“성격이 더러우셔서 그렇지, 그런 행동에는 다 이유가 있는 법 아니겠습니까.”

“방금 그 성격 더럽다는 말을 전해 줘도 여전히 끈끈할까?”

“……뜨끈해지긴 하겠네요. 저 하남에서 깨어나는 꼴 보고 싶으세요?”

“그걸 지금 말이라고 하느냐? 당연히…….”

한 치의 망설임도 없는 대답이 흘러나오던 그때, 슬쩍 누군가의 눈치를 살핀 남호가 침통한 표정으로 말을 이었다.

“당연히 비밀로 해야지. 암, 그렇고말고.”

“……?”

뭐지. 방금 주화란이 도끼눈을 뜬 것 같았는데.

하지만 반달처럼 휘어진 그녀의 눈매를 보니 내 착각이었던 것 같다. 아마 아직 잠이 덜 깨서 그런 거겠지.

짝.

소리 내서 뺨을 두드린 나는 기지개를 쭉 켰다. 우드득, 굳어 있던 뼈가 풀리며 몸이 한층 가뿐해진다.

‘몸 상태는 최상.’

레벨 업과 칠 주야간의 휴식으로 더할 나위 없이 좋다.

악몽을 꾼 덕분에 기분이 약간 더럽긴 하지만, 뭐 그거야 차차 나아질 문제다.

‘아마 다른 누군가도 마찬가지겠지.’

내심 중얼거린 나는 사람들을 향해 짐짓 졸린 표정을 지어 보였다.

“아, 간만에 말을 길게 했더니 꽤 피곤하네. 다들 잠시 자리 좀 비켜 주시겠어요?”

내게 환자라는 건 나름대로 큰 장점이다. 무슨 말을 해도 사람들이 의심 없이 고분고분하게 받아들여 주니까.

그리고 모두가 사라진 뒤, 나는 창문을 통해 전각을 빠져나왔다.



* * *



그저 단순한 짐작이었을 뿐이다.

없으면 말고. 있으면 다행이고. 딱 그 정도의 느낌.

하지만 그 누구도 찾지 않는 외진 풀숲에 들어선 순간, 내 짐작은 확신으로 바뀌었다.

“오, 여기네.”

스슥.

가볍게 건넨 인사에 풀잎이 미세하게 흔들린다. 동시에 한 줄기의 섬광이 나를 향해 쏘아졌다.

쐐액, 콰득!

볼 것도 없이 정확히 미간을 향해 날아든 비수를 잡아챘다. 손에 담긴 열양지기의 열기를 이기지 못한 비수의 날이 벌겋게 달아오른다.

투둑. 치이이익.

지면 위로 떨어지는 쇳물. 그제야 아직 복면을 벗지 않았음을 깨달은 나는 두 손을 번쩍 들어 올렸다.

“접니다, 진태경.”

그리고 다음 순간.

파팟.

허공에서 울려 퍼진 미세한 파공성과 함께, 우거진 풀숲 사이로 여러 개의 인영이 내려앉았다.

‘하나, 둘, 셋. 일곱.’

맞다. 내가 파악한 숫자도, 더불어 그들의 정체도.

“칠묘호(七苗虎). 맞죠?”

저벅.

“부디 결례를 용서하십시오.”

한 걸음 앞으로 나선 선두의 인영이 가면을 벗자 성격 좋아 보이는 사내의 얼굴이 드러난다.

뇌옥에서 보았던, 바로 그 얼굴이다.

“늦게나마 통성명을 하게 됐군요. 칠묘호의 원후(猿猴)가 남만의 은인이신 진 대협을 뵙습니다.”

“진 대협을 뵙습니다.”

원후를 따라 어색하게나마 공손히 포권을 취하는 그들의 모습에, 나는 피식 웃으며 대답했다.

“은인은 무슨. 오히려 제가 감사드려야지. 그날은 신세 많이 졌습니다.”

뇌옥에서의 일을 언급하자 원후 역시 미소를 머금었다.

“별말씀을. 진 대협이 아니었다면 우리 모두 죽은 목숨이나 다름없었습니다. 혹은…… 이지를 상실한 괴물이 되었겠지요.”

씁쓸한 뒷말과 함께 흐릿해지는 미소. 한숨을 내쉰 그가 문득 곤란한 표정을 지어 보였다.

“한데 이곳은 어찌 아시고 오셨는지.”

“전에 한번 와 본 적이 있어요. 야율 대협을 만나기 위해서.”

원후가 뭔가 짐작한 듯 고개를 끄덕였다.

“아마 그날이었나 보군요. 직속 호위인 저희에게도 아무런 말씀도 없이 사라지셨기에 많이 당황했었습니다.”

“네. 그때는 야율목, 아니 소궁주의 안내로 왔었죠.”

“이제는 누구도 찾지 않는 곳이니 밀담(密談)을 나누기에는 적격이지요.”

“다시 와 보니 확실히 그래 보이긴 하네요.”

외궁의 면적만 해도 어마어마하다. 작은 나라의 수도(首都)라 칭해도 부족함이 없을 정도이니, 굳이 길마저 사라진 외진 풀숲까지 사람들이 찾아올 이유는 없었다.

“그럼 진 대협께서는 혹시…….”

“예. 야율 대협을 뵈러 왔습니다. 왠지 여기 계실 것 같아서.”

“음.”

작게 침음성을 흘린 원후가 나를 물끄러미 바라보았다. 그리고 예상과는 다른, 나직한 한 마디가 그의 입술 사이로 흘러나왔다.

“길을 터라.”

그의 등 뒤에 도열해 있던 칠묘호가 동시에 몸을 움찔했다.

“대형(大兄).”

“하지만 주군께서 그 누구도 들이지 말라고…….”

“두 번 말 안 한다.”

단호한 원후의 목소리에, 잠시 머뭇거리던 칠묘호가 한숨을 푹 내쉬며 좌우로 갈라섰다.

“정확한 위치는 이미 알고 계실 거라 믿습니다. 그럼 이만.”

다시 한번 어색한 포권을 취한 원후가 돌아섰다.

아니, 돌아서려다 문득 고개를 돌려 나를 응시했다.

“하늘과 땅에 맹세컨대, 저를 비롯한 모든 남만인들은 진 대협의 도움을 기억할 것입니다.”

그건 나 역시 마찬가지다. 그들이 준 도움을 죽을 때까지 기억할 것이고, 살아 있어 주어서 감사할 따름이다.

칠묘호에게 목례로 인사를 대신한 나는 무성한 풀숲을 해치며 걸음을 옮겼다.

그렇게 촌각이나 지났을까. 다 무너져 가는 낡은 사당이 마침내 모습을 드러냈다.

저벅.

굳이 인기척을 감추지 않고 다가갔다. 오랜 세월 속에 모서리가 바스러지고, 구멍이 숭숭 뚫린 문틈 사이로 누군가의 등이 보였다.

“들어가도 됩니까?”

물음에 대한 대답은 돌아오지 않았고, 나는 낡은 사당 안으로 들어갔다.

끼이익. 낡은 바닥이 발에 닿자마자 비명을 질러 댔다.

“어우, 이 정도면 기름칠 좀 해야겠는데요.”

너스레를 떨며 주위를 둘러보던 그때, 가부좌를 튼 채 앉아 있던 넓은 등에서 나직한 목소리가 흘러나왔다.

“괜찮다. 이미 오래전부터 그랬으니.”

“하긴, 야율 대협께서 더 잘 아시겠죠. 어릴 적 대형 사고를 친 날이면 늘 이곳에 숨으셨다고 하셨으니.”

“……그랬던가.”

“벌써 잊으셨습니까? 지난번에 제게 말씀해 주셨으면서.”

“내가 별말을 다 했었군.”

기억하지 못해서 저렇게 말하는 것이 아니다. 이제는 이 세상에 없는 누군가의 죽음이 괴로워서일 것이다.

언제나 함께 이 낡은 사당에 숨어들었던 한 사람이.

그런 야수묘왕의 뒷모습을 물끄러미 바라보던 나는 문득 입을 열었다.

“왜 모습을 감추셨습니까? 말이라도 하고 가시지.”

“그저 그러고 싶었다.”

“떠나신 후 다들 불안해하고 있습니다. 우리 궁주 어디 갔냐고.”

“그래서 직접 찾아왔느냐?”

“산책 겸해서 와 봤습니다. 우리 궁주가 느그 궁주 되기 전에는 돌아가셔야죠.”

“궁주라.”

작게 실소를 흘린 야수묘왕이 공허한 목소리로 중얼거렸다.

“너는…… 내게 궁주의 자격이 있다고 생각하느냐?”

“음. 이곳에 온 이유에 따라 달라질 것 같은데요.”

“이유?”

“앞서 하셨던 대답처럼 그저 그러고 싶었다고 퉁 칠 거면 궁주도 때려치워야죠. 뭐, 자격도 없는 제가 왈가왈부할 문제는 아니지만.”

잠시간의 짧은 침묵이 흐른 끝에, 야수묘왕이 입을 열었다.

“괴로웠다. 견딜 수 없을 만큼.”

“무엇 때문입니까?”

“지키지 못했기 때문이다. 나를 따르는 수많은 부족민을, 그리고 가장 가까운 곳에서 고통받던 내 하나뿐인 의형제를.”

“…….”

“그중에서도 날 가장 괴롭게 한 것이 무엇인지 아느냐?”

나는 대답하지 않았고, 야수묘왕의 목소리는 계속해서 이어졌다.
```

## Final English reading copy

```markdown
# Chapter 717

Seven days and nights can be a long time or a short time, depending on the person.

But considering the current situation in the Nanman Beast Palace, it was also nowhere near enough time to repair all the damage they had suffered.

Even though the demonic qi flowing from the rift had disappeared, its aftermath was still painfully clear.

Countless people had died. Some had lost their families and homes. Others were probably living in fear of the disaster that might return at any moment.

*The Beast Miao King disappeared in a situation like this?*

I narrowed my brows, lost in thought, then finally opened my mouth.

“Tell me in more detail.”

Hyuk Mujin scratched the back of his head as he answered.

“Uh, I’m sorry, but I don’t actually know that much. If I had to add anything, it would be what I mentioned earlier—the Nanman leadership is in an uproar, and they were even discussing deploying a net over heaven and earth to search for Great Hero Yayul.”

That was only natural from the Nanman people’s perspective.

The Palace Lord, who should have been their center of gravity more than anyone else in such a difficult situation, had disappeared.

And their concerns probably included the possibility that Dark Heaven had made another move.

*An assassination, for example. Or a kidnapping.*

Maybe I was getting ahead of myself, but it wasn’t impossible.

The Beast Miao King had suffered considerable injuries in his battle with the Southern Heaven Demon Empress.

His personal martial prowess was extraordinary, and Jeok Cheongang had arrived before it was too late to help him. Even so, he couldn’t have simply shaken off his injuries and gotten back on his feet after only a few days.

“So, what were the results of the search?”

At my question, Hyuk Mujin tilted his head.

“What search?”

“……Did you really injure your head? You don’t even remember what you just said?”

“Oh. The net over heaven and earth.”

Hyuk Mujin slapped his forehead and continued.

“I only said it was being discussed.”

“Huh?”

“It fell through.”

What? It fell through? This was a matter of such importance?

I blinked a few times before asking,

“Did the Nanman Beast Palace get swallowed up by Dark Heaven while I was asleep?”

“The leadership? I don’t think so.”

“Ah, then they’re secretly conducting a search because they don’t want to make the tribespeople anxious?”

“I don’t think so either.”

“Then what the hell are they doing, not looking for their Palace Lord?”

“Why are you asking me? He isn’t my Palace Lord.”

*Whack!*

Having finally earned another point toward his back-of-the-head mileage, Hyuk Mujin collapsed with a silent scream.

Watching him writhe on the ground, Namho clicked his tongue softly and turned toward me.

“Under normal circumstances, the leadership would have done something. Whether that meant deploying a net over heaven and earth or secretly sending out warriors to search.”

I lowered my fist and replied,

“But they gave up?”

“More precisely, they had no choice but to give up. Because of someone else.”

“Someone else?”

“What choice did they have? This wasn’t some nobody who’d crawled in off the street. The great Fire King himself told them to drop everything.”

“……!”

“He reportedly told them that if the Palace Lord didn’t appear by midnight two days later, he would step in personally, so they should shut their mouths and focus on calming the people. The Young Palace Lord agonized over it, but in the end, he listened to the Fire King. The other chieftains had no choice either.”

Jeok Cheongang—and Yayul Mok, too?

But my surprise lasted only a moment. After thinking briefly, I nodded calmly.

“If it was midnight two days later, that means tonight, right?”

“That’s right.”

“I see.”

“I see? That’s all you have to say?”

“What else is there to say? If Ol—no, if Master said to drop it, then we should drop it.”

Namho stared at me silently, then smacked his lips.

“Well, the trust between master and disciple is awfully strong.”

“His personality is terrible, but there’s always a reason behind his actions.”

“If I told him you said his personality was terrible, would the bond still be that strong?”

“……It might get heated. Do you want to see me wake up in Henan?”

“Why would you even ask? Of course…”

As an answer came out without the slightest hesitation, Namho glanced at someone’s reaction before continuing in a mournful voice.

“Of course I’ll keep it a secret. Absolutely.”

“……?”

What was that? Had Ju Hwaran just given him an axe-eyed glare?

But when I looked at the way her eyes curved like a half-moon, I decided it had only been my imagination. I probably hadn’t fully woken up yet.

*Smack.*

I patted my cheeks and stretched. With a series of cracks, my stiff bones loosened, and my body felt even lighter.

*My condition is perfect.*

Between leveling up and resting for seven days and nights, I was feeling better than ever.

My mood was a little foul thanks to the nightmare, but that was something that would improve with time.

*Someone else is probably feeling the same way.*

I muttered inwardly, then deliberately put on a sleepy expression for everyone around me.

“Ah, I talked for quite a while after not speaking much for so long. I’m pretty tired. Could everyone give me some space for a moment?”

Being a patient had its advantages. No matter what I said, people accepted it obediently without suspicion.

And once everyone had left, I slipped out of the pavilion through the window.

* * *

It had only been a simple guess.

*If he isn’t there, no big deal. If he is, then great.*

That was all I had expected.

But the moment I entered a remote patch of grass that no one ever visited, my guess became certainty.

“Oh, there you are.”

*Rustle.*

At my casual greeting, the blades of grass trembled faintly. At the same time, a streak of light shot toward me.

*Whoosh—crack!*

The dagger flew straight toward the space between my brows. I caught it without even looking, and the blade began to glow red, unable to withstand the heat of the Scorching Yang Qi in my hand.

*Drip. Hissss.*

Molten metal fell to the ground. Only then did I realize that I was still wearing my mask, so I quickly raised both hands.

“It’s me. Jin Taekyung.”

And then—

*Fwish!*

With several faint sounds of air splitting through the empty sky, multiple figures landed among the dense grass.

*One, two, three…… seven.*

That was the number I had sensed, and I had correctly identified them as well.

“The Seven Miao Tigers, right?”

*Step.*

“Please forgive our rudeness.”

When the figure at the front stepped forward and removed his mask, the face of a good-natured-looking man was revealed.

It was the same face I had seen in the underground prison.

“At last, we can exchange names. Wonhu of the Seven Miao Tigers pays his respects to Great Hero Jin, Nanman’s benefactor.”

“We pay our respects to Great Hero Jin.”

Following Wonhu, the others performed awkward but respectful fist-palm salutes.

I gave a quiet laugh and answered,

“Benefactor? Not at all. I’m the one who should be thanking you. You helped me a great deal that day.”

At the mention of what had happened in the underground prison, Wonhu smiled as well.

“Please, think nothing of it. If not for you, Great Hero Jin, all of us would have been as good as dead. Or…… we would have become monsters who had lost their minds.”

His smile faded along with his bitter words. After letting out a sigh, he suddenly looked troubled.

“But how did you know about this place?”

“I came here once before, to meet Great Hero Yayul.”

Wonhu nodded as if he had guessed the reason.

“That must have been the day. He disappeared without saying a word even to us, his direct guards, so we were very confused.”

“Yes. Yayul Mok—or rather, the Young Palace Lord—guided me here that time.”

“Now that no one comes here anymore, it is perfect for a private conversation.”

“After coming back, I can see that.”

The Outer Palace alone was enormous. It was large enough to be called the capital of a small country, so there was no reason for anyone to seek out a remote patch of grass where even the path had disappeared.

“Then, Great Hero Jin, might you perhaps……”

“Yes. I came to see Great Hero Yayul. I had a feeling he would be here.”

“Hmm.”

Wonhu let out a low hum and stared at me. Then, instead of the answer I had expected, a quiet command slipped from his lips.

“Make way.”

The Seven Miao Tigers standing behind him flinched in unison.

“Big Brother.”

“But our lord ordered us not to let anyone in……”

“I won’t say it twice.”

At Wonhu’s firm voice, the Seven Miao Tigers hesitated for a moment before sighing heavily and splitting apart to either side.

“I trust you already know the exact location. Then, I’ll take my leave.”

Wonhu gave me another awkward fist-palm salute and turned around.

Or he was about to turn around when he suddenly looked back at me.

“I swear by heaven and earth that all the Nanman people, myself included, will remember Great Hero Jin’s help.”

I felt the same way. I would remember the help they had given me until the day I died, and all I could do was be grateful that they were still alive.

I substituted a nod for a farewell to the Seven Miao Tigers, then moved forward through the thick grass.

A few moments later, a dilapidated old shrine finally came into view.

*Step.*

I approached without bothering to conceal my presence. Through the gaps in the door, whose corners had crumbled with age and which was riddled with holes, I could see someone’s back.

“May I come in?”

No answer came, so I entered the old shrine.

*Screeech.*

The moment my foot touched the worn floor, it let out a shriek.

“Whoa. At this point, it could really use some oil.”

As I looked around and continued making small talk, a low voice came from the broad back of the man sitting cross-legged.

“It’s fine. It’s been like that for a long time.”

“True. Great Hero Yayul would know better. You said you always hid here whenever you caused some major incident as a child.”

“……Did I?”

“Have you already forgotten? You told me about it last time.”

“I must have told you all sorts of things.”

He wasn’t saying that because he didn’t remember.

He was saying it because he was suffering over the death of someone who was no longer in this world.

Someone who had always hidden in this old shrine with him.

As I gazed at the Beast Miao King’s back, I suddenly opened my mouth.

“Why did you disappear? You could have at least said something before you left.”

“I simply wanted to.”

“Everyone’s anxious after you left. They keep asking where our Palace Lord went.”

“So you came looking for me yourself?”

“I came on a walk. You should get back before our Palace Lord becomes your Palace Lord.”

“Palace Lord.”

The Beast Miao King let out a quiet, humorless laugh and muttered in an empty voice,

“Do you think…… I have the qualifications to be a Palace Lord?”

“Hmm. I suppose it depends on why you came here.”

“Why?”

“If you’re going to brush it off with the same answer as before and say you simply wanted to, then you should quit being Palace Lord, too. Though, it’s not really my place to say anything when I have no qualifications myself.”

After a brief silence, the Beast Miao King opened his mouth.

“It hurt. More than I could bear.”

“What was it?”

“Because I failed to protect them. The countless tribespeople who followed me, and my one and only sworn brother, who suffered right beside me.”

“……”

“Do you know what hurt me the most of all?”
```

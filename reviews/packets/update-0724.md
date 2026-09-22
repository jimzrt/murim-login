<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0724.txt",
      "sha256": "46f9d70ed7489023e897096fa9e6850986ba44cc1883da158368fb8a4b6abc47",
      "bytes": 13614
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "db8d4cfaa1a743b7bb3f38ef9b26bd3e9307cd1cdd5c2fb185f0616f16211d38",
      "bytes": 1820
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6de3db0b4bce57d862aa99f8498cabf98cd943f94faedafcb0c64157ed6cf676",
      "bytes": 209577
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "9d2d993c9a61849c7133599295008417dd819c23f47ac1f86d18a293b4a7e3b5",
      "bytes": 928
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9f315490d5f311c851af279a9a0d592ccefd84d2b722e39681d8358d4f7ade5d",
      "bytes": 553
    },
    {
      "path": "characters/Hanga.md",
      "sha256": "be6a5ba0a8560e74e01d62c9f7174c05a757112314d7f78173b24b3230fa41ca",
      "bytes": 568
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "569c6ca4cda1cdbaadcc40fabd102fab7b72d7a75c8dfca57b80175fd9ca824c",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2aa40583b71102c6f3e997301f24ff936a346f18df0e8f2b29fa4cdfd6ae4b82",
      "bytes": 1702
    },
    {
      "path": "characters/Namho.md",
      "sha256": "8d2b0baac27c6d16cb39468cd593eafb39689c8f2506fbc70880c109217f21c0",
      "bytes": 843
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "c8f701e8a7131e1a71751338e7010e115866bf44b2b7eb57fa4568707a2f5e48",
      "bytes": 715
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "5850c83a8a40ced25d92e4071d7ce7381540144ce6899ef8b7ddc4d0ebcc3fdd",
      "bytes": 787
    },
    {
      "path": "characters/White Tiger.md",
      "sha256": "69fa3be37157d38372f85c0f71fff23727ce420d4bc30506a8b196d2693b8cc3",
      "bytes": 641
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "f466cf4fef1fb252c563321fd805f10a32b66c32ffcedca13d8dbab9df3430d8",
      "bytes": 951
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9dea8b4187f83ff9e3ad17cb4601943617d80ed52fb46c971ef5bc835fdcdfc6",
      "bytes": 219534
    }
  ],
  "estimated_tokens": 12772
}
-->

# Durable State Update — Chapter 724

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 724. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 724. Profile updates may replace only one
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
  "chapter": 724,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 724,
    "continuity_sources": [724],
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
    "The Sacred Rain is still restoring Nanman's land and empowering its people, but its effects will end when the rain stops.",
    "The Nanman Beast Palace's restoration is nearing completion after the Inner Palace's devastation and the Outer Palace's destruction.",
    "The Great Chieftain system has been abolished, and the Nanman Beast Palace now operates under the Palace Lord's sole authority with the Tribal Grand Council retained as a safeguard.",
    "Yohi was pardoned for helping evacuate the Outer Palace and became the first advocate of abolishing the Great Chieftain system.",
    "The Beast Miao King serves as Nanman's Palace Lord and public priest of the Earth Mother Goddess.",
    "The Mother Goddess Scripture establishes the Earth Mother Goddess as Nanman's sole deity and records her apostles throughout Nanman's history.",
    "Jin Taekyung has gained the Title Apostle of the Earth Mother Goddess and the Religious Reformation achievement.",
    "Yayul Cheok has formally petitioned Jin Taekyung for Nanman's admission into the Murim Alliance."
  ],
  "continuity_sources": [
    723
  ],
  "open_questions": [
    "Will the Murim Alliance accept Yayul Cheok's petition for Nanman's admission?",
    "How will the Mother Goddess Scripture shape Nanman's unified religious system?",
    "How will Nanman's new political structure function after the Great Chieftain system is abolished?",
    "What will happen to Nanman after the Sacred Rain ends?"
  ],
  "safe_through": 723,
  "temporary_decisions": [
    "Render 모신전 as Mother Goddess Scripture.",
    "Render 대지모신의 사도 as Apostle of the Earth Mother Goddess.",
    "Render 종교 개혁 as Religious Reformation.",
    "Retain buff for 버프 in Jin Taekyung's narration."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 소림     | **Shaolin**                      |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 사부     | **Master**                                   |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 정마대전   | **Great Faction War**         |
| 소협      | **Young Hero**                                                  |
| 소저      | **Young Lady**                                                  |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 대지모신 | **Earth Mother Goddess** | New deity proclaimed by Jin Taekyung as Nanman's One God. |
| 성우 | **Sacred Rain** | Name later given to the rain released as the Earth Mother Goddess's blessing. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 항아 | visiting_adult_to_local_child | little one | coaxing and encouraging | Questions Hanga with an artificially kind smile and offers two food bundles. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 야율목 | 남호 | Nanman Young Palace Lord to elderly guest and Hidden Shadow Pavilion agent | old man | respectful and familiar | Yayul Mok uses the honorific 노인장 while praising Namho's knowledge of White Tigers. |
| 야율목 | 야수묘왕 | son_to_father | Father | formal and deferential | Yayul Mok calls out to the Beast Miao King after the rescue party arrives. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 야수묘왕 | 적천강 | junior allied master to legendary senior martial master | Old Master Jeok | formal-deferential | The Beast Miao King respectfully addresses Jeok while asking him to sit and consulting him about the demonic stone. |
| 적천강 | 야수묘왕 | senior allied martial master to Nanman Beast Palace Lord | you | blunt, commanding, and mocking | Jeok orders the Beast Miao King to stand aside and mocks his inability to destroy the corrupted artifact. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 723
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, Great Chieftain of the Miao people, the publicly recognized sole priest of the Earth Mother Goddess, and the ruler of newly unified Nanman leading its religious and political reform.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 723
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hanga.md

# Hanga (항아)

- **Safe through:** Chapter 723
- **Aliases:** None
- **Role:** Local village girl, Jang-pal’s daughter, who lives near Jang Taebo and regularly visits him.
- **Personality:** Curious, energetic, observant, and already attentive to the value of information and food.
- **Voice:** Childlike, direct, and inquisitive, with an occasional surprisingly worldly remark.
- **Relationships:** Calls Jang Taebo Grandpa; Jang Taebo is his elderly neighbor and only conversational companion.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 721
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 723
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 723
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 719
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 723
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### White Tiger.md

# White Tiger (백호)

- **Safe through:** Chapter 721
- **Aliases:** Whitey
- **Role:** The White Tiger was the guardian spirit and protector of the land; after absorbing the sacred stone, it entered the rift to seal it, became corrupted, and was killed.
- **Personality:** Irritable and contemptuous of Jin Taekyung's jokes.
- **Voice:** Telepathic, terse, and easily exasperated.
- **Relationships:** The White Tiger shared a roughly three-hundred-year friendship with Yayul Cheon and entrusted Jin Taekyung and Jeok Cheongang with killing it if corruption overcame it.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 723
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger and speaks Han Chinese haltingly but capably; he is helping complete the Palace's restoration and implement its post-crisis reforms.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

## Korean source

```text
＃724화



누군가는 떠나고, 누군가는 남았다.

하지만 먼 길을 떠나는 이들의 뒷모습을 지켜보던 야수묘왕은 알고 있었다. 이 이별의 여운이 채 가시기도 전에 그들은 다시 재회하리라는 것을.

그리고 그 만남의 장소가, 함께 등을 맞대고 싸울 전장(戰場)이 되리라는 것 역시도.

“결국, 다시 한번 중원으로 향하게 되었군요.”

귓가를 파고드는 누군가의 목소리에, 야수묘왕이 작게 고개를 끄덕였다.

“그래. 끝끝내 이리되었다.”

“많은 피가 흐를 것입니다.”

“이 아비의 결정이 잘못되었다 생각하느냐?”

“아닙니다.”

야율목이 담담하게 말을 이었다.

“아버님께서. 아니, 궁주께서 중원행을 원치 않으셨다면 저 혼자서라도 저들과 함께 떠났을 테니까요.”

“……!”

야율목의 시선이 저 멀리 멀어져 가는 이들의 뒷모습을 향한다.

낯선 땅에서 온 이방인들. 그러나 저 이방인들이 있었기에, 자신들의 고향을 지켜 낼 수 있었다.

“이제는 우리가 저들을 도울 차례입니다.”

분명 그 역시 중원을 적대시하고, 한족을 배척하던 때도 있었다.

하지만 이제는 다르다. 아직 여물지 않은 남만야수궁의 소궁주는 한 이방인으로부터 인의(人義)을 배웠고, 언젠가 그와 나누었던 대화를 평생토록 잊지 못할 것이다.



‘만약 목초지에 불이 나면 어쩔래?’

‘당장 꺼야지.’

‘왜?’

‘꺼트리지 않으면 불길이 사방으로 번질 테니까.’

‘좋아. 답 나왔네.’

‘……!’

‘우리가 온 이유에 대해 복잡하게 생각하지 마. 불이 났으니까 끄려고 하는 것뿐이야. 수십 년 전 고향을 떠나 중원으로 향한 이 땅의 남만인들처럼.’



처음에는 믿지 않았다. 믿을 수 없었다.

야율목이 알고 있는 한족은, 신뢰를 저버리고 숱한 남만인을 죽음으로 내몰았던 비열하기 짝이 없는 족속이었으니까.

아무 대가 없는 도움을 주기 위해 만 리가 넘는 거리를 넘어 찾아왔을 리 없었다.

분명…… 그리 생각하던 때가 있었다.

‘그러나 지금은 안다. 네가 했던 그 말의 의미를.’

이미 천하(天下)라는 목초지에 불이 붙었고, 암천이라는 거대한 화마(火魔)는 모든 것을 집어삼킬 것이다.

어디에서 태어나고 자랐는지, 어떤 복색과 생김새를 지녔는지는 이제 중요하지 않다.

비로소 하나로 통합된 남만처럼, 저 불을 끄기 위해서는 모두가 합심해야 한다.

“목숨을 걸고 싸울 것입니다. 이 땅에 살아가는 모두를 위해서. 그리고 저들을 위해서.”

그리고 이처럼 굳은 의지를 보이는 야율목의 모습에, 야수묘왕은 희미한 웃음을 머금었다.

‘언제 이리 컸는지.’

마침내 하나가 된 남만처럼, 그의 하나뿐인 아들도 한 단계 성장했다.

그러나 어째서일까. 지금 이 순간 야수묘왕의 마음은 텅 빈 항아리처럼 허전했다.

‘못난 녀석.’

씁쓸한 뇌까림을 삼킨 야수묘왕은 품에서 꺼낸 호리병을 기울였다.

향긋한 주향(酒香)을 풍기는 과실주가 서서히 잦아드는 빗줄기와 함께 땅으로, 어느 의형제가 함께 나고 자란 고향의 흙 속으로 스며들었다.

“술맛 한번 좋군. 그렇지 않으냐?”

술 한 방울 입에 대지 않은 야수묘왕의 중얼거림에 주위의 사람들이 의아한 표정을 지었지만, 그는 후련하게 웃어 보였다.

이것으로 되었다.

먼 훗날, 그들은 다시 만나 술잔을 기울이게 될 테니까.

‘그래, 언젠가 반드시.’

야수묘왕은 문득 고개를 들어 하늘을 바라보았다.

서서히 그쳐 가는 빗줄기 사이, 무수히 많은 남만인들의 머리 위로 푸르른 창천(蒼天)이 펼쳐져 있었다.

아니, 그것은 어쩌면 보이지 않는 절대자의 시선일지도 몰랐다.

“전고(戰鼓)를 울려라.”

숨 막히는 적막을 깨트리는 나직한 목소리. 크게 심호흡한 야수묘왕은 공력을 끌어올려 외쳤다.

“신께서 원하신다!”

사방을 떨어 울리는 창룡후(蒼龍吼)와 함께, 높은 언덕 어딘가에서 그들을 굽어보고 있던 새하얀 백호가 포효를 내질렀다.

- 크아아아앙!

차차창!

와아아아아!

수천, 수만에 달하는 짐승과 인간이 힘껏 발을 구르고 함성을 내질렀다. 무수히 많은 날붙이에 반사된 햇빛이 사방으로 퍼져 나간다.

바야흐로, 대전쟁의 서막이었다.



* * *



우수에 찬 눈빛과 진중한 분위기. 혁무진이 모두의 시선 속에서 천천히 입술을 열었다.

“그저 사람이, 사람을 살리고자 한 것뿐입니다.”

“그만해라.”

“대가를 얻기 위해 한 일이 아니라서. 다시 한번 누군가의 희생을 요구할 수가 없어서. 그래서 떠나려고 했습니다.”

“그만하라고.”

“에이, 왜 그러십니까. 이런 건 몇 번을 다시 해도 안 질립니다. 솔직히 다들 인정하시죠?”

쉼 없이 달려가는 곰 위에서 멧돼지 뒷다리를 뜯고 있던 태산이 세차게 고개를 끄덕였다.

“태산이! 인정한다!”

“보세요. 쟤도 인정하잖아요. 그저 사람이, 사람을 살리고자…….”

나는 조용히 혁무진의 말을 끊었다.

“무진아.”

“예.”

“고자 되고 싶니?”

혁무진의 얼굴에 만연해 있던 미소가 사그라졌다.

“아뇨.”

“아니면 인생이 무료해?”

“그럴 리가요. 이미 지금도 제 인생이 너무 격렬한 것 같아서 걱정입니다.”

“그럼 평안하게 해 줘?”

“혹시 죽이시겠다는 뜻은 아니죠?”

“맞다면?”

“우와, 저기 좀 보세요. 경치가 참 좋네요.”

“그래. 조용히 가자.”

“……넵.”

하지만 조용히 입을 다문 혁무진과는 달리, 태산은 아쉬운 표정으로 앵콜을 요청했다.

“각주! 태산이는 더 듣고 싶다!”

그리고 나는 담당 일진을 불렀다.

“남 노인, 저 새끼 주둥이를 틀어막을 때가 된 것 같습니다.”

“오오, 드디어!”

광복을 맞이한 독립투사처럼 환호한 남호가 기다렸다는 듯이 품속에서 입마개를 꺼냈다.

검고 단단한 철과 가죽끈으로 이어진, 해괴하면서도 한편으로는 익숙한 형태의 입마개를.

“잠깐. 그거 어디서 났어요?”

“남만인 조련사에게 얻었다. 주로 야생 곰을 길들일 때 쓴다더군.”

“…….”

“왜 그런 눈빛으로 보는 거지? 무슨 문제라도 있느냐?”

“그, 문제가 될 것까진 없는데.”

왠지 모르게 약간 마음에 걸린다고나 할까. 앞으로는 태산이라는 이름 대신 TAESAN-317이라는 품번으로 불러야 할 것 같은 느낌적인 느낌이랄까…….

잠시 망설이던 나는 이내 찝찝함을 이겨 내지 못하고 한숨을 내쉬었다.

“그거 채우지 마세요. 아니다. 그냥 버리세요.”

“안 돼! 어째서!”

어째서긴. 내 눈만 더러워질 것 같아서 그렇지.

나는 거의 통곡하다시피 하는 남호로부터 입마개를 뺏어 저 멀리 던져 버렸고, 그 광경을 모두 지켜보던 적천강은 떨떠름한 얼굴로 입을 열었다.

“도대체 남만에서 무슨 일이 있었던 게냐?”

순간 말을 이해하지 못한 내가 되물었다.

“예?”

“무슨 일이 있었기에 다들 제정신이 아니냐고 묻는 게다.”

“남만에서 많은 일이 있던 건 사실이지만, 다들 처음 상태 그대로인데요.”

“뭣이!”

“놀랍게도 사실입니다.”

“이노옴! 헛소리하지 말거라. 돌아가는 꼴이 이토록 개판인데 한 사람도 죽지 않았다는 것이 말이 되느냐!”

“…….”

그러게요. 시바 거.

남만에서의 일을 돌이켜보니 정말 대지모신의 가호가 있던 건 아닌가, 하는 합리적 의심이 들 정도다.

‘죽을 고비를 여러 번 넘기긴 했지만, 멀쩡히 돌아가는 것만으로도 기적이지.’

물론 그 고비를 여러 번 넘긴 것은 내가 유일하고, 각각 크고 작은 부상을 입었던 일행들도 전부 성우(聖雨)의 효력을 톡톡히 본 덕분에 지금은 씻은 듯이 나을 수 있었다.

‘게다가 암천의 흉계도 어찌어찌 막았고.’

비록 그 과정에서 적지 않은 희생자가 나왔지만, 애당초 나와 화룡각의 최우선 목표나 다름없던 남천마후를 저지할 수 있었다는 것만으로도 절반 이상의 성공이다.

‘거기에 더해 남만야수궁의 정식 입맹(入盟)까지.’

사실 남만야수궁의 합류는 남천마후를 저지함과 동시에 예견된 것이나 다름없었다.

설령 대지모신이라는 브랜드 효과가 없었어도 결과는 크게 달라지지 않았을 것이다.

어중간하게 짓밟은 불씨는 더욱 크게 타오르고, 분노라는 감정은 흩어졌던 이들을 하나로 뭉치게 하니까.

나는 단지 그들에게 또 다른 구심점을 만들어 주었을 뿐이다.

수백 년간 내려온 부족 간의 경계마저 지울 수 있는 유일신의 존재. 그들이 보다 더 단결되고 강력한 세력으로 거듭날 수 있는 구심점을.

‘그리고 그 덕분에 무림맹의 전력 역시 강해졌고.’

이번만큼은 단언할 수 있다. 이 사건으로 인해 남만야수궁은 확실한 아군이 되었다.

떠나기 전 야수묘왕이 약속한 바에 따르면 그들은 과거 정마대전 때보다도 많은 병력을 파견할 것이고, 사력을 다해 암천을 막아설 것이다.

하지만 어째서일까.

‘왜 이렇게 불안하지?’

분명 큰 성과를 거두었음에도, 내 마음 한구석은 여전히 석연치 않은 찝찝함으로 가득했다.

그리고 어쩌면 그 이유는, 아직 해결되지 못한 의문 때문일지도 몰랐다.

‘신(新) 무림맹이 탄생하고, 구파일방과 오대세가를 중심으로 중원의 모든 힘이 모이고 있다. 그런데도 암천의 완전한 전력이 드러나지 않았어.’

산서성에서의 첫 개입. 이후 벌어진 소림혈사부터 지금까지 이어진 일련의 사건들을 절대 소소하다 할 수는 없지만, 그건 암천이라는 집단 전체가 아닌 파편의 일부분에 불과하다.

‘간을 볼 시기는 이미 지났을 텐데.’

도대체 놈들의, 아니 천주의 의도는 무엇일까.

그리고 천주는 어째서…….

“왜 굳이 나한테 이렇게까지 관심을 가지는 거지?”

무심코 흘러나온 내 중얼거림에, 모두의 시선이 확 쏠렸다. 뭐라 수습하기도 전에 혁무진이 미어캣처럼 바짝 고개를 쳐들었다.

“헉, 조장님. 혹시 누구한테 고백받으셨어요? 세상에. 남만인?”

“…….”

저 샛별처럼 반짝이는 혁무진의 눈깔을 후벼 파고 싶다.

나는 애써 충동을 억누르며 대답했다.

“그런 거 아냐. 미친놈아.”

“미쳤다. 그럼 한족?”

“아니라고 몇 번을 말해야…… 아, 생각해 보니까 한족은 맞겠네.”

“와. 도대체 언젭니까? 고백한 상대는 누구예요?”

“천주(天主).”

“이야. 이름부터가 범상치 않은 처자일세. 딱 봐도 양갓집 규수 같은…….”

호들갑을 떨던 혁무진이 문득 입을 다물었다. 눈을 깜빡이며 잠시 생각하던 녀석이 말을 이었다.

“누구요?”

“천주.”

“제가 아는, 그러니까 모두가 아는 그 천주요?”

“그럼 걔 빼고 누가 있냐.”

침묵하던 혁무진이 작게 중얼거렸다.

“씨바, 그 양갓집이 신강(新疆)에 있었네…….”

곤륜파가 위치한 청해(靑海)를 넘으면 신강이고, 신강은 이미 천 년 전부터 마도(魔道)의 영역.

내게 관심을 보인다는 처자가 암천댁 규수라는 걸 알게 된 사람들은 잠시 할 말을 잃은 채 서로를 바라보았고, 동시다발적으로 의문을 쏟아냈다.

“아니, 천주가 왜요?”

혁무진의 물음에 남호가 끼어들었다.

“뻔하지. 번번이 훼방을 놓으니 그런 것 아니겠느냐?”

“그건 사실이지만, 그렇다고 조장님이 삼성(三星)도, 십왕(十王)은 아니잖습니까. 꼴랑 이제 막 명성을 얻은 찌꺼기인데.”

“생각해 보니 그것도 틀린 말은 아니군.”

“태산이는 찌꺼기도 먹을 수 있다.”

“저 썅노무 새끼. 내 이럴 줄 알고 입마개를 하나 더 챙겨 왔지. 이리 와. 주둥이 벌려.”

“아니, 다들 말씀을 왜 그리하세요? 우리 각주님이 찌꺼기라니! 송 호위, 사마 소협! 무슨 말이라도 해봐요!”

“주 소저, 미안하지만 난 이쯤에서 떠나야 할 것 같소. 남만까지는 어찌어찌 왔다 해도 저자에게 천주가 관심을 보인다는 건 좀.”

“태산아! 그거 고기 아니니까 물지 마라! 남 노인! 그 입마개 당장 내려놓지 못하겠소!”

“…….”

씨바. 개판도 이런 개판이 없다.

그리고 눈 앞에 펼쳐진 총체적 난국을 멍하니 바라보던 그때. 나직한 전음(傳音)이 귓가를 파고들었다.

- 이야기 좀 하자.

적천강이었다.
```

## Final English reading copy

```markdown
# Chapter 724

Some people left, while others stayed behind.

But as the Beast Miao King watched the backs of those departing on a long journey, he knew. Before the lingering ache of this farewell had even faded, they would meet again.

And that place of reunion would be a battlefield where they fought back-to-back.

“In the end, we’re heading to the Central Plains once again.”

At the voice that pierced his ears, the Beast Miao King gave a small nod.

“Yes. It came to this in the end.”

“A great deal of blood will be spilled.”

“Do you think your father’s decision was wrong?”

“No.”

Yayul Mok continued calmly.

“If my father… No, if the Palace Lord had not wanted to go to the Central Plains, I would have left with them even on my own.”

“……!”

Yayul Mok’s gaze turned toward the figures receding in the distance.

Strangers from a foreign land. And yet, because those strangers had come, they had been able to protect their homeland.

“Now it is our turn to help them.”

There had certainly been a time when he, too, had regarded the Central Plains with hostility and rejected the Han Chinese.

But things were different now. The still-unseasoned Young Palace Lord of the Nanman Beast Palace had learned what it meant to act with humanity from one stranger, and he would never forget the conversation they had shared that day.



*“What would you do if the pasture caught fire?”*

*“Put it out right away.”*

*“Why?”*

*“If we don’t put it out, the flames will spread in every direction.”*

*“Good. There’s your answer.”*

*“……!”*

*“Don’t overthink why we came. A fire started, so we’re putting it out. Just like the Nanman people of this land who left their homeland for the Central Plains decades ago.”*



At first, he had not believed it. He could not believe it.

The Han Chinese he knew were nothing but utterly despicable people who had betrayed trust and driven countless Nanman people to their deaths.

There was no way they had crossed a distance of more than ten thousand li to offer help without asking anything in return.

That was what he had thought back then…

*But now I understand. I understand what you meant.*

The pasture called the world had already caught fire, and the enormous conflagration known as Dark Heaven would devour everything.

Where someone had been born and raised, what clothes they wore, or what they looked like no longer mattered.

Just as Nanman had finally become one, everyone would have to join forces to put out that fire.

“We will fight with our lives on the line. For everyone living on this land. And for them.”

Seeing Yayul Mok display such unyielding determination, the Beast Miao King smiled faintly.

*When did he grow so much?*

Just as Nanman had finally become one, his only son had taken another step forward.

And yet, why was it that at this moment the Beast Miao King’s heart felt as hollow as an empty jar?

*You hopeless brat.*

Swallowing the bitter mutter, the Beast Miao King tilted the flask he had taken from inside his robes.

Fruit wine carrying a fragrant scent of alcohol seeped into the earth along with the slowly fading rain—into the soil of the homeland where two sworn brothers had been born and raised together.

“This wine tastes excellent. Don’t you agree?”

The Beast Miao King had not tasted a drop, yet at his mumble the people around him looked puzzled. He merely laughed with relief.

This was enough.

In the distant future, they would meet again and raise their cups together.

*Yes. One day, surely.*

The Beast Miao King suddenly lifted his head and looked at the sky.

Between the slowly fading sheets of rain, azure heaven stretched above the heads of countless Nanman people.

Or perhaps it was the gaze of an unseen absolute being.

“Sound the war drums.”

His quiet voice broke the suffocating silence. Taking a deep breath, the Beast Miao King drew up his internal energy and shouted.

“God wills it!”

As the azure dragon’s roar reverberated in every direction, a snow-white White Tiger gazing down at them from somewhere atop a high hill let out a roar.

—Kraaaaaaang!

Clang-clang-clang!

Waaaaaaah!

Thousands—tens of thousands—of beasts and humans stamped their feet and roared. Sunlight reflected off countless blades and spread in every direction.

At long last, the prelude to the Great War had begun.



* * *



Eyes filled with sorrow and a solemn atmosphere. With everyone watching him, Hyuk Mujin slowly parted his lips.

“It was simply one person trying to save another.”

“Stop it.”

“I didn’t do it to receive a reward. And I couldn’t ask for another sacrifice. That’s why I was going to leave.”

“I said stop.”

“Come on, why are you like this? I never get tired of doing this, no matter how many times I repeat it. Honestly, you all agree, don’t you?”

Taishan, tearing at a wild boar’s hind leg atop a bear that was running without pause, vigorously nodded.

“Taishan agrees!”

“See? Even he agrees. It was simply one person trying to save another…”

I quietly cut Hyuk Mujin off.

“Mujin.”

“Yes.”

“Do you want to become a eunuch?”

The smile that had spread across Hyuk Mujin’s face faded.

“No.”

“Or is life boring?”

“Of course not. I’m already worried that my life is too intense as it is.”

“Then do you want me to make it peaceful?”

“You don’t mean that you’re going to kill me, do you?”

“What if I do?”

“Wow, look over there. The scenery is beautiful.”

“Good. Let’s travel quietly.”

“……Yes, sir.”

But unlike Hyuk Mujin, who promptly shut his mouth, Taishan wore a disappointed expression and asked for an encore.

“Pavilion Master! Taishan wants to hear more!”

So I called in his designated bully.

“Old Man Nam, I think it’s time to shut that bastard’s mouth.”

“Oh! Finally!”

Namho cheered like an independence fighter celebrating liberation and, as if he had been waiting for this moment, pulled a muzzle from inside his robes.

It was a bizarre yet strangely familiar device made of black, sturdy iron connected by leather straps.

“Wait. Where did you get that?”

“I got it from a Nanman trainer. Apparently, it is mainly used to tame wild bears.”

“……”

“Why are you looking at me like that? Is there some problem?”

“Well, I wouldn’t say it’s exactly a problem.”

It was just that it somehow bothered me a little. Or perhaps it was more like an odd feeling that, from now on, I should call Taishan by the product number TAESAN-317 instead of his name…

After hesitating for a moment, I finally gave in to my unease and sighed.

“Don’t put that on him. No. Just throw it away.”

“No! Why?”

Why? Because I felt like it would dirty my eyes.

I snatched the muzzle from Namho, who was practically wailing, and threw it far into the distance. Jeok Cheongang, who had watched the whole thing, opened his mouth with an unpleasant expression.

“What on earth happened in Nanman?”

For a moment, I failed to understand the question and asked,

“Pardon?”

“I’m asking what happened for all of you to lose your minds.”

“Nanman certainly went through a lot, but everyone is still exactly as they were before.”

“What!”

“Surprisingly, it’s true.”

“You insolent brat! Don’t talk nonsense. Does it make any sense that not a single person died when everything is this much of a goddamn mess?”

“……”

Yeah. Fuck.

Looking back on what had happened in Nanman, I had a reasonable suspicion that the Earth Mother Goddess really had blessed us.

*I had come close to death several times, but the fact that I was returning in one piece was a miracle in itself.*

Of course, I was the only one who had repeatedly come close to death. As for the others, who had suffered injuries both major and minor, the Sacred Rain had done its work thoroughly enough that they had now recovered as if they had never been hurt.

*On top of that, we somehow managed to stop Dark Heaven’s sinister plot.*

Though not a small number of people had been sacrificed in the process, being able to stop the Southern Heaven Demon Empress—who had practically been the top priority for both me and the Fire Dragon Pavilion—was more than half a success in itself.

*And on top of that, the Nanman Beast Palace had officially joined the alliance.*

In truth, the Nanman Beast Palace’s joining had been more or less inevitable the moment we stopped the Southern Heaven Demon Empress.

Even without the Earth Mother Goddess’s brand effect, the outcome would not have been much different.

An ember trampled down halfheartedly would burn even hotter, and the emotion of anger would bind together those who had been scattered.

I had merely given them another center around which to gather.

The existence of a One God who could erase even the boundaries between tribes that had been passed down for hundreds of years. A center around which they could become an even more united and powerful force.

*And thanks to that, the Murim Alliance’s strength had increased as well.*

This time, I could say it without hesitation. Because of this incident, the Nanman Beast Palace had unquestionably become an ally.

According to what the Beast Miao King had promised before we left, they would send more troops than they had during the Great Faction War and do everything in their power to hold back Dark Heaven.

But why?

*Why do I feel so uneasy?*

Even though we had achieved major results, one corner of my heart was still filled with an unpleasant unease that I could not shake.

And perhaps the reason was the question that remained unresolved.

*The new Murim Alliance has been born, and all the strength of the Central Plains is gathering around the Nine Sects and One Gang and the Five Great Families. And yet Dark Heaven’s full strength still hasn’t been revealed.*

Dark Heaven’s first intervention in Shanxi Province, the Shaolin Bloodshed that followed, and the series of incidents that had continued to this day could never be called minor.

But they were merely fragments—not even a fraction of the organization as a whole.

*The time for testing the waters should have passed already.*

What the hell were they—or rather, what was the Lord of Heaven—trying to accomplish?

And why was the Lord of Heaven…

“Why would the Lord of Heaven take this much interest in me, of all people?”

My mutter slipped out without thought, and everyone’s gaze snapped toward me. Before I could say anything to smooth things over, Hyuk Mujin suddenly raised his head like a meerkat.

“Gasp, Captain. Did someone confess to you? Oh my God. A Nanman?”

“……”

I wanted to gouge out those eyes of his, shining like newly risen stars.

I suppressed the impulse and answered.

“It’s not like that, you crazy bastard.”

“No way. Then a Han Chinese woman?”

“How many times do I have to say it isn’t… Ah, come to think of it, the Han Chinese part is right.”

“Wow. When did this happen? Who confessed?”

“The Lord of Heaven.”

“Wow. That’s quite an extraordinary name for a young lady. She sounds like the daughter of a respectable family…”

Hyuk Mujin, who had been making a fuss, suddenly fell silent. After blinking and thinking for a moment, he continued.

“Who?”

“The Lord of Heaven.”

“The one I know? I mean, the one everyone knows?”

“Who else could it be?”

Hyuk Mujin remained silent for a moment, then muttered under his breath.

“Fuck. That respectable household was in Xinjiang…”

Beyond Qinghai, where the Kunlun Sect was located, lay Xinjiang—and Xinjiang had been the domain of the Demonic Path for a thousand years.

Once everyone realized that the young lady interested in me was a daughter of the Dark Heaven household, they stared at one another in silence, at a loss for words.

Then questions erupted from all sides.

“Why would the Lord of Heaven be interested in him?”

Namho cut in at Hyuk Mujin’s question.

“Isn’t it obvious? Because he keeps getting in the way?”

“That’s true, but the Captain isn’t one of the Three Saints or the Ten Kings. He’s just a scrap who only recently earned a reputation.”

“Now that you mention it, that’s not wrong either.”

“Taishan can eat scraps too.”

“You son of a bitch. I knew this might happen, so I brought another muzzle. Come here. Open your mouth.”

“No, why are you all putting it like that? Our Pavilion Master is a scrap? Song Escort, Young Hero Sama! Say something!”

“Young Lady Ju, I’m sorry, but I think I have to leave at this point. We somehow made it all the way to Nanman, but the Lord of Heaven taking an interest in that man is a bit much.”

“Taishan! That isn’t meat, so don’t bite it! Old Man Nam! Will you put that muzzle down right now!”

“……”

Fuck. I had never seen such a complete mess.

And as I stood there blankly staring at the total disaster unfolding before my eyes, a quiet Sound Transmission pierced my ears.

—Let’s talk.

It was Jeok Cheongang.
```

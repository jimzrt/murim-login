<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1044.txt",
      "sha256": "0ba959236b8bcf28fa5dc9749e0d590082436d40efa5049a53f491ab5bfd3d13",
      "bytes": 14467
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "61e3e4b01049ebe8cb72a8fbd43faf1afcb121f9d99f42113b701a66b73cbc42",
      "bytes": 2100
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0afd5623a0348715feebbe6cb08fd73d776a2b910e1d16ba8733ee2200fbbcba",
      "bytes": 760
    },
    {
      "path": "characters/Hwangbo Eom.md",
      "sha256": "ca5986932797cea8f5d5f221a37f1d90e17adeb37ea66f68a199097d090f085f",
      "bytes": 674
    },
    {
      "path": "characters/Hyuk Sopyung.md",
      "sha256": "c18c847b608a0616da57957c4671eb7459c547eb908c75edb3428fe3c389882f",
      "bytes": 618
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e73d861a9c0f62fdd446091a097866e8d69d761e017a913ae36776baa6a4b67f",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "279b79d90704a27fe2e761f8ace863b86ba21134df4942f61146870e17288fa6",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9df36af2955c89f6f58c55a5650624d4a6427149727567c59907f84a9add95ae",
      "bytes": 623
    },
    {
      "path": "characters/Sima Gong.md",
      "sha256": "149d860ce2ae499b00175d1e7e59c42fe1ca16d2ae085520eab5b49a14f0f569",
      "bytes": 778
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "41dbf35c564a38c2f6d4e288b90c7dbd155eeec151bef509dec611744b32a584",
      "bytes": 742
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "9dccf5cc082e5b32299defc3bc9b1651f73f51967c934c95faae41da1826a15f",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4a1725c95c6435d65d74e9e1a41e0329b64a7f60a983c1a15d2d0fe2a7a69198",
      "bytes": 280489
    }
  ],
  "estimated_tokens": 13642
}
-->

# Durable State Update — Chapter 1044

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1044. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1044. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1044,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1044,
    "continuity_sources": [1044],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "Jeok Cheongang is injured but holding off the Blood-Sword Demon Lord while Jin Taekyung targets the mages.",
    "Fire Dragon Armor is severely damaged, stored in Inventory, and unavailable until its automatic repair completes in three days.",
    "Repeatedly dispelling the white-robed mages’ varied Magic causes energy backlash that incapacitates them; nineteen have fallen, and their veiled leader, the Grand Mage, remains.",
    "The Grand Mage’s Hell Fire descends as a vast sphere capable of killing thousands.",
    "Jin’s incomplete One Annihilation failed to break all the Grand Mage’s barriers, leaving him alive but severely exhausted, with an empty dantian and damaged acupoints.",
    "Jin’s White Flame spear throw bends part of the Hell Fire sphere’s course and opens a rift in its flames, but does not stop it.",
    "Other fighters launch dazzling attacks from the ground toward the Hell Fire sphere; their identities and the result are unknown.",
    "The Wind-and-Cloud Sword Lord is badly wounded and refuses to retreat; his two Senior Brothers urge him to withdraw after securing a way out.",
    "The two Black Ghosts facing the Wind-and-Cloud Sword Lord were disrupted by a shock wave; the chapter confirms that he defeated them."
  ],
  "continuity_sources": [
    1042,
    1043
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "Can the attacks from Jin and the other fighters stop or redirect the Hell Fire sphere, and what follows?"
  ],
  "safe_through": 1043,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 혁소평    | **Hyuk Sopyung**   |
| 송일     | **Song Il**        |
| 사마공    | **Sima Gong**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 열화문    | **Fire Gate Clan**               |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 영약     | **elixir**                                       |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 장문인    | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 황보엄 | **Hwangbo Eom** | Personal name of the Taeeul Merciless Sword. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 평화 | **Peace Guild** | Guild name. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 종남일룡 | **Zhongnan One Dragon** | Epithet of Hyuk Sopyung. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 황보 | **Hwangbo** | Surname form used when addressing Hwangbo Eom. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 대환단 | **Great Restoration Pill** | Shaolin elixir used in Unnamed's recovery. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 흑야왕 | **Black Night King** | Epithet of Sima Gong, Sama Pyo's father and the Sect Leader who built the modern Black Dragon Demon Gate. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 형부 | **Ministry of Punishments** | Imperial punishment authority referenced as the destination for prisoners. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 쇄월검진 | **Moon-Shattering Sword Formation** | Named sword formation of the Zhongnan Sect. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 혁소평 | 진태경 | hostile_opponents | you; bastard | hostile and contemptuous | Hyuk insults Taekyung as a beggar and attacks him after Taekyung refuses to defer to his status. |
| 진태경 | 혁소평 | hostile_opponents | you; bastard | insulting and taunting | Taekyung mocks Hyuk’s appearance, cultivation, and failed attack while forcing him to agree to end the dispute. |
| 혁소평 | 황보엄 | junior_disciple_to_senior_martial_uncle | Senior Martial Uncle | formal-deferential but strained | Hyuk Sopyung repeatedly addresses Hwangbo Eom as 사백 while resisting his criticism. |
| 황보엄 | 혁소평 | senior_martial_uncle_to_junior_martial_artist | you; nobody like you | cold and contemptuous | Hwangbo Eom uses 네 녀석 and 네까짓 놈 while reprimanding Hyuk Sopyung. |
| 진태경 | 황보엄 | junior_martial_artist_to_Zhongnan_senior | Great Hero Hwangbo | casual-polite and teasing | Taekyung uses 황보 대협 after deliberately pretending not to recognize Hwangbo. |
| 황보엄 | 진태경 | Zhongnan_senior_to_younger_martial_artist | insolent brat | blunt, amused, and probing | Hwangbo describes Taekyung as a 건방진 아해 and later treats him as a youngster. |
| 황보엄 | 적천강 | rival_martial_masters | Fire King Jeok Cheongang | cold and taunting | Reveals that he knows Jeok's illness and threatens to settle his bad blood with the Fire Gate Clan. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 풍운검군 | legendary_elder_to_Zhongnan_sect_leader | Wind-and-Cloud Sword Lord | familiar and commanding | Jeok Cheongang tells him to get the Zhongnan disciples moving. |
| 노호검객 | 적천강 | senior_martial_artist_to_legendary_elder | Senior Jeok | deferential and cautious | Addresses Jeok as 노 선배 while explaining his actions. |
| 사마공 | 적천강 | unorthodox sect leader to senior martial master | Senior | formal and deferential | Greets Jeok Cheongang as 노선배. |
| 적천강 | 사마공 | senior martial master to longtime martial acquaintance | you | blunt and familiar | Uses direct, contemptuous language while teasing Sima Gong. |
| 진태경 | 사마공 | allied young martial artist to unorthodox sect leader | Great Hero Sima | polite and deferential | Addresses him as 사마 대협. |
| 사마공 | 진태경 | unorthodox sect leader to celebrated young martial artist | you | polite and familiar | Uses 자네 while speaking to Taekyung. |
| 풍운검군 | 적천강 | Zhongnan Sect Leader to legendary martial master | Senior Jeok | respectful | Refers to Jeok as 적 대협. |
| 풍운검군 | 노호검객 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 태을무정검 | Zhongnan Sect Leader to Senior Brother | Senior Brother | respectful and strained | Addresses him as 사형 while protesting the decision. |
| 풍운검군 | 진태경 | martial artist to fellow martial artist | Daoist Friend Jin | respectful and familiar | Thinks of Jin as 진 도우 when recognizing him as a possible turning point in the battle. |
| 노호검객 | 풍운검군 | Senior Brother to Zhongnan Sect Leader and Junior Brother | Junior Brother, Sect Leader | blunt and commanding | Uses 장문 사제 while ordering him to give the retreat command. |
| 태을무정검 | 풍운검군 | Senior Brother to Zhongnan Sect Leader and Junior Brother | Junior Brother, Sect Leader | serious and restrained | Uses 장문 사제 while telling him the sect’s losses will worsen if the battle continues. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1043
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hwangbo Eom.md

# Hwangbo Eom (황보엄)

- **Safe through:** Chapter 1000
- **Aliases:** Taeeul Merciless Sword
- **Role:** Supreme Peak master of the Zhongnan Sect and its Second Martial Uncle, known as the Taeeul Merciless Sword.
- **Personality:** Ruthless, severe, proud, and deeply invested in restoring Zhongnan's standing.
- **Voice:** Calmly courteous when offering tea, then cold, commanding, and cutting when reprimanding others.
- **Relationships:** Song Il and Hwangbo Eom are Gong Iljung’s two Senior Brothers; the three served the same Master for over fifty years, and Hyuk Sopyung is Hwangbo’s junior.

### Hyuk Sopyung.md

# Hyuk Sopyung (혁소평)

- **Safe through:** Chapter 662
- **Aliases:** Zhongnan One Dragon
- **Role:** Peak master of the Zhongnan Sect known as the Zhongnan One Dragon and a senior disciple who can command the Taeeul Sword Unit in Hwangbo Eom's presence.
- **Personality:** Proud, volatile, entitled, and quick to anger, especially when drunk.
- **Voice:** Loud, confrontational, insulting, and imperious.
- **Relationships:** Baek Museong knows him from several prior encounters; Baek says their elders' connection has been passed down to them.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1042
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1043
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1043
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Sima Gong.md

# Sima Gong (사마공)

- **Safe through:** Chapter 1037
- **Aliases:** Black Night King
- **Role:** Sima Gong is the Sect Leader who built the Black Dragon Demon Gate into a major unorthodox power and the father of its Young Sect Leader, Sama Pyo.
- **Personality:** Sly and calculating yet outwardly gentle; he calmly accepts sacrificing the rear population as the cost of a strategy he believes offers the best odds of victory.
- **Voice:** Polished and persuasive, with smooth rhetorical turns and a composed, gently teasing manner.
- **Relationships:** Sama Pyo is his youngest son among seven older brothers and nine older sisters; he is personally familiar with Jeok Cheongang, who openly dislikes him.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1022
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1040
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1044화



노호검객(怒號劍客) 송일은 문득 생각했다.

자신이 지금 무엇을 하고 있는 것인지.

당장이라도 이 가망 없는 전장을 벗어나기에도 부족한 시간에, 어찌하여 온 힘을 다해 검을 흩뿌리고 있는지.

쐐애애액!

검신을 타고 줄기줄기 쏟아진 강기(罡氣)가 맹렬하게 공간을 가르며 쏘아진다.

앞도, 뒤도 아닌 허공을 향한 그 휘황한 섬광이 이십여 장의 거리를 격하고 거대한 불덩어리와 맞닿기까지 걸린 시간은, 그야말로 찰나에 불과했다.

콰앙!

굉음과 함께 흔들리는 불의 구.

하지만 주춤하는 것도 잠시, 언제 그랬냐는 듯 계속해서 낙하해 오는 재앙을 바라보는 노호검객의 눈동자에 절망감이 깃들었다.

‘틀렸다. 막을 수 없어.’

이미 몇 차례나 전력을 다했기에 직감적으로 알 수 있었다.

비록 초인이라 불리기에 한 치의 모자람도 없는 그였으나, 귀신의 조화나 다름없는 저 거대한 불덩어리를 완전히 막아 내기에는 그 힘이 터무니없이 부족하다는 것을.

‘이게 도대체…….’

숨이 막혔다.

지금 이 순간에도 서서히 전장의 일부를 뒤덮어 오는 불의 구가 뿜어내는 끔찍한 열기에.

일평생 몇 번 느껴 보지 못했던, 전신을 옥죄는 무력감에.

그러나 바로 그 순간.

팟, 쉬쉬쉬쉭!

노호검객은 느꼈고, 동시에 보았다.

자신의 곁으로 홀연히 다가온 누군가의 인기척과 함께, 힘차게 흩뿌려지는 섬광을.

화아악!

‘이건.’

노호검객의 눈이 크게 뜨였다.

휘황한 빛이 번진다. 이십여 장이나 되는 거리에서도 피부를 달구던 열기가 일순간 사라진다.

휘황한 빛을 뿜어내며 나아가는 수십여 줄기의 강기는 그물처럼 촘촘했고, 동시에 더할 나위 없이 낯익었다.

“사제!”

콰아아앙!

노호검객이 반사적으로 토해 낸 외침과 또 한 번의 굉음이 뒤섞인 그때, 격돌의 여파로 쏟아지는 불덩어리의 파편 아래로 익숙한 신형이 모습을 드러냈다.

“금세 다시 뵙는구려, 대사형.”

다른 누군가가 들었다면 차갑다고 느낄 정도의 표정과 목소리.

세상에 보여지는 그 모습 그대로 태을무정검(太乙無情劍)이라는 별호를 지닌 사제의 모습에, 노호검객은 신음하듯 뇌까렸다.

“네가 어찌 이곳에……!”

반가움보다는 의문이, 그리고 얼핏 걱정과 분노마저 내비치는 사형의 모습에 태을무정검은 담담하게 대꾸했다.

“왜, 이 황보엄이 설마 그리 순순히 말을 따를 줄 알았소?”

“네 이놈! 그게 무슨 망발이냐! 도대체 장문 사제와 다른 제자들은 어찌하고!”

노호검객은 그 별호처럼 불같은 고함을 토해 냈다.

과도한 피로와 부상에 기어코 쓰러지고만 풍운검군과, 살아남은 본산 제자들의 안위를 부탁하고 돌아섰던 것이 불과 촌각 전이었다.

한데 그들을 이끌고 속히 퇴각해야 할 태을무정검이 자신의 곁에 있다니.

노호검객은 순간 주위의 상황도 잊은 채 고래고래 외쳤다.

“이 멍청한! 네놈마저 없다면 도대체 누가 본문을……!”

“세 살 버릇 여든까지 간다더니, 확실히 별호 값을 하는구려. 생각해 보면 대사형은 어릴 적부터 항상 그랬지.”

“뭐라?”

그러나 돌아오는 대답은 없었다.

황당한 얼굴로 반문하는 사형을 무시한 채, 사제는 묵묵히 검을 휘둘렀다.

언제나처럼 냉막하기 그지없는 얼굴이었으나, 한껏 도드라진 핏줄은 그가 어느 때보다 전력을 다하고 있다는 증거였다.

슈확! 콰아아앙!

검을 타고 쭉 뻗어나간 강기와 화염이 부딪힌다.

그 여파에 또 한 번 주춤하는 불덩어리에서 떨어져 나온 파편의 일부가, 마치 부슬비와 같은 불똥과 함께 지상을 향해 떨어져 내렸다.

“역시 이 정도로는 어림도 없구려. 적어도 나 혼자서는.”

“……!”

“쇄월검진(碎月劍陳). 준비는 되었소?”

앞서 사제가 그랬듯이, 사형 또한 대답하지 않았다.

분노가 어린 눈빛으로 태을무정검을 노려보던 노호검객은 일순간 모든 힘을 집중하여 검을 쳐올렸다.

쉬쉭, 쐐애애액!

서로의 성격만큼이나 상반되는 검격(劍格)이 허공을 격하며 경쟁하듯 나란히 쏘아졌다.

아니, 충돌하는 듯하면서도 묘하게 뒤섞이며 그 위력을 증대시켰다.

한 뿌리에서 자라난 가지임을 증명하듯이.

꽈아아아앙!

그 어느 때보다 크고 강렬한 굉음과 여파.

그제야 미세하게 방향이 뒤틀린 불덩어리의 모습에 조금이나마 힘을 얻은 두 사형제는, 혼신의 힘을 다해 강기를 쏟아붓기 시작했다.

쉭, 후우우웅!

베고, 쳐올리고, 찔렀다.

그에 따라 쉼 없는 터져 나오는 굉음 사이로, 두 노도사의 늙은 입술을 비집고 흘러나온 목소리가 서로의 귓전에 닿았다.

“장문 사제와 다른 제자들은 걱정마시오. 소평, 그 아이라면 맡은바 소임을 잘해 낼 테니.”

“소평이라…… 그래, 결국 그렇게 되었더냐.”

이미 돌이키기에는 늦은 상황.

그제야 현재 종남파의 생존자들을 이끄는 이가 누구인지 알아차린 노호검객의 얼굴에 그늘이 드리워졌다.

종남의 최정예 일천.

고작 반 시진도 안 되는 짧은 시간 동안 그들 중 삼분지 일이 죽거나 다쳤고, 거동이 가능한 이들 중 미래를 맡길 만한 제자는 그리 많지 않았다.

종남일룡(綜南一龍) 혁소평.

종남파 제일의 기재이자, 중원 최고의 후기지수들이라 불리는 십봉룡(十鳳龍)의 일원.

한때 주색에 빠져 정신을 차리지 못하던 그는, 과거 태을무정검과 용봉표국의 분쟁 직후부터 눈부실 정도로 성장한 모습을 보이고 있었다.

인격적으로나, 무공으로나.

하지만 그럼에도 불구하고, 노호검객의 근심은 사라지지 않았다.

“그 아이는 아직 너무 어려. 역시 네 녀석이 남았어야 했다.”

“그렇게 따지면 대사형부터가 문제이니 끝도 없지. 그리고 정마대전 때의 나는 그보다도 어렸소. 장문 사제는 말할 것도 없고.”

“그때와 지금은 다르다.”

“무엇이 그리 다르냐고 반박하고 싶지만, 이번만큼은 참으리다.”

슈확!

공간을 찢어발기는 검신.

온 힘을 다해 강기의 그물을 펼쳐낸 태을무정검이, 낮게 가라앉은 목소리로 덧붙였다.

“적어도 그 시절에는, 이런 괴력난신(怪力亂神)의 조화가 판을 치진 않았으니.”

콰아아아앙!

하늘이 쪼개지는 듯한 굉음와 당장이라도 데일 것 같은 뜨거운 열기.

그 모든 것의 중심에는, 불과 촌각 전보다도 훨씬 거대해진 불덩어리가 있었다.

잠시나마 흔들리고 일부가 부서질지언정, 태산처럼 변함없이 떨어져 내리는 재앙이.

가까워진 만큼 거대해진, 수천의 목숨을 집어삼킬 지옥의 겁화가.

“저것을…… 막을 수 있겠느냐?”

가쁜 숨을 내뱉으며 묻는 노호검객에게, 역시 지친 기색이 역력한 태을무정검이 되물었다.

“대사형의 눈에는 내가 무엇으로 보이시오?”

짧으면서도, 한편으로는 영원처럼 길게 느껴지는 침묵이 흘렀다.

그러나 노호검객은 사제가 무슨 말을 하려는지 충분히 짐작하고 있었다.

그래. 막을 수 없다.

그들 사형제는 한낱 인간에 불과한 존재들이었고, 저것은 이해할 수 없는 괴력난신의 힘이었으니까.

이 미친 재앙을 조금이라도 저지할 수 있는 자들이 있다면, 그건 바로 인간의 육신으로 괴물이나 신에 버금가는 경지에 오른 진정한 초인들 뿐일 테니까.

“노망이라도 난 기분이군. 화왕(火王), 그 미친 노괴가 보고 싶을 줄이야.”

“오랜만에 비슷한 생각을 했구려. 순간 어느 천둥벌거숭이 같은 핏덩이가 눈앞을 스친 것을 보아하니, 내가 정말 정신이 나갔나 싶소.”

화왕 적천강.

그리고 열화신룡 진태경.

두 사형제에게 있어, 그들은 죽을 때까지 잊을 수 없는 존재나 다름없었다.

물론, 안 좋은 쪽으로.

“오지 못하겠지?”

“뭘 물어보시오. 이미 알고 있으면서.”

초절정 고수의 감각은 범인의 상상을 초월하는 수준.

전장 곳곳에서 벌어지는 상황을 읽고 있던 두 사람은 이미 열화문의 늙고 젊은 괴물들이 자신들을 돕지 못한다는 사실을 익히 짐작하고 있었다.

더불어 한편으로는, 그 어떠한 상황에서도 그들의 도움을 받고 싶지 않다는 이율배반적인 생각 역시 마음속에 품고 있었다.

지금 이 순간에도 그들은, 열화문의 두 사제(師弟)에게 품었던 원한을 완전히 버리지 못하고 있었으니까.

그리고 바로 그 원한으로 인하여, 돌이킬 수 없는 과오를 저질러 버렸으니까.

쾅! 쾅! 꽈아아앙!

연달아 터져 나오는 폭음(爆音).

하지만 어느덧 노호검객과 태을무정검의 강기는 눈에 띌 정도로 약해져 있었고, 이제는 고작 십여 장도 되지 않는 거리까지 다가온 불덩어리의 열기는 끔찍하리만치 강렬했다.

마지막 남은 전의(戰意)조차 불살라 버릴 만큼.

구구구궁.

뜨겁다.

지금껏 본 적 없는, 동시에 앞으로도 경험하지 못할 검붉은 그늘이 전장의 일부를 뒤덮었다.

“후회……하시오?”

바싹 마른 입술 사이로 조용히 흘러나온 태을무정검의 물음에, 공허한 눈빛으로 하늘을 바라보던 노호검객이 대답했다.

“그래.”

그런 사형의 모습에, 사제는 굳이 더 묻지 않았다.

무엇을 후회하느냐고.

그리고 그런 사제의 모습에, 사형 역시 묻지 않았다.

그렇게 내게 묻는 너는, 후회하고 있느냐고.

짧은 말이 오갔음에도, 그 안에는 모든 것이 담겨 있었다.

소리 없는 생각만이 각자의 머릿속을 맴돌 뿐이었다.

‘그래서는 안 되는 거였는데.’

별호만큼이나 다른 성정을 지닌 두 사람이었으나, 비슷한 삶을 살아온 그들은 지금 이 순간 같은 생각을 떠올리고 있었다.

인의(人義)보다는 무공을 갈고 닦았던 평화로운 어린 시절을.

협의(俠義)보다 공적을 쫓기에 바빴던, 피와 죽음으로 점철된 젊은 시절을.

검었던 머리가 하얗게 새 가듯이, 되찾은 평화 속에서 빠르게 사리(私利)와 사욕(私慾)에 물들었던 그 시간을.

그리고.



‘내 듣자 하니, 두 분께서 아주 큰 곤욕을 치르셨다 들었소만.’



그 과욕의 대가를 치르고 극심한 내상과 심마 속에 사로잡혀 있던 어느 날, 증오에 휩싸인 그들에게 찾아온 유혹의 손길을.



‘어렵게 구한 영약(靈藥)이오. 소림의 대환단에 버금가는 약효를 지녔으니, 능히 내상을 회복하고도 남을 거요.’



만남을 거부하는 뜻을 밝혔음에도 끝끝내 대면한 불청객은, 도무지 믿을 수 없을 정도로 후한 호의를 의심하는 두 사형제에게 거부하지 못할 한마디를 던졌다.



‘이건 호의가 아니라 거래요. 그리고 만약 두 분께서 이 거래를 받아들인다면…… 해묵은 은원(恩怨)을 해결함은 물론 종남파의 안위에도 도움이 되겠지.’



그들은 갈등했지만, 마침내 거래를 승낙했다.

종남파 장문인의 적전제자로, 정마대전의 영웅이자 강호의 명숙으로 살아온 일평생. 이대로 씻을 수 없는 수모를 떠안은 채 살아갈 수는 없었다.

복수해야 했다.

설령 그 방식이 죽음이 아니더라도, 그들이 겪은 것과 같은 수모를 열화문에 안겨 주어야 했다.

더군다나 종남파의 안위 또한 보장되는 길이었으니.

하여 그들은 이 달콤한 제안을 뿌리치지 못했다.

그렇게 불청객이. 아니, 흑야왕(黑夜王) 사마공이 내민 손을 기꺼이 잡았다.

그리고 그로부터 몇 달의 시간이 흐른 후에야, 자신들이 내린 결정을 후회하고 있었다.

지금 이 순간에도 서서히 머리 위를 덮어 오는, 이글거리는 화염을 바라보며.



‘어찌하여 이리되셨소.’



풍운검군.

자신들의 막내 사제가 공허하게 내뱉은 그 한마디.

회한에 찬 그의 음성을 듣는 순간 깨달았다.

이제 그들에게 남은 선택지가 무엇인지.

무엇을 해야 하는지.

“도망쳐라. 지금이라면 늦지 않았으니.”

“싫소. 그러는 대사형이나 가시오.”

“나도 싫다.”

삼 장.

이제는 온 시야를 가득 메운 거대한 화염의 구를, 두 사형제는 넋 나간 눈빛으로 바라보았다.

“처음부터 어림도 없는 일이었다.”

“맞소.”

“한데 왜 왔느냐?”

“대사형과 같은 이유요. 뭐라도 해야 할 것 같아서. 이렇게라도 해야 할 것 같아서. 그리고…….”

이 장.

화염이 토해 내는 그 열기가, 빛이 너무나도 눈이 부셔서 태을무정검은 눈을 감았다.

아니, 차마 떳떳하게 세상을 바라보며 죽음을 맞이하기에는 스스로가 너무 부끄러웠을지도 몰랐다.

“……부끄러워서. 미안해서 그랬소.”

인의를 가르쳤던 스승에게.

못난 자신들을 사형으로 섬겼던 막내 사제와 사문의 제자들에게.

그 외의 모든 이에게.

그리고, 이미 오래전 길을 벗어난 자신들과 달리 정도(正道)를 걷고 있는 어떤 스승과 제자에게.

“참으로, 빌어먹을 일이로군.”

태을무정검, 혹은 노호검객.

누군가의 입술 사이로 흘러나왔을지 모를 그 음성은 어느 때보다 공허했고.

화아아아아악!

반경 수백여 장에 걸쳐 드리워진 거대한 불덩어리가 토해 내는 열기와 빛은, 어느 때보다도 화려했다.
```

## Final English reading copy

```markdown
# Chapter 1044

The Roaring Fury Swordsman, Song Il, suddenly wondered what he was doing.

With barely enough time to escape this hopeless battlefield, why was he scattering his sword strikes with all his might?

Shwoooosh!

Force poured in streams along his blade, tearing through the air as it shot forward.

The dazzling streak of light, aimed neither ahead nor behind but into empty space, crossed a distance of more than twenty *jang* and struck the enormous ball of fire in the blink of an eye.

KWA-BOOM!

The sphere of fire shuddered with a deafening roar.

But its hesitation lasted only a moment. As the calamity continued its descent as if nothing had happened, despair filled the Roaring Fury Swordsman’s eyes.

*It’s no use. I can’t stop it.*

He knew by instinct. He’d already given it everything he had several times.

Though he was fully worthy of being called a superhuman, his strength was nowhere near enough to completely stop that enormous fireball, a force as unnatural as supernatural powers themselves.

*What the hell is this…*

He could barely breathe.

The unbearable heat radiating from the sphere of fire, slowly covering part of the battlefield even now.

The helplessness constricting his whole body—a feeling he’d experienced only a handful of times in his life.

But at that very moment—

Pop, sh-sh-sh-shk!

The Roaring Fury Swordsman felt it, and saw it at the same time.

Someone had appeared beside him, and with them came a dazzling light, flung forward with all their might.

Fwoosh!

*This is…*

The Roaring Fury Swordsman’s eyes widened.

Dazzling light spread. Even from more than twenty *jang* away, the heat that had warmed his skin vanished in an instant.

Dozens of streams of Force surged forward, brilliant and tightly woven like a net. And they were unmistakably familiar.

“Junior Brother!”

KWA-BOOOOM!

As his reflexive shout mingled with another deafening roar, a familiar figure appeared beneath the fragments of fire raining down from the collision.

“It hasn’t been long, Senior Brother.”

His expression and voice were so cold another person might have thought him indifferent.

The Roaring Fury Swordsman murmured, almost groaning, at the sight of his Junior Brother, known to the world by that very demeanor as the Taeeul Merciless Sword.

“How did you get here…!”

The Senior Brother’s face showed more confusion than joy, and a trace of worry and anger.

The Taeeul Merciless Sword answered calmly. “What, did you really think this Hwangbo Eom would follow your orders so obediently?”

“You fool! What kind of nonsense is that? What about Junior Brother, the Sect Leader, and the other Disciples?”

The Roaring Fury Swordsman bellowed, as fiery as his sobriquet.

Only moments ago, he’d turned away after entrusting the well-being of the Sect Leader—who’d finally collapsed from overwhelming fatigue and injuries—and the surviving Disciples of their sect to Hwangbo Eom.

And yet here he was, beside him, when he should have been leading them in a swift retreat.

For a moment, the Roaring Fury Swordsman forgot everything else around him and shouted at the top of his lungs.

“You idiot! If you’re gone too, who in the world is going to lead our sect…!”

“They say old habits die hard. You certainly live up to your sobriquet. Come to think of it, you’ve always been like that, Senior Brother—even as a child.”

“What?”

But no answer followed.

Ignoring his Senior Brother’s incredulous question, the Junior Brother silently swung his sword.

His face was as cold as ever, but his bulging veins showed that he was giving it more than ever before.

Shwaak! KWA-BOOOOM!

Force stretched out along his sword and collided with the flames.

The fireball faltered once more. Some of the fragments that broke off in the impact fell toward the ground, scattering sparks like a drizzle.

“As expected, this won’t be enough. Not by myself, at least.”

“……”

“Are you ready for the Moon-Shattering Sword Formation?”

Just as his Junior Brother had done moments earlier, the Senior Brother gave no answer.

The Roaring Fury Swordsman glared at the Taeeul Merciless Sword with fury in his eyes, then focused all his strength and swung his sword upward.

Shhk, shwoooosh!

Their sword strikes, as opposite as their temperaments, tore through the air side by side, shooting forward as though they were competing.

No—as they seemed to collide, they somehow blended together, increasing their power.

As if to prove they had grown from the same root.

KWA-BOOOOM!

The roar and shock wave were greater and more intense than ever.

Seeing the fireball’s course change by the slightest degree, the two Senior Brothers drew what little strength they could from the sight and began pouring out Force with everything they had.

Shhk, whoooosh!

They slashed, swung upward, and thrust.

Amid the ceaseless explosions, a voice slipped from the lips of the two old Daoists and reached the other’s ear.

“Don’t worry about Junior Brother, the Sect Leader, and the other Disciples. So Pyeong will do his duty well.”

“So Pyeong… I see. So that’s how it ended up.”

It was already too late to change things.

Only then did the Roaring Fury Swordsman realize who was leading the survivors of the Zhongnan Sect. Shadows fell across his face.

The Zhongnan Sect’s thousand finest.

In less than half a shichen, a third of them had been killed or wounded. Among those still able to move, there were few Disciples fit to entrust with the future.

Hyuk Sopyung, the Zhongnan One Dragon.

The Zhongnan Sect’s greatest prodigy, and one of the Ten Dragons and Phoenixes, the young talents hailed as the finest of the Central Plains.

Once, he’d been so lost in wine and women that he couldn’t come to his senses. But after the dispute between the Taeeul Merciless Sword and the Yongbong Escort Bureau, he’d shown dazzling growth.

In character as well as martial arts.

Even so, the Roaring Fury Swordsman’s concern did not fade.

“He’s still too young. You should have stayed behind instead.”

“By that reasoning, you’re the problem, Senior Brother, and we could go on forever. Besides, I was even younger than him during the Great Faction War. Junior Brother, the Sect Leader, was younger still.”

“That was different.”

“I’d like to ask how, but I’ll let it go this time.”

Shwaak!

The blade tore through the air.

The Taeeul Merciless Sword spread a net of Force with all his might, then added in a low voice,

“At least back then, the battlefield wasn’t overrun with supernatural powers.”

KWA-BOOOOM!

A roar like the splitting of the heavens. Heat so fierce it could burn them at any moment.

At the center of it all was a fireball much larger than it had been only moments ago.

It wavered for a moment, and parts of it broke away, but the calamity kept falling like an unchanging mountain.

The closer it came, the larger it seemed—the hellfire that would devour thousands of lives.

“Can we… stop that?”

The Roaring Fury Swordsman asked between ragged breaths. The Taeeul Merciless Sword, just as visibly exhausted, replied with a question of his own.

“What do I look like to you, Senior Brother?”

A short silence passed, yet felt as long as eternity.

But the Roaring Fury Swordsman had a good idea what his Junior Brother meant.

Right. They couldn’t stop it.

They were only human, and that was a power beyond their understanding, a force of supernatural powers.

If anyone could even slightly hold back this mad calamity, it would be the true superhumans—those whose human bodies had reached a realm comparable to monsters or gods.

“I feel like I’ve gone senile. I never thought I’d miss that mad old monster, the Fire King.”

“For once, I had a similar thought. A moment ago, I saw some reckless brat flash before my eyes. It made me wonder if I’d really lost my mind.”

The Fire King, Jeok Cheongang.

And the Blazing Flame Divine Dragon, Jin Taekyung.

To the two Senior Brothers, they were beings they would never forget as long as they lived.

For all the wrong reasons, of course.

“They won’t make it here, will they?”

“Why ask? You already know.”

The senses of a Supreme Peak master surpassed anything an ordinary person could imagine.

The two men, reading the events unfolding across the battlefield, already suspected that neither the old monster nor the young one from the Fire Gate Clan could come to their aid.

And at the same time, they held the contradictory wish that they didn’t want help from either of them, whatever the circumstances.

Even now, they hadn’t been able to let go of their grudge against the Fire Gate Clan’s Master and Disciple.

And that grudge had led them to commit an irreversible mistake.

KWA! KWA! KWA-BOOOOM!

Explosions rang out one after another.

But the Force of the Roaring Fury Swordsman and the Taeeul Merciless Sword had grown noticeably weaker. The fireball, now less than ten *jang* away, radiated a hideous, searing heat.

Hot enough to burn away even the last of their will to fight.

Grrrrrrr.

It was hot.

A crimson-black shadow, unlike anything they’d ever seen and something they’d never experience again, covered part of the battlefield.

“Do you… regret it?”

The Taeeul Merciless Sword’s quiet question passed between his parched lips.

The Roaring Fury Swordsman stared blankly at the sky and answered.

“Yes.”

Seeing his Senior Brother like that, the Junior Brother didn’t ask anything more.

He didn’t ask what he regretted.

And seeing his Junior Brother, the Senior Brother didn’t ask either.

He didn’t ask whether the one asking him regretted it, too.

Though they’d exchanged only a few words, they’d said everything.

Only silent thoughts circled through their minds.

*We shouldn’t have done that.*

The two men had temperaments as different as their sobriquets, but they’d lived similar lives. In this moment, the same thoughts came to them.

Their peaceful childhood, spent honing their martial arts instead of cultivating compassion and justice.

Their bloody youth, spent chasing achievements rather than the righteous path of the warrior.

The time when, as their black hair turned white, they’d quickly become tainted by personal gain and selfish desires amid the peace they’d regained.

And then—

> *I hear you two went through quite an ordeal.*

One day, after paying the price for their greed and becoming trapped in the depths of Internal Injuries and demonic thoughts, a tempting hand had reached out to them, consumed as they were by hatred.

> *This is a rare elixir I managed to acquire. Its effects rival Shaolin’s Great Restoration Pill. It will be more than enough to heal your Internal Injuries.*

Though they’d made clear they did not want to meet, the uninvited guest had secured an audience anyway. Seeing the two martial brothers distrust his almost unbelievable generosity, he said something they could not refuse.

> *This isn’t generosity. It’s a transaction. And if you accept it… not only will you settle an old grudge, you’ll help protect the Zhongnan Sect.*

They’d hesitated, but in the end, accepted the deal.

They’d spent their lives as the direct disciples of the Zhongnan Sect Leader, heroes of the Great Faction War and respected masters of the martial world. They couldn’t go on living with this indelible humiliation weighing on them.

They had to take revenge.

Even if their revenge stopped short of killing, they had to make the Fire Gate Clan suffer the same humiliation they had.

And the deal would also ensure the safety of the Zhongnan Sect.

So they couldn’t refuse the sweet offer.

They’d gladly taken the hand held out to them by the uninvited guest. No—by Sima Gong, the Black Night King.

Only months later did they regret the decision they’d made.

Even now, they stared at the blazing flames slowly covering the sky above them.

> *How did it come to this?*

The Wind-and-Cloud Sword Lord.

His Junior Brother, the youngest of them, had asked those words in a hollow voice.

The moment they heard the regret in his voice, they understood.

What choice remained to them.

What they had to do.

“Run. There’s still time.”

“I refuse. You go, Senior Brother.”

“I refuse, too.”

Three *jang*.

The two Senior Brothers stared, dazed, at the enormous sphere of flames now filling their entire field of vision.

“It was never possible to begin with.”

“That’s right.”

“Then why did you come?”

“For the same reason you did, Senior Brother. I felt I had to do something. Even if it was only this. And…”

Two *jang*.

The heat and light pouring from the flames were so blinding that the Taeeul Merciless Sword closed his eyes.

Or perhaps he was too ashamed of himself to face the world openly as he died.

“…I was ashamed. I was sorry.”

To the Master who’d taught them benevolence.

To their youngest Junior Brother and the Disciples of their sect, who’d treated them as Senior Brothers despite how unworthy they were.

To everyone else.

And to a certain Master and Disciple who, unlike them—who’d strayed from the path long ago—still walked the righteous path.

“This is truly one hell of a mess.”

The Taeeul Merciless Sword—or the Roaring Fury Swordsman.

The voice that might have slipped from either man’s lips sounded more hollow than ever.

Fwoooooosh!

The heat and light pouring from the enormous fireball, stretching across hundreds of *jang*, were more magnificent than ever.
```

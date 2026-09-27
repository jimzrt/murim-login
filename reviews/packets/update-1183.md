<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1183.txt",
      "sha256": "d7c1d01a7e0bf2dd33c13c7a11e1cc9d93576ca8569f9a37ece6b6b816813c73",
      "bytes": 12860
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "75d618d493ba1c2c3446e16bcad1565317c6eb2240829848972bfef1e3c05160",
      "bytes": 2273
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2372eff4014bbbfe2875ceb74264c004f7f386d353a549f999d2b18a5d322a72",
      "bytes": 248683
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "34cb1698c7fef69b3790e88701244e8b1b5840d10ceac34d76a2d3d5f5685710",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "546840e4de7370eb34ad69f87c145a59cf3642f1a3209a5e4c76edb3af79443a",
      "bytes": 1377
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f4ee7f525eee082c91e6ceef8db6fb7c14d36a669e9d0b7c06bd711c249b18f3",
      "bytes": 1701
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4360cae4136502065aa647bec21d16945e4deedac6bcddec6c0f8504f8c4a9c6",
      "bytes": 1666
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ca26ff6dcc0339335abdf8f7ec827876cae16bbc2d72fc67205237848a82fd82",
      "bytes": 1550
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "2905197d36ecc949a63910f7d8010e26e1e17acafcedaabaa9a64cf024bcdde4",
      "bytes": 1107
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5503418e9c6da790d3f6e36fc8345b697982b570214f9d4abcfed27ff18b74a3",
      "bytes": 623
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "9586a024bf6440db97520157919c975ebe328313a9a48e3a8d63e29f30a53724",
      "bytes": 1033
    },
    {
      "path": "characters/Namho.md",
      "sha256": "6b3eb2c6fc7e4bbcb04e1d36fc4b364efaef7b1ef0110f9464c692e1232f9f41",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "2e38ced22705f4de5e4b2227a3eb34209bcb9a0e4f0b16691e97a05ea093710f",
      "bytes": 850
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "4cae4ac754e33b370f52b9e9c525aab0374b00f600eeec7dde968780cebaf33e",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "603e3c49f5d38d12148c65f30dba06292ea6e50bd93d8155390005ac0494757a",
      "bytes": 295700
    }
  ],
  "estimated_tokens": 14284
}
-->

# Durable State Update — Chapter 1183

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
1 and safe_through 1183. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1183. Profile updates may replace only one
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
  "chapter": 1183,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1183,
    "continuity_sources": [1183],
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
    "The Murim allied forces split into three forces at the Qinghai-Xinjiang border, planning to rendezvous with the Imperial Army near Tianshan.",
    "Taekyung’s group has reached the planned rendezvous after crossing the desert and snow-covered mountains; no other forces have arrived after two days.",
    "Taekyung experiences unexplained chest pain after seeing two streaks of light and continues to have difficulty sleeping.",
    "The Son of Heaven’s army is fighting monsters in a basin. Baek Yeon and Jeong Hogun are with him, and the Twelve Palaces have joined the fight against at least twenty Black Ghosts; the outcome is unknown.",
    "The Son of Heaven says his body is no different from a dead man’s after taking up Maoshan Sect martial arts, but his heart and blood burn intensely.",
    "Jeok Cheongang, Hyuk Mujin, Cheongpung, and Ju Hwaran know Taekyung is from another world. He has said he is human and around twenty-eight.",
    "Great Sir does not know Taekyung’s secret; Jeok leaves telling him to Taekyung.",
    "Bow Saint knows Taekyung’s secret and questions whether the Martial God’s letter is right.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete. The Grand Mage serves the Lord and awaits a command; none has been given.",
    "The Main Quest “Rift and Collapse” failed. “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon. Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1182,
    1181
  ],
  "open_questions": [
    "What command will the Lord of Heaven give the Grand Mage, and what remains to be completed?",
    "What is Alpha, and what does its awakening mean?",
    "Why has no one arrived at the rendezvous point?",
    "What caused Taekyung’s chest pain and sleeplessness?",
    "Who is the person Bow Saint misses?"
  ],
  "safe_through": 1182,
  "temporary_decisions": [
    "Render 대인 as Great Sir, following the established glossary."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 무림맹    | **Murim Alliance**               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 큰형     | **eldest brother**                           |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 청해     | **Qinghai**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천산산맥 | **Tianshan Mountains** | Mountain range associated with the Demonic Cult. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 성지 | **Sacred Land** | Former name of the Poisonblood Grounds when beasts ruled Ailao Mountain. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |
| 진위경 | 문경 | Jin Family Lesser Family Head to medical apprentice | you | formal-polite | Asks whether Jin Taekyung will arrive soon. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |
| 살성 | 적천강 | familiar peer and fellow martial master | you | familiar and teasing | Uses 자네 while teasing Jeok and reassuring him. |
| 적천강 | 살성 | familiar fellow martial master | you | familiar, insulting-casual | Trades teasing insults with the Slaughter Saint over who is welcome in Taekyung’s carriage. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1181
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1178
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is deeply loyal to Taekyung, who trusts him as a close companion and values him as family, and has a warm friendship with fellow Fire Dragon Pavilion member Taishan; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung, and his parents own the Hyuk Family Textile Shop, which his younger sibling may inherit.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1179
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and follows his own path rather than pursuing grand causes; though he turned his back on the world, he wants Taekyung to pursue righteousness, practice chivalry, and win people’s hearts, and fiercely protects those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, and shares familiar, teasing camaraderie with the Slaughter Saint; he accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 1181
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry and responsibility; losses deepen his self-reproach and resolve to grow strong enough to protect others.
- **Voice:** Quiet and resonant, clipped and blunt, with dry sarcasm in familiar exchanges.
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, who shares his own grief and encourages him to keep trying; Cheol Mubaek died protecting Mukyung and left him the Shura Annihilating Fist manual; their father—the Jin Family Head—once apologized to Mukyung for his mother’s death in childbirth.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1182
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and eleventh member of the Ten Kings, a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; he serves as Thousand Captain of the Embroidered Uniform Guard, is enfeoffed as Prince Shangshan, and is widely regarded as a new-age savior.
- **Personality:** Hungry, self-aware, and dryly observant, he is pragmatic and fiercely defiant; he protects those he cherishes and meets mounting responsibility with hope and a determination to endure.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother and Jeok Cheongang his Master and trusted confidant; he shares deep loyalty with Hyuk Mujin, whom he values as family, and considers the revived Undead King, formerly the Skeleton King, a friend.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 1181
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; with his younger brothers, he is openly affectionate and markedly overprotective.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1182
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 1115
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom he helped free from his Heart Demon, he trained Jin Taekyung and considers him worthy of risking his life for, and he trusts the Bow Saint despite uncertainty about her intentions; the Salcheonmun he destroyed vows to pursue him.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1095
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1138
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1174
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1183화



그곳은 이름 모를 폐허였다.

그 면적과 건물의 숫자를 헤아려보았을 때, 한때는 족히 수천의 가호(家戶)가 어울려 살았을 소도시로 추정되었으나 모두가 예상했듯이 그 어디에도 인적은 찾아볼 수 없었다.

다만, 저 멀리 지평선을 따라 끝없이 이어지는 산줄기만이 남아 이 유령 도시를 지켜보고 있을 뿐이었다.

사시사철 녹지 않는 새하얀 만년설을 죽립처럼 눌러쓴 대자연의 거인, 바로 천산산맥(天山山脈)이.

‘하늘의 산, 이라.’

나는 마음속 뇌까림과 함께 창밖에 펼쳐진 아득한 풍경을 바라보았다.

압도적이며, 경이롭기까지 한.

그야말로 천산이라 부를 수밖에 없는 광경이었다.

구름을 뚫고 솟아오른 저 봉우리 중 어딘가에는 신선이 머무르고 있을지도 모르겠다는 허무맹랑한 상상이 들 만큼.

아니, 이건 결코 허황된 상상이 아니다.

신선이라는 두 글자를 마왕으로 고친다면, 상상은 현실이 된다.

그것도 매우 끔찍한 현실이.

“조장님?”

불현듯 귓가를 파고드는 한 줄기 음성.

나를 은인이라고 칭하는 사람은 여럿이지만, 조장이라고 부르는 사람은 한 명밖에 없다.

나는 창밖으로 시선을 고정한 채 대답했다.

“어.”

머릿속에서 실타래처럼 꼬여 있는 생각들 탓일까, 착 가라앉은 목소리에 혁무진이 우물쭈물 입을 열었다.

“그, 식사는 하셨어요?”

“대충. 왜?”

“살, 아니 문 대협께서 저한테 시간 나면 한번 들러 보라고 하셔서요. 조장님이 식사도 거르고 계신 건 아닌지.”

“그 양반이? 별일이네.”

조금 뜻밖이긴 했다.

지금껏 함께하며 서로 간에 정이 꽤 쌓였다고는 해도, 내 끼니까지 신경 쓸 만큼 섬세한 편은 아니라고 생각했으니까.

“혹시 몰라서 출발 전에 미리 만들어 놓으셨던 특제 벽곡단이래요. 가뜩이나 남은 식량도 별로 없는데 남기면 죽여 버리신다는데요.”

“……그래, 그럴 것 같더라.”

고개를 절레절레 내저은 내가 품 안에 넣어 두었던 벽곡단을 꺼내자, 혁무진의 눈빛이 짜게 식었다.

“드셨다면서요.”

“대충이라고 했지, 먹었다곤 안 했다.”

“참 나, 내 이럴 줄 알았지.”

요새 덜 맞아서 저러나.

녀석의 투덜거림을 무시하고 벽곡단을 한입에 털어 넣었다.

도무지 정체를 알 수 없는 쓴맛을 참으며 씹어 삼키니, 놀라울 정도의 포만감과 함께 시스템 알림이 울려 퍼졌다.

띠링.



- [문경의 특제 벽곡단]을 섭취하셨습니다.

- [포만감]이 하루 동안 유지됩니다.

- 약간의 피로가 회복됩니다.

- 한 시간 동안 모든 능력치가 +3 상승합니다.



맛은 더럽게 없지만, 효과 하나는 확실했다.

명색이 신의(神醫)가 만든 것치고는 뭔가 좀 아쉬운 성능이지만.

그리고 눈살을 찌푸린 채 입맛을 다시던 나는, 부담스러울 정도로 빤히 이쪽을 바라보고 있는 혁무진과 시선이 마주쳤다.

“뭐 해?”

“예, 예?”

“뭘 그렇게 쳐다보냐고. 내 얼굴에 뭐라도 묻었어?”

“어, 아뇨. 그냥 오늘따라 너무 막, 인물이 훤해 보이셔 가지고. 헤헤.”

간신배처럼 너스레를 떨고 있는 녀석의 모습에 내심 쓴웃음이 지어졌다.

뻔하다.

근래 들어 한껏 가라앉아 있는 내 기분을 어떻게든 맞춰 주기 위해 노력하는 것이겠지.

하지만 나는 구태여 내색하지 않은 채 혀를 찼다.

“하여간 헛소리는. 볼 일 다 끝났으면 나가. 고작 끼니 챙기는 걸로 귀찮게 하지 말고.”

“어어. 고작이라뇨. 어차피 이것도 다 먹고 살자고 하는 짓인데, 밥보다 중요한 게 뭐가 있다고.”

“꼭 누구 같네.”

“지금 설마 저를 태산이 그 아귀 같은 놈이랑 비교 하…….”

문득 흐려지는 말꼬리.

마치 못 할 말이라도 한 것처럼 혁무진은 한동안 입술만 우물거렸고, 나 역시 괜히 창밖으로 시선을 돌렸다.

그리고 잠깐의 침묵이 흐른 뒤, 조금 전과는 달리 나직한 목소리가 먼지 쌓인 방 안을 울렸다.

“조장님.”

“말해.”

“태산이 그 녀석, 잘 있겠죠?”

나는 낮은 목소리로 대답했다.

“그렇겠지.”

“엄청나게 먹는 놈이라 그쪽 식량을 이미 다 거덜 냈을지도 몰라요. 시도 때도 없이 몰래 훔쳐먹다가 남 노인한테 머리도 몇 대 맞고, 사마표가 혼도 내고.”

“그럴지도.”

“분명히 그럴걸요. 저랑 내기 하실래요?”

“싫어.”

“왜요?”

“어차피 우리 둘 다 똑같은 쪽에 걸 테니까.”

“아, 그러네.”

“그렇지.”

다시금 침묵이 찾아왔다.

앞서의 것보다 더 길고, 훨씬 무거운 침묵이.

그리고 이번에도 먼저 침묵을 깬 것은, 내가 아닌 혁무진이었다.

“조장님.”

“어.”

“다들…… 아무 문제 없이 잘 있겠죠?”

나는 대답하지 않았다.

대신 지난 이틀 내내 바라본, 그럼에도 단 한 순간도 변하지 않았던 풍경을 눈에 담았다.

압도적이며, 경이로우나 아무것도 없이 텅 빈 것처럼 느껴지는 그 풍경을.

동시에, 저 빈틈없이 채워진 풍경화(風景畵)가 백지처럼 보이는 이유에 대해 생각했다.

아니.

사람들을 생각했다.

주위의 시선 따위는 조금도 신경 쓰지 않은 채 막내야, 하고 큰 목소리로 외치며 달려올 진위경을.

그렇게 앞서나가는 큰형의 모습을 뚱한 표정으로 지켜보고 있을 진무경을.

이제는 제법 일문(一門)을 이끄는 장문인답게 수백의 수하들을 거느린 사마표와, 어느덧 한 몸이 되어 버린 남호와 태산을.

목석처럼 딱딱한 표정으로 내게 고맙다고 말하던 어느 금의위 천호와, 육신은 죽었으되 과거에 비해 생기가 넘치는 대륙의 주인을.

청해에서 웃으며 헤어졌던 그들 모두를 생각했다.

이미 지나간 과거와, 곧 다가올 미래를 떠올렸다.

하지만 어째서일까.

사막을 벗어나고, 이틀이 지나 해가 저물어 가는 지금까지도 그들은 어디에서도 보이지 않았다.

서쪽에서 산처럼 솟아오를 무림맹의 깃발도, 동쪽에서 물결처럼 밀려올 황금빛 갑옷들도.

그래.

내가 바라보고 있던 것은 풍경이 아니라 저 멀리 어딘가에서 오고 있을 사람들이었다.

그러나 굳게 약속한 마지막 날이 저물어 가고 있는 지금 이 순간까지도, 그들의 모습은 찾을 수 없었다.

‘……어쩌면.’

나는 무심코 떠오른 그 세 글자를 억눌러 참았다.

그리고 흐트러진 모래사장을 파도로 지워내듯, 마음속으로 뇌까렸다.

‘아니, 그럴 리 없어.’

그들은 강하다.

창칼은 날카롭고 의기는 타오른다.

그들이 곧 무림이며, 구주 천하다.

그렇기에 나는 힘껏 손아귀에 움켜쥐고 있는 지금의 믿음을 놓지 않았다.

이 기다림은 분명 보답받을 것이라고.

끝없는 강행군으로 지치고 먼지에 뒤덮인 몰골일지언정, 곧 웃으며 다시 만날 것이라고.

그렇게 믿었다.

믿는 것만이 내가 할 수 있는 전부였다.

“하자.”

불쑥 던진 한 마디에, 어느샌가 말없이 곁에 다가와 함께 창밖을 바라보던 혁무진이 반문했다.

“뭘요?”

“아까 그 내기, 그냥 하자고.”

나는 서서히 붉게 물들어가는 세상을 응시하며 말을 이었다.

“자정, 자정 전에 올 거야. 분명히.”

동그랗게 뜬 눈으로 나를 바라보던 혁무진이 피식 웃었다.

“그건 내기일 수가 없죠.”

“왜?”

“어차피 우리 둘 다 똑같은 쪽에 걸 테니까요. 그럼 내기 성립이 안 되잖아요.”

“젠장. 그러네.”

“그렇죠?”

“그래서, 안 할 거야?”

“아뇨.”

혁무진이 힘주어 덧붙였다.

“해야죠. 당연히.”

녀석의 목소리가 바람을 타고 창밖으로 흘러 나갔다.

그리고 세상을 짓누르는 노을과 함께, 어느덧 어둠이 찾아왔다.

숨 막힐 만큼 고요한 어둠이.



* * *



“일각 뒤에 출발한다.”

어디선가 흘러 들어온 외풍(外風)에 촛불이 위태롭게 흔들렸으나, 적천강의 음성과 어조는 담담하면서도 평온했다.

“무림맹이건 금위군이건, 약속 날짜도 까먹은 저 멍청한 것들을 하루라도 더 기다렸다가는 몸에서 사리가 나오게 생겼다. 차라리 우리가 척후 겸 선봉으로 먼저 움직이는 게 백번 낫겠지.”

언뜻 듣기에는 맞는 말이었다.

이미 이 모든 상황을 처음부터 예상했다는 듯, 아무렇지 않게 말하고 있는 적천강의 태도 때문인지 더욱 그렇게 느껴졌다.

그런 그의 좌우에서 고개를 끄덕이고 있는 살성과 궁성도.

조용히 듣고만 있는 다른 일행들의 모습도.

하지만 한 사람, 진태경은 달랐다.

“먼저 움직이자고요?”

“다른 방법이 있느냐?”

“다른 방법이 있는 것이 아니라, 그 방법만은 안 됩니다.”

“계속해 보거라.”

“서쪽과 동쪽으로 하루, 아니 반나절 정도의 거리만이라도 되돌아간다면 아군의 척후와 마주칠 가능성이…….”

“자정을 넘겼으니, 그것으로 이미 약조한 날짜는 지났다. 그 후의 대처는 사전에 미리 상의 된 일이야.”

“하지만…….”

“놈!”

화아아악.

일순간 뜨겁게 달아오른 공기 속, 짧은 일갈을 내지른 스승이 착 가라앉은 눈빛으로 제자를 응시했다.

“네 녀석이 무엇을 우려하고 있는지는 모르는 바가 아니나, 그만한 대군(大群)이 움직이는 데에는 수많은 문제가 따르는 법. 우리는 미리 정해진 계획에 따라 단지 한 걸음 앞서가고자 할 뿐이니 더 이상 왈가왈부하지 말거라.”

평소였다면 진태경도 적천강의 말에 따랐을 것이다.

일반적인 사제(師弟) 관계에 비하면 격의가 없을 뿐, 그는 다른 누구보다 스승을 굳게 믿고 따랐으니까.

그러니까, 평소였다면.

그러나 오늘은, 적어도 지금 이 순간만큼은 아니었다.

진태경은 불현듯 찾아온, 왠지 모를 기시감을 느끼며 생각했다.

‘뭐지?’

뭔가 이상했다. 아니, 이건 이상함을 넘어선 무언가다.

오랜 세월 동안 마교의 지배하에 있었던 신강은 사지(死地)나 다름없는 취급을 받아왔지만, 그렇다고 해서 미지(未知)의 땅은 아니다.

교국(敎國)이나 다름없는 그 어마어마한 성세와 중원 무림과도 결전을 치를 수 있는 전력은 어디에서 나왔겠나.

신강에는 그 광활한 면적만큼이나 상당한 인력과 물산이 잠재되어 있었고, 한때는 천하에서 손꼽히는 교역로이기도 했다.

다시 말해, 신강의 지리를 포함한 여러 정보는 은영각 역시 입수한지 오래였다.

비록 단 한 명만 살아 돌아오긴 했으나, 당장 몇 달 전 수십 명의 세작(細作)을 투입하기까지 했을 정도였으니까.

하지만 천산산맥은 다르다.

신강이 마교의 그늘 아래에 놓여 있었다면, 천산은 마교가 처음으로 발호하고 뿌리내린 성지(聖地)다.

신강이라는 사지에 존재하는 진정한 미지의 땅.

‘그리고 그 뿌리에는 누구도 접근하지 못했지.’

하지만 조금 전, 적천강은 말했다.

진태경은 들어본 적도 없는 ‘정해진 계획’에 따라, 단지 한 걸음 앞서갈 뿐이라고.

‘그럴 리 없어. 한 번 천산에 들어간 이상, 아군과의 합류도 요원해진다.’

머릿속을 어지럽히는 생각 때문일까.

진태경은 세차게 뛰는 심장의 박동과, 뜨거워지는 것을 느꼈다.

그리고 동시에, 도무지 믿을 수 없는 한 가지 진실을 깨달았다.

“거짓말이었군요. 오직 저를 속이기 위한.”

파르르 떨리는 진태경의 음성에, 적천강이 대답했다.

“정해진 것은 처음부터 하나뿐이었다. 정해진 날짜에 합류하지 못한다면, 주저없이 나아갈 것.”

스승의 무거운 목소리이, 철퇴처럼 머리 위로 떨어져 내렸다.

“우리가…… 아니, 네가 주공(主攻)이다.”

스승의 무거운 목소리가, 철퇴처럼 제자의 머리위로 떨어져 내렸다.
```

## Final English reading copy

```markdown
# Chapter 1183

It was a nameless ruin.

Judging by its area and the number of buildings, it had once been a small city where several thousand households lived together. But, as everyone had expected, not a single person could be found anywhere.

Only the mountain range stretching without end along the distant horizon remained, watching over the ghost town.

A giant of nature with a crown of snow that never melted, white in every season, pressed down like a bamboo hat: the Tianshan Mountains.

*The mountains of heaven, huh.*

Muttering to myself, I gazed through the window at the vast landscape.

Overwhelming. Almost awe-inspiring.

It was a sight that could only be called Tianshan.

The peaks rose through the clouds. They were so high that I could almost imagine immortals dwelling somewhere up there.

No, that wasn’t an absurd fantasy at all.

Just replace *immortal* with *Demon King*, and fantasy became reality.

A very horrifying reality, at that.

“Captain?”

A voice suddenly pierced my ear.

Plenty of people called me their benefactor. Only one called me Captain.

Keeping my eyes on the view outside, I answered.

“Yeah.”

Maybe it was because my thoughts were tangled like a ball of string. My voice came out subdued, and Hyuk Mujin hesitantly opened his mouth.

“Um, have you eaten?”

“Sort of. Why?”

“Slau—no, Great Hero Mungyeong told me to stop by if I had a chance. He wanted to make sure you weren’t skipping meals.”

“That guy? That’s unusual.”

It was a little surprising.

We’d spent a fair amount of time together and grown close, but I hadn’t thought he was the sort to worry about whether I’d eaten.

“He said it’s a special batch of fasting pills he made before we set out, just in case. We’re already running low on food, and he said he’d kill you if you left any.”

“…Yeah, that sounds about right.”

I shook my head and took the fasting pill I’d tucked away in my clothes. Hyuk Mujin’s eyes turned cold.

“You said you ate.”

“I said I sort of did. I didn’t say I ate.”

“Honestly. I knew it.”

Maybe he was acting up because he hadn’t been hit enough lately.

Ignoring his grumbling, I popped the fasting pill into my mouth.

I chewed and swallowed, enduring its utterly inexplicable bitterness. A surprising fullness spread through me, and a System notification rang out.

*Ding.*

> **System**
>
> You have consumed Mungyeong’s Special Fasting Pill.
>
> Fullness will be maintained for one day.
>
> A small amount of fatigue has been recovered.
>
> All stats increase by +3 for one hour.

It tasted like shit, but its effects were undeniable.

For something made by the Divine Physician, the performance was a little disappointing.

I grimaced and smacked my lips. Then I met Hyuk Mujin’s gaze as he stared at me with an almost uncomfortable intensity.

“What are you doing?”

“Y-yes?”

“What are you staring at me for? Is there something on my face?”

“Uh, no. You just look really… handsome today. Hehe.”

I couldn’t help a bitter smile at his ingratiating flattery.

Obvious.

He was trying to cheer me up somehow. My mood had been low lately.

But I didn’t let on. I clicked my tongue.

“Enough with the nonsense. If you’re done, get out. Don’t bother me just to make sure I eat.”

“Hey, ‘just’ make sure you eat? We’re all doing this to stay alive. What’s more important than food?”

“You sound just like someone.”

“Are you seriously comparing me to that glutton Taishan—”

His words trailed off.

Hyuk Mujin only moved his lips for a while, as though he’d said something he shouldn’t have. I turned my gaze back out the window, too.

After a brief silence, a voice quieter than before rang through the dust-covered room.

“Captain.”

“Go ahead.”

“Taishan… he’s doing all right, isn’t he?”

I answered in a low voice.

“He should be.”

“He eats so much, he might’ve already wiped out their food supply. He’s probably been sneaking food whenever he gets the chance, taking a few whacks from Old Man Nam, and getting scolded by Sama Pyo.”

“Could be.”

“I’m sure that’s what’s happening. Want to bet?”

“No.”

“Why not?”

“Because we’d both bet on the same thing anyway.”

“Oh. Right.”

“Yeah.”

Silence returned.

Longer than before, and much heavier.

And this time, too, it was Hyuk Mujin—not me—who broke it first.

“Captain.”

“Yeah.”

“Everyone’s… doing okay, right?”

I didn’t answer.

Instead, I took in the landscape I’d been staring at for the past two days, a view that hadn’t changed for even a moment.

It was overwhelming and awe-inspiring, yet somehow felt completely empty.

At the same time, I thought about why this perfectly filled-in landscape seemed as blank as a sheet of paper.

No.

I thought about the people.

Jin Wikyung, who would run toward me without a care for who was watching, shouting, “Youngest!” at the top of his lungs.

Jin Mukyung, watching his eldest brother stride ahead with a sullen expression.

Sama Pyo, now commanding hundreds of subordinates like a proper Sect Leader, and Namho and Taishan, who had somehow become inseparable.

A Thousand Captain of the Embroidered Uniform Guard who’d thanked me with a face stiff as a block of wood—and the ruler of the continent, whose body was dead yet who seemed more full of life than before.

I thought of all of them, everyone we’d parted from with a smile in Qinghai.

I thought of the past, already gone, and the future, soon to come.

But why?

I’d left the desert behind, and now, two days later, the sun was sinking. Still, they were nowhere to be seen.

Not the Murim Alliance’s banners rising like mountains in the west, nor the golden armor that should have flowed in like a tide from the east.

That was right.

I hadn’t been looking at the landscape. I’d been looking for the people who were coming from somewhere far away.

Yet even now, as the last day we’d firmly agreed on was drawing to a close, I couldn’t find them.

*…Maybe.*

I suppressed the three syllables that had risen unbidden in my mind.

Then, as though a wave could erase the disordered sand on a beach, I repeated to myself:

*No. That can’t be.*

They were strong.

Their blades and spears were sharp, and their conviction burned bright.

They were Murim. They were the Nine Provinces and all under Heaven.

So I held tight to the belief clenched in my fist.

This wait would surely be rewarded.

Even if they were worn out from an endless forced march and covered in dust, we’d see each other again soon, smiling.

I believed it.

Believing was all I could do.

“Let’s do it.”

Hyuk Mujin had come up beside me without a word and was looking out the window with me. He glanced over.

“Do what?”

“That bet from earlier. Let’s do it after all.”

I watched the world slowly turn red and went on.

“They’ll come before midnight. They will.”

Hyuk Mujin stared at me with wide eyes, then let out a quiet laugh.

“That can’t be a bet.”

“Why not?”

“We’d both bet on the same thing anyway. Then it’s not a real bet.”

“Damn. You’re right.”

“See?”

“So, you’re not doing it?”

“No.”

He added, with conviction,

“Of course I’m doing it.”

His voice drifted out the window on the wind.

As the sunset pressed down on the world, darkness gradually fell.

A darkness so still it was suffocating.

* * *

“We leave in fifteen minutes.”

A draft blew in from somewhere, making the candle flicker precariously. Jeok Cheongang’s voice and tone, however, were calm and composed.

“If we wait another day for these fools who forgot the agreed date—whether they’re from the Murim Alliance or the Imperial Guards—I’ll start producing relics inside my own body. It’d be a hundred times better for us to move ahead as scouts and vanguard.”

On the surface, it made sense.

Perhaps it felt even more convincing because Jeok Cheongang spoke so calmly, as though he’d expected this situation from the start.

The Slaughter Saint and Bow Saint, nodding on either side of him.

The rest of the group, listening quietly.

But one person was different: Jin Taekyung.

“You want us to move ahead?”

“Is there another way?”

“It’s not that there’s another way. We can’t take that one.”

“Go on.”

“If we head back west and east—even just a day, or half a day—we might run into our scouts…”

“Midnight has passed. The agreed date is already behind us. We discussed what to do after that in advance.”

“But…”

“Fool!”

*Whoosh!*

The air abruptly heated. His master’s sharp rebuke rang out, and he fixed his Disciple with a level gaze.

“I know what you’re worried about, but moving a great army like that comes with countless complications. We’re simply going one step ahead according to the plan we already made. Don’t argue about it any further.”

Normally, Jin Taekyung would have followed Jeok Cheongang’s words.

Their master-and-Disciple relationship might have been more informal than most, but Taekyung trusted and followed him more than anyone.

That was, if this had been a normal day.

But today—at least right now—was different.

A sense of déjà vu came over Jin Taekyung as he thought:

*What is this?*

Something was wrong. No—this was more than just wrong.

Xinjiang had long been treated as a deathtrap under the Demonic Cult’s rule, but that didn’t mean it was unknown territory.

Where had the cult’s immense power, fit to be called a theocratic kingdom, and the strength to fight the Murim of the Central Plains come from?

Xinjiang had abundant manpower and resources, just as you’d expect from a region so vast. It had once been one of the most important trade routes under Heaven, too.

In other words, the Hidden Shadow Pavilion had long since obtained all kinds of information, including details on Xinjiang’s geography.

After all, just a few months ago, they’d sent in dozens of spies—even if only one had made it back alive.

But the Tianshan Mountains were different.

If the Demonic Cult’s shadow covered Xinjiang, Tianshan was its Sacred Land, where the cult had first risen and put down roots.

The true unknown land within Xinjiang, itself a deathtrap.

*And no one had ever been able to reach its roots.*

But a moment ago, Jeok Cheongang had said they were merely going one step ahead according to a “plan already made”—a plan Taekyung had never even heard of.

*That can’t be. Once we enter Tianshan, joining up with our allies will be next to impossible.*

Maybe it was the thoughts clouding his mind.

Jin Taekyung felt his heart pounding hard and heat rising inside him.

At the same time, he realized one truth he could hardly believe.

“You were lying. Just to deceive me.”

Jin Taekyung’s voice trembled. Jeok Cheongang answered him.

“From the beginning, there was only one thing decided: if we couldn’t rendezvous on the agreed date, we’d advance without hesitation.”

His master’s heavy voice came crashing down like a war hammer.

“We… No. You’re the main attack.”

His master’s heavy voice came crashing down over his Disciple’s head like a war hammer.
```

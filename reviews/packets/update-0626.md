<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0626.txt",
      "sha256": "6a80eb8cdb3fb1c6724fda8f9b7c4c0adb68261aa3b4f8960643fb5f8ad29390",
      "bytes": 13146
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "02e7a2c1f3318dc5fddb69bfc3ea045f28077c47fad0c87200592073c6a74c05",
      "bytes": 1778
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0935525ca5e9db05317a58245bf31faa25ce4cdec90b67ac01faced137cfc8b1",
      "bytes": 193161
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b2a1808693179bd5a61a16b94963a8c586e982b0cde557bf10661d82358b52ba",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "9bf4fb000dd30fb43cfa16e180ba187cacc6d6a35c4d6e690a12aa2a807f6441",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "f2fc7ee7ffc2f4d6ef5d6de43832840ba9a04c07ef3b13e101da20ba780512a2",
      "bytes": 1206
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "11d2b860e9960bb120b3c68717abd5ef2a186ea48460d9f3fe1430b4bc864387",
      "bytes": 1043
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "1bca8e27a593950067bc91f6ad0bf7b63aabf9c6d58a619d130773f197dd5075",
      "bytes": 1061
    },
    {
      "path": "characters/Namho.md",
      "sha256": "7592c8bec6bd02ab9a51c23297dbe5c5d8d64d5370e7573c630eca4ec6c05d5f",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "b2082f38154a26c84e538925862b574d212eef004aa77bb4dea74bf3156c6c5e",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "9ddf6d719a7fa20a851896be7197aff14fdf0040ab698ebc984975793394a244",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "1939b6ec45fdfc93871d7b0786e40d0d1d827fd12d1584deac87269e4b52d549",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "4054384017c556159203804c336df54fa9176cf70eed55118daf70acd8f779e3",
      "bytes": 528
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "a3e12103d4e7c9798c4f6a74f33188349a4453d45319c92bd908c576df57bc80",
      "bytes": 794
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "19db00932b6ecd5880b3561cb4ebbf8510a06f034b21c7d4b66f7357f123088d",
      "bytes": 828
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "808d51be9d4835bb64c8e1e2779b7a9ecdb0e89ef6b4355fc0ddf56450ef49a8",
      "bytes": 198598
    }
  ],
  "estimated_tokens": 12307
}
-->

# Durable State Update — Chapter 626

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 626. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 626. Profile updates may replace only one
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
  "chapter": 626,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 626,
    "continuity_sources": [626],
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
    "The Fire Dragon Pavilion is now inside the Nanman Beast Palace's main hall under Yayul Cheok's hospitality.",
    "Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain representing the Miao people.",
    "Yayul Cheok is an old acquaintance of Jeok Cheongang and warmly welcomes Jin Taekyung after recognizing him as Jeok's Disciple.",
    "The Nanman Beast Palace encompasses thirty-two tribes across Nanman, including four great tribal groups, and its Palace Lord cannot decide major matters alone.",
    "Yayul Cheok received a delayed Dark Heaven message more than a month ago, before the Mount Song Resolution, and knows the broad situation in the Central Plains.",
    "The Nanman Beast Palace has not formally rejected joining the Murim Alliance, but its decision remains unresolved.",
    "Jin Taekyung is representing the Murim Alliance as Pavilion Master rather than visiting Nanman solely as Jeok Cheongang's Disciple."
  ],
  "continuity_sources": [
    625
  ],
  "open_questions": [
    "Who is requesting a private audience with Yayul Cheok beyond the main hall doors?",
    "Will the Nanman Beast Palace join the Murim Alliance after the tribal decision is made?",
    "Are other tribes opposing membership while Yayul Cheok is personally open to it?",
    "Was the timing of the Heavenly Demon Escort Bureau massacre connected to Dark Heaven's scheme?"
  ],
  "safe_through": 625,
  "temporary_decisions": [
    "Use Beast Miao King for 야수묘왕 and Yayul Cheok for 야율척.",
    "Use Palace Lord for 궁주 and great chieftain for 대족장.",
    "Use Old Master Jeok for 적 노 in Yayul Cheok's dialogue."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 매종학    | **Mae Jonghak**    |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 내당 | **Inner Hall** | The Tang Clan's inner hall area. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 영인 | **Yeongin** | Remote county seat in Yunnan and the party's immediate destination. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 거한 | 사마표 | Subordinate addressing the Black Dragon Demon Gate Young Sect Leader | Young Sect Leader | Crude and deferential | Uses 소문주 in short, childlike replies. |
| 사마표 | 거한 | Young Sect Leader addressing his giant subordinate | This fellow | Informal and patronizing | Refers to him as 이 녀석 while assigning him responsibility for Do Sangho's death. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야율목 | 야율척 | Young_Palace_Lord_to_Palace_Lord | Palace Lord | ceremonial and deferential | Yayul Mok kneels with his guards and formally greets Yayul Cheok upon his arrival. |
| 야율척 | 야율목 | Palace_Lord_to_Young_Palace_Lord | Mok | authoritative and familiar | Yayul Cheok questions Mok's unannounced departure and later addresses him as 목아 while discussing Nanman's tribes. |
| 야율척 | 남호 | Palace_Lord_to_Hidden_Shadow_Pavilion_agent_and_guest | old man | blunt and inquisitive | Yayul Cheok calls on the old man beside Taishan to identify him. |
| 야율척 | 주화란 | Palace_Lord_to_guest_and_Fire_Dragon_Pavilion_member | you | informal but commanding | Yayul Cheok directly asks Hwaran to identify him after addressing her as the woman beside Mujin. |
| 야율척 | 태산 | Palace_Lord_to_Fire_Dragon_Pavilion_member | you | puzzled and blunt | Yayul Cheok asks Taishan, standing beside Hwaran, to identify him, receiving only Taishan's declaration that he is hungry. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 625
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 612
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 625
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 625
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, and someone who can understand the Miao and Bai languages.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 617
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 625
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 624
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 624
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 624
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 625
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 625
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain representing the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 625
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and lord of the Nanman Beast Palace; his white tiger is a long-bonded companion; he orders Jin Taekyung and the Fire Dragon Pavilion to follow him after the pasture fire.

## Korean source

```text
＃626화



“궁주. 잠시 이야기를 나눌 수 있겠습니까?”

닫힌 문틈 사이로 흘러들어온 누군가의 낮고 딱딱한 목소리.

모두가 반사적으로 등 뒤의 문으로 고개를 돌렸지만, 나는 그 찰나의 순간에 생겨난 변화를 놓치지 않았다.

‘야수묘왕. 그리고 야율목.’

외지인인 우리는 어쩌다가 굴러 들어온 돌에 불과하지만, 저들은 남만에 박혀 있다 못해 없어서는 안 될 내핵 같은 존재다.

저 목소리의 주인이 누구인지는 몰라도 저 두 사람의 눈빛이 일순간 깊숙이 가라앉은 것만으로도 충분한 답이 됐다.

‘싱글벙글 웃으면서 볼 사이는 아니라는 거겠지.’

내심 중얼거리며 결론을 내린 그때, 나와 시선이 마주친 야수묘왕이 문득 실소를 흘렸다.

“재미있는 녀석이군.”

“예?”

“별것 아니다. 그냥 나온 말일 뿐이야.”

별것 아니긴. 누가 봐도 별것 같은데.

하지만 더 이상 묻지 말라는 듯, 두꺼운 손을 작게 내저은 야수묘왕이 나를 포함한 모두를 향해 입을 열었다.

“미안하지만 다른 객이 왔으니 자리를 비켜 줄 수 있겠느냐? 아직 시간이 있으니 여독을 푼 후에 자세한 이야기를 나누었으면 한다.”

아직 시간이 있다는 야수묘왕의 말에는 약간의 어폐가 있다. 암천이 존재하는 이상 무슨 일이 터질지는 아무도 모르니까.

그러나 잠시 휴식 후 이야기를 나누자는 제안에는 찬성이다.

‘적어도 아직까지는 남만에 별다른 특이 사항은 없는 것 같고.’

그런 생각을 하며 고개를 끄덕이자, 야수묘왕의 시선이 오른편에 시립한 야율목에게 닿았다.

“목아.”

짧은 한마디였지만 그것만으로 충분했다. 공손히 예법을 취한 야율목이 우리를 향해 눈짓했다. 따라오라는 뜻이다.

“이만 물러가겠습니다.”

“그래. 내 거한 환영식을 준비하지.”

거한 환영식은 괜찮으니까 입맹(入盟)과 암천에 대한 논의만 잘 해결됐으면 좋겠다.

야수묘왕을 하고 돌아선 우리가 문 앞까지 다다르자 암석을 깎아 만든 석문이 움직이기 시작했다.

구구궁.

무거운 소음과 함께 천천히 열리는 문틈 너머, 곰 가죽을 뒤집어쓴 채 문과 연결된 쇠사슬을 잡아당기는 근육질의 역사(力士) 두 명이 보인다.

그리고…….

“오랜만이구나.”

앞서 들려온 딱딱한 목소리의 주인도 함께.

불쑥 건네어진 그의 인사에 야율목이 고개를 숙였다.

“묘족의 야율목이 백상(白象) 숙부를 뵙습니다.”

머리부터 발끝까지 온통 새하얀 옷과 장신구를 걸친 중년의 이민족. 야율목에게 백상 숙부라 불린 그가 입을 열었다.

“돌아왔다는 소식은 들었다. 북동쪽의 목초지에서 제법 큰 화재가 있었다지?”

“사소한 문제였습니다. 금세 진압되었고요.”

“사소한 문제라.”

딱딱한 목소리에 어울리는 차가운 눈빛이 흘러나온다. 백상은 냉정한 시선으로 야율목과 그 뒤에 선 우리를 훑었다.

정확히는 그중에서도 특히 나를.

동시에 낮고 느릿한 목소리가 이어졌다.

“그러길 바라지.”

“…….”

“궁주께서는?”

“안에서 기다리고 계십니다.”

그것으로 끝이었다. 지금까지도 고개를 숙인 야율목을 힐끗 바라본 백상은 가타부타 말없이 우리를 스쳐 지나갔다.

구구궁. 다시 한번 묵직한 소음과 함께 석문이 닫히자, 그제야 비로소 야율목의 고개가 들렸다.

입을 꾹 다문 채 굳게 닫힌 석문을 응시하는 녀석에게 내가 물었다.

“저 사람, 누구야?”

“알 것 없다.”

“말하기 싫은가 보네. 그럼 뭐 됐지. 남 노인?”

내 부름에 은영각이 자랑하는 생생남만통, 남호가 망설임 없이 대답했다.

“남만에서 가장 강성한 네 개의 거대 부족 중 한 곳인 백족(白族)의 대족장이다.”

“아. 어쩐지 온통 새하얗게 차려입었더라. 백족이라면 남만 초입에서 몇 명 봤습니다. 그 흰둥이들 말하는 거죠?”

남호가 떨떠름한 목소리로 대답했다.

“흰둥…… 뭐, 틀린 말은 아니군. 부족 자체가 백색을 숭상하니까.”

남만 땅에는 서른 개가 넘는 부족들이 공존하고, 곳곳에 마을을 이루고 살며 저마다의 풍습을 지켜 나간다.

하지만 영인은 남만에서도 만남의 장소 같은 곳이라서 여러 개의 부족이 적당히 타협하며 살아가는 곳이었는데, 그중에는 백족도 있었다.

‘그 정도로 강한 부족인 줄은 몰랐네.’

그나저나 이 넓은 남만 땅을 네 등분하는 거대 부족의 대족장이라…….

야율목이 숙부 운운할 때부터 짐작은 했지만, 생각했던 것 이상으로 거물이다.

기본적인 정보를 얻은 나는 어느새 멀찍이 앞서가는 야율목의 뒤를 바짝 따라붙었다.

“근데 별로 안 친해 보이던데? 친 숙부 맞냐?”

“…….”

“야, 야. 안 들려?”

“…….”

“사람이 불렀으면 대답을 해야지. 불타는 목초지 보고 싶어? 어? 돌아가는 길에 불 한번 시원하게 싸질러 줘?”

“…….”

“어. 이 새끼가 끝까지 말을 씹네. 오케이, 알았다. 넌 관이 아니라 불을 봐야 눈물을 흘린다 이거지.”

지금까지의 내 아가리 파이터 전적을 따져보면 승률이 100%다. 그리고 그건 이번에도 마찬가지였다.

“……알아들을 수 없는 개소리 좀 그만해라. 부탁이다.”

“아, 그럼 처신 잘 하라고. 재깍재깍 대답하면 이런 일 없잖아.”

나를 지그시 노려보던 야율목이 한숨처럼 내뱉었다.

“생각을 좀 하고 물어봐라. 친 숙부면 부족이 다를까.”

“하긴. 그런데 웬 숙부 타령이야?”

“아버지와 호형호제하는 분이시다. 어릴 적부터 깊은 교분을 쌓았고, 정마대전 당시에도 늘 함께 싸우셨다고 들었지.”

나는 놀라서 눈을 크게 떴다.

“뭐? 사실이냐?”

“내 듣기로 한족 놈들은 의심이 많다더니 정말이었군. 왜, 못 믿겠나?”

“그건 아니긴 한데…… 확실히 좀 놀라긴 했어.”

“두 분이 의형제라는 게 그렇게 놀랄 일인가?”

“아니, 그거 말고.”

“……?”

“야율척 대협이 네 아버지였어? 할아버지나 증조할아버지가 아니라?”

“……!”

야율목의 눈빛이 짜게 식었지만 놀라운 건 놀라운 거다.

세상에, 많이 쳐 줘야 이십 대 중반인 녀석이 여든을 훌쩍 넘긴 야수묘왕의 아들이었다니.

제아무리 무림인들이 일반적으로 늦게 결혼하는 편이라지만 이건 다른 의미에서 대단하다.

“저, 저기. 각주님?”

주화란의 조심스러운 부름에 내가 손을 내저었다.

“잠시만요. 마지막으로 하나만 더 물어보고요. 너 혹시 장남이냐? 아니지?”

타다닥.

갑자기 빨라진 발걸음. 야율목이 씹어뱉는 듯한 말투로 대답했다.

“삼대독자다.”

“이야. 야율독자. 전지적 남만 시점 쌉가능이고.”

“무슨 말이지? 진짜 미친놈인가?”

“내가 가끔 알아들을 수 없는 얘기를 하긴 하지. 뭐 어쨌든 저 백상인지 뭔지 하는 양반이 입맹에 반대하는 쪽인가 봐? 예전 일이야 어찌 되었건 지금은 사이도 좀 안 좋고?”

“그건 네놈 같은 외부인이 신경 쓸 바가 아니……!”

이래서 대화의 흐름이 중요하다.

열이 뻗친 얼굴로 대답하던 야율목이 멈칫하며 말꼬리를 흐렸지만, 이미 엎질러진 물이요, 번져 버린 불길이나 다름없다.

완벽하게 상대를 낚은 나는 푸근하게 웃으며 녀석의 어깨를 툭툭 두드렸다.

“새끼. 말을 왜 하다가 말아. 그래서 결국 내 짐작이 맞다는 뜻이지?”

“……이놈.”

“지금 당장은 이 정도면 됐으니까 나중에 필요하면 또 물어볼게. 일단 고맙다. 아, 그리고 여기가 우리 숙소지? 안내하느라 고생했어.”

나는 대답 대신 죽일 듯이 노려보는 야율목을 뒤로하고 돌아섰다. 남호가 불을 발견한 원시인 같은 표정으로 나를 바라보고 있었다.

“자네 혹시 은영각 들어올 생각 없나?”

“은영각은 무슨. 그나저나 다 들었죠?”

“물론일세. 교묘하게 유인해서 낚아채는 솜씨가 최소 강태공이었어.”

나는 진중한 어조로 대답했다.

“사람 낚는 어부. 진드로라고 불러주십시오.”

“진드로……!”

주화란과 혁무진도 흥분된 표정으로 주먹을 불끈 움켜쥐었다.

“각주님. 정말, 정말 대단해요. 처음에는 진짜 미치신 줄 알았는데.”

“주 소저 말씀이 맞습니다. 오죽하면 제가 조장님 주둥이를 찢어 죽이고 싶었겠습니까.”

이거 뭔가 기분이 묘하긴 한데, 그래도 한 건 해냈다. 나는 흐뭇하게 웃으며 입을 열었다.

“주 소저 칭찬 감사합니다. 무진이는 대가리 박아.”

“옙.”

쿵.

나는 숨 쉬듯 자연스럽게 대가리를 박은 혁무진의 등에 걸터앉았다. 황당한 눈빛으로 상황을 지켜보던 송일섬과 사마표가 묻는다.

“어이가 없긴 한데…… 어찌 되었건 중요한 정보는 알았군.”

“각주. 이제 어찌할 셈인가?”

나는 말 없이 어깨를 으쓱해 보였다.

새로운 정보를 얻었지만 백족의 대족장이 남만야수궁의 무림맹 합류를 반대한다는 건 아무리 생각해도 좋은 소식이 아니다.

하지만 그보다 더 신경 쓰이는 것은 그 이유였다.

왜. 어째서.

정마대전에도 참여했던 그가, 야수묘왕과 어릴 적부터 함께 자란 불알 동생이 무슨 이유로 입맹을 반대하는 것인지.

그리고 방금 전 스치듯이 가진 만남 속, 백상에게서 느꼈던 냉랭함과 유심히 나를 살피던 시선의 의미는 무엇인지.

나는 그것이 신경 쓰였다.

꾸르르륵.

“태산이. 배고프다.”

“…….”

저 시벌 놈이.



* * *



표범과 호랑이 가죽으로 뒤덮인 태사의(太史椅).

비스듬히 턱을 괴고 앉은 야수묘왕은 앞에 놓인 술병을 들었다.

쪼르르륵.

그가 직접 돌을 깎아 만든 투박한 술병이 기울어지자, 탁한 색깔의 술이 커다란 나무 대접을 가득 채운다.

그렇게 채워진 두 개의 잔 중 하나를, 야수묘왕은 새로운 손님에게 권했다.

“네가 좋아하는 과실주다. 사양 말고 들거라, 백상(白象).”

백상. 흰 코끼리라는 뜻이다.

그러나 느릿느릿하게 날아온 술잔을 받은 중년인의 모습은 코끼리와는 거리가 멀었다.

얼음처럼 차가운 눈빛과 경직된 입꼬리. 야수묘왕과는 상반되는 마른 체구를 지닌 그는 딱딱한 목소리로 대답했다.

“괜찮습니다. 오늘은 사양하지요.”

탁.

소리 내어 술잔을 내려놓는 백상의 모습에, 야수묘왕은 씁쓸하게 웃었다.

“……그렇구나. 괜찮다.”

대답과는 달리 속마음은 쓰렸다.

이제는 기억조차 흐릿한 옛 기억 속, 함께 며칠 밤낮을 웃고 떠들며 쉬지 않고 술잔을 기울였던 그의 하나뿐인 의형제는 수십 년째 같은 대답을 하고 있었다.

오늘은 사양하지요.

오늘 하루만의 일이 아니다. 그제도, 어제도. 그리고 내일과 모레도 마찬가지일 것이다.

이미 익숙한 일이기에 짐작할 수 있었고, 자신의 짐작이 그대로 이루어질 것이라는 사실에 마음이 아팠다.

“그래, 오늘은 무슨 일로 이 우형을 찾아왔나?”

백상이 흔들림 없는 목소리로 대답했다.

“아시지 않습니까.”

“그들 때문이군.”

“무림맹에서 왔다 들었습니다.”

“맞네. 신임 맹주로 취임한 검성 매종학이 보낸 이들일세.”

야수묘왕은 순순히 긍정했다. 숨길 일도 아니고, 숨긴다 하여도 결국 백상의 귀에 들어갈 수밖에 없는 일이었다.

당장 남만야수궁의 내당에 속한 이들 중에도 백족이 수두룩했으니까.

‘어쩌면 저들의 상세한 신분까지도 알고 있을지도.’

그가 아는 백상은 언제나 철두철미한 성격이었고, 이번에도 마찬가지일 것이다.

백상의 차가운 눈빛이 말없이 술잔을 기울이는 야수묘왕을 향했다.

“지난번 부족 회의의 결과를 잊으신 것은 아니겠지요.”

그럴 리가. 마음속으로 대답하는 야수묘왕의 귓가로, 딱딱하기 그지없는 백상의 목소리가 파고 들었다.

“우리, 남만야수궁은…… 결코 입맹하지 않을 것입니다.”
```

## Final English reading copy

```markdown
# Chapter 626

“Palace Lord, may I speak with you for a moment?”

A low, rigid voice drifted through the crack between the closed doors.

Everyone instinctively turned toward the door behind us, but I didn’t miss the change that occurred in that brief instant.

*The Beast Miao King. And Yayul Mok.*

We outsiders were nothing more than stones that had happened to roll in from elsewhere. But those two were embedded so deeply in Nanman that they were like an indispensable inner core.

I didn’t know who the owner of that voice was, but the fact that both of their gazes had instantly darkened was answer enough.

*They’re not exactly on smiling terms.*

Just as I reached that conclusion inwardly, the Beast Miao King happened to meet my gaze and let out a quiet laugh.

“What an interesting fellow.”

“Pardon?”

“It’s nothing. Just something that slipped out.”

As if it were nothing. Anyone could see it was something.

But the Beast Miao King gave a small wave of his thick hand, as if telling me not to ask any further, then addressed everyone—including me.

“I’m sorry, but another guest has arrived. Could you give us some privacy? There is still time, so I would like to discuss things in greater detail after you’ve rested from your journey.”

There was a slight contradiction in the Beast Miao King’s words about there still being time. As long as Dark Heaven existed, no one knew what might happen.

Still, I agreed with his suggestion that we rest for a while before talking.

*At least, it doesn’t seem like anything unusual has happened in Nanman yet.*

As I nodded, the Beast Miao King’s gaze shifted to Yayul Mok, who was standing at attention on his right.

“Mok.”

It was only a single word, but that was enough. Yayul Mok respectfully performed the proper etiquette, then gestured toward us.

It meant we should follow him.

“We’ll take our leave.”

“Go. I’ll prepare a grand welcome.”

*Forget the grand welcome. I just hope the discussions about joining the alliance and Dark Heaven go well.*

After we took our leave of the Beast Miao King and reached the door, the stone door carved from solid rock began to move.

*Rumble.*

Beyond the slowly opening gap, accompanied by a heavy grinding sound, two muscular strongmen wearing bear hides could be seen pulling on chains connected to the door.

And then…

“It’s been a long time.”

The owner of the rigid voice we had heard earlier was there as well.

At his sudden greeting, Yayul Mok lowered his head.

“Yayul Mok of the Miao people pays his respects to Uncle Baeksang.”

The middle-aged man of another ethnicity was dressed entirely in white, from head to toe, including his clothing and accessories. The man Yayul Mok had called Uncle Baeksang opened his mouth.

“I heard you had returned. I also heard there was quite a large fire in the northeastern pasture.”

“It was a minor problem. It was put out quickly.”

“A minor problem.”

The cold gaze that accompanied his rigid voice swept over us. Baeksang examined Yayul Mok and everyone standing behind him.

More precisely, he examined me in particular.

At the same time, his low, unhurried voice continued.

“I hope so.”

“……”

“Where is the Palace Lord?”

“He is waiting inside.”

That was all.

Baeksang glanced at Yayul Mok, who was still bowing his head, then passed by us without another word.

*Rumble.*

When the stone door closed once more with another heavy grinding sound, Yayul Mok finally raised his head.

He stared at the firmly closed stone door with his lips pressed tightly together. I asked him,

“Who was that?”

“None of your business.”

“You don’t want to tell me. Fine, then. Elder Namho?”

Namho, the Hidden Shadow Pavilion’s walking encyclopedia of Nanman, answered without hesitation.

“He is the great chieftain of the Bai people, one of the four most powerful great tribes in Nanman.”

“Oh. No wonder he was dressed entirely in white. I saw a few people like that near the entrance to Nanman. You mean those whiteys, right?”

Namho answered with a reluctant tone.

“White guys… Well, that isn’t exactly wrong. The tribe itself venerates the color white.”

More than thirty tribes coexisted throughout Nanman. They formed villages in various places and preserved their own customs.

Yeongin was practically a gathering place even in Nanman, so several tribes lived there by making various compromises. The Bai people were among them.

*I didn’t know they were that powerful.*

In any case, the great chieftain of one of the great tribes dividing this vast land of Nanman into four…

I had suspected as much from the moment Yayul Mok called him Uncle, but Baeksang was an even bigger figure than I had imagined.

After learning the basic information, I quickly caught up with Yayul Mok, who had moved well ahead of us.

“But you two didn’t seem very close. Is he really your actual uncle?”

“……”

“Hey. Hey, can’t you hear me?”

“……”

“If someone calls you, you’re supposed to answer. Do you want to see the burning pasture? Huh? Want me to start a nice fucking fire on the way back?”

“……”

“Oh, this bastard is ignoring me to the very end. Fine, I get it. You have to see fire, not a coffin, before you’ll cry.”

Judging by my record as a mouth-fighting champion, my win rate was one hundred percent.

This time was no different.

“……Please stop spouting incomprehensible bullshit.”

“Oh, then behave yourself. If you answered promptly, none of this would happen.”

Yayul Mok glared at me for a moment before letting out a sigh.

“Think before you ask. If he were my actual uncle, would he belong to a different tribe?”

“True. But why are you calling him Uncle?”

“He and my father are sworn brothers. They formed a deep friendship when they were young, and I heard they always fought together during the Great Faction War.”

My eyes widened in surprise.

“What? Is that true?”

“I heard you Han bastards were suspicious by nature, and it seems that was true. What? You don’t believe me?”

“It’s not that, but… I was a little surprised.”

“Is it really so surprising that the two of them are sworn brothers?”

“No, not that.”

“……?”

“Great Hero Yayul Cheok was your father? Not your grandfather or great-grandfather?”

“……!”

Yayul Mok’s gaze turned icy, but surprising was surprising.

Good grief. A fellow who looked no older than his mid-twenties was the son of the Beast Miao King, who was well over eighty.

Even if martial artists generally married late, that was impressive in an entirely different way.

“Um, Pavilion Master?”

At Ju Hwaran’s cautious call, I waved my hand.

“Just a moment. I only have one last question. Are you the eldest son? No, right?”

*Tap tap tap.*

Yayul Mok’s footsteps suddenly quickened. He answered through clenched teeth.

“I am the only son for three generations.”

“Wow. Yayul Only-Son. An omniscient Nanman point of view is totally possible.”

“What does that mean? Are you actually insane?”

“I do sometimes say things people can’t understand. Anyway, that Baeksang fellow seems to be on the side opposing Nanman Beast Palace joining the alliance, right? Whatever happened in the past, you two aren’t exactly on good terms now?”

“That is no concern of an outsider like you—!”

This was why the flow of a conversation was important.

Yayul Mok had been answering with his face flushed from anger, but he faltered and let his sentence trail off. However, the water had already been spilled, and the fire had already spread.

Having baited him perfectly, I smiled warmly and patted his shoulder.

“You bastard. Why did you stop talking? So my guess was right, then?”

“……You.”

“This is enough for now. I’ll ask again later if I need to. Thanks, by the way. Oh, and this is our lodging, right? Thanks for showing us the way.”

I turned away from Yayul Mok, who was glaring at me as if he wanted to kill me.

Namho was staring at me with the expression of a primitive man who had just discovered fire.

“Have you ever considered joining the Hidden Shadow Pavilion?”

“The Hidden Shadow Pavilion? Forget it. Anyway, you heard all that, didn’t you?”

“Of course. The way you lured him in and hooked him was at least Jiang Taigong’s level.”[^1]

I answered in a solemn tone.

“A fisherman who catches people. Please call me Jindro.”

“Jindro…!”

Ju Hwaran and Hyuk Mujin also clenched their fists, excitement written across their faces.

“Pavilion Master. You’re truly, truly amazing. At first, I really thought you had lost your mind.”

“Young Lady Ju is right. I was so frustrated that I wanted to tear Captain’s mouth open and kill him.”

It felt a little strange, but I had still accomplished something. I smiled with satisfaction and opened my mouth.

“Thank you for the compliment, Young Lady Ju. Mujin, put your head down.”

“Yes, sir.”

*Thud.*

Hyuk Mujin planted his head on the ground as naturally as breathing. I sat astride his back.

Song Ilseom and Sama Pyo had been watching the situation with dumbfounded expressions. They asked,

“That was outrageous, but… regardless, we learned some important information.”

“Pavilion Master, what do you intend to do now?”

I shrugged without a word.

We had gained new information, but the fact that the great chieftain of the Bai people opposed the Nanman Beast Palace joining the Murim Alliance was hardly good news.

What concerned me even more was the reason.

*Why? Why?*

Why would a man who had fought in the Great Faction War—the Beast Miao King’s childhood best friend and sworn younger brother—oppose joining the alliance?

And what did the coldness I had sensed from Baeksang during our brief encounter mean? What did it mean that he had been studying me so carefully?

That was what bothered me.

*Grrrrrrk.*

“Taishan. Hungry.”

“……”

*That fucking bastard.*

* * *

A high-backed chair covered in leopard and tiger hides.

The Beast Miao King sat in it with his chin resting on one hand, then picked up the wine bottle placed before him.

*Glug-glug.*

As the rough stone bottle he had carved himself tilted, cloudy liquor filled a large wooden bowl.

Of the two cups he filled, the Beast Miao King offered one to his new guest.

“It’s the fruit wine you like. Don’t hold back, Baeksang.”

Baeksang. The name meant white elephant.

Yet the middle-aged man who caught the slowly drifting cup looked nothing like an elephant.

His gaze was as cold as ice, and the corners of his mouth were stiff. With a lean build completely unlike the Beast Miao King’s, he answered in a rigid voice.

“I’m fine. I’ll pass today.”

*Clack.*

Baeksang deliberately set the cup down with a noise. The Beast Miao King smiled bitterly.

“……I see. That’s fine.”

Despite what he said, his heart ached.

Somewhere in the old memories that had grown hazy with time, his one and only sworn brother had once spent days and nights laughing, talking, and constantly raising their cups with him.

For decades, that brother had been giving him the same answer.

*I’ll pass today.*

It wasn’t just today. It had been the same the day before yesterday and yesterday. Tomorrow and the day after would be no different.

The Beast Miao King was already familiar with it, which was why he could predict it. And knowing that his prediction would come true pained him.

“So, what brings you to seek out this older brother today?”

Baeksang answered in an unwavering voice.

“You know why.”

“It’s because of them.”

“I heard they came from the Murim Alliance.”

“That’s right. They were sent by Sword Saint Mae Jonghak, who has taken office as the new Alliance Leader.”

The Beast Miao King readily admitted it. There was no reason to hide it, and even if he did, Baeksang would inevitably hear about it in the end.

There were already countless Bai people among those belonging to the Nanman Beast Palace’s Inner Hall.

*He may even know their exact identities.*

The Baeksang he knew had always been meticulous, and this time would be no different.

Baeksang’s cold gaze settled on the Beast Miao King as he silently tipped his cup.

“You haven’t forgotten the result of the last tribal council, have you?”

*Of course not.*

As the Beast Miao King answered inwardly, Baeksang’s rigid voice pierced his ears.

“We—the Nanman Beast Palace… will never join the alliance.”

[^1]: Jiang Taigong is a legendary Chinese fisherman famed for luring people through patience and skill; his name is also used for someone who expertly hooks others.
```

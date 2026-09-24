<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1012.txt",
      "sha256": "e4e3a4d07dddeb93e758d306a35b29152ccab86ce6c642e4a421ef9718e3a680",
      "bytes": 12077
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "57a411f284035c0b84ff4de7d8cd8c839b95e6ce1ab27829c102828694e99cc3",
      "bytes": 1536
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "516a8b203d28c7930cfab6973246cc4b7ce64aa1171e07d163cf23cb52f7cc20",
      "bytes": 237525
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8f34be15c4704140dc3fc566b247ef2b2c0c58e90194a2649817322c1ebaf222",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c0856c5f2814087863fc1492f39c7f2198be5cbe1803a578a1999894c47e4e51",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "012f94758ad53af89527dfed0df11de3a8d883dfdbfe6056576b4226bba925af",
      "bytes": 1408
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "a0ade900d3c9a89cb9db2caf0e9daef57e78f9d9abb1a8db617102400df12f8c",
      "bytes": 974
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "af032c2a8aeaa3066d3d591ee7d885e5b50750617dc776cdbc62f060a535d1e4",
      "bytes": 636
    },
    {
      "path": "characters/Namho.md",
      "sha256": "99e6b8e6f71d3840ed1129620dfd555a45810daeebdcf13a7349ccb9ab006f92",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "e95178c365f1b1a51ced469222086a52ae1a2e9476bee918aa7b8c30a86c0d12",
      "bytes": 937
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "19b1f95d3c21cbceb7c6d164c2a0f20a7908a8b5ecee783a706a4c5ba5f8c54a",
      "bytes": 742
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "782a4ad96c0e42998e6f6bfb773846ac28d9db0d47e75b3bc1a54347c943f3a1",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "54ea822c45c6672cd344df577921d4751105e01bca1562a5e0b1aea50af65260",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8a36c21af3e33ce8297d5a41a312212a7b74793dcd26a6bf5d9ca9c9372e2ef2",
      "bytes": 276653
    }
  ],
  "estimated_tokens": 12393
}
-->

# Durable State Update — Chapter 1012

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
1 and safe_through 1012. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1012. Profile updates may replace only one
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
  "chapter": 1012,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1012,
    "continuity_sources": [1012],
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
    "Baekma Bang, led by Ma Junggeol and his six sworn brothers, has joined Taekyung’s force and is assigned to the Fire Dragon Pavilion.",
    "Ma Junggeol and his brothers were formerly mounted bandits in Ningxia; they say they avoided harming civilians and credit the Lord with leading them onto a better path.",
    "The brothers sent messengers toward Ningxia and are considering sending one of their own to check on the Lord, whose mental state they distrust.",
    "Taekyung can now detect and eavesdrop on nearby Sound Transmissions, subject to the participants’ relative levels.",
    "Dark Heaven’s force was reported in the western desert, and its strength, objective, and timing of advance remain uncertain.",
    "Taekyung stays with the allied force moving toward the threatened Gansu front; Gansu’s defenses and the potential loss of its control remain at stake.",
    "Taekyung’s linked Quest, “Road of Blood,” requires annihilating hostile forces in Gansu; failure means Dark Heaven wins and Gansu’s control is lost."
  ],
  "continuity_sources": [
    1010,
    1011
  ],
  "open_questions": [
    "Who is the Lord who helped reform Ma Junggeol and his brothers, and is he currently mentally stable?",
    "What is Dark Heaven’s full strength and objective in the western desert, and have its forces begun advancing?",
    "Who was the unknown master who helped reform the Ningxia bandit leaders?"
  ],
  "safe_through": 1011,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마적     | **mounted bandits**                              |                                                       |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 노부      | **this old man / I**                                            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 마중걸 | **Ma Junggeol** |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 프랑스 | **France** | Country containing Paris and Luxembourg Gardens. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |
| 백마칠종 | **Seven Masters of Baekma Bang** | Collective title for Ma Junggeol and his six associates. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1008
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1005
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1010
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1005
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1011
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his group, and places firm trust in the benefactor who led them onto a better path.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1005
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1006
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1005
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1005
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1005
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1012화



쉼 없이 내달리는 말발굽을 따라, 시간은 바람처럼 스쳐 지나갔다.

석양이 광야를 집어삼키고, 이내 찾아온 어둠이 세상을 짓누를 때까지. 뒤이어 어스름한 여명이 그 사이를 비집고 번져올 때까지.

그리고 두 번째로 찾아온 어둠이 깊어졌을 때, 쉴 틈 없이 달싹이던 마중걸의 입술도 마침내 휴식을 취할 수 있었다.

“……그렇게 된 겁니다.”

긴 이야기를 끝마친 마중걸은 하룻밤 사이에 폭삭 늙어 있었다.

지난 십여 년간 있었던 일들을 꼬박 하루가 넘게 줄줄 읊어서이기도 했지만, 그보다는 나를 시작으로 하나씩 늘어난 청중(聽衆)들로 인한 부담감이 더욱 컸을 것이다.

물론 그중에서도 특히, 화왕(火王)이라는 거인에게서 뿜어져 나오는 압박감은 말할 것도 없었다.

“그렇게 되긴 뭐가 돼. 더 지껄여 보거라.”

나지막한 적천강의 윽박지름에, 가뜩이나 녹초가 되어 있던 마중걸이 울상을 지어 보였다.

“진짜 끝입니다. 이제 더는 말할 것도 없다니까요.”

“지금부터 뒤져서 나오면 한 음절에 열 대다. 이래도 없느냐?”

“예?”

아니, 무슨 썰 보따리가 있는 것도 아닌데 뒤지긴 뭘 뒤져.

마중걸의 애처로운 눈빛을 받은 나는 고개를 절레절레 내저으며 입을 열었다.

“그만하시죠. 그리고 한 음절에 백 대면 미쳤다고 말합니까? 설령 남은 이야기가 있더라도 죽을 각오로 버티지.”

“그래? 그럼 열 대로 낮춰 줄 테니 싹 다 털어놔라.”

“그 정도만 해도 충분히 죽어요.”

“좋다. 한 대. 노부의 마지막 제안이다.”

“……차라리 마지막 유언을 하라고 하십쇼. 이쯤 되면 그냥 죽이고 싶어 하시는 것 같은데.”

내 조곤조곤한 반박에 적천강이 눈살을 찌푸렸다.

“네 녀석은 너무 물러터졌다. 이렇게라도 해야 뭐든 한 마디라도 더 쥐어 짜내지.”

“저 양반 꼴을 좀 보세요. 이제는 쥐어 짜내도 육수 한 방울 안 나옵니다.”

그냥 하는 말이 아니라, 지금의 마중걸은 반쯤 영혼이 빠져나가 있는 상태나 다름없었다.

생각해 보라.

말이 쉬워서 십 년이지, 강산도 변하는 그 긴 세월 동안 있었던 모든 일을 잠 한숨 못 자고 세세하게 떠올려야 했으니 하루 조금 넘는 시간 만에 반건조 오징어가 될 수밖에 없었다.

“미, 믿어 주십시오. 저는 진짜 하나도 안 빼놓고 전부 말씀드렸습니다.”

마중걸이 그렁그렁해진 눈으로 애원하듯 말하자, 그의 여섯 의형제도 덩달아 입을 열었다.

아니, 정확히는 열다가 말았다.

“대형께서 하신 말씀이 맞…….”

“처맞기 전에 전부 주둥이 닥쳐라. 특히 네놈.”

적천강에 의해 지목된 난쟁이가 바짝 얼어붙었다.

“저, 저 말입니까?”

“그래. 앞으로 한 번만 더 갈갈거리면 뒈질 줄 알아라. 말 한마디 끝날 때마다 뭔 추임새 넣는 것도 아니고, 어린 놈의 새끼가.”

적천강의 일갈에 난쟁이가 입을 꾹 다물자, 그 광경을 옆에서 지켜보던 주먹코가 희열에 찬 목소리로 중얼거렸다.

“드디어…….”

드디어는 뭐가 드디어야.

이놈이나 저놈이나 제정신이 아닌 것 같지만, 여하튼 하나는 확실해졌다.

“무진아.”

내 부름에 담긴 의미를 알아차린 혁무진이 입맛을 다셨다.

전날부터 흑룡마문과 함께하게 된 사마표, 태산을 제외한 다른 대원들 역시 반응은 엇비슷했다.

“씁. 괜찮을까요? 영 찝찝한데.”

“은인, 아니 진 공자, 아니 각주님.”

“포박이라도 하는 게 좋을 듯싶은데.”

“내 생각은 좀 다르…… 제기랄. 이 빌어먹을 말안장!”

안락하기 그지없던 태산의 어깨와는 달리, 거칠게 들썩이는 말안장 위에서 엉덩이 통증을 호소하던 남호가 찡그린 얼굴로 말을 이었다.

“각주 지시를 따라야지. 그게 맞아. 그리고 뭐 굳이 포박하거나 하지 않아도 저놈들이 언감생심 딴 마음을 품을 수나 있겠나?”

“그것도 그러네요.”

고개를 끄덕여 수긍한 혁무진을 시작으로, 주화란과 송일섬도 각자 쥐고 있던 말고삐를 놓았다.

물론 그 말고삐는 그들 자신의 것이 아닌, 포위하듯 바짝 옆에 붙어 달리던 백마칠종(白馬七宗)의 것이었다.

“믿어 줘서 고맙소.”

“아직 완전히 믿는 건 아니니까 고마워하실 필요는 없고.”

눈물까지 글썽이는 마중걸에게는 그렇게 대꾸했지만, 내 속마음은 달랐다.

‘아무리 생각해 봐도 암천이 보낸 간자(間者)들은 아니야.’

물론 처음 전음을 엿들었을 때만 해도 잠시 묻어 두었던 의심이 무럭무럭 솟아났었다.

그러니까, 처음에는.

하지만 마중걸의 이야기를 모두 들은 지금, 마음속 의심은 어느새 누군가를 향한 호기심으로 변해 있었다.

마중걸과 그의 의형제들이 대인(大人)이라 부르며 떠받드는, 정체불명의 고수에 대한 호기심.

- 어찌 생각하느냐.

귓가를 파고드는 나지막한 전음.

적천강의 물음에 담긴 의미를 이미 알고 있는 나는, 자연스럽게 고개를 돌려 전방을 주시하며 대답했다.

- 글쎄요.

- 말을 아끼는 것이냐. 아니면…….

- 정말 잘 모르겠어서 드리는 말씀입니다. 대인이라는 그자, 수상하다기보다는 묘해요. 정말 희한할 정도로.

과장이 아니라, 사실이 그랬다.

어느 날 홀연히 나타나 관부의 통제마저 벗어난 마적단을 단숨에 일망타진한 의문의 초절정 고수, 이른바 대인은 그만큼 베일에 싸인 존재였으니까.

‘이름도, 출신 내력도, 그 무엇하나 제대로 아는 게 없다고 했지.’

백마칠종이 그를 모시기 시작한 지 무려 십여 년이다.

그런데 마중걸은 물론 백마칠종 중 그 누구도 대인의 정체를 몰랐고, 그런 그들에게 추궁을 가할 때마다 이구동성으로 토해 낸 대답은 대부분 엇비슷했다.



‘아니, 전부 사실입니다. 원래 그런 분이라니까요?’

‘저희가 어느 안전이라고 감히 거짓을 아뢰겠습니까. 제발 좀 믿어 주십쇼.’

‘저희가 나눈 대화를 들으셨다니 이미 아시겠지만 그분이 원래 좀, 아니 상당히 오락가락합니다. 예? 이름이랑 나이요? 말도 마십시오. 물어볼 때마다 달라집니다. 막내야, 안 그러냐?’

‘형님들 말씀이 맞습니다. 칠복이, 개똥이…… 삼 년 전인가? 스스로를 열일곱 살 된 소향이로 알고 있더라고요. 그때부터 저희도 두 손 두 발 다 들었습니다.’

‘녕하성에 언제부터 머물렀는지도 모르겠습니다. 그냥 갑자기 나타나서 말도 안 되는 신위(神威)로 인근을 평정하더니, 그 후로는 거처에 처박혀서 꿈쩍도 안 하지 뭡니까. 근 십 년을 그랬어요. 믿기지 않으시겠지만 사실입니다.’



뽑아도 뽑아도 줄줄이 끌려 나오는 고구마 줄기처럼, 들을수록 황당한 이야기들이 우후죽순으로 쏟아졌다.

듣던 와중에 문득 이런 생각이 들 수밖에 없을 만큼.

‘그 인간, 도대체 뭐지?’

누구에게나 탐욕은 있다.

옳고 그른 방향인지를 떠나, 사람이라면 한 번쯤 마음속에 품은 목표가 존재하기 마련이니까.

하지만 이야기 속의 대인은 어디에도 해당하지 않았다.

녕하 일대를 손에 넣고 위풍당당한 패자(霸者)로 군림한 것도 아니요. 그렇다고 신분을 감추기 위해 변방으로 스며든 악명 높은 마두(魔頭)나 인생을 마무리하기 위해 아무도 찾지 않는 곳을 떠도는 은거기인(隱居伎人)도 아니었다.

‘패자로 군림할 속셈이라면 곧장 동굴에 처박힐 이유가 없고, 마두였다면 정체가 발각될 테니 기를 쓰고 숨겼겠지. 아니면 처음부터 마적단들을 수하로 부리거나.’

은거기인일 경우는 깊게 생각할 필요조차 없다.

솔직히 어느 정신 나간 은거기인이 풍경 좋고 물 맑은 심산유곡(深山幽谷)을 놔두고 사시사철 미세먼지 농도 짙음에 황사가 불어오는 변방으로 향하겠나.

무식한 나도 알 정도로 유명한 시인인 폴 발레리가 프랑스가 아닌 녕하성에 살았다면, ‘황사가 분다. 시발 죽고 싶다.’라고 했을 거다.

‘심지어 늙어서 노망이 들었거나 심산유곡을 찾을 필요도 없이 죽을 날을 받아 둔 노인네냐, 하면 그것도 아니고.’

백마칠종의 증언에 의하면, 대인은 워낙 씻지 않아 땟국물이 줄줄 흘렀음에도 대충 그 용모와 음성은 중년 어림.

게다가 마중걸과 그 의형제들이 찾아와 술과 음식을 바치면 그 대가로 약간의 가르침을 베풀기도 하고, 거처에 머무르다가 가끔 한 번씩 마실까지 나간다고 했다.

계속 안에만 있으면 답답하다고. 사람 냄새 좀 맡고 싶다고.

얼마나 자주 싸돌아다녔으면, 백마칠종이 굳이 나서서 대인의 정체를 숨기지 않아도 자연스럽게 녕하성에 녹아들 정도라고 했다.

거지1 정도의 느낌으로.

‘이딴 게…… 은거기인?’

깊은 수렁에 빠진다면 마치 이런 기분일까.

생각할수록 어이없음과 호기심만 부풀어 가던 그때, 아마도 나와 같은 상념을 떠올린 것이 분명한 적천강이 입술을 달싹였다.

- 노부가 이만하면 살기도 오래 살고, 미친놈들도 수백 수레쯤은 봤다고 생각했는데…… 이런 인간 군상은 머리털 나고 처음 본다.

- 새로 나기 시작한 지 얼마 안 되셨잖아요.

- ……뒈지고 싶으냐?

- 아뇨. 그보다 노야께서 하신 말씀에는 저도 공감합니다. 도무지 종잡을 수가 없어요.

- 천주, 그놈이 부리는 수족 중 하나일까?

- 남아 있는 손발이야 당연히 있겠죠. 하지만 만약 노야께서 천주라면, 저런 인간을 수족으로 부리시겠습니까?

적천강이 망설임 없이 대답했다.

- 미쳤느냐?

- 그렇죠?

- 대가리에 멸염신권을 맞아도 그런 놈은 수하로 안 부린다. 물론, 저 흉악하게 생겨 먹은 놈들이 털어놓은 이야기가 모두 진실이라는 가정하에.

- 그런데 이미 믿고 계시잖아요.

- 그건…….

흐려지는 전음과 함께 반사적으로 돌아가는 고개.

시선을 마주치기가 무섭게 석상처럼 굳어 버리는 백마칠종의 모습에, 적천강이 고개를 절레절레 저었다.

- 그래, 네 녀석의 생각이 맞느니라. 노부가 느끼기에도 저놈들은 거짓말을 하고 있지 않다. 아니, 그럴 깜냥조차 없어.

이것 하나만큼은 내가 보기에도, 그리고 다른 모두가 보더라도 마찬가지일 것이다.

하지만 저들과 대인의 존재가 아군에게 무해(無害)하다는 결론을 도출했다 한들, 우리 두 사람만의 직감으로 모든 것을 결정지을 수는 없는 법.

- 어찌하겠느냐?

적천강의 전음이 재차 귓가를 파고든 순간, 짧은 고민 끝에 판단을 내린 나는 말고삐를 서서히 늦추며 백마칠종과 말머리를 나란히 했다.

“이, 이번에는 도대체 왜…….”

지레 겁부터 집어먹는 마중걸과 그의 의형제들.

그런 그들을 말없이 응시하던 나는 불쑥 입을 열었다.

“얼마나 필요합니까?”

“그게 무슨…….”

“대인이라고 부르는 그 사람을 지금 향하는 목적지까지 데려오는 데까지 걸리는 시간.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 1012

Time swept by like the wind, keeping pace with the horses’ ceaseless gallop.

Until the sunset swallowed the wilderness and the darkness that followed pressed down on the world. Until the pale dawn came creeping through the gap between them.

And when darkness fell for the second time, Ma Junggeol’s lips, which had been moving nonstop, could finally rest.

“……And that’s what happened.”

By the time he finished his long story, Ma Junggeol looked as if he’d aged ten years overnight.

Partly because he’d spent more than a full day reciting every event of the past decade or so. But the burden of his audience—which had grown one by one, starting with me—must have weighed on him even more.

Of course, nothing compared to the pressure radiating from that giant known as the Fire King.

“What do you mean, that’s what happened? Keep talking.”

At Jeok Cheongang’s low growl, Ma Junggeol, already dead on his feet, looked like he was about to cry.

“I’m really finished. I’m telling you, there’s nothing else to say.”

“If I dig around and anything comes out later, it’s ten hits per syllable. Still nothing?”

“What?”

It’s not like he had a whole stash of stories tucked away. What was there to search?

At Ma Junggeol’s pleading look, I shook my head and spoke up.

“Give it a rest. And if it’s a hundred hits per syllable, why would he say anything? Even if he had more to tell, he’d hold out even if it killed him.”

“Is that so? Then I’ll lower it to ten. Spill everything.”

“Ten would be enough to kill him.”

“Fine. One hit. That’s my final offer.”

“……You might as well tell him to make his last will. At this point, it seems like you just want to kill him.”

Jeok Cheongang frowned at my quiet rebuttal.

“You’re too soft. Sometimes you have to do this to squeeze even one more word out of someone.”

“Look at him. There’s not a drop of broth left to squeeze out of him.”

I wasn’t just saying that. Ma Junggeol was practically half out of his soul.

Think about it.

It was easy to say ten years, but he’d had to recall every single thing that happened over a whole decade, the kind of time it takes for mountains and rivers to change, without a wink of sleep. No wonder he’d turned into a half-dried squid in just over a day.

“P-please believe me. I really did tell you everything. I didn’t leave out a single thing.”

Ma Junggeol pleaded, his eyes brimming with tears. His six sworn brothers joined in.

Or, more precisely, they started to speak and then stopped.

“What our eldest brother said is righ—”

“Shut your mouths before I beat the hell out of you. Especially you.”

The shorty Jeok Cheongang had singled out froze stiff.

“M-me?”

“Yeah, you. Make one more racket and you’re dead. You don’t need to chime in after every damn sentence. What are you, some little brat?”

At Jeok Cheongang’s shout, the shorty clamped his mouth shut. Watching from the side, the bulbous-nosed one murmured in a voice full of delight:

“At last…”

At last what?

These guys were all out of their minds, but at least one thing was clear.

“Mujin.”

Hyuk Mujin understood what I meant by calling his name and clicked his tongue.

The other members, apart from Sama Pyo and Taishan, who’d joined us the day before along with the Black Dragon Demon Gate, reacted much the same way.

“Yikes. Is this really okay? I’ve got a bad feeling about it.”

“Benefactor—no, Young Master Jin—no, Pavilion Master.”

“I think we should tie them up, at least.”

“I think differently—damn it. This miserable saddle!”

Unlike Taishan’s shoulders, which were as comfortable as a cushioned seat, Namho was perched on a saddle that bounced violently beneath him. Grimacing at the pain in his backside, he continued:

“We should follow the Pavilion Master’s orders. That’s the right thing to do. And do you really think those guys would dare entertain any other ideas, even without tying them up?”

“That’s true.”

Hyuk Mujin nodded in agreement. Ju Hwaran and Song Ilseom then let go of the reins they’d each been holding.

Of course, those weren’t their own reins. They belonged to the Seven Masters of Baekma Bang, who had been riding close beside them, boxed in on all sides.

“Thank you for trusting us.”

“I’m not completely trusting you yet, so there’s no need to thank me.”

That was what I said to Ma Junggeol, whose eyes were even welling up with tears. But my thoughts were different.

*No matter how I look at it, they’re not spies sent by Dark Heaven.*

When I first overheard their Sound Transmission, my suspicions had flared up again, after I’d set them aside for a while.

At first, anyway.

But now that I’d heard Ma Junggeol’s whole story, the suspicion in my heart had quietly turned into curiosity about someone.

The mysterious master Ma Junggeol and his sworn brothers revered as “the Lord.”

—What do you think?

Jeok Cheongang’s low Sound Transmission slipped into my ear.

I already knew what he meant, so I turned my gaze naturally toward the road ahead and answered.

—I’m not sure.

—Are you holding back? Or…

—I really don’t know. That person they call the Lord seems less suspicious than… strange. Unbelievably strange.

That wasn’t an exaggeration. The mysterious Supreme Peak master they called the Lord had appeared out of nowhere one day and wiped out a band of mounted bandits who’d escaped even the authorities’ control. He was a person shrouded in mystery.

*They said they didn’t know his name, where he came from, or anything else about him.*

The Seven Masters of Baekma Bang had been serving him for more than ten years.

Yet neither Ma Junggeol nor any of the Seven Masters knew who he was. And whenever they were pressed about it, they all gave much the same answer.

*“No, it’s all true. That’s just what he’s like!”*

*“Why would we dare lie to you? Please, you have to believe us.”*

*“You’ve already heard us talking, so you know he’s a bit—no, quite a bit—all over the place. Huh? His name and age? Don’t even ask. They’re different every time. Isn’t that right, Youngest?”*

*“The others are right. Chilbok, Gaettong… Was it three years ago? He thought he was a seventeen-year-old girl named Sohyang. We gave up trying after that.”*

*“We don’t know when he started living in Ningxia Province, either. He just suddenly appeared, subdued the whole area with his absurd divine might, then shut himself away in his residence and wouldn’t budge. He’s been like that for nearly ten years. I know it’s hard to believe, but it’s true.”*

The stories kept piling up, one after another, like sweet potato vines that kept coming no matter how many you pulled.

They were so absurd that, as I listened, I couldn’t help thinking:

*What the hell is that guy?*

Everyone had their own ambitions.

Regardless of whether they were good or bad, there was bound to be some goal a person had carried in their heart at least once.

But the Lord in their stories fit none of them.

He hadn’t taken over Ningxia and ruled as a mighty conqueror. Nor was he a notorious fiend who’d slipped into the frontier to hide his identity, or a hermit master wandering where no one would find him because he was nearing the end of his life.

*If he wanted to rule as a conqueror, there’d be no reason to hole up in a cave. If he were a fiend, he’d have tried his damnedest to keep his identity hidden—or from the start, he’d have put the mounted bandits under his command.*

If he were a hermit master, there wasn’t even much to think about.

Honestly, what kind of deranged hermit would choose the frontier, with its year-round high levels of fine dust and blowing yellow sand, over some remote mountain valley with beautiful scenery and clear water?

Even I knew the famous poet Paul Valéry. If he’d lived in Ningxia Province instead of France, he would’ve written, *The yellow dust is blowing. Fuck, I want to die.*

*And it wasn’t as if he were an old man gone senile, or a dying elder who didn’t need to seek out some remote mountain valley, either.*

According to the Seven Masters of Baekma Bang, the Lord rarely washed, and grime streamed from him, but his general appearance and voice seemed to belong to a man around middle age.

What’s more, when Ma Junggeol and his sworn brothers brought him liquor and food, he’d offer them a little instruction in return. He’d stay in his residence, then occasionally head out to town.

He said staying inside all the time was stifling. He wanted to get a little human company.

He must have wandered around so often that the Seven Masters didn’t even need to hide his identity for him to blend naturally into Ningxia Province.

Like Beggar Number One.

*This is a hermit master?*

Was this what it felt like to sink into a deep mire?

Just as my disbelief and curiosity kept growing the more I thought about it, Jeok Cheongang moved his lips. He’d clearly come to the same conclusion I had.

—In my long life, I’ve seen hundreds of carts’ worth of lunatics…but I’ve never seen anyone like this.

—You’ve only just started growing hair again.

—……Do you want to die?

—No. But I agree with what you said, Old Master. There’s no figuring him out.

—Could he be one of the Lord of Heaven’s minions?

—Of course he still has hands and feet left to command. But if you were the Lord of Heaven, would you put someone like that under you?

Jeok Cheongang answered without hesitation.

—Am I crazy?

—Right?

—Even if I took a Flame-Extinguishing Divine Fist to the head, I wouldn’t take a man like that as a subordinate. Of course, that’s assuming every word those vicious-looking bastards told us is true.

—But you already believe them.

—That’s…

His Sound Transmission faded as he turned his head without thinking.

As soon as their eyes met, the Seven Masters of Baekma Bang went rigid like statues. Jeok Cheongang shook his head.

—Yes, you’re right. I can tell they aren’t lying, either. No—they aren’t even capable of it.

That much seemed clear to me, and to everyone else as well.

But even if we concluded that they and their Lord posed no danger to our side, the two of us couldn’t make every decision on nothing but our own instincts.

—What are you going to do?

As Jeok Cheongang’s Sound Transmission slipped into my ear again, I considered it briefly and made up my mind. I gradually eased up on the reins and drew my horse level with the Seven Masters of Baekma Bang.

“W-why now? What is it this time…?”

Ma Junggeol and his sworn brothers were already frightened before I’d said a word.

I looked them over in silence, then suddenly asked:

“How long would it take?”

“What do you mean…?”

“To bring the person you call the Lord to our current destination.”

“……!”
```

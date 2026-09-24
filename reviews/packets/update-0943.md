<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0943.txt",
      "sha256": "daae432c691705244eab210edfffc53119e18d35f1df0b12b7c942900b9f1a67",
      "bytes": 12738
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fe30d35eff55582aae0c509f79ea5b8dddd81ab179d4040964f5c78ffe7f7b8b",
      "bytes": 2601
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bf5fc17b6bb6e8afe85dde4372e566811c088e0e074d1913c7f254ffd989efbb",
      "bytes": 233310
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "5e37222aa00adcf34820d2affea7b2a07e3b1bc2238c1ff9dda2007ba9c749e0",
      "bytes": 1445
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "71ae1a8e8dac25c27c234b83fe6a786b5026d033f8cff5f2de268f9be2714ad4",
      "bytes": 1204
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "3d050e6ec2543f7bfb5da5a6d88ede880fcf8f3671bf6b3e4c70e4aa8ed20a3b",
      "bytes": 973
    },
    {
      "path": "characters/Namho.md",
      "sha256": "244d629690afb348bda73ccdd2dfddd5f5bf1af2a4353ecee7382db69f0adfd8",
      "bytes": 973
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "bb659dd14f22bfd5d84c8f0d171b84428d84a67dce6766e9a49c04365a280577",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "7298b42e81adb275f71d8fd489fadb6673c39fb2eb2800f894ac5bab4a48dcfd",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "b02e0eacc7f3ee6221c7c393cea481f18b83424e77f640c6fd2c5313b7c61594",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "d3be605fa5679be80342c5e22b66ef25d7988a1f19911b1f384c682ab6334d92",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f66daa4bae985fcbafa7ec30ad9fc462f9834c125f917088f6bc22c9afe669f8",
      "bytes": 267309
    }
  ],
  "estimated_tokens": 12460
}
-->

# Durable State Update — Chapter 943

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
1 and safe_through 943. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 943. Profile updates may replace only one
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
  "chapter": 943,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 943,
    "continuity_sources": [943],
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
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician had said his vitality was at its limit and could not guarantee he would survive another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method is not yet explained.",
    "The old bamboo slip Taekyung gave the Divine Physician bears the names Maoshan Sect and White Illusion Jiangshi Art; its full significance is unknown.",
    "Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao.",
    "War against Dark Heaven has begun, and the imperial court is mobilizing after Taekyung warned of a possible invasion of Shanxi before the Double Ninth Festival.",
    "The Emperor appointed Taekyung Marquis of Shangshan and Thousand Captain, entrusting him with a thousand Embroidered Uniform Guards to fight the foreign enemy.",
    "Taekyung’s party is racing toward Shanxi; he decides to split the force after Deokcheong County so he and two companions can advance ahead of the main force.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "Taekyung’s System update reward is a durable pocket watch that appears broken and bears the faint inscription “A broken clock is right twice a day.”",
    "The Bow Saint says the Martial God chose her; she tested Taekyung to confirm he was the chosen one and assess his power and character."
  ],
  "continuity_sources": [
    942,
    941
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "Who sent the Shanxi Annihilation Plan missive, and when will Dark Heaven’s invasion begin?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 942,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 궁성     | **Bow Saint**                 | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 남궁세가   | **Nangong Family**               |
| 표국     | **Escort Bureau**                            |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 안휘     | **Anhui**              |
| 노부      | **this old man / I**                                            |
| 소협      | **Young Hero**                                                  |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 본단 | **League headquarters** | The League headquarters to which Hwang Tae-gu will be transported. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 절강 | **Zhejiang** | Region from which the boat travels east. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 진중 | **Jinzhong** | County included in Taekyung’s fief. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
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
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 940
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 940
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 942
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 930
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 930
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 930
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 930
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 937
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃943화



“말도 안 됩니다!”

내 짧은 설명이 끝나기 무섭게, 딱딱하게 굳은 얼굴로 외친 혁무진은 이내 한숨을 내쉬었다.

“하지만…… 젠장.”

말은 더 이상 이어지지 않았지만, 녀석이 현실을 인정했다는 것쯤은 이 자리의 모두가 느낄 수 있었다.

“다급한 마음에 앞만 보고 달려가다간 돌부리에 걸려 넘어지는 법. 저마다 안타까운 마음은 알지만, 지금으로서는 이것이 최선의 판단이다.”

남호가 진중한 표정으로 모두를 향해 말했다.

아마도 그가 캥거루 새끼마냥 태산의 품에 쏙 들어가 있지만 않았다면, 상당한 연륜과 무게감이 느껴졌을 말이었다.

“……아까부터 묻고 싶었는데, 도대체 왜 그러고 계세요?”

“이게 가장 편하니까.”

쓸데없이 단호하게 대답한 남호가 덧붙였다.

“뒷자리에 타면 엉덩이가 으스러질 것 같고, 이놈 어깨에 타면 일각에 한 번씩 나뭇가지에 얼굴을 얻어맞게 되지. 나 같은 늙은이는 산서성에 도착하기도 전에 죽고 말 거다.”

천연 가죽 소파 뺨치는 푹신한 허벅지를 가진 태산이가 고개를 끄덕였다.

“태산이, 남호 살린다.”

아니, 언제부터 저렇게 사이가 좋아졌지.

사뭇 비장하기까지 한 그 모습에 의문이 들던 그때, 흡족하게 웃은 남호가 행낭에서 무언가를 꺼내 들었다.

“기특한 놈 같으니. 입 벌려, 오향장육 들어간다.”

“오! 향! 장! 육!”

“…….”

그래, 어쩐지 이상하다 싶었다.

고개를 절레절레 내저은 나는 잠시 말고삐를 늦추며 입을 열었다.

“남 노인께서는 절강성을 벗어나는 즉시 무림맹과 접선해 주십시오. 그쪽에서도 나름의 준비를 하고 있을 겁니다.”

“노부 역시 그럴 생각이었네. 지금으로서는 짐만 될 것이 뻔하니, 되도록 지원군을 이끌고 후발대로 향하지.”

황도가 자리 잡은 절강성의 경우에는 문파는커녕 무림인조차 찾아볼 수 없는 상황.

그러나 산서성으로 향하는 경로에 있는 안휘(安徽)와 하남(河南)이라면 이야기가 다르다.

무림맹 본단이 위치한 하남은 말할 것도 없고, 현재의 위치에서 가장 가까운 곳에는 남궁세가(南宮世家)라는 거목이 버티고 있으니.

“일섬. 마표.”

내 부름에 말을 몰아 가까이 다가온 송일섬과 사마표가 차례대로 대답했다.

“듣고 있다. 각주.”

“몇 번째 말하는지 모르겠지만, 사마는 이름이 아니라 성씨니까 다음에 부를 때는…….”

“알아, 일부러 그런 거야.”

내 단호한 대답에 사마표가 혼잣말처럼 중얼거렸다.

“그래, 어쩐지 그런 것 같더군.”

“됐고, 각자 해야 할 일은 알고 있으리라 믿는다.”

송일섬과 사마표.

젊은 나이임에도 뛰어난 무위를 지닌 두 사람은 무겁게 고개를 끄덕였다.

“물론이다.”

“우리를 믿어라. 설령 도중에 어떠한 불상사가 생기더라도, 아무런 문제 없이 산서성까지 모두를 데려가지.”

그리고 나는 결연한 목소리로 대답하는 두 사람을 향해 이렇게 말했다.

“둘이 싸우지 마.”

“……!”

“……!”

“금의위들 보기 쪽팔리니까 투닥거리지 말라고. 알겠어?”

“…….”

“…….”

“대답.”

짜게 식은 눈빛으로 나를 바라보던 두 사람이 곧 실소를 흘렸다. 지금 내가 건네는 말이 그저 농담에 지나지 않는다는 사실을, 녀석들 또한 누구보다 잘 알고 있었다.

“알겠다.”

“노력해 보지.”

“들었냐, 무진아?”

나를 물끄러미 바라보고 있던 혁무진이 말없이 고개를 끄덕였다.

현실을 알기에 더 이상 뭐라 말하지는 않았지만, 착잡한 표정에서는 숨길 수 없는 감정이 느껴졌다.

망설임 없이 자신을 떼놓고 떠나는 나를 향한 섭섭함과, 현재의 상황에서는 짐밖에 되지 못하는 스스로를 향한 분노가.

“죽상하고 있지 마. 안 그래도 못생긴 얼굴, 더 못생겨 보이니까.”

피식 웃으며 건넨 말에, 혁무진의 얼굴이 한층 더 어두워졌다.

“그것뿐입니까?”

“응?”

“저한테는…… 왜 아무것도 부탁하지 않으십니까.”

순간 시종일관 애써 끌어올리고 있던 입꼬리가 느슨하게 늘어졌다.

생각지도 못한 물음이었기에 놀랐고, 한편으로는 당황할 수밖에 없었다.

이런 생각을 할 줄은 몰랐으니까.

그리고 아주 잠시, 녀석을 물끄러미 바라보던 나는 이내 담담하게 입을 열었다.

“따로 무언가를 부탁하지 않아도, 넌 알아서 잘 해낼 테니까.”

“……!”

“네게 있어 산서성은 일평생을 살아온 고향이고, 태원진가는 두 번째 집이지. 지금 네 마음이 어떨지는 충분히 알아.”

나를 바라보는 혁무진의 눈동자가 파르르 떨렸다.

우득.

새하얗게 물들어 가는 두 주먹.

한껏 힘이 들어가 금방이라도 찢겨 나갈 것 같은 말고삐를 노려보며, 혁무진이 작은 목소리로 뇌까렸다.

“조장님은 모르실 겁니다. 반드시 지켜야 할 것이 있음에도, 나설 만한 힘이 없어 무력하게 바라만 보고 있어야만 하는 제 마음을.”

“……뭐?”

“아니, 아닙니다. 괜한 헛소리를 했네요. 지금 가장 힘드신 건 조장님이실 텐데…… 진심으로 사죄드립니다.”

나는 붉어진 얼굴로 고개를 푹 숙인 녀석을 말없이 응시했다.

말해 주고 싶었다.

그 마음, 나 역시 잘 알고 있다고.

영혼이 조각 나고 뼈마디가 으스러질 만큼 똑똑히 느꼈었다고.

하지만, 혀끝에 맴도는 그 진심을 나는 끝끝내 입 밖으로 토해 내지 못했다.

때때로 강자의 위로는 약자에게 있어 무력감보다 더한 비참함을 안겨 주는 법이니까.

더불어 힘이 있음에도 지킬 수 없는 것이 있다는 잔인한 현실 역시, 지금의 혁무진에게는 와닿지 못하는 진실일 테니까.

그렇기에 내가 할 수 있는 유일한 일은, 부끄러움과 죄스러움에 휩싸여 고개를 들지 못하는 녀석에게 짧은 한마디를 건네는 것뿐이었다.

“믿는다. 누구보다.”

“……조장님.”

“산서에서, 아니 태원진가에서 다시 보자.”

툭.

잘게 떨리는 혁무진의 어깨를 두드려주는 것으로 인사를 대신한 뒤, 나는 박차를 가해 앞으로 나아갔다.

그리고 유난히도 서늘해진 듯한 바람을 느끼며 말고삐를 말아쥔 그때, 다가오는 말발굽 소리와 함께 나직한 목소리가 귓가를 울렸다.

“혁 소협이 했던 말…… 진심이 아니었을 거예요.”

가까워진 것은 말발굽 소리만이 아니다.

어디선가 전해지는 꽃내음을 맡으며, 나는 애써 미소지었다.

“알고 있습니다.”

“혹시 그거 알아요?”

“무슨.”

의아함을 느끼며 고개를 돌린 내 시야에, 담담한 표정을 한 주화란이 들어왔다.

그녀의 나직한 목소리도 함께.

“어떤 종류의 웃음은, 때로 위태로워 보이기까지 한다는 거.”

“……!”

“저도 함께 가고 싶은 마음은 굴뚝 같지만, 짐이 될 수는 없으니 괜한 투정 부리진 않을게요. 하지만 그래도…….”

주화란이 웃었다.

마치 하늘 위에서 쏟아지는 달빛처럼.

“다음에 봤을 때는, 진심으로 웃으면서 봐요. 우리.”

나는 말 없이 그런 그녀를 바라보다가, 문득 입을 열었다.

“그렇게 될 겁니다. 반드시.”

그리고 다음 순간, 한 치의 망설임도 없이 말안장을 박차고 뛰어올랐다.

슈확!

서늘하다. 세찬 바람에 머리카락이 흩날린다.

전신을 휘감은 부유감(浮游感)과 함께 드높은 허공으로 도약한 내 뒤를, 희끄무레한 두 인영이 어스름한 달빛을 해치며 좇았다.

“자, 서두르자고.”

낮게 가라앉은 적천강의 목소리에 궁성이 조용히 고개를 끄덕인다.

나, 아니 우리는 말발굽이 허락되지 않는 험준한 산맥을 향해 쏘아졌다.

쐐애애액!



* * *



“거 참, 희한하네.”

불쑥 들려온 동료의 혼잣말에, 나무에 기대어 꾸벅꾸벅 졸고 있던 산적이 눈을 게슴츠레하게 떴다.

“갑자기 뭐가.”

막 선잠에서 깼으니 태도가 상냥할 리는 없다.

열 살도 넘게 차이 나는 선배 산적의 퉁명스러운 목소리에, 동료는 마른침을 꿀꺽 삼켰다.

“별건 아닙니다요. 그냥 계속 있다 보니 뭔가 이상해서…….”

“이상한 점? 딱히 모르겠는데.”

산적이 고개를 갸웃거리던 그때. 동료가 하늘을 가리키며 말을 이었다.

“오늘따라 새들이 통 안 보여요. 아주 쥐 죽은 듯이 조용한 게, 왠지 좀 찝찝하지 않습니까?”

“어?”

눈을 동그랗게 뜬 산적은 그제야 주위를 유심히 둘러보았다.

그러고 보니 정말 그랬다.

텅 빈 하늘은 물론이고, 사방에 펼쳐진 울창한 숲에서 쉬지 않고 울려 퍼졌어야 할 새들의 울음소리도 들리지 않았다.

‘뭐지?’

순간 머릿속을 스친 의문.

그러나 산적은 이내 심드렁한 얼굴이 되었다.

그깟 날짐승 몇 마리 안 보인다고 뭐가 달라진단 말인가.

말이 산적이지, 그들은 어차피 말단 졸개다.

각자가 맡은 구역에서 눈깔이 빠지도록 산길을 감시하다가 손님이 오면 산채(山寨)에 연락을 취하는 것이 유일한 역할이었다.

“매라도 나타났나 보지 뭐. 눈 깜짝할 새에 채여 잡아 먹히기는 싫으니 저것들도 입 닥치고 있는 거다.”

“어, 그러고 보니 아까 매가 몇 마리 지나가긴 했습니다.”

“아까? 아까 언제?”

“글쎄요. 한 시진 전쯤? 네댓 마리가 아주 그냥 쏜살같이 날아가지 뭡니까.”

아무래도 자고 있느라 못 봤던 모양이다.

산적은 덥수룩한 턱수염을 쓰다듬으며 중얼거렸다.

“그건 좀 희한하긴 하구먼. 그놈들은 워낙 제멋대로라 무리를 지어 이동하는 건 거의 못 봤는데.”

“그럼 산채에 보고할까요?”

“보고? 산채에?”

“예. 부두령님께서 조금이라도 이상한 점이 보이면 바로 보고하라고 하셨잖습니까.”

“나쁘지 않지. 산 채로 썰리는 게 소원이라면.”

“…….”

“지금쯤이면 한숨 늘어지게 자고 있을 텐데, 깨워 봤자 좋은 꼴 못 본다. 고작 그딴 일로 깨웠다간 도끼나 날아오지.”

흐아암.

늘어지게 하품을 한 산적은 짙은 그늘에 팔다리를 쭉 펴고 드러누웠다.

어젯밤의 숙취가 남아 있는 상태에서 나무에 기대어 선잠을 잤더니 몸이 뻐근하다. 이참에는 아예 허리가 아프도록 푹 자 볼 생각이었다.

아직 열의가 넘치는 젊은 동료에게 모든 것을 맡긴 채.

“괜히 용쓰지 말고 사람이나 봐라. 사람이나.”

중양절이 얼마 남지 않은 지금, 큰 건수를 노리는 것은 상인들뿐만이 아니다.

떡이 크면 떡고물도 많다.

제법 규모 있는 상단이나 표국의 행렬을 잘만 노린다면, 이를 통해 벌어들인 통행료만으로도 산채의 곳간이 넉넉해질 것은 자명한 사실이었다.

바로 지금처럼.

“오, 옵니다! 온다고요!”

“뭐. 뭐?”

와락!

촌각도 흐르기 전에 울려 퍼진 동료의 숨죽인 외침에, 무언가에 튕겨지듯 벌떡 일어난 산적은 허겁지겁 도끼를 쥐었다.

잠기운은 이미 사라진 지 오래다.

그늘진 산길을 노려보는 그의 시선은 매의 그것처럼 빛나고 있었다.

“산채에 연락해. 어서!”

“예, 옛!”

헐레벌떡 떠나는 동료의 뒷모습을 힐끗 바라본 산적은 가늘어진 눈매로 산길을 응시했다.

보인다. 확실하게.

천천히 흔들리는 몇 개의 깃발이.

그리고 수십이나 되는 인기척이.

‘저 덜떨어진 놈이 이번에는 제대로 잡았군.’

내심 중얼거린 산적은 나뭇가지 사이로 스치는 깃발을 유심히 살폈다.

그리고 그 검푸른 비단에 친절하게 쓰인, 이 먹음직스러운 손님들의 정체를 보았다.

대남궁세가(大南宮世家).

“……!”
```

## Final English reading copy

```markdown
# Chapter 943

“You can’t be serious!”

The moment my brief explanation ended, Hyuk Mujin cried out, his face stiff with shock. Then he let out a sigh.

“But… damn it.”

He said no more, but everyone here could tell he’d accepted reality.

“If you charge ahead in your haste, you’ll trip over a rock. I know everyone’s upset, but for now, this is the best decision.”

Namho addressed everyone with a serious expression.

It might have sounded like a speech from a seasoned elder—if he hadn’t been tucked into Taishan’s arms like a baby kangaroo.

“…I’ve been meaning to ask. Why are you sitting like that?”

“This is the most comfortable.”

Namho answered with unnecessary firmness, then added,

“If I ride in the back, my ass feels like it’s going to get crushed. If I sit on this fellow’s shoulder, I get smacked in the face by a branch every fifteen minutes. An old man like me would be dead before we even reached Shanxi Province.”

Taishan, whose thighs were softer than a leather sofa, nodded.

“Taishan save Namho.”

Since when had those two gotten so close?

I was still wondering why Taishan looked downright solemn when Namho smiled with satisfaction and pulled something from his pack.

“You’re a good boy. Open wide. Five-spice pork coming in.”

“Oh! Five! Spice! Pork!”

“…”

Right. I’d been wondering why something felt off.

I shook my head and eased my horse’s pace for a moment before speaking.

“Elder Namho, please make contact with the Murim Alliance as soon as you leave Zhejiang Province. They’ll be making preparations of their own.”

“I intended to do that anyway. As things stand, I’d only be a burden. I’ll try to lead the reinforcements and follow behind you.”

There wasn’t a single martial artist to be found in Zhejiang Province, where the imperial capital stood—not even a sect.

But Anhui and Henan, which lay along our route to Shanxi Province, were another matter.

Henan was home to the Murim Alliance headquarters, of course. And the great tree closest to our current position was the Nangong Family.

“Ilseom. Ma Pyo.”

At my call, Song Ilseom and Sama Pyo rode over and answered in turn.

“I’m listening, Pavilion Master.”

“I’ve lost count of how many times I’ve said this, but Sama is your surname, not your given name. Next time you call me…”

“I know. I’m doing it on purpose.”

At my firm reply, Sama Pyo muttered as if to himself,

“Yeah, I thought that might be the case.”

“Enough. I trust you both know what you have to do.”

Song Ilseom and Sama Pyo.

Despite their youth, both were formidable martial artists. They nodded solemnly.

“Of course.”

“Trust us. Even if something goes wrong along the way, we’ll get everyone to Shanxi Province without a problem.”

I answered their determined assurances with,

“Don’t fight with each other.”

“…”

“…”

“Don’t start bickering in front of the Embroidered Uniform Guards. It’s embarrassing. Got it?”

“…”

“…”

“Answer me.”

The two of them stared at me with flat expressions, then let out quiet laughs. They both knew better than anyone that I was only joking.

“Understood.”

“I’ll try.”

“Did you hear that, Mujin?”

Hyuk Mujin, who’d been watching me in silence, gave a small nod.

He understood the situation and didn’t say anything more, but there was no hiding the emotions in his troubled expression.

His resentment toward me for leaving him behind without hesitation, and his anger at himself for being nothing but a burden in the current situation.

“Quit looking so miserable. Your face is ugly enough already—you’re making it look even worse.”

I gave him a wry laugh. Hyuk Mujin’s expression darkened further.

“Is that all?”

“Hm?”

“Why… haven’t you asked me to do anything?”

The smile I’d been forcing onto my face loosened.

The question caught me by surprise—and, in a way, left me at a loss.

I hadn’t expected him to think of it that way.

After looking at him in silence for a moment, I answered calmly.

“Because even without me asking, you’ll do just fine on your own.”

“…”

“Shanxi Province is where you’ve lived your whole life, and the Jin Family of Taiyuan is your second home. I know well enough how you feel right now.”

Hyuk Mujin’s eyes trembled as he looked at me.

Crack.

His fists were turning white.

He glared at the reins, pulled so taut they looked ready to snap, and muttered in a quiet voice,

“Captain, you wouldn’t understand. What it feels like to have something you must protect, but not the strength to step in—to be left helpless, just watching.”

“…What?”

“No, forget it. I said something stupid. You’re the one who has it hardest right now… I sincerely apologize.”

I silently watched him bow his head, his face red.

I wanted to tell him:

I understood that feeling, too.

I’d felt it all too clearly—as my soul shattered and every bone in my body broke.

But I couldn’t bring myself to let the truth on the tip of my tongue escape.

Sometimes, comfort from the strong can make the weak feel even more powerless and wretched.

And the cruel truth that you can still fail to protect something even when you have the strength to fight—that was something Hyuk Mujin couldn’t understand yet.

So the only thing I could do was offer one short line to the man who couldn’t lift his head, weighed down by shame and guilt.

“I trust you. More than anyone.”

“…Captain.”

“I’ll see you in Shanxi—or rather, at the Jin Family of Taiyuan.”

Pat.

I patted his trembling shoulder in farewell, then kicked my horse forward.

The wind felt colder than before. I tightened my grip on the reins, and hoofbeats approached. A quiet voice reached my ears.

“Young Hero Hyuk didn’t mean what he said.”

It wasn’t just the hoofbeats drawing closer.

I caught the scent of flowers drifting from somewhere and managed a smile.

“I know.”

“Do you know something?”

“What?”

I turned, puzzled, and saw Ju Hwaran beside me, her expression calm.

Her voice was just as quiet.

“Some kinds of smiles can look so fragile they almost seem ready to break.”

“…”

“I want more than anything to go with you, too, but I know I’d only be a burden, so I won’t complain. Still…”

Ju Hwaran smiled.

Like moonlight spilling down from the sky.

“When we meet again, let’s meet with genuine smiles. Both of us.”

I watched her in silence, then suddenly spoke.

“That’s exactly what we’ll do. I promise.”

And in the next instant, I sprang from the saddle without a moment’s hesitation.

Whoosh!

Cold. The fierce wind whipped my hair around.

As a weightless feeling swept over me and I leapt high into the air, two pale figures followed behind, chasing me through the hazy moonlight.

“Come on. Let’s hurry.”

At Jeok Cheongang’s low voice, the Bow Saint quietly nodded.

I—or rather, we—shot toward the rugged mountain range where no horse could travel.

* * *

“Well, that’s strange.”

At the sudden mutter from his companion, the bandit leaning against a tree and nodding off opened his eyes to a slit.

“What is?”

He’d just woken from a light sleep. There was no reason he’d be in a good mood.

At the brusque voice of a senior bandit more than ten years his elder, his companion swallowed nervously.

“It’s nothing, sir. It’s just… the longer I’ve been here, the more something’s felt off.”

“Something’s off? I don’t see anything.”

The bandit tilted his head. His companion pointed up at the sky and continued.

“I haven’t seen any birds all day. It’s dead quiet. Doesn’t it feel a little unsettling?”

“Huh?”

The bandit’s eyes widened. Only then did he take a careful look around.

Now that he thought about it, it was true.

The sky was empty. And from the dense forest stretching in every direction, there wasn’t a single birdsong—though it should have been full of them.

*What’s going on?*

The question flashed through his mind.

But his face soon settled into indifference.

What difference would it make if a few birds were missing?

They called themselves bandits, but in the end, they were nothing but low-ranking thugs.

Their only job was to keep watch over their assigned stretch of mountain road until their eyes popped, and contact the mountain stronghold if any travelers showed up.

“Maybe a hawk came around. Those birds don’t want to get snatched up and eaten in the blink of an eye, so they’re keeping their beaks shut.”

“Oh, come to think of it, I did see a few hawks fly by earlier.”

“Earlier? When?”

“About two hours ago, I think. Four or five of them, flying like arrows.”

The bandit must have missed them while he was asleep.

He stroked his shaggy beard and muttered,

“That is a little strange. Those birds do whatever they want. I’ve hardly ever seen them travel in a flock.”

“Should I report it to the stronghold?”

“Report it? To the stronghold?”

“Yes. The deputy chief said we should report anything unusual right away.”

“Not a bad idea. If you’re hoping to get chopped up alive.”

“…”

“The deputy chief’s probably fast asleep by now. Wake him, and you won’t like what happens. Disturb him over something like that and he might throw an axe at you.”

The bandit let out a long yawn and sprawled out beneath the deep shade, stretching his arms and legs.

He’d slept sitting against a tree with last night’s hangover still weighing on him. His body was stiff. This time, he planned to sleep so soundly his back would hurt.

He left everything to his young companion, who still had plenty of enthusiasm.

“Quit straining yourself. Just keep an eye out for people. People.”

With the Double Ninth Festival coming up, merchants weren’t the only ones looking to score big.

The bigger the haul, the bigger the crumbs.

If they picked the right caravan—one belonging to a sizable trading company or Escort Bureau—the tolls alone would be enough to fill the stronghold’s storehouse.

Just like now.

“They’re—they’re coming!”

“What? What?”

Wham!

At his companion’s hushed cry, which rang out barely a moment later, the bandit sprang up as if he’d been launched from a catapult and grabbed his axe in a panic.

The sleep was gone from his eyes.

His gaze fixed on the shadowed mountain path, shining like a hawk’s.

“Contact the stronghold. Hurry!”

“Y-Yes, sir!”

The bandit glanced after his companion as he ran off, then narrowed his eyes at the mountain road.

He could see them. Clearly.

A few flags, swaying slowly.

And he could sense dozens of people.

*That idiot finally got one right.*

The bandit studied the flags fluttering between the branches.

Then he read the helpful lettering on the dark blue silk and learned the identity of these mouthwatering guests.

The Great Nangong Family.

“…”
```

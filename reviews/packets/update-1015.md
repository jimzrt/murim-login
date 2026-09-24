<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1015.txt",
      "sha256": "fc7ee7a11a1d4daf6211ff97bd073fa5cfd06f65068ea3fc33bbd9cdc87c3856",
      "bytes": 13924
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bc5cb7d989c39c22cf216708dc56bbbcc014ad2c54b96ff3f03d15951bc384fd",
      "bytes": 1276
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e6e846ce6a2a615d7cff75488953a6c3e58a154e06b2f4c847bc3eec831d825b",
      "bytes": 238137
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "9a76f9ecf355943d830ea23f7424c51ca050a05384f8b935c180f783d6c4ea2b",
      "bytes": 760
    },
    {
      "path": "characters/Heo Jun.md",
      "sha256": "efd0202d64c02b898d1f59ae471b285d21da1a8ad8ef3dba0b51fc97fc3d73b0",
      "bytes": 716
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "91f8a53de51a1cba324139427b47497ef18aad417aaf033b89c13131052c61c4",
      "bytes": 1375
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "a4986a215150466cc5ac49e772312c8242b5202b3fdeb4b34e0170575832f19c",
      "bytes": 974
    },
    {
      "path": "characters/Namho.md",
      "sha256": "e06a7e2dec25eb7f471693f695a7e658ba729f2354ad01b0f3c1a5999be87738",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "afd5639c3d24144f01cbabaa65e049e6d8f6a3895eb4998444cf96f5d4e6d3c5",
      "bytes": 904
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "9a49602203e5cab9bb43438d8c361eb83c42df062448325290cb12d844d9ca77",
      "bytes": 742
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "9ec8f7264da2ade9fb343707269adc8672056a6f58cb89c9d761d782c084301a",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "9c01298f57050e4f126f01ee76d0fb87dc991f80ce4ce0b2d97ed0392b4ac3ca",
      "bytes": 686
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "cb295d54ac2a266ccad7518c77a359b39bebc45ed6941b2d9ea4d81f0af66872",
      "bytes": 2458
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ea4fa708d06a7ed84ec51073f216e02313b8909ae07dc5283532587a5cce86e1",
      "bytes": 276773
    }
  ],
  "estimated_tokens": 12751
}
-->

# Durable State Update — Chapter 1015

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
1 and safe_through 1015. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1015. Profile updates may replace only one
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
  "chapter": 1015,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1015,
    "continuity_sources": [1015],
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
    "The Lord advised Ma Junggeol and his sworn brothers for more than ten years, helped them form Baekma Bang, and supported their western trade route.",
    "Six of the Seven Masters left to fetch the Lord within five days of the march’s halt; Ma Junggeol remains with Taekyung’s group.",
    "Namho has an important matter he says he can only disclose to Taekyung now.",
    "Sama Pyo disobeyed Sima Gong’s order to return to Gansu, accepted responsibility, and is now riding back to the Black Dragon Demon Gate.",
    "Sima Gong ordered that two martial artists be dealt with for making a taboo remark about Sama Pyo’s succession."
  ],
  "continuity_sources": [
    1014
  ],
  "open_questions": [
    "Who is the Lord, and what are his motives and connection, if any, to Dark Heaven?",
    "Will the six Baekma Bang men return with the Lord within Taekyung’s deadline?",
    "What does Namho need to tell Taekyung, and why can he only tell him now?",
    "What is Dark Heaven’s full strength and objective in the western desert, and have its forces begun advancing?",
    "What consequences, if any, will Sama Pyo face for disobeying Sima Gong’s order?"
  ],
  "safe_through": 1014,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 허준     | **Heo Jun**        |
| 월화     | **Wolhwa**         |
| 태원진가   | **Jin Family of Taiyuan**        |
| 하오문    | **Lower District Sect**          |
| 종남파    | **Zhongnan Sect**                |
| 암천     | **Dark Heaven**                  |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 중원     | **Central Plains**                               |                                                       |
| 지부장    | **Branch Leader**                            |
| 표국     | **Escort Bureau**                            |
| 총표두    | **Chief Escort**                             |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 태을무정검 | **Taeeul Merciless Sword** | Title of the Zhongnan Sect’s Second Martial Uncle, who is in Xi’an. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 하오문도 | **Lower District Sect member** | Member of the Lower District Sect. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 기련산 | **Qilian Mountains** | Mountain range in Qinghai from which the Qilian Three Fiends emerged. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 황하 | **Yellow River** | River along which civilization began. |
| 상호 | **Sangho** | Go Se-won's young son. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 종남 | **Zhongnan Sect** | Orthodox faction that fought in the historic battle. |
| 천수 | **Tianshui** | City on Gansu’s eastern edge, bordering Shaanxi. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 주화란 | 허준 | niece_to_uncle | Uncle Heo | formal-polite | Hwaran addresses her uncle and Chief Escort as 허 숙부. |
| 허준 | 주화란 | uncle_to_niece | Hwaran; Young Bureau Head | concerned-familiar and commanding | Heo Jun calls her 화란아 and orders the escorts to protect the Young Bureau Head. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
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
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1014
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Heo Jun.md

# Heo Jun (허준)

- **Safe through:** Chapter 801
- **Aliases:** Uncle Heo, Chief Escort
- **Role:** Former Chief Escort of the Yongbong Escort Bureau and Ju Hwaran's uncle, Heo Jun secretly colluded with Zhongnan for two years before Ju Hwaran exposed his betrayal and killed him with a sword strike.
- **Personality:** Deceitful, greedy, manipulative, and fiercely self-preserving beneath a long-maintained paternal facade.
- **Voice:** Formal, paternal, calm, and quietly reassuring.
- **Relationships:** He is Ju Hwaran's uncle and former Chief Escort, but his two-year betrayal of her and the Yongbong Escort Bureau has shattered their bond.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1012
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1012
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1013
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1014
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1012
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1012
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1014
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 1004
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear; has negotiated a mutually beneficial alliance with Jin Wikyung and the Jin Family

## Korean source

```text
＃1015화



아군의 머릿수는 물경 삼천에 달했지만, 그들 한 사람 한 사람이 무림인인 만큼 그 이동 속도는 일반적인 상식을 훌쩍 뛰어넘었다.

동쪽 끝자락에 위치한 천수(天水)에서 출발한 지 단 이틀 만에, 감숙성의 성도인 난주(蘭州)를 지나 거침없이 진격하고 있었으니까.

아마도 그즈음이었을 것이다.

어느 순간 서늘하기 그지없는 고원(高原)과 드넓은 광야가 사라지고, 좌우로 크고 작은 돌산이 늘어선 좁은 길이 모습을 드러낸 것은.

‘이곳은…….’

잠시 현대를 떠나 무림을 종횡하다 보면 종종 그럴 때가 있다.

인간의 손이 닿지 않은, 아득한 세월을 고스란히 간직한 자연의 장엄함에 잠시나마 압도될 때가.

그리고 내가 잠시 말고삐를 놓고 고원 아래 끝없이 펼쳐진 풍경을 말없이 바라보던 그때, 나직한 목소리가 귓가에 닿았다.

“하서주랑(河西柱廊)이에요. 복도와 같은 형태로 황하 서쪽을 향한다고 해서 붙여진 명칭이죠. 누가 처음 그렇게 부르기 시작했는지는 몰라도, 퍽 어울리지 않나요?”

그 말에 공감하는 것과는 별개로, 목소리의 주인을 구분하는 것은 쉬운 일이었다.

굳이 사마표와 태산이 자리를 비우지 않았더라도 마찬가지였을 것이다.

내 주위에 이렇게 싱그럽고 맑은 음성의 소유자는 오직 한 사람뿐이니까.

“역시 잘 알고 계시네요. 주 소저는.”

내 대답에 주화란이 쑥스럽게 웃었다.

“저한테는 당연한 일인걸요. 비록 기간이 그리 길지는 않았지만 임시로 표국을 이끈 적도 있고, 명색이 표왕(鏢王)의 손녀인데.”

얼핏 들으면 맞는 말이지만, 겸양이기도 하다.

무가의 핏줄이라고 꼭 무공을 익히라는 법은 없듯이, 주화란 역시 구태여 가업(家業)을 이을 필요는 없었을 테니까.

그렇기에 그녀가 중원의 지리와 관련 지식에 능통할 수 있었던 건, 순전히 본연의 노력 때문이다.

‘그러고 보니 처음 용봉표국도 태원진가와 별반 다를 것 없는 상황이었지.’

한때의 영광을 뒤로한 채, 몰락의 길에 접어든 가문.

얼마 안 되는 차이점이 있다면 아들 셋으로 고추 파티를 벌인 태원진가와 달리 주화란은 무남독녀였으며, 그만큼 더 무거운 짐을 홀로 짊어져야 했다는 것이다.

‘물론, 앓아누운 상태였긴 해도 이쪽과는 달리 아버지인 국주가 있었지만.’

어디까지나 스쳐 지나간 과거의 이야기다.

용봉표국의 국주는 원기(元氣)를 회복하여 일선으로 복귀했고, 내가 태을무정검을 족치며 역으로 뜯어낸 막대한 액수의 금자는 서서히 무너져 가던 가문을 일으켜 세우고도 남았다.

모용세가, 아니 모용가의 공백을 메우며 새롭게 오대세가(五大世家)의 반열에 오른 태원진가야 말할 것도 없고.

‘암천의 존재만 아니었더라면, 이쯤에서 모두가 행복한 해피 엔딩으로 마무리 지을 수 있었을 텐데.’

그러나 현실은 외면하는 것이 아니라 직시해야 하는 것이고, 기회란 늘 위기 속에서 찾아오는 법이다.

그렇기에 주화란과 용봉표국도, 나와 태원진가도 위기를 극복하며 한층 더 성장할 수 있었다.

다만 그 과정에서 수많은 희생을 치렀고, 앞으로도 그럴 수밖에 없다는 사실이 가슴 한구석을 무겁게 짓누를 뿐이었다.

더불어…….

‘아니, 아니다. 지금 당장은 여기까지만.’

나는 바로 하루 전, 평소와 달리 한껏 굳은 얼굴을 한 채 다가왔던 남호의 모습을 뇌리에서 털어 냈다.

아직도 귓가에 맴도는 듯한 그의 나지막한 목소리도 함께.

그리고 어느샌가 걱정스러운 눈빛으로 나를 바라보고 있던 주화란을 향해 애써 아무렇지 않게 웃어 보였다.

“아, 미안해요. 그냥…… 그냥 잠깐 고민되는 일이 있어서.”

“아니에요. 이해해요. 곧 있을 전투 때문에 심란하실 텐데.”

이걸 뭐라고 해야 하나.

확신할 수도 없는 이야기를 곧이곧대로 털어놓을 수도 없고.

다시 말 머리를 나란히 한 채 달리는 주화란의 옆모습을 말없이 응시하던 나는, 반쯤 충동적으로 입을 열었다.

“당연히 그런 것도 있지만, 관계에 대한 고민도 있어서요.”

“관계라면?”

“사람 간의 관계요. 누군가와의 믿음, 바람. 뭐 그런 것들.”

나는 고개를 들어 저 멀리, 돌산들 사이의 좁은 길을 향해 물밀듯이 쏟아지는 수천의 아군을 바라보며 말을 이었다.

“뭐 하나 쉬운 게 없다지만, 저는 이런 게 특히 어렵더라고요. 사람과 사람 사이의 교감이나 감정 같은 거.”

“교감과 감정…….”

혼잣말처럼 뇌까린 주화란이 나직하게 덧붙였다.

“뭔지 알 것 같네요. 그 기분.”

“아마 이해할 것 같았어요. 주 소저라면.”

직접 겪었으니 그럴 수밖에.

아직도 똑똑히 기억한다.

주화란이 과거 종남파와의 분쟁 당시, 암중의 배신자였던 총표두 허준을 자신의 손으로 직접 베었던 것을.

‘그래도 한때는 친 숙부처럼 따랐다고 했으니, 그때의 상처는 지금도 마음에 남아있겠지.’

사람 간의 관계는 그래서 어렵다.

상대방에게 한 가지를 선뜻 건네주어도, 그만큼을 돌려받을 수 있을지 없을지 혹은 그 이상이 되돌아올지는 아무도 모른다.

‘지금의 나도, 그래서 더욱 망설여지는 거고.’

하지만 다음 순간 주화란이 불쑥 던진 한마디는, 또다시 슬금슬금 기어 올라오던 마음속의 고민을 말끔히 몰아내기에 충분했다.

“월화, 맞죠?”

“예…… 예?”

반사적으로 수긍할 뻔한 나는 끔뻑거리는 눈으로 주화란을 바라보았다.

뭐지? 지금, 내가 지금 뭔가 잘못 들은 건가?

“그, 죄송한데 방금 뭐라고 하셨습니까?”

주화란이 고개를 돌리지 않은 채 대답했다.

“월화라는 분이요. 하오문 섬서 지부장. 아닌가요?”

“예. 맞죠.”

“그러니까요.”

“아니, 저는 월화가 섬서 지부장이 맞는다는 뜻으로 말씀드린 건데요.”

“그래요?”

“네.”

“그리고요?”

“네?”

“아니에요.”

도대체 이게 무슨 대화지.

순간 할 말을 잃은 내가 멀뚱멀뚱 주화란을 바라보던 그때였다.

힘차게 내달리는 말발굽 소리를 뚫고 들려올 만큼 격렬한 기침이 울려 퍼진 것은.

“쿨럭! 쿨럭! 쿨러어어억!”

저 자식은 또 갑자기 왜 저래.

흔들리는 말안장 위에서 거의 발작을 일으키고 있는 혁무진에게 한마디 하기 위해 등 뒤를 쳐다본 순간, 나는 똑똑히 볼 수 있었다.

필사적으로 고개를 내젓는 혁무진과, 녀석의 좌우에서 딱하다는 눈빛으로 나를 바라보고 있는 남호와 송일섬의 모습을.

그리고 동시에, 불현듯 떠오른 어떤 짐작이 뇌리를 스쳤다.

음.

으음.

이거 설마, 내가 생각하는 그런 건가.

‘지금 같은 상황에서는 썩 좋은 타이밍은 아닌데.’

그래도, 쓸데없는 오해는 풀어야지.

나는 살짝 묘해지는 기분을 느끼며 잠시 닫았던 입술을 뗐다.

“어, 주 소저?”

“네. 말씀하세요.”

저 앞에 가문의 원수라도 발견했는지, 여전히 꼿꼿하게 정면을 주시하고 있는 시선.

더불어 그와는 별개로 어느새 쫑긋 세워진 귀.

그런 주화란의 모습에, 나는 괜히 간지럽지도 않은 턱을 긁적였다.

“뭐, 이건 딱히 궁금하시진 않겠지만 그냥 드리는 말씀인데요.”

“맞아요. 딱히 궁금하지는 않지만, 그냥 들어 볼게요.”

“저, 월화랑 별로 안 친해요.”

“…….”

“아니 뭐, 어느 정도의 왕래는 있었죠. 겨우 일이 년 전만 하더라도 섬서가 아니라 산서 지부장이었거든요. 하오문과는 이래저래 상호 간의 거래로 얽힌 부분도 있었고, 여하튼 그렇게 안면이 좀 있죠.”

잠시 침묵하던 주화란이 입을 열었다.

“별로 안 친한 것치고는 말을 편하게 하시네요. 이름도 막 함부로 부르시고.”

“큰 오해를 하시는 겁니다. 지금 이 자리에 없으니까 편하게 부르지, 마주한 상태면 저도 꼬박꼬박 존칭 써야죠.”

“그러시구나. 그래서 가끔 이번처럼 마음이 담긴 전서도 주고받고요?”

“전서요?”

말없이 눈만 깜빡이던 나는, 그제야 왜 갑작스럽게 월화에 대한 이야기가 나왔는지 어렴풋이 깨달았다.

전서.

감숙까지 우리를 안내한 하오문도가 건네주었던, 월화의 이름으로 된 전서.

“그거 때문이었어요?”

“뭐가요?”

“그게 그러니까…….”

이걸 뭐라고 해야 하지.

아니, 지금 생각난 대로 말하는 게 맞긴 한 건가?

내가 딱히 뭐라 말을 잇지 못하고 머뭇거리던 그때, 드디어 고개를 돌린 주화란이 나를 똑바로 응시했다.

“그 전서에 적혀 있던 내용……혹시 물어봐도 되나요?”

희한한 일이다.

내달리는 말발굽을 따라 안장이 거칠게 들썩이고, 맹렬한 바람이 전신을 스쳐 지나가는 와중에도 주화란의 목소리는 그 무엇보다 선명하게 귓가에 닿고 있었다.

분명, 평소의 절반도 되지 않는 아주 자그마한 음성임에도.

아마도 그래서였을 것이다.

그런 주화란을 멍하니 바라보다, 나도 모르게 불쑥 대답이 튀어나온 것은.

“아니요.”

“아.”

주화란이 살짝 어두워진 낯빛으로 입을 다문 그때, 나는 천천히 말을 이었다.

“전서에 관해서는 뭐라 말씀드릴 수가 없네요. 아직 저도 그 내용을 확인 안 해 봐서.”

“……!”

“음. 그렇지 않아도 상황이 상황이었던지라 잠시 잊고 있었는데. 지금 같이 볼래요?”

대답은 필요 없었다. 활짝 웃고 있는 주화란의 모습만으로 충분했으니까.

‘인벤토리 오픈, 소환.’

품 안에 손을 집어넣고 명령어를 읊음과 동시에, 손가락 사이로 전해지는 단단한 촉감.

자연스럽게 며칠 전 하오문도에게 전달받은 죽통(竹筒)을 꺼내 든 나는, 주화란이 보는 앞에서 그 안에 돌돌 말려 있던 전서를 꺼내어 펼쳤다.

망설임? 혹시나 하는 걱정?

정말, 단연코 단 한 줌조차 없었다.

‘그런 게 있을 리가 있나. 애초에 월화도 직접 대면했을 때나 말장난으로 놀리려고 들지, 일적으로는 철두철미한데.’

내가 이토록 확신할 수 있는 이유는, 월화에게서 소식이 온 것이 이번이 처음이 아니기 때문이다.

태원진가와 맺은 협약 덕분인지 타지(他地)에 있을 때도 두어 번에 걸쳐 전서를 받았고, 거기에는 제법 쓸만한 정보들이 적혀 있었다.

하오문 지부의 위치라든지, 긴급 상황 시의 접선 방법이라든지.

혹은 산서나 섬서 땅의 근황이라던지 하는 것들.

그건 말 그대로 ‘정보’였다.

월화가 아닌 하오문 섬서 지부장으로서 신경 써 주는, 일종의 우수 고객 관리랄까.

그렇기에 나는 일말의 거리낌 없이 전서를 펼쳤고, 이내 뭔가 잘못됐다는 사실을 깨달았다.



진 공자, 잘 지내요?

너무 오랫동안 못 봐서 그런가. 너무 보고 싶네. 오죽했으면 어젯밤 꿈에 진 공자가 나왔다니까?



스르륵.

본능적으로 손을 놓자 돌돌 말려 올라가는 종이.

함께 전서를 보기 위해 말머리를 바짝 붙이고 있던 주화란이 입을 열었다.

위화감이 들 만큼, 아주 사근사근한 목소리로.

“다시 펼쳐 줄래요?”

“…….”

“저 보고 있었잖아요.”

“……그, 주 소저?”

“네. 말씀하세요. 듣고 있으니까.”

뭐라도 말해야 할 것 같아 급하게 입을 열었는데, 조곤조곤한 대답과 함께 나를 지그시 쳐다보는 그녀의 시선에 등골이 얼음장처럼 차가워졌다.

이미 오래전에 얻은 한서불침(寒暑不侵)의 공능을 몸뚱어리가 까맣게 잊어버린 것처럼.

‘이걸 뭐라고 말해야 하지?’

마치 빠져나갈 수 없는 깊은 늪에 발을 디딘 기분.

할 말을 찾지 못한 내가 동공 지진만 일으키던 그때, 주화란이 흐릿하게 웃었다.

“아니다. 괜찮아요. 아무 말 안 해도 돼요.”

“예, 예?”

“저는 신경 쓰지 마시고 마저 보세요. 아주 깊고 중요한 얘기인 것 같은데. 그럼 이만.”

“잠깐만요. 주 소……!”

두두두두!

다급한 외침이 끝나기도 전에, 빠르게 말을 몰아 앞으로 치고 나가는 주화란.

그 뒷모습을 멍하니 바라보던 나는 말없이 손에 쥔 전서를 펼쳤다.

평소와는 달리 온갖 시시콜콜한 개인적인 이야기로 가득한 전서의 끝부분에는, 화룡정점을 찍는 한 문장이 적혀 있었다.



언젠가 하청지회(河淸之會)할 수 있기를 바라며, 월화.



“…….”

아주 날 죽이려고 작정했구나.

누가 보더라도 아주 긴밀한 사이로 오해할 수밖에 없는 문구를 하염없이 바라보던 그때, 혁무진이 조심스럽게 다가와 입을 열었다.

“저기, 조장님.”

“왜.”

“기련산이 보이는데요.”

“꺼져.”

“넵.”

아, 죽고 싶다.
```

## Final English reading copy

```markdown
# Chapter 1015

Our force numbered a staggering three thousand, but every last one of them was a martial artist, so we moved far faster than common sense would suggest.

We’d been on the road for only two days since leaving Tianshui, on the eastern edge of Gansu, and we’d already passed Lanzhou, the provincial capital, and were pressing ahead without slowing down.

It must have been around then.

At some point, the bone-chilling plateau and endless wilderness vanished, replaced by a narrow road lined on both sides with rocky hills of every size.

*This place…*

Sometimes, after leaving the modern world behind and roaming the Murim, I’d find myself overwhelmed, even if only for a moment, by the majesty of nature untouched by human hands, preserving the passage of countless ages.

And just as I let go of my reins and silently gazed at the endless view below the plateau, a soft voice reached my ear.

“This is the Hexi Corridor. It’s called that because it stretches west of the Yellow River like a corridor. I don’t know who first gave it that name, but doesn’t it suit the place?”

I agreed with her, but that aside, it was easy to recognize the voice’s owner.

Even if Sama Pyo and Taishan hadn’t been away, it would have been the same.

There was only one person around me with such a fresh, clear voice.

“You certainly know your stuff, Young Lady Ju.”

Ju Hwaran gave a shy smile at my reply.

“It’s only natural. I once led the Escort Bureau temporarily, even if it wasn’t for very long. And I am the Escort King’s granddaughter, after all.”

At first glance, she was right. But there was modesty in her words, too.

Just as being born into a martial family didn’t mean you had to learn martial arts, Ju Hwaran hadn’t been obligated to take over the family business.

The reason she knew so much about the Central Plains’ geography and related matters was entirely her own effort.

*Now that I think about it, the Yongbong Escort Bureau was in a situation not all that different from the Jin Family of Taiyuan at first.*

A family that had left its former glory behind and begun to fall into ruin.

One small difference was that, unlike the Jin Family of Taiyuan, which had three sons and a whole lot of testosterone, Ju Hwaran was an only child—and had to bear that much heavier burden alone.

*Though her father, the Head of the Escort Bureau, was still there, unlike mine, even if he was bedridden.*

That was all in the past.

The Head of the Yongbong Escort Bureau had recovered his vitality and returned to the front lines. And the huge sum of gold I’d beaten out of the Taeeul Merciless Sword in return had been more than enough to pull the crumbling family back onto its feet.

And the Jin Family of Taiyuan had risen to join the Five Great Families, filling the void left by the Murong great family—or rather, what remained of the Murong household.

*If Dark Heaven didn’t exist, we could’ve wrapped things up here with a happy ending where everyone lived happily ever after.*

But reality wasn’t something you could ignore. You had to face it head-on, and opportunities always came in the midst of crises.

That was how Ju Hwaran and the Yongbong Escort Bureau, and I and the Jin Family of Taiyuan, had overcome their crises and grown stronger.

It was only the many sacrifices we’d made along the way—and the fact that more would inevitably come—that weighed heavily on my heart.

And besides…

*No, never mind. I’ll leave it at that for now.*

I pushed from my mind the sight of Namho approaching me just yesterday, his face unusually stiff. His low voice still seemed to ring in my ears.

When I realized Ju Hwaran was watching me with concern, I forced a casual smile.

“Ah, sorry. I was just… just thinking about something.”

“It’s all right. I understand. You must be troubled with the battle coming up.”

How should I put it?

I couldn’t exactly tell her something I wasn’t even sure of myself.

I silently watched Ju Hwaran’s profile as she rode alongside me, then spoke almost on impulse.

“That’s part of it, of course. But I’ve also been thinking about relationships.”

“Relationships?”

“Between people. Trust, expectations. Things like that.”

I lifted my head and looked toward the narrow pass between the distant rocky hills, where thousands of our allies were pouring through like a flood.

“Nothing’s easy, I suppose, but I find this especially hard. The connections and feelings between people.”

“Connections and feelings…”

Ju Hwaran murmured the words as if to herself, then added quietly,

“I think I understand how you feel.”

“I thought you might, Young Lady Ju.”

She’d been through it herself. How could she not?

I still remembered it clearly: during the conflict with the Zhongnan Sect, Ju Hwaran had personally cut down Chief Escort Heo Jun, who had betrayed her from the shadows.

*She once followed him like a real uncle. The wound from that must still be with her.*

That was why relationships between people were so difficult.

You could readily give someone something, but no one knew whether they’d give as much in return—or more, or nothing at all.

*That’s why I’m hesitating so much, too.*

But the next thing Ju Hwaran blurted out was enough to sweep away the doubts that had been creeping back into my mind.

“It’s Wolhwa, isn’t it?”

“Y-yes?”

I’d almost agreed without thinking. I blinked at Ju Hwaran.

What? Had I just heard her wrong?

“Um, sorry, what did you just say?”

Without turning her head, Ju Hwaran answered,

“The woman named Wolhwa. The Branch Leader of the Lower District Sect in Shaanxi. Isn’t she?”

“Yes. That’s right.”

“Exactly.”

“No, I meant that she is the Branch Leader of the Shaanxi branch.”

“Oh, really?”

“Yes.”

“And?”

“Pardon?”

“Never mind.”

What on earth was this conversation?

I stared blankly at Ju Hwaran, speechless, when a violent fit of coughing rang out loud enough to cut through the pounding hooves of our galloping horses.

“Cough! Cough! Cough-aaargh!”

What’s that idiot doing now?

I turned to look behind me, ready to say something to Hyuk Mujin, who was practically convulsing in his saddle. And that was when I saw it clearly.

Hyuk Mujin desperately shaking his head, while Namho and Song Ilseom, on either side of him, looked at me with pity.

At the same time, a certain suspicion suddenly crossed my mind.

Hmm.

Hmmmm.

Could it be… what I thought it was?

*This isn’t exactly the best time for something like this.*

Still, I had to clear up any needless misunderstanding.

Feeling a little strange, I parted my lips.

“Um, Young Lady Ju?”

“Yes. Go ahead.”

Her eyes were still fixed straight ahead, as if she’d spotted her family’s sworn enemy up the road.

And, quite apart from that, her ears had somehow perked up.

Watching her, I rubbed my chin even though it didn’t itch.

“Well, this isn’t something you’re particularly curious about, but I thought I’d mention it.”

“That’s right. I’m not particularly curious, but I’ll hear you out.”

“I’m not very close with Wolhwa.”

“……”

“We did have some dealings, sure. Just a year or two ago, she was the Branch Leader in Shanxi, not Shaanxi. The Lower District Sect and I had various mutual dealings, so we got to know each other a little.”

After a brief silence, Ju Hwaran spoke.

“You speak casually for someone you’re not close to. And you just call her by her name.”

“You’re badly mistaken. I call her that when she isn’t here. If we were face-to-face, I’d use proper honorifics.”

“I see. So you sometimes exchange heartfelt missives like this one, too?”

“Missives?”

I blinked silently. Only then did I begin to understand why she’d suddenly brought up Wolhwa.

The missive.

The one delivered by the Lower District Sect member who’d guided us to Gansu, written under Wolhwa’s name.

“Was that why?”

“Why what?”

“That’s, well…”

How should I put it?

Was it really a good idea to say the first thing that came to mind?

I faltered, unable to find the words. At last, Ju Hwaran turned her head and looked me straight in the eye.

“Can I ask what was written in that missive?”

It was strange.

Even as our saddles jolted with every pounding hoof and the fierce wind rushed past us, Ju Hwaran’s voice reached my ears more clearly than anything else.

Though it was barely half as loud as usual.

Maybe that was why.

I stared at her blankly, then blurted out an answer without meaning to.

“No.”

“Ah.”

Ju Hwaran closed her mouth, her expression dimming slightly. I continued, slowly.

“I can’t tell you about the missive. I haven’t checked what it says yet.”

“……!”

“Hmm. With everything going on, I’d forgotten about it for a while. Want to read it together now?”

I didn’t need an answer. Ju Hwaran’s bright smile said enough.

*Inventory open. Summon.*

As I slipped my hand inside my robe and spoke the command, I felt something solid between my fingers.

I naturally pulled out the bamboo tube I’d received from the Lower District Sect member a few days ago, then took out the missive rolled up inside and unfolded it in front of Ju Hwaran.

Hesitation? The slightest worry?

Not a trace of either. Not even a pinch.

*Why would I have anything like that? Wolhwa only teases me with wordplay when we meet in person. When it comes to business, she’s meticulous.*

There was a reason I was so sure. This wasn’t the first time I’d heard from Wolhwa.

Maybe because of the agreement with the Jin Family of Taiyuan, she’d sent me a couple of missives while I was away, and they’d contained some fairly useful information.

The location of Lower District Sect branches. How to make contact in an emergency.

Or the latest news from Shanxi or Shaanxi.

That was all it was: “information.”

It wasn’t Wolhwa writing to me personally. It was the Branch Leader of the Lower District Sect’s Shaanxi branch looking after a valued client.

So I unfolded the missive without a moment’s hesitation—and immediately realized something was wrong.

Young Master Jin, have you been well?

Maybe it’s because we haven’t seen each other in so long. I miss you so much. I missed you so much that you even appeared in my dream last night!

*Rustle.*

The paper rolled back up as I instinctively let go.

Ju Hwaran, who’d brought her horse right alongside mine so we could read the missive together, spoke.

Her voice was so gentle it felt out of place.

“Could you open it again?”

“……”

“I was reading it.”

“…Um, Young Lady Ju?”

“Yes. Go ahead. I’m listening.”

I hurriedly opened my mouth, feeling like I had to say something. But her soft reply—and the steady gaze she fixed on me—sent a chill down my spine.

As if my body had completely forgotten the power I’d gained long ago: Unaffected by Cold and Heat.

*How am I supposed to explain this?*

It felt like I’d stepped into a deep swamp with no way out.

As I struggled to find something to say, Ju Hwaran gave a faint smile.

“Never mind. It’s fine. You don’t have to say anything.”

“Y-yes?”

“Don’t mind me. Go ahead and finish reading. It sounds like a very deep and important conversation. Well, I’ll leave you to it.”

“Wait, Young Lady Ju—!”

*Thud-thud-thud!*

Before my desperate shout was even finished, Ju Hwaran urged her horse forward and sped ahead.

I stared blankly at her retreating back, then silently unfolded the missive in my hand.

Unlike usual, it was full of trivial personal chatter. And at the very end, it had one line that put the finishing touch on the whole thing.

*Hoping for the day the Yellow River runs clear and we can meet again,[^1] Wolhwa.*

“……”

She really was trying to get me killed.

I stared at the words, which anyone would mistake for a message between people on very intimate terms. Then Hyuk Mujin carefully approached and spoke.

“Um, Captain.”

“What.”

“I can see the Qilian Mountains.”

“Get lost.”

“Yes, sir.”

*God, I want to die.*

[^1]: The Korean expression evokes the Yellow River running clear—a rare, auspicious event—and uses it to express the hope of meeting again.
```

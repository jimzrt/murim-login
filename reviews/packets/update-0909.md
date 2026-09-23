<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0909.txt",
      "sha256": "63112a934148d02ff14360ca10dc4aa8c8f64d66610a4ef9e2041971391bbc67",
      "bytes": 13172
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0f7f71dfbda469272f987da32fafe9c5158a0473d6b3b975034a7d4b1efadcb5",
      "bytes": 1339
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "acd9684a058afcc0bbe3f5e01a5af4246b19251d761221cade8efde9fd414db4",
      "bytes": 231263
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0364746e74ab7c83972a620667770317684bd1bbcdbbbccda917fb770c1eddc3",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "dd7f76957546a71e683790cb56cef7522358809d8373c4070ffdce9620d9ca72",
      "bytes": 1445
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "31ed7044ad435165bd7ac9701a0dd46d852f2640b0044d6369e74ff9c2a56272",
      "bytes": 973
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "84031a553f60e343a20b32c8374033506bfc48c59d81933c7451fba965faa03a",
      "bytes": 1002
    },
    {
      "path": "characters/Namho.md",
      "sha256": "a7cc684e856dd79e8a9572fab4fb75a92bb712fe30b27ec336d7505e56fcf343",
      "bytes": 973
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "7cd7d74bd6e9c0dbf9b94535784363385e9fad753a4e6d697e69f7cf3ffdb25a",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "7d08fee6c25d6a2044a1e7b2cd0eb31475a23316e05ab65aa55efd5d557f42f8",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "479898b6d8ee6c19a50f0e3c5df2cff14307fc149eb75f31d9fa96313b3aace1",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "f897e500e95a507dc76447fd546e578385d56762739e8ef08751c22f9f94beee",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c336a9b74793e3bf73bdc6e4d5a7447e62c84594f5d5258f730ffe7383f34d3d",
      "bytes": 262942
    }
  ],
  "estimated_tokens": 12221
}
-->

# Durable State Update — Chapter 909

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
1 and safe_through 909. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 909. Profile updates may replace only one
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
  "chapter": 909,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 909,
    "continuity_sources": [909],
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
    "Taekyung remains injured and in the banquet-hall battle; he has killed Ma Sanbao and the Golden Ox Palace commander.",
    "Taekyung can halt and redirect arrows with the unknown power of his Middle Dantian.",
    "Taekyung offers the Imperial Guards a chance to return to the imperial court and calls on them to eliminate committed traitors.",
    "Fire Dragon Pavilion members are fleeing a large force of black-clad attackers; Taekyung is going to protect them.",
    "Jeok Cheongang is fighting Cang Gong, the Eastern Heaven Demon Lord.",
    "Jeong Hogun and the Embroidered Uniform Guard are on the Emperor’s side and have intervened to protect Taekyung.",
    "So Gyo’s identity and allegiance remain unknown.",
    "The Emperor and Cang Gong have not revealed all their forces."
  ],
  "continuity_sources": [
    907,
    908
  ],
  "open_questions": [
    "Who is So Gyo, and where does her allegiance lie?",
    "What is the nature of Cang Gong’s power and his relationship to the Lord of Heaven?",
    "What forces are the Emperor and Cang Gong still withholding?",
    "Who are the black-clad attackers pursuing the Fire Dragon Pavilion members?",
    "How many Imperial Guards will side with the imperial court?"
  ],
  "safe_through": 908,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 초식     | **form**                                         | Numbered technique movement                           |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 노부      | **this old man / I**                                            |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 화룡일미 | **Fire Dragon's Single Tail** | A form of the Fire Dragon Divine Spear. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 열화신창 | **Blazing Flame Divine Spear** | Jin's spear technique; its first form appears in this chapter. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
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
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 908
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 907
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; he regards Taekyung as the person who has repeatedly saved him and now believes he may be able to save Taekyung in turn. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 894
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 908
- **Aliases:** None
- **Role:** Ma Sanbao was the East Depot’s Brush-Holding Eunuch and a Supreme Peak martial artist who secretly led a restoration effort for Prince Shangshan and served as disciple of the Eastern Heaven Demon Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, led the restoration effort for Prince Shangshan, and recruited Jin Taekyung and Jeok Cheongang as allies; Jin killed him during the banquet-hall battle after Ma revealed his allegiance to his master, the Eastern Heaven Demon Lord.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 903
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he now guides the Fire Dragon Pavilion.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 893
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 893
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 893
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 903
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃909화



허억, 헉.

숨이 턱 끝까지 차오른다. 긴장된 상태에서 쉴 새 없이 움직인 팔다리가 남의 것처럼 삐걱거렸고, 심장은 당장이라도 터질 것만 같았다.

‘어쩌다가 이렇게 됐지?’

죽어라 내달리는 와중에도, 혁무진은 생각했다.

도대체 언제, 어디서부터 이 모든 것이 뒤틀리기 시작했는지.

하지만 항상 그래 왔듯이 의문에 대한 답은 꼬리에 꼬리를 물며 끝도 없이 이어졌고, 결국 그 종착지에는 자조 섞인 한마디만이 덩그러니 남아 있을 뿐이었다.

‘시바, 그냥 태어난 것부터가 실수였나.’

혁무진은 억울하고 서러워서 눈물이 날 것 같았다.

포목점 아들놈이 왜 무인이 된다고 염병을 떨었을까. 얌전하게 가업이나 물려받으면 됐을 텐데.

날고 기는 무림인들이 영웅으로 등장하는 잡서(雜書)만 읽지 않았더라면, 지금쯤 남들처럼 가정을 꾸리고 눈에 넣어도 안 아플 자식도 두셋쯤 있었을지도 모른다.

적어도 지금처럼 어디서 튀어나왔는지도 모를 이상한 놈들에게 쫓기고 있지는 않겠지.

두두두두!

등 뒤에서 울려 퍼지는 추격자들의 육중한 발걸음 소리에, 혁무진은 등골이 서늘해지는 것을 느꼈다.

‘빌어먹을. 붙잡히면 끝장이다.’

저들의 정체가 무엇인지, 어디에 숨어 있다가 불쑥 튀어나왔는지는 모르겠지만 한 가지는 확실했다.

‘괴물 같은 놈들. 아니, 괴물들.’

혁무진의 판단은 단순히 무공의 고하에 국한된 것이 아니었다.

저 흑의인들을 처음 발견했을 때부터 느꼈던 오싹함, 원초적인 공포는 시간이 흐를수록 짙어지고 있었으니까.

‘도대체…… 정체가 뭐지?’

머릿속을 가득 채운 해결할 수 없는 의문.

그리고 이미 한계에 다다라 있던 몸뚱어리는, 혁무진도 모르는 사이에 조금씩 통제를 벗어나 있었다.

스륵.

“……!”

순간 맥없이 풀려 버린 다리.

달려 나가던 속도를 이기지 못하고 앞으로 고꾸라지는 신형에, 혁무진이 눈을 부릅뜬 그때였다.

“혁무우우우!”

덥석.

쩌렁쩌렁한 외침과 함께 억센 힘이 옷깃을 잡아챈다. 하마터면 땅으로 처박힐 뻔한 혁무진은 벌렁거리는 가슴을 가라앉히며 고개를 들었다.

쿵. 쿠웅!

그의 몸을 마치 짐짝처럼 옆구리에 낀 채 뛰고 있는 거인, 아니 태산의 얼굴이 보였다.

“혁무. 괜찮나?”

혁무진이 간신히 목소리를 쥐어 짜내어 대답했다.

“아니, 전혀 안 괜찮아.”

“응. 그래 보인다.”

“……알면서 뭘 물어보냐. 지금 사람 놀려?”

“혁무. 그게 생명의 은인에게 보일 만한 태도인가?”

“그건 아니지. 일단 고맙다.”

“고마우면 나중에 오향장육 백 그릇으로 갚아라.”

“백 그릇이 아니라 이백 그릇도 사 줄 수 있으니까 우선 살고 보자. 살고.”

“이백 그릇?”

미간을 좁힌 태산이 문득 걸음을 늦추며 중얼거렸다.

“이백 그릇이 어느 정도지?”

태산의 듬직한 양쪽 어깨 위를 차지하고 있던 남호와 신의. 그리고 어쩌다 보니 한 몸이 되어 버린 혁무진이 동시에 비명을 내질렀다.

“이런 정신 나간 놈을 보았나! 왜 갑자기 속도를 늦추고 지랄이냐!”

“태산 소협! 지금 이럴 때가 아니오!”

“뭐 해, 미친 새끼야!”

하지만 불꽃과도 같은 성화에도, 이해할 수 없는 난제를 맞이한 태산의 미간은 좀처럼 펴지지 않았다.

“하지만 이해가 되지 않는다. 이백이라는 숫자는 어느 정도인가?”

“이런 시팔……!”

하늘을 우러러 탄식한 남호는 고개를 돌려 뒤를 바라보았다.

후위를 맡은 다른 이들과 그 뒤를 바짝 쫓는 흑의인들의 모습이 빠르게 가까워지고 있는 상황.

“그냥 대답해 주십시오! 보아하니 대가리가 깨져도 대답을 들어야 하는 모양입니다! 어서!”

신의의 다급한 부탁에, 얼굴이 새파랗게 질린 남호가 외쳤다.

“백 그릇! 백 그릇이 두 번 나오면 몇이냐!”

“으음. 백 그릇이 두 번이면…… 아. 태산이, 이제 알았다.”

마침내 답을 찾은 태산이 의기양양한 얼굴로 입을 열었다.

“백 둘.”

“야, 이 개새끼야!”

“이 시벌 놈아!”

“아아, 스승님……!”

사방에서 터져 나오는 곡소리.

분노의 임계점에 도달한 남호는 태산의 돌대가리를 팔꿈치로 내리찍었고, 혁무진은 울음 섞인 비명을 내질렀으며, 신의는 이 자리에 없는 자신의 스승을 떠올리며 소매 안의 대침(大針)을 만지작거렸다. 처음으로 누군가를 죽이고 싶다는 생각과 함께.

그러나 열렬하게 반응하는 그들과 달리, 이백 그릇이 어느 정도의 단위인지 나름대로 답을 찾은 태산의 얼굴은 정오의 태양처럼 환하게 빛나고 있었다.

“이백 그릇. 많다. 아무튼 엄청 많다!”

백 그릇만으로도 배가 터지게 먹을 수 있는데, 이백 그릇이라니.

사실 이백과 백 둘의 정확한 차이점은 모르겠지만, 태산은 그런 시시콜콜한 문제에 크게 신경 쓰지 않기로 했다.

그리고 이 기쁜 소식을 아직 전해 듣지 못한 누군가를 향해 활짝 웃으며 두 손을 흔들었다.

“각주! 각주우! 태산이 오향장육 먹는다! 혁무가 백둘? 이백? 아무튼 배 터지게 먹여 준다고 했다!”

“배 터질 걱정은 하지 말거라. 그 전에 노부가 하늘에 맹세코 네놈 대가리를 터트려 버릴…… 잠깐, 지금 뭐라고?”

우공이산(愚公移山)의 마음으로 하염없이 태산의 정수리를 내리찍던 남호가 눈을 부릅뜨며 고개를 들었다.

그리고 보았다.

남호가, 신의가. 혁무진이. 뒤따라오던 화룡각 대원 모두가.

쐐애애액!

세찬 파공성과 함께 그들을 향해 달려오고 있는 누군가를. 그의 발끝에서 터져 나오는 익숙한 화염을.

“아이고오! 조장니이이임!”

혁무진이 참고 있던 울음을 터트렸다.



* * *



인생을 살아가다 보면 참 이해할 수 없는 일들이 자주 벌어지곤 한다.

대격변 이전의 삶을 살아가던 이들에게는 어느 날 하늘에서 뚝 떨어진 듯한 몬스터와 헌터의 존재가 그러할 테고, 내게는 캡슐을 통해 알게 된 이 세상이 그랬다.

그리고 앞서 들었던 예시만큼은 아니지만, 지금 이 상황도 충분히 당황스럽기는 매한가지다.

“오향장육! 백둘! 이백!”

광기에 가까운 환희로 물든 태산이.

“당장 이놈을 죽여! 자네라면 능히 이 육시랄 놈의 대가리를 깰 수 있어!”

광기라는 표현도 부족할 정도의 분노를 뿜어내는 남호.

“어흐흑. 조장니이임! 왜 이제야 오셨어요!”

죽었다가 살아난 사람만이 보일 수 있는 안도와 함께 펑펑 울어 재끼는 혁무진.

“아아, 스승님…… 이 못난 제자가 그릇된 마음을 품었습니다.”

마지막으로 부처조차 여래신장으로 날려 버릴 것 같은 해탈한 표정으로 중얼거리는 신의까지.

“…….”

뭐여, 시벌.

이게 도대체 무슨 상황인지 감도 안 잡힌다.

나는 아주 잠시 동안 할 말을 잃은 채 그들을 바라보았고, 이내 이해하길 포기했다.

물론, 이 상황에서는 이해할 만한 시간조차 부족하다는 것이 훨씬 정확한 표현이었겠지만.

파파팟!

“각주님! 아니, 진 공자! 아니, 은인!”

짧은 순간 세 번이나 호칭을 바꿔 부르는 신기를 선보인 주화란이 엉망이 된 옷차림으로 달려오는 것이 보인다.

그녀의 뒤에서 미친 듯이 병장기를 휘두르며 추격자들을 뿌리치고 있는 송일섬과 사마표의 모습도.

카카캉!

서걱!

은은하게 빛나는 검기가 어둠 속에서 번뜩이고, 핏물로 보이는 액체가 허공에 흩뿌려졌다.

그리고 바람을 타고 전해지는, 참을 수 없는 악취도 함께.

‘뭐지, 이 냄새는?’

아직 상당한 거리가 있음에도 불구하고, 저절로 눈살이 찌푸려지며 속이 메슥거릴 정도다.

하지만 저 냄새의 정체를 곰곰이 유추해 볼 시간적 여유 따위는 없었다. 나는 아슬아슬하게 추적자들을 뿌리치며 가까워지는 세 사람을 향해 입술을 달싹였다.

- 신호를 보내면, 모두 엎드려.

그리고 제각각의 귓가로 흘려보낸 전음(傳音)과 함께, 체내의 모든 공력을 끌어모았다.

스아아악.

나는 몸 안 깊숙한 곳에서부터 끌어올린 열기를 전신의 사지백해로 흘려보냈다.

아직 성치 않은 혈도가 비명을 지르고, 전투 과정에서 입은 크고 작은 부상이 더욱 벌어지는 것이 느껴졌지만 다른 방법은 없었다.

‘해야 한다.’

우우웅.

석벽에서 뛰어내리기 직전, 어느 이름 모를 금위군에게서 빼앗아 온 철창이 열양지기를 머금고 부르르 떨린다.

불그스름하게 달아오른 창날 위로는 도무지 예전 같지 않은, 그러나 그 위력만큼은 무시할 수 없는 청백색의 화염이 뒤덮여 가고 있었다.

그리고 마침내.

화륵.

창날을 휘감으며 솟아오른 겁화가 공기를 태우고 어둠을 잡아먹는다. 아무런 비명도, 외침도 없이 빠르게 가까워지는 그들을 향해 몸집을 부풀렸다.

양 떼를 향해 달려 나갈 준비를 마친 한 마리의 맹수처럼.

세상에 존재하는 그 무엇보다 뜨겁고. 맹렬하게.

- 지금.

세 사람을 향한 전음과 함께, 나는 세상을 베어 가를 듯이 온 힘을 다해 창을 휘둘렀다.

마치 끝없이 뻗어 나가는 용의 꼬리와 같이.

‘열화신창 일초식.’

화룡일미(火龍一尾).

화아아악!

그 순간, 온 사방이 대낮처럼 환하게 밝아졌다.

마침내 창날을 타고 뛰쳐나온 청백색의 화염은 황궁 곳곳에 놓인 조형물을 불태우고, 녹이며 나아갔다.

마지막 순간, 내 전음을 듣고 반 박자 빨리 엎드릴 수 있었던 세 사람의 머리 위로.

또한 그 뒤를 바짝 쫓고 있던 흑의인들의 시야를 뒤덮으며.

콰아아아아아!

구구구궁!

거대한 폭발과 굉음. 마지막으로 진동.

섬광이 번뜩이고, 부풀어 오른 화염이 비가 되어 반경 수십여 장을 뒤덮는다.

그야말로 화마(火魔)라는 표현이 부족하지 않을 광경.

그리고 비명조차 들려오지 않는 그 불구덩이 속에서, 매캐한 연기를 뚫고 달려오는 이들이 있었다.

파팟!

주화란. 송일섬. 사마표.

익숙한 얼굴들을 발견한 나는 흐릿하게 웃었다.

아니, 사실 흐릿한 것은 지금 이 순간에도 조금씩 기울어져 가는 내 시야일지도 몰랐다.

턱.

아무도 눈치채지 못할 만큼, 최대한 자연스럽게 창을 바로 세워 몸을 지탱한 나는 가빠진 호흡을 억눌렀다.

‘……젠장.’

살아 있는 뱀처럼 스멀스멀 전신을 기어오르는 탈력감이 느껴진다.

비록 불안정할지언정 충만했던 공력은 어느새 바닥을 드러낸 상태였고, 안정을 취했어야 할 육신은 무리한 움직임으로 고통을 호소하고 있었다.

게다가 참을 수 없는 정신적인 피로까지.

‘중단전(中丹田)의 힘은 최대한 자제해야 했었는데…….’

사실 이 모든 게 의미 없는 후회라는 것쯤은 나도 알고 있다.

힘을 더 자제했다면 지금 정도의 몸 상태는 아니었겠지만, 그렇다고 전체적인 상황이 나아졌으리란 보장 따위는 없었으니까.

그저 당장 눈앞에 들이닥친 위기를, 무슨 이유에서인지 이곳으로 돌아온 화룡각 대원들을 구할 수 있었다는 것에 만족할 따름이었다.

“은인!”

어느새 코앞까지 다가온 주화란이 다급한 얼굴로 외쳤다.

그녀의 양옆에서 나란히 다가오던 송일섬과 사마표 또한 일그러진 표정으로 입을 열었다.

“모두, 모두 도망쳐야 한다.”

“지금 당장!”

그들이 이런 반응을 보이는 것은 당연했다.

내가 전력을 다한 일격이 선두를 휩쓸었다고는 해도 남아 있는 적들의 숫자는 언뜻 보기에도 일천이 넘어갔고, 자세히는 모르지만 개개인의 실력도 결코 녹록지 않을 테니까.

하지만 다음 순간, 흩어지는 연기 속에서 서서히 드러난 광경을 확인한 나는 비로소 깨달았다.

왜 그들이 이토록 다급하게 말했는지.

그리고 왜 마삼보가 그토록 반란의 성공을 자신했었는지.

“저건…….”

나도 모르게 벌어진 입술 사이로, 흐릿한 신음이 흘러나왔다.
```

## Final English reading copy

```markdown
# Chapter 909

“Hah… Hah…”

Hyuk Mujin was gasping for breath. His arms and legs, moving nonstop while he was on edge, creaked like they belonged to someone else. His heart felt ready to burst at any second.

*How did it come to this?*

Even as he ran for his life, Hyuk Mujin wondered when and where everything had started going wrong.

But, as always, one question led to another, and they went on without end. In the end, all that remained at the end of the trail was a single, self-mocking thought.

*Fuck. Was being born the mistake?*

Hyuk Mujin felt so wronged and miserable he could have cried.

Why the hell had a textile-shop owner’s son thrown a fit about becoming a martial artist? He could’ve quietly taken over the family business.

If he hadn’t read all those trashy books where martial artists who could fly and fight like the wind appeared as heroes, he might be just like everyone else by now—with a family and two or three kids he loved more than life itself.

At the very least, he wouldn’t be getting chased by a bunch of weirdos who’d appeared out of nowhere.

*Thud-thud-thud-thud!*

The pursuers’ heavy footsteps rang out behind him. A chill ran down Mujin’s spine.

*Shit. If they catch me, I’m done for.*

He didn’t know who they were or where they’d been hiding before suddenly showing up, but one thing was certain.

*Those things are monsters. No—actual monsters.*

Mujin’s judgment wasn’t based solely on the level of their martial arts.

The primal fear and chill he’d felt from the moment he first spotted the black-clad figures had only grown stronger with time.

*What the hell… are they?*

His mind was full of questions he couldn’t answer.

And his body, already pushed to its limit, was slipping out of his control a little at a time without him even realizing it.

*Slide.*

“……!”

His legs suddenly gave out.

Unable to stop himself from the momentum of his run, Mujin pitched forward. His eyes flew wide—

“Hyuuuuuk!”

*Grab!*

A thunderous shout rang out as a powerful hand seized his collar. Mujin had nearly slammed face-first into the ground. He steadied his wildly beating heart and looked up.

*Thump. Thump!*

He saw the face of the giant—no, Taishan—running with Mujin tucked under his arm like a piece of luggage.

“Hyuk. You okay?”

Mujin barely managed to squeeze out a reply.

“No. Not even a little.”

“Yeah. You look that way.”

“……If you know, why ask? Are you messing with me?”

“Hyuk. Is that how you treat the person who saved your life?”

“Not really. Thanks, then.”

“If you’re thankful, pay me back with a hundred plates of five-spice pork later.”

“I’ll buy you two hundred plates, not a hundred. For now, let’s just stay alive. Alive.”

“Two hundred plates?”

Taishan furrowed his brow and slowed down, muttering to himself.

“How much is two hundred plates?”

Namho and the Divine Physician, who occupied Taishan’s broad shoulders, and Mujin, who had somehow become one with the whole arrangement, all screamed at once.

“What kind of lunatic does that? Why the hell are you slowing down all of a sudden?”

“Young Hero Taishan! This is no time for that!”

“What are you doing, you crazy bastard?”

But even amid their fiery protests, Taishan’s brow remained furrowed as he pondered the problem.

“I don’t understand. How much is the number two hundred?”

“Goddamn it…”

Namho groaned toward the heavens and turned to look behind them.

The others bringing up the rear—and the black-clad figures right on their heels—were rapidly drawing closer.

“Just answer him! Looks like he’ll need an answer even if his head gets smashed in! Hurry!”

At the Divine Physician’s desperate plea, Namho’s face went pale as he shouted,

“One hundred plates! If you have one hundred plates twice, how many is that?”

“Hmm. One hundred plates twice is… Ah. Taishan understands now.”

At last, Taishan found his answer and spoke with a triumphant look.

“One hundred two.”

“You fucking bastard!”

“You goddamn idiot!”

“Ah, Master…”

Wails erupted all around them.

Namho, driven to the edge of his patience, brought his elbow down on Taishan’s blockhead. Mujin let out a sobbing scream. The Divine Physician thought of his absent Master and felt around inside his sleeve for a large acupuncture needle, entertaining for the first time the thought of killing someone.

But unlike the others, who were reacting with such passion, Taishan’s face shone like the midday sun. He’d found his own answer to how much two hundred plates was.

“Two hundred plates. A lot. Anyway, it’s a whole lot!”

Even a hundred plates would be enough to eat until his stomach burst. And two hundred plates!

Truthfully, he didn’t know the exact difference between two hundred and one hundred two. But Taishan decided there was no need to worry about such trivial details.

Then, grinning broadly, he waved both hands at someone who hadn’t heard the good news yet.

“Pavilion Master! Pavilion Master! Taishan gets to eat five-spice pork! Hyuk said he’ll feed me until I burst—one hundred two? Two hundred? Anyway, until I burst!”

“Don’t worry about your stomach bursting. Before that, I swear to Heaven I’ll burst your head myself—Wait, what did you just say?”

Namho, who’d been steadily hammering Taishan on the crown with the heart of the Foolish Old Man who moved mountains, widened his eyes and looked up.

And saw them.

Namho. The Divine Physician. Hyuk Mujin. Every Fire Dragon Pavilion member running behind them.

*Whoooosh!*

Someone was rushing toward them amid a fierce whistle of air. The familiar flames burst from his toes.

“Captain!”

Mujin finally let out the tears he’d been holding back.

* * *

A lot of things in life are hard to understand.

For people living before the Great Cataclysm, there were monsters and Hunters, as if they’d dropped from the sky one day. For me, it was the world I’d come to know through the capsule.

The situation in front of me wasn’t quite on that level, but it was still more than enough to leave me confused.

“Five-spice pork! One hundred two! Two hundred!”

Taishan, his face alight with near-maniacal joy.

“Kill this bastard right now! You’re more than capable of cracking this fucking idiot’s head open!”

Namho, radiating so much rage that even *mania* didn’t quite cover it.

“Waaah! Captain! Why’d you only get here now?”

Hyuk Mujin, sobbing his eyes out with the relief of someone who’d died and come back to life.

“Ah, Master… This unworthy Disciple had a wicked thought.”

And finally, the Divine Physician, muttering with such a serene, transcendent expression that he looked like he could even knock the Buddha flying with a Palm Strike of the Tathagata.

“……”

What the fuck?

I had no idea what was going on.

I stared at them, speechless for a brief moment, then gave up on trying to understand.

Of course, it would’ve been more accurate to say there wasn’t time to make sense of the situation in the first place.

*Pat-pat!*

“Pavilion Master! No, Young Master Jin! No, Benefactor!”

Ju Hwaran came running toward me, showing off her skill at changing how she addressed me three times in one short moment. Her clothes were a mess.

Behind her, Song Ilseom and Sama Pyo were desperately swinging their weapons, trying to keep their pursuers at bay.

*Clang!*

*Slice!*

Sword Energy flashed in the darkness, and what looked like blood sprayed through the air.

The wind carried an unbearable stench with it.

*What’s that smell?*

Even though they were still a considerable distance away, it was enough to make me frown and feel nauseous.

But I didn’t have time to guess what the smell was. I moved my lips toward the three who were barely managing to shake off their pursuers as they drew closer.

—When I give the signal, everyone get down.

Along with the Sound Transmission I sent into each of their ears, I gathered all the internal energy in my body.

*Shhhh…*

I sent the heat I’d drawn up from deep within me flowing through every limb and acupoint.

My battered acupoints screamed, and I could feel the large and small wounds I’d sustained in the fight tearing wider. But there was no other way.

*I have to do it.*

*Whummm.*

The iron spear I’d taken from some nameless Imperial Guard just before jumping down from the stone wall trembled, filled with Scorching Yang Qi.

The spearhead glowed red. Over it spread a blue-white flame, no longer anything like it once was—but still too powerful to ignore.

And at last—

*Fwoosh.*

Hellfire surged up around the spearhead, burning the air and devouring the darkness. It swelled toward the figures drawing closer without a scream or a shout.

Like a beast preparing to charge a flock of sheep.

Hotter and more ferocious than anything else in the world.

—Now.

As I sent the signal to the three, I swung the spear with all my strength, as if I were about to cut the world in two.

Like the tail of a dragon reaching out without end.

*The first form of the Blazing Flame Divine Spear.*

**Fire Dragon’s Single Tail.**

*Fwoooosh!*

In that moment, all around us lit up as brightly as day.

The blue-white flames leaped from the spearhead and surged forward, burning and melting the ornaments scattered throughout the imperial palace.

They passed over the heads of the three, who’d heard my Sound Transmission and dropped down half a beat before the final moment.

They also filled the field of vision of the black-clad figures close on their heels.

*Kwaaaaaa!*

*Rumble-rumble-rumble!*

A tremendous explosion and roar. Then the earth shook.

A flash of light, and the swelling flames fell like rain, covering a radius of several dozen *jang*.

There was no better way to describe it than as a fire demon.

And through the smoke in that pit of flames, where not even a scream could be heard, people came running.

*Pat-pat!*

Ju Hwaran. Song Ilseom. Sama Pyo.

I spotted their familiar faces and gave a faint smile.

Or maybe it was my vision that was growing faint, tilting a little more with every passing moment.

*Thump.*

Making it look as natural as possible, and without anyone noticing, I straightened the spear and used it to support myself. Then I suppressed my labored breathing.

*……Damn it.*

A wave of weakness crawled up my body like a living snake.

My internal energy, which had been abundant despite its instability, had run dry. My body, which should’ve been resting, was crying out in pain after all that exertion.

And on top of that, I was mentally exhausted beyond what I could bear.

*I should’ve held back with the Middle Dantian as much as possible…*

I knew well enough that there was no point regretting it now.

If I’d held back more, I wouldn’t be in this state. But there was no guarantee the overall situation would’ve been any better.

I could only be grateful that I’d managed to save the Fire Dragon Pavilion members who, for some reason, had come back here—save them from the danger that had just rushed up in front of me.

“Benefactor!”

Ju Hwaran, now right in front of me, shouted with alarm written across her face.

Song Ilseom and Sama Pyo, approaching at her sides, spoke too, their expressions twisted with concern.

“We have to run. Everyone—we have to get out of here.”

“Right now!”

Their reaction was only natural.

Even though my all-out strike had swept through the front ranks, there were still more than a thousand enemies at a glance. I couldn’t judge their individual strength precisely, but none of them would be easy to deal with.

But the next moment, as the smoke dispersed and the scene slowly came into view, I finally understood.

Why they’d been so desperate.

And why Ma Sanbao had been so confident the rebellion would succeed.

“That’s…”

A faint groan slipped through my parted lips.
```

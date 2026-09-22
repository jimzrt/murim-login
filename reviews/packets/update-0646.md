<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0646.txt",
      "sha256": "3c9367f434acbd84e83efd3838dc83d9d96efa4811c3abaa4f4df054ffc121e4",
      "bytes": 13934
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2b3d6e70e417cd17f58e1aa53ee4e004745a2faeeca3cd087a3ba7b2e8821442",
      "bytes": 2011
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "eccbca171855bf58670470015d45bb7fd6cb0a2726b01333b0f8dc76c1460fee",
      "bytes": 198757
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "a806aa058cfcdc85fb7ea2314cf140af303cfb63bab75bc5b3e25ff8eaba19b3",
      "bytes": 762
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "645027cba8c8b5aba1c71846f35f43d860d5c3384c22aee238ece8bac9265756",
      "bytes": 638
    },
    {
      "path": "characters/Blood Monk.md",
      "sha256": "3e845c1d73049020344896c8a917bd4414f23f51bd193f6f23b6fa3167424230",
      "bytes": 552
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "af33f7590a268c09dc72c27102bbea75d1e91235f1bb5679eaeee3f3cfd908a5",
      "bytes": 1347
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "4a30f335183d7cd8b607837539b83bf19093a8fccd55b9e6e7874934cb927014",
      "bytes": 1043
    },
    {
      "path": "characters/Namho.md",
      "sha256": "dc3a788d31da285cfcc3aa04614c76270cc57a3e067a34e1a07c38b1756ad057",
      "bytes": 843
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "8239f1848eff7456a0f6350f8a804abbcc28609b38d0d834eee2b16e15f5bb30",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "01b86983e71a27ce7d4a249abaf17b867ec0c3c0f97e89662d75c4415ab62cd1",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "8e7b55c6ac249ffb4a3d45a7b6e79933d9b74273c6378ee8a4e62719a5c27b57",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "8b140e8bd282fde44ed0bc2364a91bb676c9034304988231544aa99078c8c611",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "634ee76740dd1f8888e7e9c7f86b94b96db9ad200ed419b7980b365e55bf3084",
      "bytes": 204908
    }
  ],
  "estimated_tokens": 12760
}
-->

# Durable State Update — Chapter 646

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 646. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 646. Profile updates may replace only one
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
  "chapter": 646,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 646,
    "continuity_sources": [646],
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
    "Jin Taekyung has majority-backed admission to the Nanman tribal grand council.",
    "Baeksang attacked Jin Taekyung at the council, but Jin overpowered him with Flame Divine Palm while remaining seated.",
    "The Beast Miao King stopped the fight; Baeksang withdrew with Yohi, Heugung, and nearly half of the chieftains.",
    "More than ten thousand Bai people and roughly half of Nanman's chieftains are now hostile to Jin.",
    "The council continues for three days with a memorial stele and banquet scheduled for tonight.",
    "The Beast Miao King ordered scouts toward Guizhou to monitor the Blood Monk and prepare for possible Dark Heaven involvement.",
    "Approximately two hundred Ailao Mountain warriors remain inside the Thousand-Year Spider webs, which appear to shield them from the Poison Mist.",
    "The missing ferocious beasts have not been found in the Poisonblood Grounds.",
    "Ailao Mountain's Wraith and the pure-white eggs in the Poisonblood Grounds remain unexplained.",
    "An unidentified entity who recognizes Jin Taekyung has killed two informants.",
    "The Blood Monk's destination and connection to Dark Heaven remain unknown."
  ],
  "continuity_sources": [
    645,
    644
  ],
  "open_questions": [
    "Who is the hidden entity that recognizes Jin Taekyung, and what is the nature of their past connection?",
    "Where did the missing ferocious beasts go?",
    "Did Dark Heaven influence the Thousand-Year Spider attack, and is the Blood Monk connected to Dark Heaven or heading toward Nanman?",
    "What does Ailao Mountain's Wraith intend to do?",
    "What are the pure-white eggs in the swamp, and what will emerge from them?"
  ],
  "safe_through": 645,
  "temporary_decisions": [
    "Use Tribal Grand Council for 부족 대회의.",
    "Use Blood Monk for 혈승.",
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사.",
    "Use Thousand-Year Spider for 천년지주."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 헌터      | **Hunter**            |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 정마대전   | **Great Faction War**         |
| 소저      | **Young Lady**                                                  |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈승 | **Blood Monk** | Sobriquet of the unidentified bald martial artist active in Guizhou. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 은자 | **silver nyang** | Silver currency unit. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 광동진가 | **Guangdong Chen Family** | Family whose last child Ju Gongsan carried to Henan during the Great Faction War. |
| 광동 | **Guangdong** | Province under Demonic Cult control during the war. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 귀주 | **Guizhou** | Region whose Murim representatives send a delegate. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 전도 | **complete map of the realm** | Mae Jonghak's map marking terrain, place names, and sect locations. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 대역 | **stand-in** | Jin's term for the substitute Go Jun used to fake Song Cheonwoo's departure. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |

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
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 645
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he opposes the Nanman Beast Palace joining the Murim Alliance, attacked Jin Taekyung at the tribal grand council, and withdrew with the pro-Baeksang faction after being stopped.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 645
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace, is responsible for the forces stationed at Ailao Mountain, and has ordered scouts toward Guizhou because of the possible Blood Monk threat.

### Blood Monk.md

# Blood Monk (혈승)

- **Safe through:** Chapter 645
- **Aliases:** None
- **Role:** The Blood Monk is an unidentified bald martial artist who carries a single Zen staff and has killed several hundred people in Guizhou; his current destination is unknown.
- **Personality:** Unknown; the captured witness who described him was unable to provide further information before dying.
- **Voice:** Not established.
- **Relationships:** His connection to Dark Heaven and Nanman is unknown.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 645
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 645
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, an experienced Nanman escort guide with route knowledge from the Escort King's records, and someone who can understand the Miao and Bai languages.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 645
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 627
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 645
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 645
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 645
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃646화



이대로면 대역죄인이 될 판이라, 나는 결국 대회의에서 있었던 모든 일을 처음부터 끝까지 설명해야 했다.

물론 중간중간 들어오는 질문에 대한 답도 함께.

“절반이 넘는 부족장들의 인정을 받았다고요?”

“예, 포권도 하더라고요. 부족민들이랑 혈육을 구해 줘서 고맙다고.”

“세상에. 기다려도 안 오시길래 충분히 짐작은 했는데……. 외부인, 그것도 한족이 부족 대회의에 참석한 건 남만, 아니 무림 역사상 최초일 거예요.”

놀라는 주화란의 모습에, 옆에 있던 남호가 푸근한 미소를 지으며 덧붙였다.

“암. 최초지. 부족 대회의에 외부인이 참석한 것도 최초고, 그 외부인이 백족 대족장이랑 한판 붙은 것도 최초지. 아암, 그렇고말고.”

“…….”

“…….”

“허허. 아주 자랑스럽고 기뻐서 웃음이 절로 나오는구나. 난 신경 쓰지 말고 계속해라.”

매우 신경 쓰였지만, 일단 계속했다.

“어쨌든 그렇게 대회의가 시작됐는데…….”

이어지는 내 설명을 듣고 있던 주화란이 눈을 동그랗게 떴다.

“혈승(血僧)이요?”

“네. 지금 귀주 땅을 휘젓고 있다더라고요. 벌써 기백 명을 쳐 죽이고 활개를 치고 있다던데 전 이번에 처음 들어 본 별호라서. 혹시 주 소저께서는 들어 본 적 있으세요?”

용봉표국의 본거지는 사천이고, 귀주는 사천의 남동쪽 방면과 맞닿아 있다.

더군다나 한동안 가세가 기울었다고는 하나 한때는 천하에서 손꼽히던 표국인 만큼 정보력도 상당하다.

‘그러니까 주 소저라면 알 수 있을지도.’

하지만 그런 기대감은 얼마 지나지 않아 급격히 사그라졌다.

내게 혈승의 특징을 전해 들은 주화란이 이내 고개를 내저었기 때문이었다.

“죄송해요. 어렴풋이 떠오르는 별호가 몇 있기는 한데, 그들 전부 그 정도의 고수는 아니라서. 그렇다고 특정한 용모파기가 있는 것도 아니고요.”

“음. 그래요?”

약간 실망감이 드는 건 사실이었지만, 크게 내색하지는 않았다.

주화란의 말마따나 용모파기도 없이 특징만으로 한 사람을 추려내는 것은 어려운 일이었으니까.

내가 알려 준 정보라고 해 봤자 고작 중년쯤 되는 나이에 초절정으로 예상되는 무공, 그리고 독문병기가 선장이라는 것 정도였다.

‘하긴, 무림이 얼마나 넓은데.’

넓은 건 땅덩어리뿐만이 아니다. 사람도 많다.

당장 잡철(雜鐵)로 만든 싸구려 칼 한 자루 차고 다니는 놈들도 비룡객이니, 검귀니 하는 별호를 지어 어깨에 힘주는 판국이었다.

‘끝없이 펼쳐진 모래사장에서 모래 한 알갱이를 찾는 셈이지.’

내가 입맛을 다시고 있던 그때, 미안한 표정을 짓고 있던 주화란이 문득 생각났다는 입을 열었다.

“아, 하지만 그런 부분에 관해서는 저 대신 송 호위가 더 잘 알고 있을 거예요. 그렇죠, 송 호위?”

어? 그러네?

나를 포함한 모두의 시선이 한쪽을 향해 쏠린다.

언제나 그렇듯 묵묵히 입을 다물고 있던 송일섬이 중얼거렸다.

“흠, 글쎄.”

글쎄는 개뿔이. 캐릭터 파악을 모두 끝낸 나는, 녀석에게 은자 한 냥을 던져 주며 말했다.

“어이, 추혼객(抽魂客). 아는 것 있으면 시원하게 털어놔 보지?”

지금은 일개 호위를 자처하고 있지만, 광동진가의 핏줄을 이은 무공의 천재이자, 새파란 나이에 백번이 넘는 생사결(生死結)에서 승리하며 낭인 세계의 전설이 되었던 녀석이 바로 송일섬이다.

어떻게 보면 낭인들만큼 사람과 소문에 민감한 직업군도 몇 없다. 당장 오늘 내일의 목숨이 걸려 있으니까.

탁.

날아든 은자를 잡아챈 송일섬이 눈살을 찌푸렸다.

“누구를 돈에 환장한 놈으로 아는군.”

“응.”

“…….”

“그래서, 싫어?”

“싫진 않지.”

“여기서 돈 더 주면?”

“더 좋지.”

“옜다, 은자 더 가져가라. 돈에 미친놈.”

휘익. 탁.

“……뭔가 기분이 더럽군.”

추가 수당을 낭낭하게 확보한 송일섬이 찜찜한 표정으로 입을 열었다.

“중년의 나이에, 선장을 사용한다고?”

“어, 듣기로는 강철로 만들어진 것 같다던데.”

“자세한 용모는?”

“그거까지는 몰라. 민머리에 수염이 없다는 것 빼고는. 남만까지 도망쳐 온 생존자도 거기까지만 알려 주고 죽어 버렸다고 들었고.”

“총체적 난국이군. 하지만 생각나는 인물이 셋 정도 있다. 선장을 독문 병기로 사용하는 무림인은 그리 많지 않으니까.”

“오, 셋씩이나?”

“딱 한 가지 문제가 있긴 한데…….”

“괜찮아. 말해 봐.”

그리고 나를 포함한 모두의 기대 어린 시선 속, 송일섬이 입을 열었다.

“죽었다.”

“어?”

“정확히는 내가 죽였다고 해야겠지. 하필이면 의뢰를 받고 전장에서 마주쳤거든.”

“음…… 뭐, 그럴 수도 있지. 그럼 나머지 둘은?”

“그게 무슨 소리지? 둘이라니?”

“방금 그랬잖아. 하나 죽였다고.”

“셋 다 죽였는데.”

“……?”

“둘은 전장에서, 하나는 생사결에서 죽였다. 마지막으로 만난 놈이 가장 강했지.”

“……!”

잠깐 무거운 침묵이 흘렀고, 모두의 심정을 대변하는 남호의 중얼거림이 들려왔다.

“미친 새끼가 하나 더 있었군.”

다른 미친 새끼가 누군지는 모르겠지만, 매우 동감이다.

나는 멀뚱멀뚱 서 있는 송일섬을 노려보며 고민했다. 우선 은자부터 뺏고 때릴지. 때리고 은자를 뺏을지.

그러다가 한심하다는 눈빛으로 송일섬을 바라보는 한 사람을 발견하고 문득 입을 열었다.

“어이, 거기 사파 잡졸.”

“……사파 잡졸?”

“그래. 넌 뭐 아는 거 없냐?”

작금 천하에서 가장 강성한 사파 세력이자, 감숙의 패자를 자처하는 대 흑룡마문. 그곳의 소문주인 사마표가 미간을 찡그렸다.

“말하고 싶은 것이 세 가지 있다. 첫째, 나는 사파 잡졸이 아니고. 둘째, 감숙과 귀주는 일천 리 가까이 떨어져 있어 왕래하기가 힘들다. 그리고 마지막 셋째. 그걸 왜 내가 알 거라고 생각한 거지?”

“네가 사파니까.”

“……?”

“원래 나쁜 놈들끼리는 서로 다 알고 지내는 법이잖아.”

“……!”

“뭐, 아니면 말고.”

석상처럼 굳어 버린 사마표를 향해 손을 내저은 나는, 그의 곁에 있는 또 다른 거대한 사파잡졸을 바라보았다.

그리고 뭐라 말을 꺼내기도 전에 우렁찬 대답을 들을 수 있었다.

꼬륵. 꾸르르륵.

“…….”

뭐여, 시벌.

무슨 월드컵 결승전도 아니고, 남만 한복판에서 울려 퍼진 힘찬 부부젤라 소리에 남호가 껄껄 웃었다.

“허허, 그놈 참. 내가 무공만 익혔어도 저 염병할 배때기를 갈라 버리는 건데. 으허허.”

아까부터 웃는 모습을 보니 정신이 반쯤 나간 모양이다. 그런 남호를 두려움 가득한 눈빛으로 바라본 혁무진이 입을 열었다.

“저기, 조장님.”

“대가리 박아.”

“예?”

“아, 습관적으로 그만. 미안하다. 근데 이 상황에서 다른 놈들처럼 헛소리하면 죽여 버릴 거야.”

“아니, 그게 아니라요. 혈승인지 뭔지 하는 그놈. 무림인치고는 정보가 너무 없는데요?”

그나마 지금까지 나온 말 중에서는 주화란 다음으로 정상적이다. 답답함에 뒤통수를 긁적인 나는 입맛을 다셨다.

“그렇긴 하지. 도대체 얼마나 나이를 처먹었는지, 어떻게 아는 사람이 하나도 없냐?”

살벌한 시선으로 태산을 노려보던 남호가 끼어들었다.

“나이를 처먹을 만큼 처먹은 입장에서 말하자면, 내가 알기로도 그런 놈은 없다. 과거 정마대전 때 살불(殺佛)이라는 마두가 있긴 했지만, 혈승이라는 놈의 특징과는 제법 차이가 있지. 당시에도 워낙 노괴였던지라 지금껏 살아 있을지조차 의문이고.”

단순한 이민족 늙은이라면 모를까, 남호는 은영각에서도 제법 중책을 맡았던 요원이었으니 그의 말이 맞을 가능성이 높다.

‘그럼 도대체 정체가 뭐지? 이 정도면 은거기인 수준인데.’

까마득한 과거의 인물인 남호도, 현세대에 속한 화룡각 대원들도 모른다면 그야말로 괴인(怪人)이다.

하지만 이 상황에서 가장 중요한 것은 혈승의 진짜 정체가 아니라, 놈의 배후와 목적이었다.

무릎을 툭툭 두드린 남호가 내 생각을 읽은 것처럼 입을 열었다.

“아직 확신할 수는 없지만, 혈승의 배후에는 암천이 있을 가능성이 농후하다.”

“동감입니다. 대회의에서도 그렇게 말했고요.”

“야수묘왕과 다른 부족장들은 어찌 생각하더냐?”

“우선은 일부 척후대와 전사들 일부를 귀주 방면으로 이동시키기로 결정이 났는데…… 그전에 백상이 보였던 반응이 마음에 걸리더군요.”

“중원의 일이니 더는 신경 쓰지 말라고 했겠군.”

“어?”

“하루 이틀 일도 아니니 그리 놀랄 것 없다. 정마대전 이후 백상은 중원의 일이라면 치를 떨었으니. 그나마 있던 남만의 교역로도 백족을 위시한 여러 부족들의 반발로 폐쇄되었지. 다만 지금 드는 의문은…….”

남호가 낮은 한숨과 함께 말을 이었다.

“그런 백상의 행보가 한족들의 전쟁에 휘말려 하나뿐인 자식을 잃은 슬픔 때문인지, 그 과정에서 정파 무림에 대한 어떤 원한을 품었는지다.”

“음.”

“만약 전자라면 자식 잃은 아비의 반발심으로 끝나겠지만, 후자의 경우라면…….”

조용히 흘러가는 이야기를 듣고 있던 주화란이 작게 뇌까렸다.

“배반(背叛)이겠죠. 남만 전체를 위태롭게 만들 만한.”

“그래, 맞다. 그가 암천과 손을 잡았다면 사태는 걷잡을 수 없이 커질 것이다.”

외부의 적보다 위험한 것이 바로 내부의 적이다.

제아무리 단단한 철옹성이라 할지라도, 내부에서부터 무너진다면 파도에 휩쓸린 모래성과 진배없다.

하물며 그 내통자가 야수묘왕과 함께 남만을 양분하는 대족장이라면.

‘말 그대로 끝장이지.’

어떻게든 밝혀 내고, 막아야 한다.

내부에서 벌어지는 흉계(凶計)의 정체도. 지금쯤 머나먼 귀주 땅에서 또다시 어딘가로 향하고 있을 혈승의 목적지도.

하지만 F급 헌터였던 나를 지금의 자리에 오르게 만들어 준 시스템이라 할지라도, 하나뿐인 몸뚱어리를 두 개로 나누어 주지는 못한다.

‘그렇다면…….’

나는 고개를 들어 주위의 사람들을 찬찬히 훑어보았다.

그들의 무공과 특징, 성격을 하나씩 떠올리고 고민했다. 누가 가장 적임자인지. 누가 알 수 없는 위험으로부터 살아 돌아올 수 있을지.

그리고 언제 끝날지 알 수 없는 깊은 생각에 빠져 있던 그 순간. 한 사람이 불쑥 입을 열었다.

“제가 갈게요.”

“……!”

“보내 주세요. 반드시 임무를 완수하고 돌아올 테니.”

나는 놀랐다. 일언반구도 하지 않았음에도 내 마음을 읽었다는 것에 한 번. 그 사람이 다른 누구도 아닌 주화란이라는 것에 다시 한번.

그리고 내 대답은 처음부터 정해져 있던 것처럼 튀어나왔다.

“안 됩니다.”

“왜요? 제가 혈승이라는 노괴(老怪)에게 해를 입을 것 같나요?”

“그건…….”

“비록 각주님께 비하면 일천한 무공이겠지만, 제 한 몸 지킬 정도의 수준은 된다고 생각해요.”

“주 소저.”

“걱정하시는 바를 알아요. 물론 혈승을 상대하기에는 역부족이겠죠. 하지만 남만야수궁이 가려 뽑은 전사들이 함께할 것이고, 여기 있는 대원들 중 일부도 함께할 거예요. 제 말이 틀렸다면 말씀해 주세요.”

나는 대답 대신 굳게 입을 다물었다. 주화란의 말은 틀림없는 사실이었으니까.

화룡각 대원 중 일부를 선발하여 곧 출발할 척후조에 끼워 넣고, 그들로 하여금 혈승의 정체와 목표를 알아낼 생각이었다. 최악의 경우 벌어질 전투도 감안해서.

다만 한 가지, 미처 생각하지 못했던 것은 주화란의 지원이었다.

“각주님. 아니, 은인.”

은인. 몇 달 전 사천에서 용봉표국의 일이 끝난 직후, 그녀가 처음 나를 불렀던 호칭이다.

떠나기 전 마지막으로 걸었던 화원(火院)의 꽃내음이 스쳐 지나가는 듯했다.

그리고 달빛 아래에서 촉촉하게 젖어있던 한 사람의 눈동자는, 지금 굳은 결의로 빛나고 있다.

“보내 주세요. 저를.”

“……!”

“할 수 있어요.”

문득 그런 생각이 들었다.

저 눈. 저 목소리로 하는 부탁을 앞으로도 영원히 거절할 수 없을 거라는 생각을.

후우.

바람은 덥고, 입맛은 썼다.

작게 한숨을 내쉰 나는 마침내 고개를 끄덕였다.

동시에 환하게 밝아지는 주화란의 얼굴. 어느덧 저 멀리에서는 연회의 시작을 알리는 연주 소리가 들려오고 있었다.
```

## Final English reading copy

```markdown
# Chapter 646

If this continued, I was liable to be branded a traitor guilty of high treason, so in the end, I had to explain everything that had happened at the tribal grand council from beginning to end.

Of course, I also had to answer the questions that came up along the way.

“More than half of the chieftains acknowledged you?”

“Yes. They even gave me cupped-fist salutes. They thanked me for saving their tribespeople and blood relatives.”

“My goodness. When you didn’t come even after we waited for you, I had a good idea of what must have happened… But for an outsider—especially a Han Chinese person—to attend the tribal grand council is probably a first in the history of Nanman. No, in the history of the Murim.”

At Ju Hwaran’s astonished expression, Namho, who was sitting beside her, added with a warm smile.

“Of course it’s a first. An outsider attending the tribal grand council was a first, and that outsider getting into a fight with the great chieftain of the Bai people was a first too. Yes, indeed.”

“……”

“……”

“Hoho. I’m simply laughing because I’m so proud and happy. Don’t mind me. Please continue.”

It bothered me a great deal, but I continued for the moment.

“Anyway, that’s how the grand council began, and then…”

Ju Hwaran’s eyes grew round as she listened to my explanation.

“The Blood Monk?”

“Yes. Apparently, he’s rampaging through Guizhou right now. I heard he’s already beaten several hundred people to death and is running wild. This was the first time I’d heard that sobriquet, so I was wondering if Young Lady Ju had ever heard of him.”

The Yongbong Escort Bureau’s headquarters was in Sichuan, and Guizhou bordered Sichuan to the southeast.

Furthermore, although its fortunes had declined for a while, it had once been one of the most renowned escort bureaus in the world, so its intelligence network was considerable.

*So Young Lady Ju might know something.*

But that hope quickly faded.

After hearing the Blood Monk’s characteristics from me, Ju Hwaran shook her head.

“I’m sorry. A few sobriquets vaguely come to mind, but none of them belonged to a master of that caliber. Besides, there’s no specific sketch or description of his appearance.”

“Hmm. Is that so?”

I was admittedly a little disappointed, but I did not show it too much.

As Ju Hwaran had said, narrowing down one person based only on a few characteristics, without even a sketch of his appearance, was difficult.

All I had been able to tell her was that he was probably a middle-aged man, that his martial arts were expected to be at the Supreme Peak level, and that his unique weapon was a Zen staff.

*Well, the Murim is a huge place.*

And it wasn’t only the land that was vast. There were countless people, too.

Even men who carried cheap swords made of scrap iron went around puffing out their chests after giving themselves sobriquets like Soaring Dragon Guest or Sword Fiend.

*Finding him would be like searching for one grain of sand on an endless beach.*

Just as I was clicking my tongue, Ju Hwaran, who had been wearing an apologetic expression, suddenly spoke up as though she had remembered something.

“Oh, but Song Captain would know more about that than I do. Right, Captain Song?”

Oh. She was right.

Everyone’s eyes, including mine, turned toward one person.

As always, Song Ilseom remained silent for a moment before muttering,

“Hmm. I don’t know.”

*Like hell you don’t.*

Having already figured out exactly what kind of person he was, I tossed him a silver nyang and spoke.

“Hey, Soul-Chasing Guest. If you know something, why don’t you lay it all out?”

Although he currently pretended to be nothing more than an escort, Song Ilseom was a martial arts prodigy descended from the Guangdong Chen Family. At an absurdly young age, he had won more than a hundred life-and-death duels and become a legend among wandering martial artists.

In some ways, there were few professions more sensitive to people and rumors than wandering martial artists. Their lives could depend on it from one day to the next.

*Clack.*

Song Ilseom snatched the silver out of the air and frowned.

“What kind of person do you take me for? Someone obsessed with money?”

“Yes.”

“……”

“So, you don’t like it?”

“I don’t dislike it.”

“What if I give you more money?”

“That would be even better.”

“Here. Take more silver, you money-crazed bastard.”

*Whoosh. Clack.*

“……Somehow, this feels even worse.”

After securing a generous bonus, Song Ilseom opened his mouth with an uneasy expression.

“A middle-aged man who uses a Zen staff?”

“Yeah. I heard it was made of steel.”

“What does he look like?”

“I don’t know that much. Aside from the fact that he’s bald and has no beard. I heard the survivor who escaped all the way to Nanman only managed to tell them that much before he died.”

“This is a complete mess. Still, I can think of about three people. There aren’t many martial artists who use a Zen staff as their unique weapon.”

“Oh, there are three?”

“There is one small problem, though……”

“That’s fine. Tell me.”

Then, amid the expectant gazes of everyone present, including mine, Song Ilseom opened his mouth.

“They’re dead.”

“Huh?”

“More precisely, I should say I did the killing. I happened to cross paths with my quarry on a battlefield while carrying out a commission.”

“Hmm… Well, that can happen. What about the other two?”

“What are you talking about? What other two?”

“You just said you killed one.”

“I killed all three.”

“……?”

“I killed two on battlefields and one in a life-and-death duel. The last one I met was the strongest.”

“……!”

A heavy silence descended over the room. Then Namho’s mutter spoke for everyone.

“There was another crazy bastard.”

I didn’t know who the other crazy bastard was, but I wholeheartedly agreed.

I stared at Song Ilseom, who was standing there with a blank expression, and considered my options.

Should I take back the silver first and then beat him up? Or beat him up first and then take back the silver?

Then I noticed someone looking at Song Ilseom with an expression of utter contempt and spoke up.

“Hey, you unorthodox grunt over there.”

“……Unorthodox grunt?”

“Yeah. Do you know anything?”

Sama Pyo, the Young Sect Leader of the Black Dragon Demon Gate—the most powerful unorthodox faction in the world at present and the self-proclaimed hegemon of Gansu—knitted his brows.

“I have three things to say. First, I am not an unorthodox grunt. Second, Gansu and Guizhou are nearly a thousand li apart, making travel between them difficult. And third. Why did you think I would know something like that?”

“Because you’re part of the unorthodox faction.”

“……?”

“Bad people all know one another, don’t they?”

“……!”

“Well, maybe not.”

I waved a hand at Sama Pyo, who had frozen like a stone statue, and looked toward the other enormous unorthodox grunt standing beside him.

Before I could even say anything, a booming answer reached my ears.

*Grrrrowl. Grrrrrrrrowl.*

“……”

*What the fuck?*

This wasn’t some World Cup final. Yet a vigorous vuvuzela blast rang out in the middle of Nanman, and Namho burst out laughing.

“Hoho. What a bastard. If only I’d learned martial arts, I’d split open that goddamn gut. Hahaha!”

Judging by how much he had been laughing, he seemed to be half out of his mind.

Hyuk Mujin, who was staring at Namho with fear in his eyes, opened his mouth.

“Captain.”

“Put your head down.”

“What?”

“Ah, sorry. That was just a habit. But if you start talking nonsense like the others in this situation, I’ll kill you.”

“No, that’s not what I meant. That Blood Monk fellow. There’s too little information about him for a martial artist, isn’t there?”

Of everything that had been said so far, it was the second most sensible thing after Ju Hwaran’s comment.

I scratched the back of my head in frustration and clicked my tongue.

“That’s true. How fucking old is he, anyway? How is there not a single person who knows him?”

Namho, who had been glaring at Taishan with a murderous look, cut in.

“Speaking as someone who’s eaten more years than I care to count, I can say that there is no such man as far as I know. There was a fiend called the Killing Buddha during the Great Faction War, but his characteristics differed quite a bit from those of this Blood Monk. He was already an ancient monster even back then, so it’s questionable whether he could still be alive.”

Namho might have been an old foreigner, but he had once held a fairly important position in the Hidden Shadow Pavilion, so he was probably right.

*Then what the hell is his identity? At this point, he’s practically a hermit master.*

If even Namho, a man from the distant past, and the Fire Dragon Pavilion members of the current generation had never heard of him, then he was truly a freak.

But the most important thing in this situation was not the Blood Monk’s true identity. It was the power behind him and his purpose.

Namho tapped his knees as though he had read my thoughts and spoke.

“I cannot be certain yet, but there is a strong possibility that Dark Heaven is behind the Blood Monk.”

“I agree. I said as much at the grand council.”

“What do the Beast Miao King and the other chieftains think?”

“We decided to send some scouts and warriors toward Guizhou first, but before that… Baeksang’s reaction bothered me.”

“He must have told you not to concern yourselves with it because it was a matter involving the Central Plains.”

“Huh?”

“It isn’t as though this is the first or second time something like that has happened, so you shouldn’t be surprised. Ever since the Great Faction War, Baeksang has shuddered whenever the matter involved the Central Plains. Even the few trade routes Nanman had were closed because of opposition from several tribes, led by the Bai people. However, the question that occurs to me now is……”

Namho continued with a low sigh.

“Was Baeksang’s behavior caused by the grief of losing his only child after being caught up in a war between Han Chinese people? Or did he develop some kind of grudge against the orthodox Murim in the process?”

“Hmm.”

“If it was the former, then it would amount to nothing more than the resentment of a father who had lost his child. But if it was the latter……”

Ju Hwaran, who had been quietly listening to the conversation, murmured,

“It would be betrayal. The kind that could place all of Nanman in danger.”

“Yes, exactly. If he has joined hands with Dark Heaven, this situation will grow beyond control.”

More dangerous than an enemy from outside was an enemy from within.

No matter how impregnable a fortress was, if it collapsed from the inside, it was no different from a sandcastle swept away by the waves.

And if that traitor was a great chieftain who shared control of Nanman with the Beast Miao King—

*Then it was all over.*

I had to uncover it and stop it somehow.

The identity of the sinister plot unfolding within Nanman. And the destination of the Blood Monk, who by now would be heading somewhere else in the distant land of Guizhou.

But even the System that had raised me from an F-rank Hunter to my current position could not split my one body into two.

*In that case……*

I raised my head and slowly looked over everyone around me.

I recalled their martial arts, characteristics, and personalities one by one as I considered who was best suited for the task. Who could return alive from an unknown danger?

And just as I was sinking into a deep train of thought with no end in sight, one person suddenly spoke.

“I’ll go.”

“……!”

“Please send me. I will complete the mission and return without fail.”

I was shocked.

First, because she had read my mind even though I had not said a single word. And again because that person was none other than Ju Hwaran.

My answer burst out as though it had been decided from the beginning.

“No.”

“Why? Do you think I’ll be harmed by that old monster called the Blood Monk?”

“That’s……”

“My martial arts may be meager compared to yours, Pavilion Master, but I believe I am strong enough to protect myself.”

“Young Lady Ju.”

“I know what you’re worried about. Of course, I would be no match for the Blood Monk. But handpicked warriors from the Nanman Beast Palace will be accompanying us, and some of the members here will come too. Tell me if I’m wrong.”

Instead of answering, I pressed my lips together.

What Ju Hwaran had said was undeniably true.

I intended to select some of the Fire Dragon Pavilion members and add them to the scouting party that would soon depart, having them uncover the Blood Monk’s identity and objective. I was taking into account the possibility of a battle in the worst-case scenario.

But the one thing I had not considered was Ju Hwaran’s participation.

“Pavilion Master. No, Benefactor.”

*Benefactor.*

That was what she had first called me several months ago, right after the Yongbong Escort Bureau’s business in Sichuan had ended.

For a moment, the scent of flowers from the Fire Courtyard, where we had taken our last walk before leaving, seemed to drift past me.

And the eyes that had been moist beneath the moonlight were now shining with firm determination.

“Please send me. Send me.”

“……!”

“I can do it.”

A thought suddenly occurred to me.

*Those eyes. That voice.*

I would never be able to refuse a request made in that voice and with those eyes.

*Whew.*

The wind was hot, and my mouth tasted bitter.

I let out a small sigh and finally nodded.

At the same time, Ju Hwaran’s face lit up brightly.

From somewhere in the distance, music announcing the beginning of the banquet had begun to play.
```

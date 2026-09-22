<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0622.txt",
      "sha256": "7095bbebc0887a133e9f38d6b45aebfaea665efa9fc2a5a3e35ddaa53187a318",
      "bytes": 13288
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1c77cfaf2492934d913cb2ae2a6124cbce1110fec759e0c5e6c05fff02d451a7",
      "bytes": 1540
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ed8b5f1275828f77a95de0c602b8557fa857c9174e1458041eebdd2162a24160",
      "bytes": 192785
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "4724657503df6111f038d2d1c944d249c4caf7b968eea0d6cff0003ebc1417ac",
      "bytes": 1206
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c0967a5b1f729a9482bf05f10a4945fcc1cd3cb4b1e2d6dd477431b465d79749",
      "bytes": 1702
    },
    {
      "path": "characters/Ju Gongsan.md",
      "sha256": "34a22586057f5c6f5d4790c0cabd27ab98eabddffb23d20e5bf1ec45b915df7f",
      "bytes": 900
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "178d59589612bf36966c8a9f5d46cad7ae4b5a40fd1b40d6cf8c0bb4561e15eb",
      "bytes": 988
    },
    {
      "path": "characters/Namho.md",
      "sha256": "0902da6eabc0f65b484bcffadc9782025ab96b48387d80d2b1bc5b6b21c39e4a",
      "bytes": 809
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "1a7b5e6ee24be8167f63ef20450923d96da155cc4e136b97610a8a8545b4bd06",
      "bytes": 899
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "fd8394b46d9f9c838cbb160b9f1b6068e70f0d07c396680bd0665a61b46b8a6d",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "588604279402512a7c019342fa2da0803131b536e7887e760c589e58001e4b02",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "d94a63fbb87e486443c4cfce54bfc5a4218943158cdc441a829e032da351917e",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "82b2a311822797f8d4e776ed21c6e009ee6203d1844ad848c4ef951fecc8b194",
      "bytes": 195658
    }
  ],
  "estimated_tokens": 12238
}
-->

# Durable State Update — Chapter 622

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 622. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 622. Profile updates may replace only one
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
  "chapter": 622,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 622,
    "continuity_sources": [622],
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
    "The Fire Dragon Pavilion is traveling through Nanman under Namho's guidance toward the Nanman Beast Palace.",
    "The Nanman Beast Palace Quest is Grade Supreme Peak and requires Jin Taekyung and the Fire Dragon Pavilion to arrive at the palace.",
    "The Quest's reward is an unknown Chain Quest.",
    "The party has reached the vicinity of the Nanman Beast Palace after crossing Ailao Mountain and traveling for four days.",
    "The party is concealing its identities because Nanman's non-Han peoples are hostile toward Han Chinese.",
    "Dark Heaven is targeting Nanman, and Taekyung believes a catastrophe involving the rift is imminent.",
    "The Beast Miao King participated in the Great Faction War and is believed to favor Jeok Cheongang and the Fire Gate Clan."
  ],
  "continuity_sources": [
    621
  ],
  "open_questions": [
    "Was the woman in the Heavenly Demon Escort Bureau group the Southern Heaven Demon Empress?",
    "Who poisoned and killed the Heavenly Demon Escort Bureau group, and why?",
    "What catastrophe will Dark Heaven cause in Nanman?",
    "What dangers and response await the Fire Dragon Pavilion inside the Nanman Beast Palace?"
  ],
  "safe_through": 621,
  "temporary_decisions": [
    "Render 南琥, Namho's code name, as Namho rather than translating it literally as southern amber.",
    "Use Elder Chao for the local title 챠오 어르신.",
    "Render 애뇌산 as Ailao Mountain.",
    "Render 혈생균 as blood-feeding fungus."
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
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 주공산 | **Ju Gongsan** | Former head and founder of the Yongbong Escort Bureau. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 묘족 | **Miao people** | Ethnic group the Escort Bureau expects to encounter near Yunnan. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |

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

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 621
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 621
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Ju Gongsan.md

# Ju Gongsan (주공산)

- **Safe through:** Chapter 615
- **Aliases:** Escort King
- **Role:** Founder and former head of the Yongbong Escort Bureau; during the Great Faction War, he was a wandering escort who refused to surrender a pregnant woman of the Guangdong Chen Family to the Demonic Cult after accepting her escort fee, carried her from Guangdong through Jiangxi and Hubei to Henan over two years, and became known as the Escort King; he later founded an escort bureau in his hometown of Shaanxi and died from internal injuries sustained during the war.
- **Personality:** Remarkably skilled, chivalrous, principled, and unwavering in his obligations.
- **Voice:** Not established.
- **Relationships:** Ju Hogun was his only blood child and successor as head of the Yongbong Escort Bureau; Ju Hwaran is his granddaughter.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 620
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 621
- **Aliases:** Elder Chao
- **Role:** Namho is a non-Han Hidden Shadow Pavilion agent who operated for decades under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, observant, and willing to use theatrical violence and crude insults to protect an intelligence operation.
- **Voice:** Measured and serious in private, but loudly abusive and convincing when maintaining his local cover.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 621
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 620
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 620
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 621
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃622화



순수하게 무림에서 보낸 시간만 따져도 어언 1년이 훌쩍 넘었다.

뜻하지 않게 여러 사건에 얽히다 보니 산서성을 벗어나 타지를 전전하게 되었고, 그 과정에서 숱한 인간 군상과 그들이 속한 문파를 방문하기도 했다.

하지만 단언컨대, 그 어떤 거대 문파라 해도 지금 내 눈 앞에 펼쳐진 광경과는 비교조차 할 수 없을 것이다.

“허.”

“미친…….”

곳곳에서 탄성이 터져 나왔다.

산봉우리에서 봤을 때도 엄청난 면적이라는 건 알았지만 이 정도일 줄이야.

운무(雲霧)가 사라지고 목적지에 점점 가까워질수록 내 입도 점점 더 크게 벌어졌다.

‘아니, 이게 문파라고?’

두 가지 의미로 놀라웠다.

첫 번째 놀라움은 앞서 말했듯이 그 광활함에서 오는 것이었고, 두 번째는…….



남만야수궁(南蠻野獸宮)



광활한 면적을 둘러싼 울타리와 누군가 엉성한 글씨체로 휘갈겨 쓴 목판 때문이었다.

높고 단단한 성벽이나 철문이 아니라, 말 그대로 울타리다. 울타리.

‘……아니. 이게 문파라고?’

같은 생각. 다른 의미.

심지어 울타리가 멀쩡한 것도 아니다.

반쯤 허물어진 울타리를 보며 잠깐 생각에 잠겨 있던 내가 남호를 향해 물었다.

“남 노인, 설마 여기가 진짜…….”

“남만야수궁이 맞냐고?”

“아, 예.”

내가 고개를 끄덕이자, 남호가 담담하게 입을 열었다.

“자네, 글 읽을 줄은 아나?”

“당연하죠.”

“그럼 저 글씨 좀 읽어 보게. 아니, 내가 대신 읽어 주는 게 낫겠군.”

남호가 엉성한 글씨로 적힌 표지만을 가리키며 말을 이었다.

“남. 만. 야. 수. 궁.”

“…….”

“적힌 그대로일세. 이곳부터가 남만야수궁이야.”

알긴 안다. 머릿속에 예상했던 그림을 아득히 벗어나서 문제지.

위에서 언뜻 봤을 때는 엄청 거대한 건축물이 있나 보다, 싶었는데 막상 안개를 벗어나 가까운 곳에서 목격하니 이건 숫제 허허벌판이 아닌가.

“조장님, 남만야수궁이 아니라 그냥 남만목장 아닙니까? 사방에 울타리만 쳐져 있고.”

주위를 둘러보던 주화란도 혁무진의 떨떠름한 말에 고개를 끄덕였다.

“저도 남만야수궁은 처음이라 잘은 모르겠지만…… 궁이라고 부르기에는 손색이 있긴 하네요.”

묵묵히 상황을 지켜보던 송일섬과 사마표도 한마디씩 보탰다.

“확실히 이상한 부분이 있구려.”

“혁무진의 말대로 사람이 안 보인다는 점이 걸리는군. 그렇다고 다른 전각이나 건물이 있는 것도 아니고. 그렇지 않으냐, 태산?”

“주군. 태산이 배고프다. 저 버섯 먹어도 되나?”

사마표가 단번에 고개를 저었다.

“안 된다.”

“그럼 소는? 저기 걸어가는 소가 맛있어 보인다.”

“흑룡마문의 소문주라고 했나? 이건 부탁인데, 저 금수만도 못한 놈 주둥이 좀 틀어막게. 한 번 더 들으면 복장 터져서 죽을 것 같으니까.”

“……알겠소.”

“하나 더. 지금 눈에 보이는 모든 풀과 짐승들은 남만야수궁의 것일세. 부디 잊지 말라고. 터지기 직전의 내 복장도.”

부쩍 늙은 얼굴로 사마표에게 엄중한 경고를 날린 남호가, 광활한 대지를 가리키며 말을 이었다.

“그리고 자네들의 생각은 충분히 이해하네만, 나는 이곳이 남만야수궁이라고 한 적은 없네.”

“예? 아까 분명 그러셨는데요.”

“아닐세.”

“아, 혹시 노망나셨습니까?”

“…….”

표정이 급격히 어두워지는 것을 보니 확실하다. 나는 측은지심을 담아 남호를 바라보았다.

“저런. 그래도 괜찮을 겁니다. 저와 가까운 지인 중에도 노환으로 고생하셨던 분이 있는데, 지금은 거의 다 나으셨거든요.”

“먼저 세 가지를 말하고 싶군. 첫째, 난 노환이 아닐세. 둘째. 이건 듣는 와중에 살짝 궁금해져서 묻는 건데, 자네 지인이라는 그분은 어떻게 노환을 이겨 낸 건가?”

“반로환동이요.”

“……그거 아주 좋은 방법이로군. 내가 무공을 익히지 않은 여든 살 노인이라는 것만 빼면.”

“원래 인생은 여든부터 아닙니까.”

“자네 인생을 여기에서 끝내고 싶지만, 힘이 없으니 참겠네.”

솟구치는 울화를 삭힌 남호가 말을 이었다.

“마지막 세 번째는 앞서 했던 말과 동일하네. 나는 이곳이 남만야수궁이라는 말을 한 적이 없어. ‘이곳부터’ 남만야수궁이라고 했지.”

“아.”

비슷하지만 의미는 확실히 다르다.

이제야 남호의 말이 의미하는 바를 깨달은 내가 되물었다.

“그럼?”

“맞네. 이곳은 남만야수궁의 지배하에 놓인 땅 중 하나일세. 남만의 다른 지역과는 달리 궁주가 직접 다스리는 직할지(直轄地)라고 하면 더 이해하기 쉽겠군.”

“황제가 천하 곳곳에 번왕(藩王)이나 성주를 두는 것과 비슷한 느낌이군요. 이곳은 한 나라의 수도인 셈이고.”

“정확하네. 물론 궁주의 권위가 천자에 미치지 못하고, 남만에 존재하는 여러 부족장의 권위는 성주 이상이라는 차이가 있긴 하지만.”

남호의 이야기를 듣고 있던 주화란이 나직한 탄성과 함께 입을 열었다.

“그러고 보니 오래전 조부님께서 남긴 기록에서 그런 글귀를 읽은 적이 있어요. 남만은 하나의 왕국이며, 남만야수궁은 다섯 개의 현읍을 아우르는 거대한 목장과 같다고.”

“표왕의 손녀답군. 하지만 그 주공산 대협도 이 울타리 너머까지 도달한 적은 없다네. 이민족이 아닌 이들은 출입할 수 없거든.”

“그 정도입니까?”

“그 정도일세.”

남호의 말이 사실이라면, 폐쇄성으로는 천하에서 둘째가라면 서러운 문파인 사천당가도 남만야수궁에는 한 수 접어줘야 한다.

혀를 내두른 나는 끝없이 늘어선 울타리와 목초지 너머를 바라보았다.

“그런데 저희는 들어가야 하잖습니까.”

“그렇지.”

“다른 방법이라도 있습니까? 혹시 남 노인께서는 이민족이니까 출입이 가능…….”

“외지인의 출입이 불가능하다고 했지, 이민족이라고 해서 출입이 쉽다고 한 기억은 없네만.”

“아.”

“이곳에서 나는 그저 힘없고 평범한 묘족 늙은이일 뿐일세. 만약 암천이 천하에 마수를 뻗지 않았고, 자네들이 찾아오지 않았다면 조용히 생을 마감했을…… 호로 새끼!”

남호의 갑작스러운 호통에 깜짝 놀란 나는 눈을 크게 떴다.

“아니, 남 노인. 왜 자책을 하세요. 조용히 생을 마감한다고 호로 새끼라니.”

“나 말고! 저 새끼! 저 시벌 호로 새끼 붙잡아!”

금방이라도 숨이 넘어갈 듯한 남호의 외침에 고개를 돌린 우리는, 울타리를 넘어 엉금엉금 기어가는 커다란 궁둥이를 볼 수 있었다.

그 앞에서 평화롭게 풀을 뜯고 있는 누런 송아지 한 마리도.

“어. 어어?”

“저놈, 설마.”

“저 새끼 언제 저기까지 갔어!”

“태 소협!”

“태산아!”

사람들의 목소리에 이어, 마지막으로 울려 퍼진 사마표의 부르짖음에 태산이 움찔한 그 순간.

음머?

이상함을 알아차린 송아지가 번쩍 고개를 치켜들었다.

어느새 가까워진 태산의 모습에 커다랗고 맑은 눈망울에 느낌표가 떠올랐고, 동시에 아직 완전히 자라지 않은 발굽이 풀을 밟았다.

타다닥!

빠른 상황 판단과 도주 시도. 그러나 송아지보다 태산이 한발 빨랐다.

“소고기! 거기 딱 서라!”

굳은 의지가 담긴 외침과 함께 태산의 거대한 덩치가 허공을 날았다.

호랑이나 표범 같은 맹수도 아니고, 덜 자란 송아지가 어떻게 작정하고 움직인 절정 고수를 피하겠나.

쿵, 하는 둔중한 소리와 함께 밑에 깔린 송아지가 비명을 질렀다.

음머어어어!

듣기만 해도 눈시울이 축축해지는 애달픈 울음소리였지만, 연이은 강행군과 적량 배식으로 뱃가죽이 뒤집힌 태산에게는 입가가 축축해질 만한 소리였다.

“태산이! 소고기!”

“당장 저 새끼 붙잡아!”

남호의 외침이 끝나기도 전, 이미 울타리를 넘어 쇄도한 내 신형은 태산의 코앞까지 도달해 있었다.

덥석.

“놔라! 소고기 육회!”

“그만해. 이 피도 눈물도 없는 미친놈아. 워낭소리도 못 봤어?”

“못 봤다!”

“……아.”

그건 그렇겠네.

순간 납득이 되긴 했지만 그건 그거고 이건 이거다. 단번에 태산의 뒷덜미를 잡아챈 나는 적당히 힘을 주어 뒤로 당겼다.

산만 한 덩치가 뒤로 나동그라지자 겨우 살아난 소고기. 아니, 송아지가 벌떡 일어나 달리기 시작했다.

두두두두!

사정없이 뒤집히는 풀과 일어나는 먼지.

꽁무니가 빠져라 목초리를 벗어나는 송아지의 엉덩이를 바라보며, 태산이 구슬프게 중얼거렸다.

“안 된다. 태산이 우둔살…….”

이 새끼는 고향이 무슨 마장동인가.

내가 녀석의 출신 성분을 의심하고 있던 그때, 남호가 불같은 외침과 함께 길길이 날뛰었다.

“노옴!”

“남 노인. 진정하세요, 진정.”

“지금 진정하게 생겼나! 남만야수궁의 영역에서는 아무것도 건드리지 말라고 그토록 신신당부했거늘! 이 덩치 큰 식충이 새끼가 어른 말을 귓등으로도 안 듣고 사고를 쳐?”

황급히 달려온 사마표가 남호와 태산 사이를 가로막았다.

“미안하오, 남 노인. 내가 잠시 한눈을 판 사이에 그만…… 태산이 네 이 녀석, 당장 사과드리지 못하겠느냐.”

태산이 남호를 똑바로 바라보며 대답했다.

“태산이. 배고프다.”

“저 씨벌놈이. 당장 이 손 놓게. 놔. 안 놔? 내가 이 꼴 보려고 남만에서 오십 년 넘게 모기 물려 가며 기다린 줄 알아?”

역시 인생은 여든부터가 확실하다. 무공도 안 익혔으면서 적천강도 한 수 접어들 정도의 기세를 뿜어내는 남호만 봐도 알 수 있었다.

활화산처럼 날뛰던 늙은 은영각 요원이 진정한 것은 그로부터 일각이 흐른 뒤였다.

“후. 이제 괜찮아졌으니 손 놓게.”

“정말 괜찮으신 거 맞습니까?”

“잠깐 사이에 오장육부가 한 바퀴 뒤집히긴 했는데, 당장 죽을 정도는 아닐세.”

180도 돌았다면 문제가 있지만 360도는 인정이지.

고개를 끄덕인 내 눈짓에 혁무진이 손을 놓자, 남호가 임종을 앞둔 얼굴로 한숨을 내쉬었다.

“그래, 그나마 아무 일도 없었으니 다행이지. 남만야수궁의 인물이 그 꼴을 봤었다면 초장부터 일이 어긋났을 게야.”

중원의 다른 문파였다면 소 한 마리 정도쯤이야, 라고 생각할 수도 있지만 이건 결국 문화와 사람의 차이다.

초원의 유목민들이 말을 목숨처럼 아끼는 것처럼, 부족 간의 불화와 경계가 확실한 이곳에서는 가축이 큰 재산이었다.

‘이름부터가 남만야수궁인데, 뭐.’

척 들어도 동물 친화적인 냄새가 솔솔 풍기지 않나.

괜히 남호가 처음부터 아무거나 건드리지 말라고 한 게 아니었다.

“그럼 이제부터는 어떻게 합니까? 사람 나타날 때까지 여기서 기다릴 수도 없는 노릇이고.”

“허락 없이 남만야수궁의 영역을 침범했다가는 분란이 일어날 걸세. 그렇다면 응당 다른 방법을 찾아야지.”

혁무진의 물음에 대답한 남호가 봇짐에서 뭔가를 꺼내 들었다.

“그게 뭡니까?”

“비상시에 사용하는 신호용 폭죽일세. 이게 터진다면 최소한 누군가 나와보기라도 하겠지.”

남호가 자신 있는 미소와 함께 화섭자로 불씨를 당겼다.

치지직. 빠르게 끝부분으로 타들어 가는 심지.

동시에 커다란 소리와 함께 폭죽이 솟구쳤다.

쐐애애액, 퍼어엉!

문제는, 폭죽에서 솟구친 불꽃이 허공이 아니라 목초지에 떨어졌다는 거다.

“……어?”

“……어어?”

화륵, 콰아아아!

사람들의 얼빠진 음성과 함께 화염에 흽싸인 목초지.

사방으로 도망치는 가축들을 멍하니 바라보던 내가 중얼거렸다.

“……확실히 누가 나와 보긴 하겠네.”

“……이, 이게 아닌데.”

아니긴 개뿔. 좆 됐구만.

그리고 내가 참혹한 마음으로 불타는 목초지를 바라보던 그때였다.

크아아앙!

맹수의 거친 포효와 함께, 불타는 목초지의 언덕 너머에서 한 인영이 모습을 드러냈다.
```

## Final English reading copy

```markdown
# Chapter 622

Even counting only the time I had spent in the Murim, well over a year had already passed.

After getting tangled up in one incident after another, I had left Shanxi Province and spent my days traveling from place to place. Along the way, I had met all kinds of people and visited the sects they belonged to.

But I could say this with certainty: no matter how large or powerful a sect was, none of them could even compare to the sight unfolding before my eyes.

“Whew.”

“You’ve got to be kidding me…”

Exclamations erupted from all around us.

I had known it covered an enormous area even when I saw it from the mountain peak, but I hadn’t expected anything like this.

As the clouds and mist faded and we drew closer to our destination, my jaw dropped wider and wider.

*No, seriously. This is a sect?*

It was astonishing in two different ways.

The first, as I had already mentioned, was the sheer vastness of the place. The second was…



**Nanman Beast Palace**



The fence surrounding the vast grounds, and the wooden sign someone had scrawled in an atrocious hand.

It wasn’t a high, sturdy fortress wall or an iron gate.

It was literally a fence.

A fence.

*…No, seriously. This is a sect?*

The thought was the same. The meaning was different.

The fence wasn’t even in good condition.

I stared at the half-collapsed fence for a moment before turning to Namho.

“Elder Namho, surely this isn’t really…”

“You’re asking if this is truly the Nanman Beast Palace?”

“Ah, yes.”

When I nodded, Namho calmly opened his mouth.

“Can you read?”

“Of course.”

“Then read that sign over there. No, I suppose it would be better if I read it for you.”

Namho pointed at the sign covered in clumsy writing and continued.

“Nan. Man. Beast. Palace.”

“……”

“It says exactly what it says. The Nanman Beast Palace begins here.”

I knew that.

That was the problem.

It was so far beyond the image I had imagined in my head that I didn’t know what to make of it.

When I had seen the place from above, I had assumed there must be some enormous structure here. But now that we had emerged from the mist and come close enough to see it clearly, this was practically an empty field.

“Captain, shouldn’t this be called the Nanman Ranch instead of the Nanman Beast Palace? There are nothing but fences all around us.”

Ju Hwaran, who had been looking around, nodded at Hyuk Mujin’s dubious comment.

“This is my first time at the Nanman Beast Palace, so I can’t say I know much about it, but… it does fall short of deserving the name palace.”

Song Ilseom and Sama Pyo, who had been silently observing the situation, each added a comment.

“There is certainly something strange about this.”

“As Hyuk Mujin said, it bothers me that we haven’t seen a single person. There aren’t any other pavilions or buildings, either. Am I wrong, Taishan?”

“My lord. Taishan is hungry. Can Taishan eat that mushroom?”

Sama Pyo immediately shook his head.

“No.”

“Then what about the cow? That cow walking over there looks delicious.”

“You said you were the Young Sect Leader of the Black Dragon Demon Gate, didn’t you? This is a favor, but please shut the mouth of that beast worse than an animal. If I hear one more word, I think my chest will burst and kill me.”

“……I understand.”

“One more thing. Every blade of grass and every animal you can see belongs to the Nanman Beast Palace. Please don’t forget that—or that my insides are about to burst.”

After issuing Sama Pyo a stern warning with a face that had suddenly aged, Namho pointed toward the vast land and continued.

“I understand your thinking perfectly well, but I never said this place was the Nanman Beast Palace.”

“What? You definitely said that a moment ago.”

“I did not.”

“Ah. Have you perhaps lost your mind with age?”

“……”

Namho’s expression darkened so rapidly that there could be no doubt.

I looked at him with sympathy.

“Oh dear. Still, I’m sure you’ll be fine. Someone close to me also suffered from infirmities of old age, but they’ve almost completely recovered now.”

“I would like to say three things first. One, I do not suffer from infirmities of old age. Two. This came to mind while listening to you, so I’m a little curious. How did this acquaintance of yours overcome infirmities of old age?”

“Returned to Youth.”

“……That is a very good method. Except for the fact that I’m an eighty-year-old man who has never learned martial arts.”

“Isn’t that when life begins?”

“I’d like to end your life here, but I’ll let it go since I don’t have the strength.”

After suppressing his surging anger, Namho continued.

“Third, what I said before remains unchanged. I never said this place was the Nanman Beast Palace. I said the Nanman Beast Palace began here.”

“Oh.”

The words were similar, but their meanings were clearly different.

Now that I finally understood what Namho had meant, I asked again.

“Then?”

“That’s right. This is one of the lands under the rule of the Nanman Beast Palace. Unlike the other regions of Nanman, it is directly administered by the Palace Lord. That may make it easier to understand.”

“So it’s similar to how the Emperor appoints vassal kings or City Lords throughout the realm. This place is like the capital of a country.”

“Exactly. Of course, there are differences. The Palace Lord’s authority does not reach the Son of Heaven’s, while the authority of the various tribal chiefs throughout Nanman exceeds that of City Lords.”

Ju Hwaran, who had been listening to Namho, let out a quiet exclamation before speaking.

“Now that I think about it, I once read something similar in a record my grandfather left behind. It said that Nanman was a single kingdom, and that the Nanman Beast Palace was like a gigantic ranch encompassing five counties.”

“You truly are the Escort King’s granddaughter. But even that Great Hero Ju Gongsan never made it beyond these fences. Anyone who isn’t a member of the local ethnic groups is forbidden to enter.”

“It’s really that strict?”

“It is.”

If Namho was telling the truth, then even the Sichuan Tang Clan, a sect whose isolation was second to none in the world, would have to yield to the Nanman Beast Palace.

I clicked my tongue and stared beyond the endless line of fences and grasslands.

“But we have to get inside.”

“That’s right.”

“Is there another way? Since you’re one of the local ethnic groups, perhaps you can enter…”

“I said outsiders cannot enter. I don’t recall saying that entry was easy simply because I’m one of the local ethnic groups.”

“Oh.”

“Here, I’m nothing more than a powerless, ordinary old man of the Miao people. If Dark Heaven hadn’t extended its claws into the world, and if you people hadn’t come looking for me, I would have quietly ended my life… you bastard!”

I flinched at Namho’s sudden bellow and opened my eyes wide.

“Elder Namho, why are you blaming yourself? Why would quietly ending your life make you a son of a bitch?”

“Not me! That bastard! That fucking son of a bitch—catch him!”

At Namho’s shout, which sounded as if he were about to choke to death, we turned our heads.

A huge backside was crawling over the fence.

And in front of it, a single yellow calf was peacefully grazing.

“Oh. Oh, no?”

“That guy, surely not…”

“When did that bastard get over there?”

“Young Hero Tae!”

“Taishan!”

At the voices of the others, followed at last by Sama Pyo’s desperate cry, Taishan flinched.

*Moo?*

The calf realized something was wrong and raised its head sharply.

Taishan had somehow already drawn close. An exclamation mark seemed to pop into the calf’s large, clear eyes, and at the same time, its still-growing hooves struck the grass.

*Pat-pat-pat!*

It made a split-second judgment and tried to flee.

But Taishan was one step faster than the calf.

“Beef! Stop right there!”

With a shout filled with iron determination, Taishan’s enormous body soared through the air.

It wasn’t a tiger or leopard, but how could a half-grown calf evade a Peak master who had set his mind on catching it?

With a heavy *thud*, the calf pinned beneath him let out a scream.

*Moooooo!*

It was such a plaintive cry that merely hearing it made my eyes sting.

But to Taishan, whose stomach had turned inside out from the consecutive forced marches and strictly rationed meals, it was enough to make his mouth water.

“Taishan! Beef!”

“Grab that bastard right now!”

Before Namho had even finished shouting, I had already vaulted over the fence and dashed right up to Taishan.

*Grab.*

“Let go! Beef tartare!”

“Stop it, you heartless, bloodthirsty lunatic. You haven’t even seen *The Sound of the Bell*?”[^1]

“I haven’t!”

“……Ah.”

That made sense.

I understood for a moment, but that was that and this was this. I grabbed Taishan by the back of the neck and pulled him away with an appropriate amount of force.

When his mountain-sized body toppled backward, the beef—or rather, the calf—finally escaped with its life. It sprang to its feet and started running.

*Thundering thud-thud-thud!*

Grass flipped wildly into the air, followed by clouds of dust.

As Taishan watched the calf’s rump disappear from the pasture at full speed, he muttered mournfully.

“No. Taishan’s rump meat…”

*Was this guy born in Majang-dong or something?*[^2]

I was beginning to question his origins when Namho suddenly started raging, shouting like a volcano erupting.

“You bastard!”

“Elder Namho, calm down. Please, calm down.”

“How am I supposed to calm down right now? I repeatedly warned you not to touch anything in the Nanman Beast Palace’s territory! And this hulking glutton of a bastard ignored every word an elder said and went and caused trouble?”

Sama Pyo hurried over and stepped between Namho and Taishan.

“I’m sorry, Elder Namho. I only looked away for a moment, and then… Taishan, you wretch, apologize at once.”

Taishan looked Namho straight in the eye and answered.

“Taishan hungry.”

“That fucking bastard. Let go of this hand right now. Let go! You won’t? Do you think I spent more than fifty years waiting in Nanman, getting bitten by mosquitoes, just to see this?”

Life really did begin at eighty.

I only had to look at Namho, who had never learned martial arts yet was giving off an aura fierce enough to make even Jeok Cheongang yield to him for once, to know it.

The old Hidden Shadow Pavilion agent, who had been raging like a live volcano, finally calmed down after fifteen minutes.

“Whew. I’m fine now, so let go of my hand.”

“Are you really all right?”

“My internal organs turned over once in the meantime, but I’m not about to die.”

If they had turned 180 degrees, that would have been a problem.

But 360 degrees? That was acceptable.

At my nod, Hyuk Mujin released Namho’s hand. Namho sighed with the face of a man on the verge of death.

“Yes, at least nothing actually happened. If someone from the Nanman Beast Palace had witnessed that, things would have gone wrong from the very beginning.”

If this had been another sect in the Central Plains, someone might have thought, *It’s only one cow.*

But in the end, this was a difference in culture and people.

Just as grassland nomads treasured their horses like their own lives, livestock was a valuable asset here, where the divisions and boundaries between tribes were so clear.

*The place is called the Nanman Beast Palace, after all.*

Even the name gave off an unmistakably animal-friendly feeling.

There was a reason Namho had warned us from the start not to touch anything.

“Then what do we do now? We can’t just wait here until someone appears.”

“If we trespass into the Nanman Beast Palace’s territory without permission, it will cause a disturbance. In that case, we must naturally find another way.”

Answering Hyuk Mujin’s question, Namho pulled something out of his bundle.

“What is that?”

“A signal firework for emergencies. If this explodes, someone will at least come out to see what’s happening.”

With a confident smile, Namho struck a spark with a fire striker.

*Crackle.*

The fuse burned rapidly toward the end.

At the same time, the firework shot into the sky with a tremendous bang.

*Fwoooosh—boom!*

The problem was that the firework’s burst came down on the pasture instead of exploding in the air.

“……Huh?”

“……Huh?”

*Whoooosh—roar!*

The pasture was engulfed in flames alongside the stunned voices of the others.

I stared blankly at the livestock fleeing in every direction and muttered.

“……Someone will definitely come out now.”

“……This isn’t how it was supposed to go.”

Not how it was supposed to go, my ass.

We were fucked.

And just as I stared at the burning pasture with a devastated heart—

*Kraaaar!*

Along with the harsh roar of a wild beast, a figure appeared beyond the hill of the burning pasture.

[^1]: *The Sound of the Bell* is a Korean documentary film about an elderly farmer and his ox.

[^2]: Majang-dong in Seoul is famous for its livestock and meat markets.
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0615.txt",
      "sha256": "b632b8db0cd1acc8891985d1cf6c1d9fbf3e9ac3696b925aea2cb9b20d818e63",
      "bytes": 12528
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "96ad424d7be9594fd2d98314a3b32ecc6b3964929b2cbe8937c4d0990e0e0245",
      "bytes": 2623
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "6d839467692b34349160bdd09e0445e3ceadd25b210cb2e9a17f071a6e060ba4",
      "bytes": 191113
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "da477f5683f0048ef70a566cae4708363408f545f3074c0fdf6465ae8fab4996",
      "bytes": 1147
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "47b332e600331d6e417f566a26457eea9a05c0bc541f286dd425f0d6fd223664",
      "bytes": 1775
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "c5d7c8668082bb40dac7dca7eadf50655bc34edfa26229427ab643c1df267a78",
      "bytes": 622
    },
    {
      "path": "characters/Ju Gongsan.md",
      "sha256": "1b2bd21c9e3a42aa7269ec2463e11f358a4693a39d1551d87438b00d6e4e932f",
      "bytes": 900
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "1e0bd0629554ffe00ddaef813cd7927cecc8507b464c1a3d36f618fef15819ca",
      "bytes": 959
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "1cb463ff22c1098580622c88ecf110eed8e4f4c24436c79b7fec703af6812a54",
      "bytes": 840
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "e950e1c39c8d806f73614d950f2196a5d938858d533042d8e90fb6b71367a02c",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "85558b3bcc3476e0652a6ce7615bab469b683ed386287807e012f8b402a7081f",
      "bytes": 811
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "414a153b1bf43e97b00c6ce4ad0318c89b5797a5057b25c367ebf1a2d4bc23fa",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "84a274646934f8e28fbbc2d811bf8cb696e2a266d502a1d5e3202c37f92403be",
      "bytes": 193201
    }
  ],
  "estimated_tokens": 11892
}
-->

# Durable State Update — Chapter 615

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 615. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 615. Profile updates may replace only one
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
  "chapter": 615,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 615,
    "continuity_sources": [615],
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
    "Jin Taekyung has returned to the Murim and is leading the Fire Dragon Pavilion's Nanman expedition from Mount Daebyeol.",
    "The Fire Dragon Pavilion's current expedition party includes Hyuk Mujin, Ju Hwaran, Song Ilseom, and Taishan.",
    "Jin Taekyung has completed an unnamed cultivation technique intended for even the lowest-rank Hunter to learn without making it easily abusable.",
    "Jin Taekyung has entrusted the Skeleton King with the completed martial art and a letter for Choi Minwoo.",
    "Choi Minwoo is serving as Guild Master of the Peace Guild and Vice Guild Master of Ares Guild while grieving his grandfather Kim Hwajong.",
    "Al Diab Jawahiri, the leader of Al-Qaeda, remains in the Skeleton King's custody.",
    "The Skeleton King is an undead named monster who has fought alongside Jin Taekyung and is accepted by Chuck Hagel as an ally.",
    "Al-Qaeda possesses a large Magic Gem research laboratory that appears to have operated for at least ten years.",
    "Restricted supplies found among the terrorists indicate support from established military, political, or smuggling networks.",
    "Jin-ho has inferred Jin Taekyung's involvement in the masked group's campaign and agreed to keep it secret.",
    "The masked group's campaign has destroyed terrorist leadership and headquarters, prompting Middle Eastern terrorist groups and Afghan rebels to promise restraint.",
    "The Lord of Heaven has awakened, empowered Dark Heaven's servants, and declared that the Great War is beginning."
  ],
  "continuity_sources": [
    614,
    613
  ],
  "open_questions": [
    "Who supplied Al-Qaeda with the restricted equipment, weapons, artifacts, and military goods?",
    "What results, if any, did Al-Qaeda obtain from its long-running Magic Gem experiments?",
    "What fate will the Skeleton King ultimately assign to Al Diab and the remaining terrorists?",
    "Will the terrorist groups' apparent surrender and restraint last beyond the immediate pressure of the masked group's campaign?",
    "How will Choi Minwoo respond after receiving Jin Taekyung's martial art and letter?"
  ],
  "safe_through": 614,
  "temporary_decisions": [
    "Use Al Diab Jawahiri as the full English rendering of 알 디아브 자와히리.",
    "Retain Crazy Korean as Chuck Hagel's address for the masked protagonist.",
    "Preserve Jin-ho hyung as Jin-ho's familiar address.",
    "Render 심마 as heart demon, 심법 as cultivation technique, and 무공 as martial arts.",
    "Keep Magic Gem laboratory for 마정석 관련 비밀 실험실."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 암천     | **Dark Heaven**                  |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 신법     | **movement technique**                           |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 표사     | **escort**                                   |
| 소국주    | **Young Bureau Head**                        |
| 사숙     | **Martial Uncle**                            |
| 헌터      | **Hunter**            |
| 사천     | **Sichuan**            |
| 감숙     | **Gansu**              |
| 본문      | **our sect / this sect**                                        |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주공산 | **Ju Gongsan** | Former head and founder of the Yongbong Escort Bureau. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 유엽도 | **willow-leaf saber** | Saber wielded by Song Ilseom. |
| 표왕 | **Escort King** | Epithet of Ju Gongsan. |
| 광동진가 | **Guangdong Chen Family** | Family whose last child Ju Gongsan carried to Henan during the Great Faction War. |
| 광동 | **Guangdong** | Province under Demonic Cult control during the war. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 만리표 | **Ten-Thousand-Mile Escorts** | The Escort King’s famed escort missions. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 원정 | **Origin Essence** | The Water God Dragon's purified energy core, which humans call an inner core. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 흑룡도 | **Black Dragon Saber** | Sama Pyo's sobriquet. |
| 호거아 | **Tiger Giant Child** | Epithet for Taishan. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 대별산 | **Mount Daebyeol** | Secondary meeting point for the departing party. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 614
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 614
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 614
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Gongsan.md

# Ju Gongsan (주공산)

- **Safe through:** Chapter 340
- **Aliases:** Escort King
- **Role:** Founder and former head of the Yongbong Escort Bureau; during the Great Faction War, he was a wandering escort who refused to surrender a pregnant woman of the Guangdong Chen Family to the Demonic Cult after accepting her escort fee, carried her from Guangdong through Jiangxi and Hubei to Henan over two years, and became known as the Escort King; he later founded an escort bureau in his hometown of Shaanxi and died from internal injuries sustained during the war.
- **Personality:** Remarkably skilled, chivalrous, principled, and unwavering in his obligations.
- **Voice:** Not established.
- **Relationships:** Ju Hogun was his only blood child and successor as head of the Yongbong Escort Bureau; Ju Hwaran is his granddaughter.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 614
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 549
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan and willing to redirect blame onto his subordinate.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 614
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 614
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran, is Song Pyosan’s son, and his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 614
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃615화



정식 명칭인 운남성(雲南省). 중원에서는 흔히들 남만(南蠻)이라 부르는 그곳으로 향하는 길은 멀고도 험했다.

푸르륵, 푸륵.

말의 숨결이 거칠다.

대별산을 떠나 쉴새 없이 말을 달린 지 장장 네 시진.

주화란이 수급해 온 준마를 타고 호북에 진입한 우리는, 이를 모를 협곡에서 잠시 말고삐를 늦췄다.

“단순히 이렇게만 이동한다면 상당한 시일이 소요될 거예요. 각주님께서도 사천(四川)에 가 보신 적이 있으니 알고 계시겠죠?”

“저요?”

알지, 당연히 알지. 그때만 생각하면 지금도 종아리에 알이 배기는데.

맑고 반짝이는 눈동자로 묻는 주화란을 향해, 나는 무의식적으로 고개를 끄덕였다.

“그럼요. 진짜 조옷…….”

“네?”

“조옷금 힘들었습니다. 조금이요.”

순간 뭐 빠질 뻔했다고 대답하려던 걸 겨우 참았다.

나 진태경, 동성에게는 한없이 냉혹하지만, 이성에게는 젠틀하면서도 따뜻한 남자다.

물론 지금까지 살면서 연애는 한 번도 못 해 봤지만.

“그때는 경신법을 발휘했는데도 보름 가까이 걸리더라고요.”

“사천까지만 해도 삼천 리가 훌쩍 넘는 거리예요. 더군다나 지름길 없이 이동하셨을 걸 생각하면 대단하시네요.”

칭찬을 해 주니 기분이 좋기야 한데, 단순히 칭찬을 받기 위해서 이런 대화를 하는 것은 아닐 것이다.

내 눈짓에 싱긋 웃은 주화란이 품에서 낡은 가죽 두루마리를 꺼내 들었다.

‘저게 뭐지?’

내가 의문을 느낀 그때, 말안장에 앉아 유엽도(​柳葉刀)의 날을 살펴보고 있던 송일섬이 뜻밖이라는 표정으로 입을 열었다.

“말가죽으로 만들었군. 혹시 마방(馬幇)의 물건이오?”

주화란이 고개를 끄덕였다.

“알아보시는군요. 맞아요, 정확히는 그들이 사용하던 지도죠.”

“허, 마방의 지도는 만금을 줘도 구할 수 없는 귀물(貴物)이라 들었는데.”

“용봉표국의 소국주로서 말씀드리자면, 이 세상에 재물로 구하지 못할 물건은 없어요. 하지만 제 조부께서는 금보다 더 귀중한 우정을 얻으셨죠. 그 증표로 이 지도를 선물 받았고요.”

음. 그렇군.

……사실 하나도 못 알아들었다. 주화란의 조부인 표왕 주공산이 마방이란 곳의 인물에게 대단한 지도를 선물 받았다는 것 빼고는.

두 사람의 대화를 참을성 있게 지켜보던 내가 입을 열었다.

“그, 주 소저. 죄송한데 마방이 도대체 뭡니까?”

“북방 기마민족의 후예들이다.”

“수백 년 전부터 고대 교역로를 오가며 새외와 중원의 문물을 실어나르던 자들이지. 오랜 시간이 흐른 지금은 숫자가 많이 줄었지만.”

“…….”

아니, 뭐. 일단 마방이 뭔지는 이해는 했는데.

분명 나는 주화란에게 물어본 것 같은데, 대답은 왜 시커먼 사내 두 놈이 하는지 모르겠다.

거의 동시에 입을 연 송일섬과 사마표가 서로를 바라보았다.

“보기보다 제법 견식이 있군.”

“보기보다? 내가 속한 흑룡마문(黑龍魔門)이 어디에 있는지 잊었나? 지금도 본문이 자리 잡은 감숙성에서는 마방들이 활동하고 있어.”

“활동? 쥐어짜 내는 것이 아니라?”

송일섬이 피식 웃으며 말을 이었다.

“흑룡마문이 교역로를 틀어쥐고 막대한 통행세를 거두고 있다는 소문은 익히 들었지.”

“낭인 출신이라고 들었는데. 본문에 안 좋은 인연이라도 있나?”

“딱히. 그냥 사마외도가 눈에 보이면 죽이고 싶을 뿐이야.”

“어느 부분에 관해서는 나와 생각이 비슷하군. 난 검부터 들이미는 놈을 만나면 참을 수가 없거든. 그래서 무기 손질은 끝났나?”

“아직. 하지만 어차피 곧 피를 묻히게 될 테니 나중에 해도 상관없어.”

“그럼 잠시 자리를 옮기지.”

아니, 이야기 전개가 왜 이렇게 되는 건데.

사이좋게 말머리를 돌리는 두 놈을 멍하니 바라보던 내가 입을 열었다.

“옮기긴 뭘 옮겨. 이 미친놈들아.”

송일섬과 사마표가 동시에 대답했다.

“개인적인 일이니 끼어들지 마라.”

“어차피 말도 쉬게 해야 하니 차나 한잔하고 있게. 금방 끝내고 돌아오지.”

“…….”

한 놈은 개인주의자고, 한 놈은 관운장이네.

야심 차게 출범한 남만원정대가 초장부터 균열의 징조를 보이자, 화룡각의 각주로서 나서지 않을 수가 없다.

쉭!

순간 울려 퍼진 두 줄기의 파공성.

내가 쏘아 보낸 지풍(指風)을 피해 지상으로 착지한 송일섬과 사마표가 반사적으로 무기를 뽑으려던 그때, 내가 담담한 목소리로 경고를 건넸다.

“그거 뽑으면 후회할 텐데.”

“……!”

“……!”

말로만 건넨 경고가 아니다. 사방에서 옥죄어 오는 막대한 기파(氣波)를 느낀 두 녀석의 움직임이 우뚝 멈춘다.

흔들리는 눈동자에는 숨길 수 없는 놀라움이 떠올라 있었다.

‘강하다.’

나를 향한 녀석들의 눈빛은 그렇게 말하고 있었고, 그건 누구도 부정할 수 없는 사실이었다.

감숙성의 패자인 흑룡마문의 소문주이자 사파 제일의 후기지수라는 흑룡도(黑龍刀) 사파표도, 치열한 전장과 생사결에서 숱한 적들을 쓰러트리며 전설이 된 추혼객(抽魂客) 송일섬도 똑똑히 깨달았을 것이다.

아니, 이건 그들이 결코 어쭙잖은 절정 고수가 아니기에 더 잘 알 수 있는 부분이었다.

높은 곳에 자리 잡은 사람이 보다 멀리, 전체를 파악할 수 있는 법이니까.

‘예전에도 내가 두 수는 위였지만, 지금 느끼는 압박감은 더하겠지.’

언제나 그랬듯이, 깨어난 직후의 나는 잠들기 전보다 강해져 있었다.

현대의 헌터들을 위한 보급형 무공을 정립하고 창안하는 과정에서 작은 깨달음을 얻었기 때문이었다.

물론 대단한 무공을 만든 것은 아니라서 진일보(進一步)라 표현할 정도는 아니지만…… 반의 반 걸음 정도를 나아간 것만으로도 큰 성과다.

그 성과를 가장 먼저 실감한 놈들이 암천이 아니라 같은 편이라는 게 안타까울 뿐이고.

“앞으로 남은 길이 수천 리다. 그래도 싸울 거라면 지금 당장 한 놈이 죽을 때까지 싸우든가. 그것도 아니면…….”

“각주님.”

나는 분명 주화란에게 호의를 품고 있지만, 지금은 그녀의 말을 들을 때가 아니다.

굳을 얼굴로 말을 건넨 주화란에게 작게 고개를 내저은 나는 말을 이었다.

“그것도 아니면 둘이 합심해서 나한테 덤벼. 지금 아니면 앞으로도 기회 없다.”

“…….”

“…….”

입을 꾹 다문 채 서로를 응시하던 송일섬과 사마표가 결정을 내리기까지는 그리 오랜 시간이 걸리지 않았다.

스르릉. 철컥.

서늘한 마찰음과 함께, 미세하게 드러나 있던 두 개의 도신(刀身)이 모습을 감췄다.

아무 일 없었다는 듯 다시 안장에 오른 두 사람을 바라본 주화란이 작게 한숨을 내쉬었다.

“후우…… 이런 일이 없기를 바랐는데.”

그건 나도 마찬가지다. 하지만 저 녀석들을 화룡각에 받아들이기 전, 한 차례 심사숙고했던 부분이기도 했다.

‘아무래도 감정이 좋지는 않겠지. 특히 송일섬의 입장에서는.’

모든 것이 수십여 년 전, 정과 마가 천하를 양분하여 결전을 벌일 무렵부터 시작된 악연이었다.

주씨 성을 쓰는 젊고 담대한 표사는 어느 여인의 의뢰를 받아 만리표(萬里漂)라는 전설을 새로 썼고, 그 여인이 낳은 아이는 무럭무럭 자라나 한 사내아이를 남기고 세상을 떠났다.

그리고 그 사내아이가 바로 송일섬이었다. 사마외도에 의해 멸문당한 광동진가의 마지막 후예.

그가 부처나 예수가 아닌 이상, 사파에 대한 혐오를 가진 건 충분히 예상하고 있던 바였다.

‘이렇게 빨리 터질 줄은 몰랐지만.’

시바, 기세 좋게 출발한 지 몇 시진이나 됐다고 벌써 파토 조짐이냐. 대학생들이 조별 과제를 왜 그렇게 싫어하는지 알 것 같다.

무림 최단 시간 앙숙이 된 두 놈을 논외로 친다 해도 마찬가지였다.

“조장님, 아까 배를 맞아서 그런지 자꾸 똥이 마려워요.”

“주군. 싸우지 마라. 태산이. 주군 위험해지면 걱정되고 배고프다.”

“…….”

라인업 봐라. 시벌 거.

몸보다 위장이 활발한 혁무진과, 위장 대신 인벤토리를 갖고 있는 게 아닌가 의심되는 호거아(虎巨兒) 태산을 보고 있자니 눈앞이 깜깜해진다.

하지만 이 암울한 상황 속에서도 한 줄기 빛은 있었다.

“주 소저.”

“네?”

“감사합니다. 저는 주 소저가 있어서 정말 기뻐요.”

진심이다. 미인이고 아니고를 떠나서 가장 정상인이 아닌가.

다른 조원들에 비해 무공이 조금 부족한 것은 사실이지만, 무림 견문도 넓은 데다 길도 척척 잘 찾아낸다.

지금도 마방들 사이에서만 은밀히 알려져 있다는 지름길을 찾아낸 것만 봐도 알 수 있었다.

그런데 왜 대답이 없지?

“주 소저?”

“…….”

“저기요? 주 소저?”

재차 불러도 대답은 돌아오지 않았다.

말없이 말고삐를 쥔 주화란이 고개를 돌린 채 더듬더듬 입을 열었다.

“이, 이쪽으로 길을 잡으면 될 거예요.”

“예? 아니, 참 잘하신 건 맞는데. 제 말은…….”

“그럼 전 먼저 가서 마방들의 표식을 살펴보고 있을게요. 이럇!”

“어어. 어어어?”

뭐라 더 말해 볼 시간도 없었다. 말과 한 몸이 되어 다급히 달려 나가는 주화란의 뒷모습만 멍하니 바라보던 나는, 따끔거리는 뒤통수를 느끼고 돌아섰다.

‘……이것들은 또 왜 이래.’

송일섬. 사마표. 혁무진. 심지어는 태산까지.

정확히 네 쌍의 시선이 그 자리에 우뚝 멈춘 채 나를 뚫어져라 바라보는 중이었다.

도무지 뜻을 짐작할 수 없는 오묘한 눈빛들에, 반사적으로 흠칫한 내가 물었다.

“뭐야. 왜 다들 그렇게 쳐다봐?”

“음. 아무것도 아니다.”

“먼저 가 보지. 각주.”

송일섬과 사마표는 복잡한 표정으로 천천히 말을 몰아 앞으로 나아갔고. 혁무진과 태산은 떨떠름한 표정으로 대답했다.

“어, 그냥 봤습니다. 똥 마려워서.”

“……똥이 마려운데 왜 날 봐.”

“조장님을 보고 있으면 나오려던 것도 다시 돌아갑니다.”

“태산이. 그냥 배고파서 쳐다보고 있었다. 아무 뜻 없다.”

“……도대체 배고픈 거랑 나랑 뭔 상관인데.”

“아니다. 그냥. 그냥. 음. 태산이. 감 잡았다. 이제 좀 알았다.”

이건 또 무슨 개소리일까.

혁무진까지는 그렇다 쳐도 저 떡대 큰 식충이가 나를 짠하게 바라보는 건 더럽게 찝찝하다.

하지만 내가 뭐라 추궁하기도 전에, 태산은 반쯤 죽어 가는 준마의 엉덩이를 후려치며 달려나갔다.

“태산이! 간다! 말도 함께 간다!”

안 그래도 이미 반쯤 골로 간 준마가 비틀비틀 달려 나가자, 혁무진이 황급히 그 뒤를 따랐다.

“거기, 거 같이 좀 갑시다!”

“싫다! 따라오지 마라! 태산이는 앞만 보고 달린다!”

“나 육포 있어요.”

“태산이! 친구 만났다! 우리는 영원히 함께다!”

미친놈들…….

하지만 저 미친놈들에게 무시당하고 있다는 느낌이 드는 건 왜일까.

나는 똥 씹은 표정으로 말고삐를 쥐었다.

“야. 우리도 가자.”

푸르륵,

“…….”

이제는 말 새끼마저 띠꺼운 표정을 짓는구나.

나는 콧김을 뿜어내는 말의 머리통을 한 대 친 뒤 옆구리를 바짝 조였다.

작은 울음소리와 함께 준마가 협곡을 내달렸다.
```

## Final English reading copy

```markdown
# Chapter 615

The road to Yunnan Province—the region officially known by that name, though people in the Central Plains commonly called it Nanman—was long and arduous.

*Prrrff. Prrf.*

The horse’s breathing was ragged.

We had been riding without a break for a full four shichen since leaving Mount Daebyeol.

After entering Hubei on the fine horses Ju Hwaran had procured, we finally loosened the reins for a moment in an unfamiliar ravine.

“If we travel only like this, it will take a considerable amount of time. You’ve been to Sichuan before, Pavilion Master, so you know that, don’t you?”

“Me?”

Of course I knew. Just thinking about it made my calves cramp even now.

I unconsciously nodded at Ju Hwaran as she asked me with her clear, sparkling eyes.

“Of course. It was really fucki—”

“Pardon?”

“It was a little… difficult. A little.”

I barely stopped myself from saying that something almost fell off back then.

I, Jin Taekyung, was endlessly cold-blooded toward men, but a gentleman—warm and considerate—toward women.

Of course, despite having lived this long, I had never once been in a relationship.

“Even using a movement technique, it took nearly half a month.”

“Just getting as far as Sichuan is a distance of well over three thousand li. And considering that you must have traveled without any shortcuts, that’s remarkable.”

I felt good about being praised, but she probably hadn’t started this conversation just to compliment me.

At my meaningful glance, Ju Hwaran smiled and pulled an old leather scroll from inside her robes.

*What’s that?*

Just as I began to wonder, Song Ilseom, who was sitting in the saddle and inspecting the edge of his willow-leaf saber, spoke with an unexpected look on his face.

“It’s made of horsehide. Is it perhaps something belonging to the horse caravans?”

Ju Hwaran nodded.

“You recognize it. You’re right. More precisely, it’s a map they used.”

“I’ve heard that a map of the horse caravans is a treasure that cannot be obtained even for ten thousand gold pieces.”

“As the Young Bureau Head of the Yongbong Escort Bureau, I can tell you that there is nothing in this world that cannot be obtained with wealth. But my grandfather gained a friendship more precious than gold. He received this map as a token of it.”

Hmm. I see.

*…Actually, I didn’t understand a damn thing.*

Aside from the fact that Ju Hwaran’s grandfather, Escort King Ju Gongsan, had received an amazing map from someone belonging to a place called the horse caravans.

After patiently listening to the two of them, I opened my mouth.

“Um, Young Lady Ju. Sorry, but what exactly are the horse caravans?”

“They are descendants of the northern mounted tribes.”

“They traveled along the ancient trade routes for hundreds of years, carrying goods from the Outer Lands and the Central Plains back and forth. Their numbers have dwindled considerably over the years, though.”

“……”

Well, all right. I understood what the horse caravans were now.

But I was pretty sure I had asked Ju Hwaran. Why were the answers coming from two dark-clad men?

Song Ilseom and Sama Pyo had spoken almost simultaneously, and now they looked at each other.

“You’re more knowledgeable than you look.”

“Than I look? Have you forgotten where the Black Dragon Demon Gate is located? Horse caravans are still active in Gansu, where our sect is based.”

“Active? You mean being squeezed dry?”

Song Ilseom gave a short laugh and continued.

“I’ve heard the rumors. The Black Dragon Demon Gate has seized control of the trade routes and collects enormous tolls.”

“I heard you were a wandering martial artist. Do you have some bad blood with our sect?”

“Not particularly. I just want to kill any demonic, heterodox practitioner I see.”

“We agree on that point. I can’t stand meeting people who draw their weapons before anything else. So, are you finished tending to your weapon?”

“Not yet. But we’ll be getting blood on it soon enough, so there’s no harm in doing it later.”

“Then let’s move somewhere else for a while.”

What the hell was happening to the conversation?

I stared blankly at the two men as they amicably turned their horses around, then opened my mouth.

“Move somewhere else for what, you lunatics?”

Song Ilseom and Sama Pyo answered at the same time.

“It is a personal matter. Do not interfere.”

“We need to let the horses rest anyway, so have some tea while we’re gone. We’ll be back shortly.”

“……”

One was an individualist, and the other was Guan Yu.

When the Nanman expedition, which had set out with such high hopes, began showing signs of cracking right from the start, I had no choice but to intervene as the Fire Dragon Pavilion Master.

*Whish!*

Two sharp blasts of air rang out.

Song Ilseom and Sama Pyo landed on the ground after avoiding the Finger Qi I had fired at them. Just as they reflexively began to draw their weapons, I warned them in a calm voice.

“You’ll regret drawing those.”

“……!”

“……!”

It wasn’t merely a verbal warning. The two men froze when they felt the immense qi pressing in from every direction.

Unmistakable astonishment appeared in their trembling eyes.

*He’s strong.*

That was what their gazes said.

And it was an undeniable fact.

Sama Pyo, the Black Dragon Saber, was the Young Sect Leader of the Black Dragon Demon Gate, Gansu’s dominant power, and the foremost young prodigy of the unorthodox faction. Song Ilseom, the Soul-Chasing Guest, had become a legend after cutting down countless enemies on fierce battlefields and in life-and-death duels. Both of them must have understood it clearly.

No, they could understand it all the better precisely because they were not mediocre Peak masters.

A person standing at a higher place could see farther and grasp the whole picture.

*I was already two moves above them before, but the pressure they’re feeling now must be much greater.*

As always, I had grown stronger after waking up than I had been before falling asleep.

That was because I had gained a small insight while developing and systematizing a mass-produced martial art for modern Hunters.

Of course, I hadn’t created some earth-shattering martial art, so it wasn’t enough to call it a great advance…

But even moving forward a quarter of a step was a major achievement.

It was merely unfortunate that the first people to experience that achievement were allies rather than Dark Heaven.

“There are several thousand li left to travel. But if you still want to fight, then fight right now until one of you dies. If not…”

“Pavilion Master.”

I certainly had goodwill toward Ju Hwaran, but now was not the time to listen to her.

I shook my head slightly at Ju Hwaran, whose expression had gone rigid, and continued.

“If not, the two of you can join forces and come at me. You won’t get another chance, now or ever.”

“……”

“……”

Song Ilseom and Sama Pyo kept their mouths tightly shut as they stared at each other. It did not take long for them to reach a decision.

*Shrrrk. Click.*

With a cold scraping sound, the two blades that had been faintly exposed disappeared from view.

Ju Hwaran watched the two men climb back into their saddles as if nothing had happened, then let out a small sigh.

“Whew… I had hoped nothing like this would happen.”

So did I. But it was also something I had thought long and hard about before accepting those two into the Fire Dragon Pavilion.

*Their feelings toward each other probably aren’t very good. Especially from Song Ilseom’s perspective.*

Everything had begun with a feud that went back several decades, to the time when the orthodox and demonic factions had divided the world between them and fought a decisive battle.

A young and bold escort bearing the surname Zhu accepted a commission from a certain woman and created a new legend known as the Ten-Thousand-Mile Escorts. The child that woman bore grew up strong, then left behind a son and passed away.

That son was Song Ilseom—the last descendant of the Guangdong Chen Family, which had been wiped out by demonic, heterodox arts.

Unless he was Buddha or Jesus, it was only natural that he would harbor hatred toward the unorthodox faction.

*I just didn’t expect it to blow up this soon.*

Shit, we’d only been on the road for a few shichen. Were there already signs that this whole thing was falling apart? I was beginning to understand why college students hated group projects so much.

And that was true even if I excluded the two men who had become archenemies faster than anyone in Murim history.

“Captain, maybe it’s because I got hit in the stomach earlier, but I really need to take a shit.”

“My lord. Do not fight. Taishan worry when my lord in danger. Taishan hungry.”

“……”

Look at this lineup.

*For fuck’s sake.*

Watching Hyuk Mujin, whose stomach was more active than his body, and Taishan, the Tiger Giant Child, who seemed to have an inventory instead of a stomach, made my vision go dark.

But even in this bleak situation, there was one ray of light.

“Young Lady Ju.”

“Yes?”

“Thank you. I’m really glad you’re here.”

I meant it. Setting aside whether she was beautiful, wasn’t she the most normal person here?

It was true that her martial arts were slightly weaker than those of the other members, but she had extensive knowledge of Murim and was excellent at finding her way.

The fact that she had found a shortcut known only among the horse caravans proved it.

But why wasn’t she answering?

“Young Lady Ju?”

“……”

“Um, Young Lady Ju?”

Even when I called her again, no answer came.

Still holding the reins in silence, Ju Hwaran turned her head away and stammered.

“I-I think we should take this road.”

“What? No, you certainly did a great job. I mean…”

“I’ll go ahead and look for the horse caravans’ markers. Hyah!”

“Whoa. Whoa, whoa?”

I had no time to say anything else.

I could only stare blankly at Ju Hwaran’s back as she hurriedly rode away, her body moving as one with her horse. Then I felt an irritating prickling at the back of my head and turned around.

*Why are these guys acting like this now?*

Song Ilseom. Sama Pyo. Hyuk Mujin. Even Taishan.

Exactly four pairs of eyes were fixed in place, staring holes through me.

Their mysterious gazes were impossible to interpret. I flinched instinctively and asked,

“What? Why is everyone staring at me like that?”

“Hmm. It is nothing.”

“Let us go ahead, Pavilion Master.”

Song Ilseom and Sama Pyo slowly urged their horses forward, their expressions complicated. Hyuk Mujin and Taishan answered with dubious looks.

“Uh, I was just looking. Because I need to take a dump.”

“If you need to take a dump, why are you looking at me?”

“When I look at you, whatever was about to come out goes right back in.”

“Taishan. Taishan was just looking because hungry. Nothing else.”

“Why the hell would your hunger have anything to do with me?”

“No. Just… just. Hmm. Taishan understand now. Taishan know a little more.”

What kind of bullshit was that supposed to be?

I could understand Hyuk Mujin, but having that giant glutton look at me with such pity was deeply unsettling.

Before I could press him for an explanation, Taishan slapped the rump of the half-dead thoroughbred and charged off.

“Taishan! Go! Horse go too!”

The thoroughbred, already half-dead, staggered into motion. Hyuk Mujin hurriedly followed after him.

“Hey, wait! Let’s go together!”

“No! Do not follow! Taishan only look ahead and run!”

“I have jerky.”

“Taishan! Found friend! We together forever!”

Those lunatics…

But why did I feel like I was the one being ignored by those lunatics?

I grabbed the reins with an expression like I had bitten into something foul.

“Hey. Let’s go, too.”

*Prrrff.*

“……”

Now even the horse was making an annoyed face.

I smacked the horse on the head as it snorted, then squeezed its sides hard.

With a small whinny, the fine horse raced through the ravine.
```

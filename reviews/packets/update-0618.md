<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0618.txt",
      "sha256": "88f7461fba675dd89cdb217352011db023bf4aa810cb6b3859511030342470c2",
      "bytes": 14380
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3602f85c5f1e4111a0ee96251abc2392854c83006ffa8d09978eb22a069bc2b3",
      "bytes": 1371
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8a44e789c451ac3ae35504e7f0acbdf7dcf140a973d06a3ca3655de42a8fdcf6",
      "bytes": 191796
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "f2886ce01cf665eb083921b36530f1bd3cf80fd088652216cce599f9ed30b4a8",
      "bytes": 1206
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "efb1f04005476b6db315c76d7aacedd1856966ea093476fcc5b4e8738a9c2329",
      "bytes": 1775
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "7648701aca0df5ae88eb00e56819ed8228b99e97f7b14bc4685b50d88b95e1cd",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "21bd003f8b58f06bddd5c77068114d81d61422ae47352fe8b699632c0dc698c1",
      "bytes": 959
    },
    {
      "path": "characters/Song Ho.md",
      "sha256": "4275b709b428f06b0791983524fd2eb9c9d6291a9150e9941d7379325ec074bf",
      "bytes": 767
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "4568b959f905957714cfabde8738927a60659171874b82beedaa2067f59b3629",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "cbc3f2324550b7cb3ade5741006a7ad96a31550c2061c9aaaaca34a2c8866949",
      "bytes": 957
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "675c8207276c46fe9140c3640a539ce73a4d7a4e801ee8174d32c6e520289aa8",
      "bytes": 528
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "692b720c4e0a64c9d34e66cdb655ddef2821d6f6435171e988fa2f5721d9fad9",
      "bytes": 194503
    }
  ],
  "estimated_tokens": 12345
}
-->

# Durable State Update — Chapter 618

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 618. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 618. Profile updates may replace only one
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
  "chapter": 618,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 618,
    "continuity_sources": [618],
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
    "The Fire Dragon Pavilion is traveling by Water Dragon Stronghold swift ship down the Yangtze toward Yunnan and Nanman.",
    "Mu Song is away at the Yangtze River Channel League headquarters under Pa Ryun's direct summons.",
    "Mu Song ordered Water Dragon Stronghold to aid Taekyung and the Jin Family in repayment for past assistance and the matter involving Hwang Chung.",
    "Hyuk Mujin uses fishing as a way to empty his mind and spends each night training or circulating his qi.",
    "The Peak-grade Journey to Nanman Quest requires Taekyung and the Fire Dragon Pavilion to enter Nanman; failure grants the Title Can’t Go to Nanman and greatly reduces Fame and trust.",
    "Ju Hwaran is anxious about the coming mission but explicitly says she will trust Taekyung."
  ],
  "continuity_sources": [
    617
  ],
  "open_questions": [
    "What dangers or scheme, if any, await the Fire Dragon Pavilion in Nanman?",
    "What role will Pa Ryun and the Yangtze River Channel League play while Mu Song is summoned to headquarters?"
  ],
  "safe_through": 617,
  "temporary_decisions": [
    "Use horse caravans for 마방 and Pavilion Master for 화룡각주 and 각주.",
    "Use Young Lady Ju for 주 소저.",
    "Preserve Taishan's clipped, childlike speech.",
    "Use Judge Bao for 판관 포청천."
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
| 무신     | **Martial God**               | —              |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 정마대전   | **Great Faction War**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 도사      | **Daoist**                                                      |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 채주 | **Stronghold Lord** | Title used for the lord of a water stronghold. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 운남성 | **Yunnan Province** | The formal name of the destination region commonly called Nanman in the Central Plains. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 수하 | 채주 | subordinate_to_stronghold_lord | Stronghold Lord | deferential | The subordinate calls Mu Song 채주 while reporting the nearby vessel. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 부채주 | 진태경 | Water Dragon Stronghold deputy to honored ally | Great Hero Jin | deferential | The Deputy Stronghold Lord reports Mu Song's orders and addresses Taekyung upon arrival. |
| 진태경 | 부채주 | Fire Dragon Pavilion Master to Water Dragon Stronghold deputy | Deputy Stronghold Lord | casual and commanding | Taekyung orders him to set off and later summons him with Jang Pil. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 617
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and a member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 617
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master with the Heavenly Martial Physique and Force, publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license, and he has completed an unnamed cultivation technique designed for even the lowest-rank Hunter to learn without making it easily abusable.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 617
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 617
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, a member of the Fire Dragon Pavilion, and an experienced Nanman escort guide with route knowledge from the Escort King's records.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather and rescued the Guangdong Chen Family’s surviving child, who became Song Ilseom’s grandmother; Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort, and Jin Taekyung is a trusted ally.

### Song Ho.md

# Song Ho (송호)

- **Safe through:** Chapter 548
- **Aliases:** Thousand-Faced Fox
- **Role:** Elderly Peak master known as the Thousand-Faced Fox, a martial artist with a prosthetic leg, and current Chief of the Hidden Shadow Pavilion, overseeing a vetted intelligence network that includes highly trained assassins.
- **Personality:** Outwardly genial and relaxed, but observant, forceful, and intimidating when pursuing information.
- **Voice:** Lightly genial and conversational, turning quietly coercive during interrogation.
- **Relationships:** He serves under Mae Jonghak's New Murim Alliance, commands the Hidden Shadow Pavilion, and recognizes Jin Taekyung as Jeok Cheongang's Disciple.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 617
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 617
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 617
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

## Korean source

```text
＃618화



어느샌가 후텁지근해진 공기. 그리고 저 멀리 모습을 드러내는 높은 산과 깊은 계곡.

수룡채의 부채주는 빠르게 가까워지는 육지를 가리키며 말했다.

“저희가 모셔다드릴 수 있는 곳은 여기까집니다요. 배에서 내리셔서 곧장 십 리를 가시면 운남이니, 금방 도착하실 겁니다.”

이 대륙에서 장강의 지류가 차지하는 범위가 실로 광활하다고는 하나, 운남성 내륙으로까지 이어져 있지는 않았다.

아니, 엄밀히 말하자면 아주 뚝 끊겨 있는 것은 아니다.

문제는 이대로 수로를 타고 운남 북부에 위치한 고원(高原)까지 이동한다면 목적지로의 도착까지 시일이 오히려 훨씬 더 소요된다는 점이었다.

‘최우선 목적지는 어디까지나 남만야수궁(南蠻野獸宮)이니까.’

내가 받은 퀘스트의 완료 조건은 남만에 도착하는 것이지만, 화룡각의 임무를 위해서는 남만야수궁으로 향해야 했다.

그런 생각을 떠올린 나는 부채주를 향해 작게 고개를 숙였다.

“정말 고맙습니다. 상선 약탈하느라 바쁘실 텐데 여기까지 데려다주시고.”

“어이구, 그런 말씀 마십시오. 다른 사람도 아니고, 진 대협께서 부르시면 만사를 제쳐 두고 언제든지 달려와야지요. 이대로 헤어지는 게 아쉬울 지경입니다, 으허허허.”

그런 것치고는 너무 행복해 보이는데.

하긴 수하들 앞에서 심심하면 대가리도 박고, 엎드려 뻗친 적도 있으니 오늘의 헤어짐이 행복하긴 할 거다.

그런 부채주의 모습에 나는 따라 웃으며 되물었다.

“하하, 정말요?”

“그러고 말굽쇼. 허허.”

“그럼 근처에 계시면 딱 좋겠다. 그렇죠?”

“허허허. 예?”

“일단 오긴 했는데, 나중에 돌아갈 거 생각하니까 걱정이었거든요. 그런데 때마침 헤어지는 게 아쉽다고 하시니까 잘됐지. 뭐.”

“……!”

“그러니까 근처에서 기다리세요.”

얼굴에서 웃음기가 싹 사라진 부채주가 더듬더듬 입을 열었다.

“아, 아니. 그건 좀. 저희도 해야 할 일이 있고…….”

“압니다. 알아요. 그러니까 한두 척 정도만 남기고 나머지는 복귀해도 괜찮아요.”

“지, 진 대협. 이러지 마시고 차라리 운남에서의 볼일이 끝나신 후에 연통을 넣어 주시면…….”

“음. 킹치만 그럼 너무 오래 기다려야 하는걸?”

“…….”

부채주의 얼굴에 가득하던 행복감은 이제 더 이상 찾아볼 수 없었다.

나는 침울하게 고개를 떨군 그의 어깨를 부드럽게 쓸어내리며 말했다.

“무리한 부탁인 거 아는데, 신세 좀 집시다.”

“아니, 그래도…….”

“아, 신세 좀 지자고.”

“…….”

“아잇, 싯팔. 대답 좀 하세요. 처신을 똑바로 해야 무림에서 오래 살아남지.”

“헉.”

얼굴이 시커멓게 물든 부채주의 대답은 이미 정해져 있는 것이나 다름없었다.

잠시 후, 결국 다시 돌아올 때까지 인근에 정박하고 있겠다는 대답을 받아 낸 후에 배에서 내린 나를 바라보는 시선들이 심상치 않았다.

“삼류 낭인을 보는 줄 알았다.”

“이건 정말 악의 없이 물어보는 건데, 혹시 태원진가의 뿌리가 사파 쪽인가?”

“역시 조장님이십니다. 기대를 저버리시지 않는군요.”

“태산이. 각주가 수적인 줄 알았다.”

“전 각주님의 판단이 맞다고 생각해요. 만일 남만에서 문제가 생긴다면 저들의 도움을 받을 수 있을 테니까요. 그렇지 않나요?”

마지막 대답이 유일하게 정답이다.

역시 내 마음을 알아주는 건 주화란밖에 없구나. 나는 감동 어린 목소리로 그녀를 바라보았다.

“맞습니다. 아주 그냥 토씨 하나 안 틀리고 제 생각이랑 똑같아요.”

“핫, 정말 그렇게 생각하신 거예요?”

“예?”

“전 그냥, 다른 사람들이 하도 뭐라 하기에 저라도 각주님 편을 들어 주려고…….”

“…….”

내 이미지, 정말 이대로 괜찮나.

그런 고민을 하며 얼마나 걸었을까. 중원과는 비교도 되지 않는 조잡한 길을 따라 걷던 와중에 익숙한 소리가 귓가를 파고들었다.

띠링.



- [남만]에 진입했습니다.

- 임무, [남만 진입]을 완료했습니다.

- 퀘스트, [남만행]을 성공적으로 완료했습니다!

- 퀘스트 완료 보상을 획득합니다!

- 소량의 경험치를 획득했습니다!

- 소량의 명성을 획득했습니다!

- 업적, [남만 찾아 수천 리]를 달성했습니다!

- 남만은 날씨가 어지럽고, 갖가지 맹수와 독물들로 가득한 험지(險地). 외부인은 늘 이곳의 풍토병과 독을 조심해야 합니다.

- [상급 해독제]x10. [중급 해독제]x20. [하급 해독제]x30을 획득했습니다!



새로운 연계 퀘스트가 생성되었습니다.

퀘스트 창을 확인하시겠습니까?

Y / N



연이어 울려 퍼지는 시스템 알림과 허공을 가득 메운 홀로그램 창들.

부채주의 말은 사실이었다. 주위에 사람 하나 안 보여서 그렇지, 걷다 보니 금방 남만의 영역에 발을 디딘 모양이다.

나는 아무렇지 않은 척 마음속으로 중얼거렸다.

‘확인.’

띠링.



퀘스트



[남만에 심은 씨앗]



당신은 수천 리를 이동한 끝에 남만에 도착했지만, 남만은 인적이 드물고 외부인이 환영받지 못하는 땅입니다.

현재 당신이 지닌 짧은 견식과 정보로는 섣부르게 움직일 수 없으니, 과거 무림맹이 남만에 심어 둔 은영각 요원과 접선하여 자세한 정보를 입수하십시오.



등급 : 절정

제한 : 진태경 및 화룡각 인원

임무 : 은영각 요원과 접선 (미완료)

보상 : 연계 퀘스트

 ???

실패 : 능력치 하락





‘음.’

은영각 요원과 접선이라.

새로운 연계 퀘스트를 몇 번에 걸쳐 읽은 나는, 하남을 떠나기 전 무림맹 은영각주인 천면호리 송호와 주고받은 대화를 떠올렸다.



‘정마대전이 끝나고 초대 맹주이신 무신께서 자취를 감추자, 은영각도 자연스럽게 해체되었지. 하지만 정보망을 유지할 최소한의 인선은 수십여 년이 흐른 지금에도 남아 있다네.’

‘그 말씀은…….’

‘말하지 않았나. 은영각의 눈과 귀는 어디에나 있다고.’



천하를 뒤흔든 대전쟁이 끝나고, 사람들은 서서히 평화에 젖어 들었지만 그렇지 않은 이들 역시 있었다.

천면호리 송호와 은영각이 바로 그랬다.



‘오직 대의(大義)와 의기(意氣). 이 두 가지를 마음에 새긴 채 오랜 세월 동안 자리를 지킨 이들일세. 남만에 도착한다면 가장 먼저 그를 찾아보게. 정보는 물론이고 많은 도움을 받을 수 있을 테니.’

‘어떻게 찾으면 되겠습니까? 설마 이름 석 자에 주소지만 알려 주시진 않을 거고.’

‘은영각 요원들만이 알고 있는 밀마(密摩)가 있네. 밀마를 확인하는 특정 장소를 따로 알려 줄 테니 그곳에 가면 만날 수 있을 걸세.’



새삼 놀라운 이야기였다. 정마대전이 끝난 지 어언 오십여 년에 가까운 세월이 흘렀음에도 은영각의 정보망이 살아 있다니.

‘그것도 남만 같은 오지(奧地)라면 더욱더 남아 있기 싫었을 텐데.’

하지만 그런 이들의 희생 덕분에 나와 화룡각의 임무가 한층 수월해질 수 있을 것이다.

생각을 정리한 나는 주위를 경계하며 이동 중이던 화룡각 대원들을 향해 입을 열었다.

“영인(永仁)으로 간다.”

“영인이요?”

고개를 갸우뚱거린 혁무진이 물었다.

“통 못 들어 본 지명인데, 거기가 어딥니까?”

“현재 위치상으로 이백리 가량 떨어진 현읍이에요. 물론 중원의 현읍과는 비교도 할 수 없을 만큼 낙후된 곳이지만요.”

나를 대신해서 대답한 주화란이 말을 이었다.

“각자 다른 여러 이민족이 융화되어 살아가고 있는 곳이기도 하죠. 그렇다고 충돌이 없는 것은 아니고요.”

막힘없이 대답하는 그녀의 말과 어조에서 무언가를 느낀 내가 물었다.

“가 본 적이 있습니까?”

주화란이 살며시 웃으며 고개를 끄덕였다.

“말씀드리지 않았었나요? 삼 년 전에 아버지를 겨우 졸라 남만으로 표행을 간 적이 있었다고.”

“아, 그게 영인이었군요.”

“네. 짧은 시간이었지만 그때의 기억은 아직도 생생해요. 여기 있는 송 호위도 함께였죠.”

사람들의 시선이 자신을 향해 쏠리자, 송일섬이 눈썹을 치켜세우며 한 마디를 툭 내뱉었다.

“남만은 두 번 다시 오기 싫은 끔찍한 곳이었지. 하지만 영인은 그나마 괜찮았다. 이민족들도 제법 온순한 축에 속했고.”

평소 송일섬이 보이는 냉소적인 태도를 생각한다면 제법 후한 평가다.

하긴, 그러니 이 거칠고 험한 남만 땅을 가로질러 표행을 올 수 있었던 거겠지.

“그런데 영인은 무슨 이유로 가는 건가요?”

주화란의 물음에 이번에는 모두의 시선이 나를 향한다. 아마 다들 처음부터 묻고 싶었는데 꾹 참고 있던 것이 틀림없었다.

굳이 숨길 문제도 아니라, 나는 솔직하게 대답했다.

“영인에서 무림맹의 정보원과 만날 생각입니다.”

“그렇다면 반드시 가야겠군요. 남만의 소식은 외부로 쉽게 알려지지 않으니.”

남만은 오지 중의 오지다.

울창한 밀림 속에서 살아가는 수십여 갈래의 이민족은 중원 본토의 한족(漢族)을 극도로 경계하며, 자신들끼리도 숱한 전쟁을 벌이며 각자의 영역을 지켜 왔다.

그렇기에 어지간한 대형 표국과 상단들조차 남만행을 꺼린다고 했다.

만약 성공한다면 각종 향신료와 약초를 비롯하여 희귀한 보석들을 얻을 수 있겠지만, 밀림에 도사린 숱한 위험 속에서 생목숨을 잃을 수도 있으니까.

분노 조절 장애에 걸린 이민족이 아니더라도 온갖 독물과 맹수, 치사율이 높은 풍토병은 심각한 장애물이었다.

“하지만 영인이라면 괜찮아요.”

주화란이 생긋 웃으며 말을 이었다.

“우리 용봉표국의 선대부터 이어진 인연도 있고, 그곳에 거주하는 이민족들은 비교적 한족에게 친절한 편이거든요.”

“아. 그렇습니까?”

“네. 만나 보면 아시겠지만, 다들 착하다니까요.”



* * *



카악, 퉤.

끈적끈적한 가래침이 발치에 떨어졌다.

백족(白族)이라는 이름이 괜히 붙여진 것이 아니듯, 흰옷을 걸친 이민족 사내가 흉흉한 눈빛으로 우리를 노려보고 사라진다.

그 모습을 말없이 지켜보던 나는 주화란을 향해 조심스럽게 입을 열었다.

“그, 혹시나 해서 물어보는 건데. 저 정도면 이민족 사이에서 착한 축에 드는 겁니까?”

“…….”

“주 소저?”

잠시 침묵하던 주화란이 대답했다.

“음. 저 사내는 좀 거친 성격인 것 같아요. 대부분은 안 그렇거든요.”

“그렇죠?”

“네, 네. 그럼요. 직접 와 봐서 잘 알아요.”

주화란이 대답하기 무섭게, 이번에는 공작새처럼 화려한 옷을 입은 중년의 이민족 여인이 어린아이의 눈을 가리며 중얼거렸다.

“세상에, 한족 놈들이 감히 여기까지 들어왔네. 들어가자. 눈 버릴라.”

“엄마. 엄마. 나 안 보여.”

“괜찮아, 우리 딸. 저 흉악한 놈들한테서 얼른 멀어지자. 여보! 빨리 나와 봐요. 마을에 한족 놈들이 들어왔어요!”

“뭐? 기다려 봐. 내가 쟁기를 들고 가서 이 한족 노무 새끼들의 대가리를 까부수겠어!”

“…….”

“…….”

똑똑히 봤다. 순간 주화란의 눈에 동공 지진이 일어나는 걸.

나는 마지막 희망을 담아 그녀에게 물었다.

“저 사람들도 그냥 좀. 평균적인 분위기에 비해 약간 거친 거죠?”

“……그럴 거예요. 아마.”

하지만 주화란의 바람은 처참하게 외면당했다.

얼마 지나지 않아 길가를 가득 메운 이민족들이 우리를 향해 적대감을 표출했기 때문이었다.

“진짜 한족이었군.”

“간도 크지. 즉시 족장님께 연락해.”

“이미 사람을 보냈습니다.”

“여자들과 아이들은 집에 들이고, 장정들을 모아 저 한족 놈들을 주시하게.”

죄인이 된 기분이다.

아니, 저들에게 있어 이미 우리는 찢어 죽여도 시원치 않을 죄인이었다.

나처럼 시스템의 번역을 사용할 수도 없고, 주화란처럼 이민족의 언어를 익히지도 못한 다른 대원들도 그 사실을 충분히 느끼고 있었다.

“조장님.”

“왜.”

“아무래도 저희 좆 된 것 같은데요.”

마른침을 꿀꺽 삼킨 혁무진이 속삭이듯 말을 이었다.

“뭐라고 하는지는 모르겠는데, 분위기가 너무 흉흉합니다. 이 정도면 그냥 몸을 피하는 게 낫지 않을까요?”

“음.”

수하를 불안감을 없애는 것도 리더의 역할. 나는 준엄한 목소리로 대답했다.

“그런 거 아니야.”

“아니에요?”

“그래. 그냥 한족이 신기해서 쳐다보는 거야.”

“그런데 왜 도끼를 들고 있습니까?”

“장작 패다가 왔나 보지.”

“칼도 들고 있는데요?”

“도축하다가 왔나 보지.”

“…….”

그렇게 보지 마라. 양심에 찔리니까.

불신 가득한 눈빛을 보내는 혁무진을 애써 외면한 나는, 흉흉한 기세를 뿜어내는 이민족들 사이를 가로질러 한 목제 건물 앞에 멈춰 섰다.

[독화루]

하도 낡아 금방이라도 부스러질듯한 간판. 천면호리가 알려준 접선 장소였다.
```

## Final English reading copy

```markdown
# Chapter 618

Before anyone knew it, the air had turned hot and muggy. In the distance, high mountains and deep valleys came into view.

The Deputy Stronghold Lord of the Water Dragon Stronghold pointed toward the rapidly approaching shore.

“This is as far as we can take you, Great Hero Jin. Once you disembark and walk ten li straight ahead, you’ll be in Yunnan. You should arrive in no time.”

The Yangtze’s tributaries covered an incredibly vast area across this continent, but they did not extend all the way into the interior of Yunnan Province.

No—that wasn’t strictly true. They didn’t simply cut off all at once.

The problem was that if we continued along the waterways to the plateau in northern Yunnan, it would actually take much longer to reach our destination.

*Our highest priority is the Nanman Beast Palace, after all.*

The Quest I had received required me to reach Nanman, but the Fire Dragon Pavilion’s mission required us to head for the Nanman Beast Palace.

With that thought in mind, I gave the Deputy Stronghold Lord a small bow.

“Thank you very much. You must be busy raiding merchant ships, yet you still brought us all the way here.”

“Oh, please, don’t say that. You’re no ordinary person. If Great Hero Jin calls for us, we should drop everything and come running at any time. I’m almost sorry to part ways with you, heh heh heh.”

He looked far too happy for someone who was supposedly sorry.

Then again, he’d had to bang his head against the ground and hold a push-up position in front of his men at the drop of a hat. He probably really was happy to say goodbye today.

I laughed along with him and asked,

“Ha ha. Really?”

“Of course. Heh heh.”

“Then it would be perfect if you stayed nearby, wouldn’t it?”

“Heh heh heh. What?”

“We came all this way, but I was worried about having to think about getting back later. But since you just said you’d be sorry to part ways, this works out perfectly.”

“……!”

“So wait nearby.”

The smile vanished completely from the Deputy Stronghold Lord’s face. He stammered,

“Ah, no. That might be a little difficult. We have things to do as well…”

“I understand. I do. So you can send the rest of the ships back and leave one or two behind.”

“G-Great Hero Jin, please don’t do this. Why don’t you send word after you’re finished with your business in Yunnan instead…”

“Hmm. But then I’d have to wait way too long.”

“……”

The happiness that had filled the Deputy Stronghold Lord’s face was nowhere to be found now.

I gently patted his shoulder as he lowered his head in dejection.

“I know it’s an unreasonable request, but let’s impose on you a little.”

“No, even so…”

“Come on. Let’s impose on you a little.”

“……”

“Ah, fuck. Answer me already. You need to conduct yourself properly if you want to survive long in the Murim.”

“Gasp.”

The Deputy Stronghold Lord’s face darkened. His answer might as well have already been decided.

A short while later, I finally extracted a promise that they would remain anchored nearby until we returned. After I disembarked, the gazes directed at me were far from ordinary.

“I felt like I was looking at a Third Rate wandering martial artist.”

“I’m asking this without any ill intent, but is the Jin Family of Taiyuan perhaps rooted in the unorthodox faction?”

“As expected of our Captain. You never disappoint.”

“Taishan thought Pavilion Master was a water bandit.”

“I think the Pavilion Master made the right decision. If something happens in Nanman, we’ll be able to receive their help. Isn’t that right?”

That last answer was the only correct one.

*As expected, Ju Hwaran is the only person who understands me.*

I looked at her with a deeply moved expression.

“That’s right. You’ve expressed my thoughts exactly, without getting a single word wrong.”

“Oh, did you really think so?”

“Huh?”

“I only took your side because everyone else was criticizing you. I thought someone should support the Pavilion Master…”

“……”

*Is my image really okay as it is?*

While I was pondering that question, we continued walking along a crude road that was nothing like the roads of the Central Plains.

Then a familiar sound pierced my ears.

*Ding.*

> **System**
>
> Entered **Nanman**.
>
> Mission, **Enter Nanman**, completed.
>
> Quest, **Journey to Nanman**, successfully completed!
>
> Quest completion rewards acquired!
>
> A small amount of EXP acquired!
>
> A small amount of Fame acquired!
>
> Achievement, **Thousands of Li in Search of Nanman**, achieved!
>
> Nanman is a perilous land with erratic weather, filled with all manner of wild beasts and venomous creatures. Outsiders must always beware of endemic diseases and poison.
>
> Acquired: **Advanced Antidote** ×10, **Intermediate Antidote** ×20, **Basic Antidote** ×30!
>
> A new Chain Quest has been created.
>
> Would you like to check the Quest window?
>
> Y / N

The System notifications rang out one after another, and holographic windows filled the air around me.

The Deputy Stronghold Lord had been telling the truth. We hadn’t seen a single person nearby, but after walking for a short while, we had apparently stepped into Nanman territory.

I muttered inwardly while pretending nothing had happened.

*Confirm.*

*Ding.*

> **System**
>
> **Quest**
>
> **Seeds Planted in Nanman**
>
> You have arrived in Nanman after traveling thousands of li, but Nanman is a sparsely populated land where outsiders are not welcomed.
>
> With the limited knowledge and information you currently possess, you cannot act recklessly. Make contact with the Hidden Shadow Pavilion agent planted in Nanman by the Murim Alliance in the past and obtain detailed information.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung and Fire Dragon Pavilion members
>
> **Mission:** Make contact with the Hidden Shadow Pavilion agent (Incomplete)
>
> **Reward:** Chain Quest
>
> ???
>
> **Failure:** Stats decreased

*Hmm.*

Make contact with a Hidden Shadow Pavilion agent.

After reading through the new Chain Quest several times, I recalled the conversation I’d had with Song Ho, the Chief of the Hidden Shadow Pavilion, before leaving Henan.



*“After the Great Faction War ended and the first Alliance Leader, the Martial God, disappeared, the Hidden Shadow Pavilion was naturally disbanded as well. But even now, after several decades have passed, the minimum personnel needed to maintain the intelligence network still remain.”*

*“You mean…”*

*“Didn’t I tell you? The eyes and ears of the Hidden Shadow Pavilion are everywhere.”*



After the Great War that had shaken the world came to an end, people gradually grew accustomed to peace.

But there were others who did not.

The Thousand-Faced Fox Song Ho and the Hidden Shadow Pavilion were like that.



*“Only great righteousness and spirit. They are people who have remained in their places for all these years with those two things engraved in their hearts. Once you arrive in Nanman, look for him first. You’ll be able to receive plenty of help from him, not to mention information.”*

*“How am I supposed to find him? You’re not just going to give me the man’s name and address, are you?”*

*“There is a secret code known only to Hidden Shadow Pavilion agents. I’ll tell you the specific place where the code can be checked. If you go there, you should be able to meet him.”*



It was astonishing when I thought about it again.

Nearly fifty years had passed since the end of the Great Faction War, yet the Hidden Shadow Pavilion’s intelligence network was still alive.

*And in a remote place like Nanman, where they would have been even less inclined to stay.*

But thanks to the sacrifices of people like them, the Fire Dragon Pavilion’s mission would become much easier.

After sorting out my thoughts, I spoke to the Fire Dragon Pavilion members as they moved forward while keeping watch over their surroundings.

“We’re going to Yeongin.[^1]”

[^1]: Yeongin (永仁) is a county seat in Yunnan.

“Yeongin?”

Hyuk Mujin tilted his head and asked,

“I’ve never even heard of that place. Where is it?”

“It’s a county seat about two hundred li from our current location. Of course, it’s far more underdeveloped than any county seat in the Central Plains.”

Ju Hwaran answered in my place and continued,

“It’s also a place where several different ethnic groups live together. That doesn’t mean there are no conflicts, though.”

I sensed something in her effortless answer and tone, so I asked,

“Have you been there before?”

Ju Hwaran smiled gently and nodded.

“Didn’t I tell you? Three years ago, I managed to persuade my father to let me go on an escort journey to Nanman.”

“Ah, so that was Yeongin.”

“Yes. It was a short visit, but I still remember it vividly. Captain Song was with me as well.”

When everyone’s gazes turned toward him, Song Ilseom raised an eyebrow and casually added,

“I never want to come to Nanman again. It was a horrible place. But Yeongin was relatively tolerable. The ethnic groups there were comparatively mild-tempered.”

Considering Song Ilseom’s usual cynical attitude, that was quite a generous assessment.

Then again, that must have been why he had been able to escort a shipment across this rough and dangerous land of Nanman.

“But why are we going to Yeongin?”

At Ju Hwaran’s question, everyone looked at me this time. They had probably all wanted to ask from the beginning but had been holding back.

There was no reason to hide it, so I answered honestly.

“We’re going to meet one of the Murim Alliance’s informants in Yeongin.”

“Then we definitely have to go. News from Nanman doesn’t easily reach the outside world.”

Nanman was the most remote of remote lands.

The dozens of ethnic groups living in the dense jungles were extremely wary of the Han Chinese from the Central Plains. They had also fought countless wars among themselves to defend their respective territories.

That was why even most major Escort Bureaus and merchant organizations were reluctant to travel to Nanman.

If they succeeded, they could acquire rare gems along with various spices and medicinal herbs. But the many dangers lurking in the jungle could also claim their lives.

Even without an ethnic group suffering from anger-management issues, countless poisonous creatures, wild beasts, and highly lethal endemic diseases were serious obstacles.

“But Yeongin should be fine.”

Ju Hwaran smiled brightly and continued,

“Our Yongbong Escort Bureau has had ties with the people there since the time of its former leaders, and the ethnic groups living there are relatively friendly toward the Han Chinese.”

“Oh. Is that so?”

“Yes. You’ll see when you meet them, but they’re all good people.”

* * *

“Caw, spit.”

A thick strand of phlegm landed at our feet.

Living up to the name Bai, or “White,” a tribesman dressed in white glared menacingly at us before disappearing from sight.

I watched him silently, then cautiously spoke to Ju Hwaran.

“Um, I’m asking just in case, but does someone like that count as one of the nicer ones among the ethnic groups?”

“……”

“Young Lady Ju?”

After a brief silence, Ju Hwaran answered,

“Hmm. That man seems to have a rough personality. Most people aren’t like that.”

“Right?”

“Yes, yes. Of course. I know because I’ve been here myself.”

The moment Ju Hwaran finished speaking, a middle-aged ethnic woman dressed in clothes as colorful as a peacock covered a child’s eyes and muttered,

“Oh, my. Those Han bastards dared to come all the way here. Let’s go inside. You’ll ruin your eyes.”

“Mom. Mom. I can’t see.”

“It’s okay, sweetheart. Let’s hurry away from those vicious men. Honey! Come out quickly! Han bastards have entered the village!”

“What? Wait there. I’ll grab a plow and smash the heads of these Han sons of bitches!”

“……”

“……”

I saw it clearly.

For an instant, Ju Hwaran’s pupils shook violently.

With one last shred of hope, I asked her,

“Those people are also just a little rough compared to the average, right?”

“……That’s probably the case. I think.”

But Ju Hwaran’s hopes were brutally ignored.

Before long, the ethnic tribesmen filling the roadside began openly displaying their hostility toward us.

“So they really are Han Chinese.”

“They’ve got some nerve. Contact the chief immediately.”

“I’ve already sent someone.”

“Take the women and children into their homes, and gather the men to keep an eye on those Han bastards.”

I felt like I was a criminal.

No. To them, we were already criminals who deserved to be torn apart and killed.

The other members, who could neither use the System’s translation nor speak the ethnic language like Ju Hwaran, could feel it well enough.

“Captain.”

“What?”

“I think we’re fucked.”

Hyuk Mujin swallowed hard and continued in a whisper.

“I don’t know what they’re saying, but the atmosphere is extremely hostile. Wouldn’t it be better to get out of here?”

“Hmm.”

One of a leader’s duties was to eliminate his subordinates’ anxiety. I answered in a solemn voice.

“It’s not like that.”

“It isn’t?”

“No. They’re just staring because Han Chinese are unusual to them.”

“Then why are they carrying axes?”

“They probably came over after chopping firewood.”

“They’re carrying swords too.”

“They probably came over after slaughtering something.”

“……”

*Don’t look at me like that. You’re making me feel guilty.*

I did my best to ignore Hyuk Mujin’s distrustful gaze and crossed through the ethnic tribesmen radiating a menacing aura.

We stopped in front of a wooden building.

**Poison Flower Pavilion**

The sign was so old that it looked as though it might crumble at any moment.

It was the meeting place the Thousand-Faced Fox had told me about.
```

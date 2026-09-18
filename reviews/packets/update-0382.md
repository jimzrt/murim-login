<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0382.txt",
      "sha256": "2fb57203aacaf6aa9b38c97ca4c4be1c4753961e2f625105113a0493d2350bca",
      "bytes": 14343
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e81025c76f6fdcc5f62eca8679765de9e354c9aa3a454a7d67b3a1cc6f961c5f",
      "bytes": 3096
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "17b3a82253bc73f26cfa58a82fb7aed9db108a0b07bb496d4104f524ce0d9a31",
      "bytes": 132816
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "2b809424c9180ef71cc7adfe0c1afbd21233b5e756ecb44f802ddbd1da757c20",
      "bytes": 533
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "600b95b34678d7bd5538a5c30ead92b1b6eb0c3b1ace049437e6d70f8fdf6697",
      "bytes": 1129
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "941ca71a48dfaf66c1be29afa89953f7b55c4cf303d537698c462275834c727b",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3847313df2472f326057e397459fe0fde1885ffaf946067dded7990e3797a30b",
      "bytes": 102437
    }
  ],
  "estimated_tokens": 10024
}
-->

# Durable State Update — Chapter 382

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 382. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 382. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 382,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 382,
    "continuity_sources": [382],
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Chengdu International Airport attack continues, with a massive army of living and undead monsters fighting the Chinese defenders.",
    "The Chinese People’s Liberation Army and Public Security Armed Forces Department Hunters are defending the airport after suffering losses approaching half their strength.",
    "Jin Taekyung and Team Leader Choi are fighting at the airport after halting their aircraft in the middle of the monster army.",
    "More than half of the nearly two-thousand-monster army are undead controlled by an external force, but the Skeleton Warlord has begun overriding that control.",
    "Jin Taekyung is Level 120 at the Supreme Peak realm, has manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "The Myriad-Poison Ring remains bound to Jin Taekyung alongside White Flame and the Fire Dragon Armor.",
    "The Skeleton Warlord is stored in Jin Taekyung’s Inventory and can control nearby undead, resurrect fallen monsters, and expand its army; its power has increased dramatically at the airport.",
    "Shao Shen commands roughly five hundred Public Security Armed Forces Department Hunters and leads them in an offensive against the non-undead monsters.",
    "Three former necromancers, reborn in the bodies of dead mages, are still incomplete Liches serving the Arch Lich.",
    "The Arch Lich ordered the three necromancers to kill humans and create more undead, and may withdraw the power granted to them if they fail.",
    "Jin Taekyung has reached the three necromancers after tearing through their monster forces with hellfire and Flamefire Path.",
    "Aehyang is manipulating the Sichuan City Lord under the direction of an unidentified person."
  ],
  "continuity_sources": [
    381,
    380
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "Who is the Arch Lich, and what will happen after Jin Taekyung confronts its three servants?"
  ],
  "safe_through": 381,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 아크 리치 as Arch Lich.",
    "Render 듀라한 as Dullahan, 포이즌 브레스 as Poison Breath, 사기 as death energy, 의념 as conveyed thoughts, and 데스나이트 as Death Knight."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 극양                        | **Extreme Yang**      |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 워로드몬 | **Warlordmon** | Taekyung's mocking nickname for the Skeleton Warlord. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 중화 | **Zhonghua** | Patriotic term used in Shao Shen’s rallying speech. |
| 바이엘른 | **Bayern** | First word in one of the necromantic chants. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 워로드몬 | captor_to_captured_monster | Warlordmon | mocking-commanding | Taekyung uses the childish nickname while ordering the Skeleton Warlord to perform tricks. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 380
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 381
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 381
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃382화



머리를 치면 몸통은 쓰러지는 법.

우두머리로 보이던 세 놈을 붙잡자 놈들이 통제하고 있던 언데드는 태엽 인형처럼 움직임을 멈췄고, 지휘력을 상실한 몬스터 군단은 뿔뿔이 와해되어 죽거나 도망쳤다.

“아크 리치(Arch Lich)?”

내 물음에 무릎을 꿇고 앉아 있던 세 놈이 고개를 끄덕였다.

이미 죽어서 뼈만 남은 이것들을 ‘놈’이라고 부를 수 있는지는 모르겠지만 어쨌든.

나는 세 개의 두개골을 차례차례 쓰다듬으며 말을 이었다.

“사람이 말을 하면 대답을 해야지. 너희 지금 죽었다고 유세 부리니?”

말이 끝나기가 무섭게 대답이 튀어나왔다.

- 예. 예. 아크 리치가 맞습니다.

- 인간님께서 들으신 것이 정확합니다.

- 그렇다.

“음. 아크 리치라. 처음 들어 보는 몬스터인데…… 그런데 마지막에 반말로 대답한 놈 누구냐.”

- 저놈입니다!

- 감히 위대하신 인간님께!

휙, 휙!

뼈만 남은 손가락들이 한 놈을 가리켰다.

전광석화와도 같은 동료들의 배신에, 지목당한 놈이 두개골을 바르르 떨었다.

- 아니다! 이건 비열한 모함이다!

“……내 생각에는 모함이 아닌 것 같은데.”

거짓말을 할 거면 말투라도 좀 고치든가.

슬쩍 주위를 확인한 나는 인벤토리에서 ‘그것’을 꺼내 들었다.

“골골아. 간식 먹자.”

기묘한 검은 광택이 흐르는 두개골 하나. 그것의 텅 빈 동공에서 불꽃이 일렁인다.

- ……골골이라니. 그럴 바에야 차라리 전처럼 워로드몬이라고 불러라.

“왜, 해골이니까 골골이. 찰떡인데.”

- 본 사령관을 이렇게 모욕하다니!

“뭐 싫으면 말든가.”

다시 인벤토리에 집어넣으려던 그때, 스켈레톤 워로드가 분노한 목소리로 외쳤다.

- 잘 먹겠습니다!

“솔직한 아이로구나.”

솔직한 아이에게는 상을 줘야지. 거짓말이나 치는 나쁜 놈에게는 벌을 주고.

“자, 이제 시식해.”

- 고맙구나. 조금 덜 간악한 인간이여. 그런데 얼마나 먹어야……?

“아까처럼 조금만.”

- 으음. 좀 더 먹고 싶은데. 하지만 알겠다.

간식도 너무 자주 주면 과한 법. 살짝 아쉬움을 표한 스켈레톤 워로드가 벌벌 떨고 있는 놈을 향해 입을 쩍 벌렸다.

- 자, 이리 오너라.

- 히, 히이익! 안 돼!

- 돼!

스켈레톤 워로드의 단호한 외침과 동시에 변화가 시작되었다.

쏴아아악!

저건 다시 봐도 신기하네.

마치 진공청소기로 빨아들이는 것처럼, 무릎을 꿇고 있는 놈의 몸뚱어리에서 흘러나온 검은 안개가 스켈레톤 워로드에게 흡수되기 시작한다.

- 흐어어어억!

변화는 거기에서 끝나지 않았다.

검은 안개, 스켈레톤 워로드가 사기(死氣)라고 부르는 그것이 흘러나올수록 놈의 안색, 아니 뼈다귀가 점점 새하얗게 변해 갔다.

반면 스켈레톤 워로드는 검은 광택이 더욱더 깊고 진해졌다.

- 그, 그만!

- 후후후. 이토록 맛 좋은 사기라니.

- 안 돼애!

- 본 사령관이 전부 가져가 주마. 사기이잇!

빡!

- 흡!

“사기잇 같은 소리 하네. 어디서 이상한 것만 배워서는.”

- ……네가 할 소린가?

“아무튼 이제 그만 먹어라.”

- 어째서!

“살쪄.”

순간 할 말을 잃은 스켈레톤 워로드를 품 안에 집어넣고 놈을 바라봤다.

처음 봤을 때만 해도 거무튀튀하던 뼈다귀는 어느새 반쯤 백골이 된 상태. 상당한 사기를 흡수당한 탓인지, 동공 안의 녹색 불빛이 위태롭게 휘청거린다.

- 크흡, 크흐흑.

뼛속까지 쪽쪽 빨린 동료의 약해진 모습에, 나머지 두 녀석은 초조하게 이빨을 딱딱 부딪쳤다.

- 무엇이든 하문하십시오. 위대하신 화염의 지배자시여.

- 부디 바라옵건대. 이 하찮은 존재, 오르페우스 폰 막시무스 발렌시아 바이엘른의 충성을 받아 주시옵소서.

“……언데드가 아니라 비데인가.”

어지간히 힘을 잃기 싫은 모양이다. 뭐 이렇게 협조적으로 나와주면 나야 고맙긴 하지만.

“자, 아직 말 안 한 게 있으면 밑바닥까지 싹싹 긁어서 털어놔 봐. 만약 거짓부렁을 늘어 놨다가는…….”

- 전부 말하겠습니다!

- 부디 바라옵건대, 이 거짓되고 하찮은 존재가 진실을 말씀드리도록 허락해 주소서!

- 마, 말하겠습니다.

이대로 사골국물이 되기는 싫은지 세 뼈다귀는 열정적으로 질의응답에 참여했다.

일주일 전, 아크 리치의 첫 등장부터 지금까지 벌어진 모든 일 들을 빠짐없이 들은 나는 짐짓 눈살을 찌푸렸다.

“확실해?”

- 그렇사옵니다!

- 죽음의 강에 맹세합니다!

- 하, 한 치의 거짓도 없습니다.

격렬하게 두개골을 끄덕이는 세 놈의 모습에, 스켈레톤 워로드가 불쑥 끼어들었다.

- 사실이다.

“얘네한테 뒷돈 받았냐? 그걸 네가 어떻게 장담해?”

- 죽음의 강에 맹세했으니까. 그건 우리 같은 존재에게는 절대적인 약속이다. 결코 거스를 수 없는.

“흠.”

평소에는 먼지처럼 가볍던 녀석이 저렇게 무게를 잡고 말하는 걸 보면 거짓말은 아닌 것 같다.

사실 지금 같은 상황에 놈들이 수작을 부릴 이유도 없고.

“오케이. 믿어 주지.”

- 감사합니다! 정말 감사합니다!

- 크흐흐흑! 충심을 다하겠나이다. 나의 왕이시여!

- 나, 아니 저도 인간님께 충성하겠습니다. 앞으로는 두 번 다시 오늘과 같은 일을 저지르지 않을 것을 죽음의 강에 맹세…….

콰직!

마지막 놈은 말을 잇지 못하고 머뭇거렸다.

파르르 떨리는 녹색 안광이 자신의 가슴팍에 틀어박힌 주먹과 나를 번갈아 바라본다.

- 어, 어째서?

“어째서긴 뭘 어째서야.”

- 나, 나는, 충성을, 맹세, 죽음의 강…….

“늦었어.”

남의 것처럼 차가운 목소리가 입술을 비집고 흘러나왔다.

“너희가 한 짓을 되돌리기에는.”

바로 오늘, 이 자리에서 수많은 사람이 죽었다.

화기를 갖춘 정규군과 헌터들로도 놈들을 막을 수 없었으니, 지난 일주일 동안 몬스터 군단의 손에 죽은 민간인들은 헤아릴 수조차 없을 것이다.

“충성은 필요 없어. 너희 같은 새끼들이 바치는 거라면 더더욱.”

단전에서 끌어 올린 열양지기를 흘려 보낸 순간.

화륵!

놈의 갈비뼈를 부수고 박혀 있던 주먹에서 극양의 기운이 피어올랐다. 초고온의 열기를 띤 청백색의 강기가 놈의 전신을 휘감았다.

콰아아아!

보였다. 바람 앞의 촛불처럼 휘청이던 놈의 녹색 안광이 꺼지는 광경이.

그리고 튕기듯이 몸을 일으키며 주문을 영창하는 두 놈의 모습도.

- 자즈차와 엄바도……!

- 바르간 마흐라……!

후우웅.

놈들을 중심으로 흩날리는 마력의 바람. 사악한 마법의 주문이 완성되려던 그때, 나는 한마디를 툭 내뱉었다.

“먹어 치워. 전부.”

마치 그 말만을 기다리고 있었다는 듯, 품 안에 넣어 둔 스켈레톤 워로드가 옷자락 사이로 뛰쳐나오며 입을 쩍 벌렸다.

- 얼마든지.

- 바르사바…… 히이익!

- 아, 안 돼!

살고자 하는, 아니 계속 언데드로 남아 있고자 하는 몬스터들의 마지막 단말마.

그러나 놈들의 염원과는 달리 스켈레톤 워로드의 흡입력은 그 어느 때보다 강했고, 신속했다.

쏴아아악! 꿀꺽!

엄청난 양의 사기를 한입에 집어삼킨 스켈레톤 워로드가 두개골을 부르르 떤 다음 순간, 모든 기운을 빼앗긴 두 개의 해골이 와르르 허물어졌다.

띠링. 띠링. 띠링.



- 돌발 퀘스트, [예상치 못한 습격]을 성공적으로 완료했습니다!

- 당신은 몬스터 군단을 와해시켰습니다! 이는 실로 뛰어난 업적입니다!

- 퀘스트 보상으로 칭호, [언데드 헌터]를 획득했습니다!

- 상당량의 경험치와 명성을 획득했습니다!

- 레벨 업!



고작 한 번?

예전 같았으면 레벨 업 몇 번은 거뜬했을 텐데, 120레벨이 되고 나니 필요한 경험치가 많아진 모양이다.

‘경험치 얻자고 한 일은 아니긴 한데.’

마땅히 해야 할 일을 했을 뿐이지만, 약간의 아쉬움이 드는 건 어쩔 수 없다.

강해지면 강해질수록, 앞으로의 전투에 더 큰 도움이 될 테니까.

‘저놈도 마찬가지고.’

나는 내심 중얼거리며 스켈레톤 워로드를 바라봤다.

엄청난 양의 사기를 흡수한 덕분인지, 녀석에게서 느껴지는 힘은 처음 만났던 그때와 비교할 바가 아니었다.

- 으음. 후우우우…….

두개골에 뚫린 코와 귀, 눈 등의 구멍 사이로 검은 안개가 뭉게뭉게 피어오른다.

횃불처럼 타오르는 보랏빛 안광과 매끈한 묵광을 자랑하는 표면. 이내 내 머릿속에 녀석의 광소가 쩌렁쩌렁 울려 퍼졌다.

- 크하, 크하하하하!

“볼륨 좀 줄여라. 시끄럽다.”

- 너, 간악한 인간이여. 이번만큼은 본 사령관이 네게 큰 감사를 표하마.

“당연히 그래야지. 누가 먹이를 줬는데.”

내 시큰둥한 대답에 스켈레톤 워로드가 발끈했다.

- 먹이라니! 이 몸이 애완동물이라도 된다는 건가!

“비슷하지. 아냐?”

- 헛소리하지 마라!

“그래? 골골이, 돌아와.”

내가 손을 내밀자 튕기듯 폴짝 뛰어올라 손바닥 위에 안착하는 두개골.

나는 상으로 녀석의 미간을 살살 긁어 주었다.

“잘했어, 골골이. 어유 예뻐.”

- ……!

두개골이 부들부들 떨렸다.

- 이, 이럴 수가! 본 사령관이 어찌 인간 따위에게!

“입은 아니라고 하지만, 몸은 솔직한 거지.”

- 나는 검은 숲의 주인이자, 위대한 언데드 군단의 사령관이다. 이 몸을 능멸하지 말라!

“머리통만 남은 사령관?”

- 뭣이! 이깟 신체 따위. 사기를 소모한다면 얼마든지 복구할 수 있다!

“그래? 그런데 왜 지금까지 복구 안 했어?”

- ……복구해 봤자 어차피 웬 미친 인간이 박살 낼 테니까.

“오, 정답.”

까드득. 이빨도 없어서 뼈마디를 간 스켈레톤 워로드의 안광이 가늘어졌다.

- 어째서냐, 간악한 인간.

“뭐가?”

- 내게 먹이를, 아니 이토록 큰 힘을 준 꿍꿍이가 있을 것 아닌가. 시커먼 속내가 있는 것이 분명할 터. 진실을 고하라!

잠깐 생각하던 나는 대답했다.

“음. 네가 좆밥이라서.”

- 어?

“어차피 넌 나 못 이겨. 그럴 거면 좀 더 강하고 쓸모있는 좆밥을 데리고 다니는 게 써먹기도 편하잖아. 안 그래?”

- ……!

“자, 이제 안에 들어가 있어라. 사람들 온다.”

나는 충격으로 굳어 버린 녀석을 인벤토리에 집어넣고 자리에서 일어났다.

본래는 공항 직원과 승객들로 붐볐을 공항 면세점 복도. 텅 비고 어두컴컴한 그곳에서 이쪽을 향해 걸어오는 세 사람이 있었다.

그리고 그중 두 사람은 낯익은 얼굴이었다.

“진태경 씨.”

「진 선생님.」

비교적 멀끔한 상태인 최 팀장과 중국 공안 무력부 소속의 A급 헌터인 샤오 쉔이다.

전투가 끝난 지 상당한 시간이 흘렀음에도 여전히 피와 먼지를 뒤집어쓴 채인 샤오 쉔의 얼굴은 피곤에 찌들어 있었다.

「여기 계셨군요.」

나는 최 팀장을 향해 눈인사를 건네며 둘러댔다.

“네. 잠시 할 일이 있어서요.”

「말씀 낮춰 주십시오. 시벌, 아니 진 선생님께서는 저와 제 동지들. 나아가 중화의 인민을 구한 영웅이십니다.」

“…….”

착각인가. 저놈 방금 시벌좌라고 하려고 했던 것 같은데.

내 생각을 아는지 모르는지, 샤오 쉔은 지극히 공손한 태도로 말을 이었다.

「다행히 평화 길드에서 오신 두 선생님의 도움으로 몬스터들을 격퇴할 수 있었습니다. 이 자리를 빌려 다시 한번 감사를 표합니다.」

“아, 예. 뭘 이 정도 가지고. 마땅히 해야 할 일이었는데요.”

나는 손사래를 치며 힐끗 최 팀장의 눈치를 살폈다.

혹시나 [통합 언어팩]이 잘못 작동해서 이상함을 눈치채면 어쩌나 했는데, 지금은 대화를 나누는 상대가 샤오 쉔인 만큼 내가 하는 말도 최 팀장의 귀에는 중국어로 들리는 것 같았다.

“그런데 옆에 계신 분은……?”

이들 중 유일하게 낯선 사람.

묵묵히 우리의 대화를 듣고 있던 반백의 장년인이 손을 내밀어 악수를 청했다.

「중앙 군사위원회에서 국방부장을 맡고 있는 웨이펑후라고 하오. 반갑소, 진 선생.」

“국방부장이라면…….”

「계급은 상장이오.」

“아아.”

대단한 사람인 건 알겠는데, 상장이 뭔진 모르겠다.

내 생각을 읽었는지, 옆에서 최 팀장이 개미만 한 목소리로 속삭였다.

“포 스타요. 포 스타.”

“아아, 아아아! 대장님이셨구나! 만나서 반갑습니다!”

나도 한때 별이 네 개였다. 어릴 때 했던 그 게임 참 재밌었지. 차기작은 쪽박도 그런 쪽박이 없었지만.

내 반응에 장년인, 웨이펑후가 희미한 미소를 띠며 손을 맞잡았다.

「젊은 분이라 그런지, 혈기왕성하시구려. 진 선생께 물어볼 것이 많은데…… 우선 가면서 얘기하시겠소?」

“그러죠, 뭐.”

웨이펑후를 따라 발걸음을 옮기려던 내가 멈칫했다.

“그런데 어디로 갑니까?”

「작전 본부요. 제트기를 대기시켜 두었소.」

“예? 본부? 제트기요?”

「그렇소. 모두 그곳에서 진 선생을 기다리고 있지.」

모두라니. 누구?
```

## Final English reading copy

```markdown
# Chapter 382

Strike the head, and the body falls.

The moment I seized the three who looked like the leaders, the undead they had been controlling stopped moving like wind-up dolls, and the monster army, having lost its command structure, scattered and collapsed. Some died, while others fled.

“Arch Lich?”

At my question, the three kneeling figures nodded.

I wasn’t sure whether I could call things that were already dead and reduced to bones “guys,” but whatever.

I stroked each of the three skulls in turn and continued.

“When someone talks to you, you’re supposed to answer. Are you putting on airs just because you’re dead?”

The answer came almost before I had finished speaking.

—Yes. Yes. It is an Arch Lich.

—What you heard is accurate, human sir.

—Indeed.

“Hmm. An Arch Lich. That’s a monster I’ve never heard of before… But which one of you answered informally at the end?”

—That one!

—How dare he speak so casually to our great human master!

Whip! Whip!

The bony fingers pointed at one of them.

Betrayed by his comrades with lightning speed, the accused skull began to tremble.

—No! This is a despicable false accusation!

“…I don’t think it’s a false accusation.”

If he was going to lie, he could at least have changed the way he talked.

After glancing around, I took *that* out of my Inventory.

“Bones. Time for a snack.”

A skull with a strange black sheen. Flames flickered in its empty eye sockets.

—…Bones? If you insist on calling me something, call me Warlordmon like before.

“Why? You’re a skeleton, so Bones. It fits perfectly.”

—How dare you insult this commander like this!

“If you don’t like it, fine.”

Just as I was about to put it back in my Inventory, the Skeleton Warlord shouted in an enraged voice.

—Thank you for the meal!

“What an honest little guy.”

Honest children deserved rewards. Liars deserved punishment.

“All right. Have a taste.”

—Thank you. You are a slightly less wicked human. But how much should I eat…?

“Just a little, like before.”

—Hmm. I want to eat more. But I understand.

Even snacks were too much if you gave them out too often. After expressing its slight disappointment, the Skeleton Warlord opened its jaws wide toward the trembling figure.

—Come here.

—Eek! No!

—Yes!

The change began with the Skeleton Warlord’s decisive shout.

Whoooosh!

That was still amazing, even after seeing it again.

Like being sucked up by a vacuum cleaner, black mist began flowing from the kneeling figure’s body and being absorbed into the Skeleton Warlord.

—Gaaah!

But the change did not end there.

The more black mist flowed out—the substance the Skeleton Warlord called death energy—the whiter the figure’s complexion became.

Or, rather, its bones became whiter and whiter.

The Skeleton Warlord’s black sheen, meanwhile, grew deeper and richer.

—S-Stop!

—Heh heh heh. Such delicious death energy.

—Nooo!

—This commander shall take it all. Deeeath energy!

Crack!

—Hrk!

“Don’t go around saying ‘deeeath energy.’ Where did you even learn something like that?”

—…Are you really in a position to say that?

“Anyway, stop eating now.”

—Why?!

“You’ll get fat.”

The Skeleton Warlord fell silent for a moment. I tucked it inside my clothes and looked at the figure.

When I had first seen it, its bones had been dark and dirty. Now, it was half-white, as though it had been bleached. Perhaps because it had lost so much death energy, the green light in its eye sockets swayed dangerously.

—Hic… Sob…

At the sight of their comrade, who had been sucked dry down to his bones, the other two anxiously clicked their teeth together.

—Command us in anything, great ruler of flame.

—Please, I beg you. Accept the loyalty of this insignificant being, Orpheus von Maximus Valencia Bayern.

“…You’re undead, not a bidet.”

They really didn’t want to lose their strength. Well, I was grateful that they were being so cooperative.

“All right. If there’s anything you haven’t told me, scrape the bottom of the barrel and confess everything. If you start feeding me any lies…”

—We will tell you everything!

—Please, I beg you. Grant this false and insignificant being permission to speak the truth!

—I-I will tell you.

Apparently unwilling to become bone broth, the three skeletons enthusiastically participated in the interrogation.

After hearing every single thing that had happened from the Arch Lich’s first appearance a week ago until now, I deliberately furrowed my brow.

“Are you sure?”

—Yes, great human!

—I swear upon the River of Death!

—T-There is not a single lie.

At the sight of the three vigorously nodding skulls, the Skeleton Warlord suddenly interrupted.

—It is true.

“Did they pay you off? How can you guarantee that?”

—Because they swore upon the River of Death. For beings like us, that is an absolute promise. It cannot be broken.

“Hmm.”

The guy was usually as frivolous as they came, so hearing it speak with such gravity made me think this probably wasn’t a lie.

Besides, the three of them had no reason to scheme in a situation like this.

“All right. I believe you.”

—Thank you! Thank you so much!

—Sob, sob! I shall devote my entire loyalty to you, my king!

—I-I mean, I will also swear loyalty to you, human sir. I swear upon the River of Death that I will never commit an act like today’s again—

Crack!

The last one could not finish speaking.

His trembling green eye light shifted back and forth between the fist embedded in his chest and me.

—W-Why?

“Why do you think?”

—I-I, loyalty, swear, River of Death…

“You’re too late.”

A voice as cold as though it belonged to someone else slipped through my lips.

“It’s too late to undo what you’ve done.”

A great many people had died here today.

Even regular troops armed with firearms and Hunters had been unable to stop them, so there was no telling how many civilians the monster army had killed over the past week.

“I don’t need your loyalty. Especially not when it’s offered by bastards like you.”

The moment I released the Scorching Yang Qi I had drawn up from my dantian—

Whoosh!

Extreme Yang energy surged from the fist embedded in the figure’s shattered ribs. Blue-white Force, radiating a heat beyond anything ordinary, coiled around its entire body.

Boom!

I saw it.

The green light in its eye sockets flickered like a candle in the wind, then went out.

I also saw the other two figures spring to their feet and begin chanting spells.

—Jazuchawa Umbado…!

—Vargan Mahra…!

Whoooom.

A wind of mana swirled around them. Just as their sinister spell was about to be completed, I casually said,

“Devour them. All of them.”

As though it had been waiting only for those words, the Skeleton Warlord leaped from between the folds of my clothes and opened its jaws wide.

—As you command.

—Varsaba… Eek!

—N-No!

The final screams of monsters that wanted to live—or, rather, wanted to remain undead.

But contrary to their wishes, the Skeleton Warlord’s suction was stronger and faster than ever.

Whoooosh! Gulp!

After swallowing an enormous amount of death energy in a single bite, the Skeleton Warlord’s skull trembled.

In the next moment, the two skeletons whose energy had been completely drained collapsed in a heap.

Ding. Ding. Ding.

> **System**
>
> —You have successfully completed the unexpected Quest, **Unexpected Attack**!
>
> —You have caused the monster army to collapse! This is truly an outstanding achievement!
>
> —As a Quest Reward, you have acquired the Title **Undead Hunter**!
>
> —You have acquired a considerable amount of EXP and Fame!
>
> —Level Up!

*Only once?*

In the past, I would have leveled up several times without difficulty. But now that I had reached Level 120, it seemed the amount of EXP I needed had increased.

*It’s not like I did this for the EXP.*

I had merely done what needed to be done, but I couldn’t help feeling a little disappointed.

The stronger I became, the more useful I would be in the battles ahead.

*That guy is the same.*

I looked at the Skeleton Warlord while thinking to myself.

Perhaps because it had absorbed such an enormous amount of death energy, the power I felt from it was incomparable to what I had sensed when we first met.

—Hmm. Hoooo…

Black mist billowed through the holes in its skull where its nose, ears, and eyes should have been.

Its violet eye light burned like torches, while its surface gleamed with a smooth, deep-black sheen. Soon, its mad laughter reverberated through my head.

—Kahaha! Kahahahaha!

“Turn down the volume. You’re loud.”

—You wicked human. This time, this commander shall offer you his profound gratitude.

“You should. Who gave you your food?”

—Food?! Are you saying this body has become some kind of pet?!

“Something like that. Isn’t it?”

—Don’t talk nonsense!

“Oh? Bones, come here.”

When I held out my hand, the skull sprang up and landed in my palm.

As a reward, I gently scratched the spot between its eyes.

“Good job, Bones. Oh, aren’t you adorable?”

—…!

The skull began to tremble.

—H-How could this happen?! How could this commander be treated like this by a mere human?!

“You say no with your mouth, but your body is honest.”

—I am the master of the Black Forest and the commander of the great undead army. Do not humiliate this body!

“A commander with nothing but a head left?”

—What?! This insignificant body can be restored as many times as necessary as long as I expend death energy!

“Really? Then why haven’t you restored it yet?”

—…Because even if I restored it, some crazy human would just smash it again.

“Oh, correct.”

Grind.

The Skeleton Warlord had no teeth, so it ground its bones together instead. Its eye light narrowed.

—Why, wicked human?

“What?”

—You must have some ulterior motive for feeding me—or rather, for giving me such enormous power. You obviously have some dark scheme in mind. Speak the truth!

I thought for a moment before answering.

“Hmm. Because you’re a fucking scrub.”

—Huh?

“You can’t beat me anyway. If that’s the case, it’s easier to make use of a stronger, more useful scrub. Don’t you think?”

—…!

“All right. Stay inside now. People are coming.”

I put the Skeleton Warlord, frozen from the shock, back into my Inventory and stood up.

The airport duty-free corridor should normally have been crowded with employees and passengers. Now, in the empty, darkened passageway, three people were walking toward me.

Two of them had familiar faces.

“Mr. Jin Taekyung.”

“Mr. Jin.”

It was Team Leader Choi, who was in relatively decent shape, and Shao Shen, an A-rank Hunter from the Public Security Armed Forces Department of China.

Even though a considerable amount of time had passed since the battle ended, Shao Shen’s face was still covered in blood and dust, and exhaustion had settled heavily over his features.

“There you are.”

I exchanged a look of greeting with Team Leader Choi before making an excuse.

“Yes. I had something to take care of.”

“Please speak casually with me. Fuc—no, Mr. Jin, you are the hero who saved me, my comrades, and even the people of Zhonghua.”

“…”

*Was that my imagination, or had he almost called me Lord Fuck just now?*

Whether he knew what I was thinking or not, Shao Shen continued in an extremely respectful tone.

“Fortunately, with the help of the two gentlemen from the Peace Guild, we were able to defeat the monsters. I would like to take this opportunity to express my gratitude once again.”

“Ah, yes. It was nothing. It was simply what had to be done.”

I waved my hands modestly and stole a glance at Team Leader Choi.

I had worried that the *Integrated Language Pack* might malfunction and he might notice something strange, but since Shao Shen was the one I was speaking with, it seemed that Team Leader Choi was hearing my words as Chinese as well.

“But who is the person beside you…?”

The only unfamiliar person among them was a middle-aged man with graying hair. He had silently listened to our conversation before extending his hand for a handshake.

“I am Wei Fenghu, the Minister of National Defense under the Central Military Commission. It is a pleasure to meet you, Mr. Jin.”

“If you’re the Minister of National Defense, then…”

“My rank is general.”

“Ahh.”

I knew that meant he was important, but I had no idea what rank that actually was.

Perhaps he had read my thoughts, because Team Leader Choi whispered from beside me in a voice barely louder than an ant.

“Four-star. Four-star.”

“Ahh, ahhh! So you’re a general! It’s a pleasure to meet you!”

I had been a four-star once, too. That game I played when I was young had been a lot of fun. The sequel had bombed so badly, though.

At my reaction, Wei Fenghu clasped my hand with a faint smile.

“You are full of youthful vigor. I have many things I would like to ask you, but shall we talk while we walk?”

“Sure.”

I started to follow Wei Fenghu, then stopped.

“Where are we going?”

“To the operations headquarters. I have a jet waiting.”

“What? Headquarters? A jet?”

“That is correct. Everyone is waiting for you there, Mr. Jin.”

*Everyone? Who?*
```

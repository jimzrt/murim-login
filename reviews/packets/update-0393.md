<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0393.txt",
      "sha256": "e201e5dadfede18928d0c8d82dc668a7aa2a66dd56935f6528a81ce608aab4f1",
      "bytes": 13980
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0e417802aead1fcb2a4e5bc389664797c99526ff44a826b115c8b8f64a0139ec",
      "bytes": 3804
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d4b9ac1249c749a195290fb23f2df20a87fc01be8f7421472e43905f74072606",
      "bytes": 134775
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ea41bba733e4cfafa90c24c959f52742e058b59123386f2f2c4239eebb36910e",
      "bytes": 1168
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ce348a1ae3f3084dd2f7bc33d074dae7b99da7e5b1dd330364f1f3618eca6dfb",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "0f1f244582bc5ee4da2ecc76c4a78739e6dc9cbe40764cdfd5fe5721a17269a0",
      "bytes": 1396
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "2d1941d11c9d291a15918db31c6291b45acc4166f56f612b1ab56d3caec32351",
      "bytes": 535
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "f3a532dd7071f456b83638c56f2815350749a2176c9b13312922f8740f4d9943",
      "bytes": 720
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "df49f1499d3c83836457ed314d835304105592bdbdf912d10d1cfe97fa1b1f54",
      "bytes": 112473
    }
  ],
  "estimated_tokens": 10638
}
-->

# Durable State Update — Chapter 393

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 393. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 393. Profile updates may replace only one
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
  "chapter": 393,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 393,
    "continuity_sources": [393],
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
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "Jin has crossed the wall into true mastery and can use overwhelming physical force without internal energy when he restrains himself.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "The Skeleton Warlord cannot raise undead deeper inside the current battlefield because the Arch Lich's control grows stronger there.",
    "The western-front force suffered a major massacre near the city; Zhang Wei's force and Shao Shen's Hunters were killed, while the attackers escaped before Jin arrived.",
    "Shao Shen is alive but was sedated by Jin after attempting to pursue revenge against the attackers and General Liao; his surviving commanders agreed to wait before retaliating.",
    "General Liao's operation caused the deaths of about one hundred Hunters and hundreds of soldiers, and Jin broke his arms and crushed his kneecaps after learning he regarded the operation's failure as unacceptable.",
    "Sichuan Province remains under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, magical communications interference, and a large undead army controlled by the Arch Lich.",
    "The Sudden Quest The Desperate War Situation remains active, while the Unexpected Assault was canceled after its target completed its objective and disappeared; Jin lost 10 Strength as its failure penalty.",
    "The Arch Lich remains weaker than its former self, serves a separate true king, and has ordered the black knight to withdraw the undead legions and draw in the human army.",
    "Wei Fenghu remains China's Minister of National Defense and the Chairman's right-hand man; Lei Fei remains unconfirmed dead or alive after disappearing with his department's Hunters.",
    "Wu Heixing remains hostile toward Jin, while Lee Jungryong is seeking an undisclosed discussion with him."
  ],
  "continuity_sources": [
    392,
    391
  ],
  "open_questions": [
    "Who is the Arch Lich's true king, who is the black knight, and why did the black knight previously spare the hidden family and withdraw?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What important discussion does Lee Jungryong intend to have with Wu Heixing?"
  ],
  "safe_through": 392,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, 아크 리치 as Arch Lich, 최상급 포션 as Top-Grade Potion, and 상급 포션 as high-grade potion.",
    "Render 전하 as His Highness, 돌발 퀘스트 as Sudden Quest, 다급해진 전황 as The Desperate War Situation, and 꽌시 as guanxi with an explanatory footnote; preserve Jin's vulgar historical and cultural jokes."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 태자당 | **Crown Prince Party** | The faction associated with General Liao. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 392
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 392
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 389
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 388
- **Aliases:** None
- **Role:** One of China's concealed S-rank Hunters and head of the Public Security Armed Forces Department stationed in Sichuan Province, currently missing with his unit after the first Monster Wave.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** Wei Fenghu is his maternal uncle and raised him as his own son.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 389
- **Aliases:** None
- **Role:** Wu Heixing is a Chinese S-rank Hunter known for frequent media exposure and scandal who secretly practices martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts.
- **Personality:** Arrogant, status-conscious, abusive, and fiercely proud of his power, he responds to humiliation with anger, jealousy, and fear.
- **Voice:** Loud, insulting, entitled, and dependent on national and political status.
- **Relationships:** He is openly hostile toward Jin Taekyung and resents Jin receiving Chairman Shao Yang's attention.

## Korean source

```text
＃393화



전쟁은 전투의 연속이다.

숱한 피와 죽음을 남긴 그날의 전투가 끝나면 비로소 승패가 갈리고, 살아남은 이들은 한자리에 모여 내일의 전투를 준비한다.

쓰촨성 동서부 전선을 맡은 수뇌부들이 한자리에 모인 것 역시 그런 이유에서였다.

「피해가 너무 큽니다.」

가장 먼저 말문을 뗀 것은 사십 대로 보이는 중년의 군인이었다. 피가 말라붙은 군복을 걸친 그가 피로한 목소리로 말을 이었다.

「간신히 고지(高地)를 지키는 데에는 성공했지만…… 오늘 하루만 3천이 넘는 병력을 잃었습니다.」

상처뿐인 승리.

3천이라는 어마어마한 병력 손실도 손실이지만, 더욱 큰 문제는 전사자 중 3할 이상이 헌터이며 그중엔 사령관을 비롯한 고위장교가 포함되어 있다는 사실이다.

세 배에 달하는 병력 차를 감안하더라도 타격이 엄청났다.

「상부에서는 답신이 왔소?」

「물론입니다. 내부 회의를 거쳐 동이 트기 전에 새로운 사령관을 파견한다더군요.」

「그나마 다행이로군. 그럼 혹시 신임 사령관은 누구…….」

침울한 분위기 속에서 사람들이 대화를 주고받던 그때, 한 사람이 불쑥 입을 열었다.

「다행? 정말 다들 그렇게 생각해요?」

「……!」

침묵을 지키던 사람의 말은 무게감을 가지기 마련이다. 그 사람이 살아 있는 대격변의 영웅이자 S급 헌터라면 더더욱.

「비행 몬스터들의 습격으로 사령관을 포함한 지휘부 중 절반이 찢겨 죽었어. 휘하 병력은 우왕좌왕하다가 피해가 가중되었고. 이런 상황을 두고 다행이라고 할 수가 있나?」

항거할 수 없는 기운이 담긴 눈빛에 사람들이 움찔했다.

「그, 그게 말입니다.」

「변명하려는 것 보니까 본인들도 알긴 아나 보네. 그런데…….」

붉은 입술 사이로 흘러나오는 서늘한 목소리.

좌중을 차례대로 응시하던 파이 첸의 시선이 한 사내에 이르러 우뚝 멈췄다.

「넌 왜 변명조차 없을까?」

잠시 침묵하던 사내, 우헤이싱이 술이 담긴 크리스털 잔을 흔들었다.

「제가 왜 변명을 해야 합니까.」

「왜냐고 묻는다면, 글쎄…….」

파이 첸의 눈빛이 깊어졌다.

「어떤 병신 하나가 맡은 지역을 이탈하는 바람에, 그때를 기다리고 있던 비행 몬스터들이 사령부를 갈기갈기 찢어 놔서가 아닐까?」

「……그건 전방을 돕기 위해서였습니다.」

우헤이싱의 대답은 구차한 변명에 불과했다. 그가 후미를 이탈했을 때, 파이 첸이 이끄는 전방의 병력은 끝없이 밀려드는 몬스터 군단의 공세를 잘 막아 내고 있었으니까.

「아, 그것도 있었구나. 네가 멋모르는 애새끼처럼 전공을 세우겠답시고 깊숙이 들어가는 바람에 진형 허물어진 거. 너 구하겠다고 쫓아갔던 아이들, 시신도 못 찾은 건 아니?」

「죽고 사는 건, 전장에서는 흔히 벌어지는 일입니다.」

「그럼. 흔한 일이지.」

파이 첸이 나직한 목소리로 말을 이었다.

「너 같은 녀석이 쥐도 새도 모르게 죽는 일은 더 흔했고. 그러고 보면 세상 참 좋아졌어. 대격변 때였으면…….」

하지만 파이 첸의 말은 끝까지 이어질 수 없었다.

쩌적, 쨍그랑!

날카로운 소리와 함께 크리스털 조각이 사방으로 튀었다.

잔을 박살 낸 우헤이싱이 천천히 몸을 일으켜 세웠다.

「그쯤 하지?」

「하지? 너, 말이 상당히 짧다?」

「참는 것에도 한계가 있어. 파이 첸.」

「더 지껄여 보렴. 말이 짧아지는 것만큼 네 수명도 짧아지고 있다는 건 알아 두고.」

「매국노나 다름없는 홍콩계 따위가 어디서 감히……!」

「아하, 네가 똥 싸 놓은 전선을 수습한 그 홍콩계가 날 말하는 거라면 맞는 것 같은데.」

스아아아아.

두 사람으로부터 흘러나온 막대한 기세가 내부를 잠식했다. 엄청난 압박감에 사람들은 숨도 제대로 쉬지 못했다.

그리고 두 S급 헌터의 짧은 대치는, 다음 순간 파이 첸의 입가에 떠오른 조소(嘲笑)와 함께 끝이 났다.

「무섭고, 지치고, 그 와중에 전공은 세워야겠고. 그러다 보니 갈수록 조급해지지?」

「뭐?」

「아가야, 전쟁이라는 게 원래 그렇단다. 늘 사람을 벼랑 끝으로 몰아세우고 시험하지. 이런 지옥에서 버티려면 정신력이 강해야 해. 너처럼 내키는 대로 살아온 철부지에게는 힘들 수밖에.」

「……!」

우헤이싱의 표정이 기괴하게 일그러졌다. 그만큼 파이 첸의 한마디, 한마디는 그의 정곡을 찌르고 있었다.

「S급 헌터? 그럼 뭐 해, 정신은 일곱 살짜리 어린애에 불과한데. 너 같은 녀석은 지금 같은 전쟁에 없으니만 못한 존재야.」

「입 닥쳐! 당신이 도대체 뭘 안다고…….」

「뭘 아냐고? 그거 나한테 하는 말이니?」

파이 첸의 코웃음에 우헤이싱의 얼굴이 벌겋게 달아올랐다.

권력과 부를 양손에 쥐고 태어난 그였지만, 상대는 대격변을 온몸으로 헤쳐 나온 전쟁 영웅이었다.

홍콩계라는 이유로 언론으로부터 차별 대우를 받기는 했으나, 경험이라는 측면에서는 우헤이싱이 범접할 수 없는 존재인 것이다.

「왜 대답이 없어?」

이를 악물고 대답을 피한 우헤이싱이 주변을 훑어보았다.

모두가 구태여 입 밖으로 이야기를 꺼내지 않았을 뿐, 그들이 보인 눈빛은 파이 첸과 닮아 있었다.

‘이런 개 같은……!’

더욱 분통스러운 일은 그들 중엔 우헤이싱과 밀접한 연관이 있는 태자당의 인물들 역시 포함되어 있다는 것이었다.

중국 공산당 최대 계파인 태자당. 바로 그 태자당에서도 손꼽히는 거두의 핏줄인 우헤이싱은 뼈에 사무치는 배신감을 느꼈다.

「오늘 있었던 일은…… 내 똑똑히 기억해 두지.」

우헤이싱은 분노에 찬 한마디를 남기고 돌아섰다.

진한 술 냄새를 풀풀 풍기며 떠나는 그의 등 뒤로, 파이 첸의 나직한 목소리가 날아와 꽂혔다.

「이것도 기억해 둬. 어린애가 객기 부리는 것도 오늘까지라는 거. 다음에도 오늘과 같은 상황이 벌어진다면…… 그때는 내가 용서하지 않을 거야.」

까드득.

이를 갈며 숙소로 돌아온 우헤이싱이 가장 먼저 한 일은, 눈에 보이는 모든 걸 때려 부수는 것이었다.

쾅! 쾅쾅쾅!

「개 같은 홍콩 년! 자라 좆 같은 배신자 새끼들!」

혼란한 와중에도 전용기를 통해 실어온 값비싼 명품 집기들이 산산이 분해된다.

괴성과도 같은 고함을 내지르며 닥치는 대로 밟고 부수기를 한참. 우헤이싱은 거친 숨을 내쉬며 침대에 몸을 눕혔다.

「빌어먹을.」

도무지 사그라지지 않는 분노.

사라지기는커녕 오히려 생각할수록 열불이 솟구쳐 심장이 쿵쿵 뛰고 눈앞이 새하얗게 물들 지경이다.

‘감히, 감히 나를 이딴 식으로 취급해?’

중국에서 최정점에 있는 권력가의 집안에서 태어나 여기까지 왔다.

S급 헌터가 된 이후로는 완전히 그의 세상이었다.

어떤 대형 사고를 쳐도 아버지께 불려 가 질책 몇 번으로 끝났고, 사람들과 반대파 세력이 비난을 퍼붓는 것도 신경 쓰지 않았다.

‘난 우헤이싱이다. 우헤이싱!’

S급 헌터는 한 국가의 얼굴이자 국력(國力)의 또 다른 이름이 되었다. 여론이 아무리 손가락질해도 그 사실은 변함이 없었고, 그것이 현실이었다.

그래서였을까? 냄새나고 더러운 레이드보다 언론 인터뷰와 파티에 열을 올리게 된 것은. 트레이닝을 관두고 마약을 시작한 것은.

하지만 난생처음 겪어 보는 전쟁은 혼란했고, 하루하루 끝도 없이 밀려드는 몬스터 군단을 보고 있노라면 숨이 막혔다.

다이아가 깔린 엘리트 코스를 밟아온 그에게는 너무나도 힘든 환경이었다.

게다가 우헤이싱이 실수를 연발하는 데에는 한 사람에 대한 영향이 남아 있었다.

‘진태경.’

살면서 두 번째로 마주한, 오랜 질투의 대상이었던 레이페이보다도 거대한 벽.

놈이 드리운 그늘은 넓고 어두웠다.

일방적인 패배로 인해 뇌리 깊숙이 새겨진 두려움은 진태경이 사라지지 않는 한 떨쳐 낼 수 없을 것이다.

‘그래, 그 빵즈 놈이 사라지지 않는 한은…… 말이지.’

천장을 응시하는 우헤이싱의 눈동자에 알 수 없는 빛이 번뜩였다.

참혹하게 패배했던 그 날 밤, 이정룡과 나눈 대화를 떠올리며 그는 웃었다. 뜨겁게 끓어오르던 분노는 어느새 사라진 지 오래였다.

‘어디 한 번 두고 보자고. 마지막에 웃는 사람이 누구인지.’

마음이 진정되자 잠시 잊고 있던 피로가 몰려와 눈꺼풀을 짓눌렀다. 우헤이싱은 밀려오는 졸음을 느끼며 문득 생각했다.

‘젠장. 그나저나 앞으로 오늘 같은 전투를 얼마나 치러야 하는 거야?’

잠시 후, 완전히 곯아떨어진 우헤이싱은 알지 못했다.

한 치 앞도 보이지 않는 깊은 밤. 야음(夜陰)을 틈타 수많은 몬스터 군단이 전선에서 물러나고 있음을.

대이동은 쓰촨성의 모든 전선에서 동시다발적으로 일어나고 있었다.



* * *



「……후우.」

눈가가 붉게 충혈된 샤오 쉔이 한숨을 내쉬었다.

수혈이 짚인 채 하룻밤을 보낸 녀석은 두 시간 전에야 정신을 차렸다.

눈을 뜨자마자 랴오 상장을 죽여 버리겠다며 길길이 날뛰는 녀석을 진정시키느라 나와 최 팀장이 진땀을 빼야 했다.

“샤오 쉔 씨. 괜찮으십니까?”

“그래, 이제 좀 진정이 되냐?”

샤오 쉔이 대답했다.

「예. 처음 깨어났을 때는 몸에 힘이 들어가지 않았는데, 지금은 괜찮습니다. 이 정도면 놈의 머리통을 뽑아 버리기에 충분해요.」

“…….”

“…….”

진정은 개뿔.

그래도 말과는 다르게 주먹만 부르르 떠는 것이, 지금 당장 랴오 상장의 머리통으로 골프를 할 생각은 없어 보여서 한시름 놨다.

“다시 한번 말하지만, 너한테 그러고 싶지 않았어. 때가 안 좋았을 뿐이지.”

잠시 말이 없던 샤오 쉔이 고개를 끄덕였다.

「알고 있습니다, 형님. 저를 대신해서 나서 주신 것도요.」

“그건 또 언제 들었어?”

「중대장들이 와서 얘기해 주더군요. 격분하신 형님께서 랴오 상장의 팔다리를 분질러 버리셨다고요.」

“……널 말린 입장에서 할 짓은 아니었는데. 뭐 그렇게 됐다.”

최 팀장이 딱딱한 목소리로 끼어들었다.

“할 짓이 아니면 왜 하셨습니까?”

“그거야, 음. 순간 눈이 돌아가는 바람에.”

“현재 시국이 혼란스럽기에 망정이지, 자칫하면 일이 커질 수도 있었습니다.”

“다행이네요. 이런 시국이라서. 만약 아니었으면 그 자식은 저한테 진작 죽었어요.”

적군보다 무능한 지휘관이 더 무서운 법이다.

천 명에 가까운 목숨을 날리고 작전 실패니, 전공 운운하는 랴오 상장은 죽어도 싸다.

“잘 해결됐잖아요. 몸도 포션으로 거의 나았고, 저쪽도 찔리는 구석이 있으니 조용히 넘어가는 걸로.”

“원한은 오래 갑니다, 진태경 씨. 중앙 군사위원회 소속의 고위 장군, 그것도 뒤끝 심하기로 유명한 태자당 성골이니 차후에 문제가 생길 여지는 충분하죠.”

“어쩌겠습니까. 이미 엎질러진 물인데. 문제가 생기면 그때 가서 생각해 보죠.”

내 태평한 대답에 최 팀장이 고개를 절레절레 내젓던 그 순간, 샤오 쉔이 나직한 목소리로 입을 열었다.

「염려하지 마십시오. 최 선생님께서 걱정하시는 일은 일어나지 않을 테니까요.」

“응?”

“샤오 쉔 씨. 따로 들은 것이 있으십니까?”

「들었다기보다는…….」

잠시 머뭇거리던 샤오 쉔이 굳은 얼굴로 고개를 저었다.

「음…… 그저 제 개인적인 생각입니다.」

“……?”

“……?”

뭐지, 이 수상쩍은 냄새는.

나와 최 팀장이 샤오 쉔을 의심 어린 눈빛으로 바라보던 그때였다.

「드, 드, 드, 들어가도 되겠습니까?」

“……성대에 지진이라도 났나. 들어오세요.”

그제야 아까부터 막사 밖을 배회하던 인기척이 조심스럽게 안으로 들어왔다.

익숙한 얼굴. 랴오 상장을 가장 가까이에서 보좌하는 참모 중에 하나다.

하루 전, 상관의 사지를 부러트리는 내 모습에 오줌을 지렸던 사람이기도 했다.

“큰 나라의 지린이가 왔구나. 그런데 무슨 일로?”

「소, 소, 소…….」

“말, 말, 말, 말하고 싶은 게 뭔데. 제발 똑바로 말해.”

흠칫 몸을 떤 참모가 침을 꿀꺽 삼키고 대답했다.

「소, 손님이 오셨습니다.」

“손님?”

「예.」

“손님 누구? 여기서 면회도 되나?”

설마 엄마랑 하연이가 온 건 아니겠지.

순간 말도 안 되는 생각을 떠올린 내게, 참모의 대답이 날아들었다.

「미국의 매직 존슨 헌터가 찾아왔습니다.」

느껴졌다. 곁에 서 있던 최 팀장의 엉덩이에 힘이 들어가는 것이.
```

## Final English reading copy

```markdown
# Chapter 393

War is a succession of battles.

When a battle that has left behind countless dead and rivers of blood finally ends, victory and defeat are decided. Those who survive gather in one place and prepare for the battle of tomorrow.

That was why the commanders of the eastern and western fronts in Sichuan Province had gathered together.

“The casualties are too high.”

The first to break the silence was a middle-aged soldier who looked to be in his forties. Wearing a uniform caked in dried blood, he continued in an exhausted voice.

“We managed to hold the high ground by the skin of our teeth, but we lost more than three thousand troops in a single day.”

A victory that had left nothing but wounds.

Three thousand troops was an enormous loss in itself, but the bigger problem was that more than thirty percent of the dead were Hunters, including the commander and several high-ranking officers.

Even taking into account the three-to-one difference in troop numbers, the damage was staggering.

“Did headquarters send a reply?”

“Of course. They said they’ll send a new commander before dawn after holding an internal meeting.”

“That’s a relief, at least. Then, do you happen to know who the new commander will be…?”

As people exchanged words in the somber atmosphere, someone suddenly spoke up.

“A relief? Do you all really think that?”

“……!”

Words spoken by someone who had remained silent carried weight. Even more so when that person was a living hero of the Great Cataclysm and an S-rank Hunter.

“Half the command staff, including the commander, were torn to pieces by the flying monsters. The troops under them panicked, which only made the casualties worse. Can you really call a situation like this a relief?”

The people flinched beneath the gaze filled with an irresistible aura.

“W-Well, the thing is…”

“You’re trying to make excuses, so I suppose you do know. But…”

A chilly voice slipped from between red lips.

Faye Chen’s gaze moved across the room before stopping abruptly on one man.

“Why don’t you have any excuses?”

After a brief silence, Wu Heixing swirled the alcohol in his crystal glass.

“Why should I make excuses?”

“If you’re asking why, well…”

Faye Chen’s eyes deepened.

“Maybe it’s because some fucking idiot abandoned the area he was assigned to, allowing the flying monsters waiting for that moment to tear the command headquarters apart?”

“I did it to help the front line.”

Wu Heixing’s answer was nothing more than a pathetic excuse. When he abandoned the rear, the troops on the front line under Faye Chen’s command had been successfully holding back the endless assault of the monster army.

“Oh, right. There was that, too. You went charging deep into enemy territory like an ignorant brat because you wanted to earn some military glory, and the formation collapsed. The kids who chased after you to save your ass—do you even know that their bodies were never found?”

“Life and death are common occurrences on a battlefield.”

“Of course. They’re very common.”

Faye Chen continued in a low voice.

“People like you dying without anyone knowing used to be even more common. Come to think of it, the world has gotten pretty nice. If this had been during the Great Cataclysm…”

But Faye Chen’s words never reached the end.

Crack! Crash!

Crystal shards flew in every direction with a sharp sound.

Wu Heixing slowly rose to his feet after smashing his glass.

“That’s enough.”

“Enough? You’re getting awfully casual with your words.”

“There’s a limit to how much I can tolerate, Faye Chen.”

“Go on. Keep talking. Just remember that as your words get shorter, so does your lifespan.”

“How dare a Hong Konger who’s practically a traitor—!”

“Ah. If you mean the Hong Konger who cleaned up the front line you shat all over, then I suppose that’s me.”

Whoooooosh.

The tremendous auras flowing from the two of them spread through the room. Under the overwhelming pressure, the people could barely breathe.

The brief standoff between the two S-rank Hunters ended the next moment with a mocking smile appearing at the corner of Faye Chen’s mouth.

“You’re scared and exhausted, but you still want to earn military glory. That’s why you’re getting more desperate by the day, isn’t it?”

“What?”

“Kid, that’s what war is like. It always drives people to the edge and tests them. You need a strong mind to endure hell like this. For an immature child like you, who’s always lived however he pleased, it was bound to be difficult.”

“……!”

Wu Heixing’s face twisted grotesquely. Every one of Faye Chen’s words had struck him in the heart.

“An S-rank Hunter? So what? Mentally, you’re nothing more than a seven-year-old child. Someone like you is worse than useless in a war like this.”

“Shut your mouth! What the hell do you know…?”

“What do I know? Are you saying that to me?”

At Faye Chen’s derisive snort, Wu Heixing’s face flushed bright red.

He had been born with power and wealth in both hands, but his opponent was a war hero who had fought her way through the Great Cataclysm firsthand.

The media had discriminated against Faye Chen because she was from Hong Kong, but when it came to experience, Wu Heixing could not hold a candle to her.

“Why aren’t you answering?”

Grinding his teeth and refusing to respond, Wu Heixing swept his gaze around the room.

No one had bothered to say anything aloud, but the looks in their eyes resembled Faye Chen’s.

*You’ve got to be fucking kidding me…*

What infuriated him even more was that some of them were members of the Crown Prince Party who had close ties to Wu Heixing.

The Crown Prince Party was the largest faction within the Chinese Communist Party. As the blood descendant of one of the faction’s most prominent leaders, Wu Heixing felt betrayed to the bone.

“I’ll remember what happened today. Every bit of it.”

Wu Heixing turned away after leaving those words behind, thick fumes of liquor trailing from him.

Faye Chen’s low voice flew after him and struck him in the back.

“Remember this, too. A child’s little act of bravado ends today. If a situation like today’s happens again… I won’t forgive you next time.”

Grind.

The first thing Wu Heixing did after returning to his quarters, grinding his teeth, was smash everything within sight.

Boom! Boom-boom-boom!

“Fucking Hong Kong bitch! You goddamn traitor bastards!”

Even amid the chaos, the expensive luxury furnishings brought over on his private jet were smashed to pieces.

After stomping and breaking whatever he could reach while screaming like a madman, Wu Heixing finally lay down on the bed, breathing heavily.

“Damn it.”

The anger refused to subside.

Rather than fading, it only grew hotter the more he thought about it. His heart pounded, and his vision nearly turned white.

*How dare they treat me like this?*

He had been born into the family of one of the most powerful men in China and had risen all the way to this point.

After becoming an S-rank Hunter, the world had completely belonged to him.

No matter what major disaster he caused, the worst that happened was being summoned by his father and scolded a few times. He had never cared about the criticism from the public or opposing factions.

*I’m Wu Heixing. Wu Heixing!*

An S-rank Hunter was the face of a nation and another name for national power. No matter how much public opinion pointed fingers at him, that fact did not change. That was reality.

Was that why he had become more passionate about media interviews and parties than smelly, dirty raids? Why he had stopped training and started using drugs?

But the first war he had ever experienced was chaotic, and watching the monster armies advance endlessly day after day made it difficult to breathe.

For someone who had walked an elite course paved with diamonds, it was an unbearably difficult environment.

On top of that, there was one person whose influence still lingered behind Wu Heixing’s repeated mistakes.

*Jin Taekyung.*

A wall even greater than Lei Fei, the object of his long-standing jealousy—the second such wall he had encountered in his life.

The shadow Jin Taekyung cast was broad and dark.

The fear carved deep into Wu Heixing’s mind by his one-sided defeat would never be shaken off as long as Jin Taekyung remained.

*Right. As long as that peninsula bangzi doesn’t disappear…*

An inexplicable light flashed in Wu Heixing’s eyes as he stared at the ceiling.

Recalling the conversation he had shared with Lee Jungryong on the night of his terrible defeat, he smiled. The anger that had been boiling hot had disappeared long ago.

*Let’s wait and see. Let’s see who gets the last laugh.*

Once his mind calmed, the fatigue he had temporarily forgotten came rushing back and weighed down his eyelids. As drowsiness overcame him, Wu Heixing suddenly thought:

*Damn it. Just how many battles like today’s are we going to have to fight from now on?*

A short while later, Wu Heixing fell fast asleep, unaware that countless monster armies were withdrawing from the front lines under cover of the pitch-dark night.

The great movement was taking place simultaneously across every front in Sichuan Province.

* * *

“……Phew.”

Shao Shen let out a sigh, his eyes red and bloodshot.

He had spent the night with his Sleep Acupoint struck and had only regained consciousness two hours ago.

The moment he opened his eyes, he had gone berserk, shouting that he was going to kill General Liao. Team Leader Choi and I had sweated bullets trying to calm him down.

“Shao Shen, are you all right?”

“Yeah. Are you feeling a little calmer now?”

Shao Shen answered.

“Yes. When I first woke up, I couldn’t put any strength into my body, but I’m fine now. This is more than enough to rip that bastard’s head off.”

“……”

“……”

Calmer, my ass.

Still, unlike his words, only his fists were trembling, so I felt some relief that he did not seem to be planning on playing golf with General Liao’s head right away.

“I’m telling you again, I didn’t want to do that to you. The timing was just bad.”

Shao Shen was silent for a moment before nodding.

“I know, hyung. I know you stepped in on my behalf, too.”

“When did you hear that?”

“The company commanders came and told me. They said that furious hyung broke General Liao’s arms and legs.”

“……As the person who stopped you, it wasn’t something I should have done. But, well, that’s how it turned out.”

Team Leader Choi cut in with a stiff voice.

“If it was something you shouldn’t have done, why did you do it?”

“That’s because, um… I lost my head for a moment.”

“It’s fortunate that the current situation is so chaotic. Otherwise, this could have become a serious problem.”

“Lucky for us, then. If things weren’t like this, that bastard would have died by my hand long ago.”

An incompetent commander was more frightening than an enemy.

General Liao had thrown away nearly a thousand lives and was talking about military glory after the operation had failed. He deserved to die.

“Everything worked out. His injuries are almost healed thanks to a potion, and they have reasons of their own to feel guilty, so they’ll let it slide.”

“Grudges last a long time, Mr. Jin. He’s a high-ranking general of the Central Military Commission, and a pure-blooded member of the Crown Prince Party, notorious for holding grudges. There’s ample room for this to become a problem later.”

“What can we do? The water’s already spilled. We’ll think about it if a problem arises.”

Team Leader Choi was shaking his head in disbelief at my nonchalant answer when Shao Shen spoke in a low voice.

“Don’t worry. The thing you’re concerned about, Mr. Choi, won’t happen.”

“Hm?”

“Shao Shen, did you hear something?”

“Rather than hearing something…”

After hesitating for a moment, Shao Shen shook his head with a stern expression.

“Um… it’s just my personal opinion.”

“……?”

“……?”

What was this suspicious smell?

Team Leader Choi and I were looking at Shao Shen suspiciously when—

“M-m-m-may I come in?”

“Did an earthquake hit your vocal cords? Come in.”

Only then did the person who had been pacing outside the tent cautiously step inside.

It was a familiar face—one of the staff officers who served closest to General Liao.

He was also the man who had pissed himself the day before when he saw me break his superior’s limbs.

“The big country’s little pisser has arrived. What brings you here?”

“G-g-g…”

“S-s-s-say it already. What is it you want to say? Speak properly, please.”

The staff officer flinched, swallowed hard, and answered.

“A-a-a guest has arrived.”

“A guest?”

“Yes.”

“Who? Are visitors even allowed here?”

*It can’t be Mom and Hayeon, can it?*

That absurd thought had just crossed my mind when the staff officer’s answer came flying at me.

“Magic Johnson, a Hunter from the United States, has come to see you.”

I could feel Team Leader Choi clench his butt beside me.
```

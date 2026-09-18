<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0394.txt",
      "sha256": "4903f9b82321b0e5f4665e1bf9216234216087c67b5c5f4bf3981ec163437317",
      "bytes": 13135
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d45854dab83e120d414c464b5c9cd5c200f9c10ce88900733db3d91342f8faed",
      "bytes": 2796
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d4b9ac1249c749a195290fb23f2df20a87fc01be8f7421472e43905f74072606",
      "bytes": 134775
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "092d46479315261be1b74384da57a25f3f7630cf4d6d4393b848caece6316265",
      "bytes": 590
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0470d453ee99d0d90495d1f6f4c7b8177354afa5c96f5711ff518a16e5643563",
      "bytes": 533
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "828e51868d31aa929460d463fbc5b16aa814aeede91019d627b65e0e0db7a6c2",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "05249829a7bbac8d126de4f75928211beb5915bf91693fb6afd71dffa4896854",
      "bytes": 1168
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ed9e1322cb5125262f9020f52e927b9b92694dc445ef01da581b752592b2a3a6",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "af297cc476a8bf0997f4115536838777481926e8cbea8dc54892e6d17b0382cb",
      "bytes": 1396
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "0945243af6dc2e468a585b705321d80157821dd85f8651836f80e3281b08c535",
      "bytes": 113556
    }
  ],
  "estimated_tokens": 9947
}
-->

# Durable State Update — Chapter 394

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 394. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 394. Profile updates may replace only one
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
  "chapter": 394,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 394,
    "continuity_sources": [394],
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
    "Sichuan Province remains under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, magical communications interference, and a large undead army.",
    "The Sudden Quest The Desperate War Situation remains active, while the Unexpected Assault was canceled and its failure cost Jin 10 Strength.",
    "The Arch Lich remains weaker than its former self, serves a separate true king, and has ordered the black knight to withdraw the undead legions.",
    "Monster armies withdrew simultaneously from every front in Sichuan Province during the night.",
    "The western-front force suffered a major massacre near the city, while Wei Fenghu remains China's Minister of National Defense and Lei Fei remains missing with his unit.",
    "Faye Chen is an S-rank Great Cataclysm veteran commanding frontline forces in Sichuan Province and is openly hostile toward Wu Heixing.",
    "Wu Heixing remains hostile toward Jin Taekyung and now intends to act against him after recalling his conversation with Lee Jungryong.",
    "Shao Shen has recovered consciousness after Jin used the Sleep Acupoint on him, and Magic Johnson has arrived at Jin's camp seeking him."
  ],
  "continuity_sources": [
    393,
    392
  ],
  "open_questions": [
    "Who is the Arch Lich's true king, who is the black knight, and why did the undead legions withdraw now?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is Wu Heixing planning after recalling his conversation with Lee Jungryong?",
    "Why has Magic Johnson come to see Jin, and what does Shao Shen know about the consequences of Jin's confrontation with General Liao?"
  ],
  "safe_through": 393,
  "temporary_decisions": [
    "Render 파이 첸 as Faye Chen and 매직 존슨 as Magic Johnson.",
    "Render 형님 as hyung when Shao Shen addresses Jin Taekyung, and retain Mr. Jin for 진태경 씨 in Team Leader Choi's formal address.",
    "Preserve the hostile, profane tone of Faye Chen's confrontation with Wu Heixing."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 이정룡    | **Lee Jungryong** |
| 사부     | **Master**                                   |
| 칭호               | **Title**                      |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 부길드장    | **Vice Guild Master** |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 슬레이어 | **Slayer** | Cheon Taemin's title after killing the Demon King. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 청두 | **Chengdu** | Administrative capital of Sichuan Province and destination airport city. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 386
- **Aliases:** Slayer
- **Role:** Ares Guild Master; humanity's great hero and the world's greatest Hunter; killed the Demon King and is known as the Slayer; created the first Mana Cultivation Method during the Great Cataclysm.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 391
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 392
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 393
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 393
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 393
- **Aliases:** None
- **Role:** Vice Guild Master of Ares Guild; one of Korea's two S-rank Hunters; effective wielder of Ares Guild's authority in place of its Guild Master; Supreme Peak-level martial artist; gave Park Jihoon his initial orders and is Jihoon's master; visited the Peace Guild's hospital after Taekyung demanded an apology, brought compensation, and demanded the captives after negotiations.
- **Personality:** Outwardly genial, calm, and humorous; calculating, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃394화



역시 대륙은 사이즈부터가 다르다.

분명 작은 소도시라고 알고 있었는데, 막상 들어와 보니 그 면적과 인구수는 내가 예상했던 것을 훌쩍 웃도는 수준이었다.

그렇다 보니 몬스터 군단이 한바탕 휩쓸고 지나간 것치고는 멀쩡한 건물도 제법 되었다.

‘여기도 마찬가지고.’

현재는 임시 사령부로 활용 중인 시립병원의 입구.

키가 훤칠한 백인 헌터가 나와 최 팀장을 발견하고 다가왔다.

「기다리고 있었습니다.」

“혹시 매직 존슨이 보낸……?”

「네, 전 마이클 존슨이라고 합니다. 편하게 마이클이라고 부르세요.」

“아, 예.”

저 동네는 뭐 죄다 존슨이여. L.A 존슨 씨 종친회 소속인가.

나는 의문을 느끼며 마이클의 손을 맞잡았다.

악수를 나눈 그가 싱글벙글 웃었다.

“왜 그러세요?”

「당신의 열렬한 팬이거든요. 시벌좌.」

“……시벌좌 말고 그냥 진이라고 불러 주면 고맙겠는데.”

「왜요. 저라면 그 별명, 아주 마음에 들 것 같은데.」

“그럼 작은 존슨이라고 불러 드려요?”

마이클이 정색하며 대답했다.

「놉.」

단호한 것 보소. 나는 어이가 없어져서 대꾸했다.

“비슷한 맥락이에요. 그러니까 진으로 불러주세요.”

「아, 오케이.」

저놈의 시벌좌는 아주 지구촌 곳곳으로 뻗어 나가는구나.

마왕을 쓰러트리고 21세기의 구세주라 불리는 천태민은 슬레이어(Slayer)라는 간지 폭풍 칭호를 얻었는데, 나는 마왕이 아니라 마신을 때려잡아도 시벌좌로 남을 것 같다.

저기서 더 진화해 봐야 씨뻘좌가 한계겠지.

“너무 기분 나빠하지 마십시오. 시벌좌, 정감 가고 좋지 않습니까.”

“팀장님. 지금 저 놀리는 겁니까?”

“그럴 리가요.”

피식 웃는 최 팀장을 바라본 마이클이 알은체를 해 왔다.

「최. 당신도 왔군요.」

“절 아십니까?”

「물론이죠. 존슨이 당신을 얼마나 마음에 들어 하는지, 이미 길드원들 사이에 소문이 쫙 퍼졌어요.」

“…….”

나는 삽시간에 안색이 어두워진 최 팀장의 옆구리를 찔렀다.

“너무 기분 나빠하지 마십쇼. 존슨의 존슨이 팀장님을 마음에 들어 한다잖아요.”

“……진태경 씨. 방금 존슨을 두 번 말씀하셨는데요.”

“그래요? 말이 헛나왔나 보네.”

최 팀장의 따가운 시선을 모른 척하며 마이클에게 물었다.

“존슨은 어디에 있습니까?”

「아, 제가 안내해 드리죠.」

우리는 그를 따라 걸음을 옮겼다. 로비로 들어서자마자 웅성거리던 소음이 싹 사라지고 사람들의 시선이 우수수 날아와 꽂혔다.

간밤에 구조된 민간인도 몇 있다고 들었는데, 아무래도 임시 사령부다 보니 죄다 군인밖에 없는 모양이었다.

「진이 등장하니까 분위기부터 달라지는데요?」

“저야 원래 유명했는데, 어제 이후로 좀 더 유명해졌을 겁니다.”

「오, 혹시 네임드 몬스터라도 잡으셨습니까?」

마이클의 물음에 나는 어깨를 으쓱해 보였다.

“뭐, 얼추 비슷하네요.”

랴오 상장이 군부에서 차지하는 위치를 생각하면 네임드는 네임드다.

저쪽에서도 나름대로 함구령을 내리긴 했는데, 어떤 경로로 소문이 쫙 퍼졌는지 내가 지나갈 때마다 군인들의 숨죽인 속삭임이 흘러나왔다.

「그거 들었나? 어제 진 선생이 사령관을…….」

「그 얘기라면 듣긴 했는데, 헛소문 아니었어?」

「소문이 아니라 사실이래. 헌터들은 물론이고, 본부 작전병도 사실이라고 했다던데. 롸우양이 똑똑히 들었다더군.」

「허, 그게 사실이라면 진 선생한테 실망인데.」

「나도. 인민의 영웅이라 생각했건만.」

충분히 예상했던 반응이다.

가재는 게 편이고 팔은 안으로 굽는다고. 군인들로서는 직속 상관을 작살 낸 내 행동이 썩 좋게 보이지 않는 건 당연…….

「사지를 부러트리는 게 아니라 모가지를 뽑아 놨어야지.」

「그러니까. 그 돼지 새끼 하나 때문에 도대체 몇 명이 죽었는데.」

「그놈 이번 방산 비리에서도 크게 한몫 챙겼다며? 그러니 팔다리가 부러져도 쉬쉬하고 넘어가려는 거지. 그나마 진 선생을 따라다녀야 전공 부스러기라도 주워 먹어서 면피할 수 있으니까.」

「망할 도둑놈의 새끼. 그런 놈은 천안문 광장에서 목을 매달아야 하는데.」

……뭐지, 썩 좋게 보는 모양인데.

일반 병사들은 물론이고, 장교들까지 수군거리고 있다.

병력을 희생시킨 무능한 돼지 새끼라느니, 본인들이 왜 아직도 국공내전 때 만들어진 수통을 쓰는지 이제야 알았다느니.

이번에 밝혀진 정황과 랴오 상장의 평소 평판이 합쳐지니 상관 모독죄로 잡혀갈 만한 발언들이 수두룩하게 쏟아져 나온다.

“분위기 좋군요. 이대로라면 뒷일은 걱정 없겠습니다.”

나란히 걸어가던 최 팀장의 말에 내가 얼떨떨한 얼굴로 대답했다.

“그러게요. 이럴 줄 알았으면 몇 대 더 때릴 걸 그랬네.”

“음. 아직 상급 포션이 몇 개 더 남아 있긴 합니다만.”

“우리 팀장님. 이젠 농담도 잘하시네.”

“글쎄요. 아주 농담은 아닌데.”

“예?”

아니, 이 양반이 갑자기 왜 이래?

뜻밖의 반응에 당황하는 나를, 최 팀장이 똑바로 응시했다.

“진태경 씨는 명실상부한 S급 헌터입니다. 소시민의 꿈과 상징이자 대중의 지지를 한 몸에 받는 유명인이기도 하지요. 반면 랴오 상장은 부패한 기득권, 그 자체입니다. 진태경 씨를 건드리기 위해서는 엄청난 부담을 각오해야 할 겁니다.”

“그러니까 더 패도 상관없다?”

“상관이야 있겠지만, 곧 몰락할 랴오 상장 따위에게 발목 잡힐 일은 없을 거라는 말입니다.”

“참나, 몇 시간 전까지만 해도 사고 치지 말라면서요?”

“스포츠카가 아무리 좋아도 액셀만 밟으면 사고 납니다. 저처럼 옆에서 브레이크라도 걸어 주는 사람도 있어야 하지 않겠습니까? 그리고…….”

최 팀장이 나직한 목소리로 말을 이었다.

“가끔은 스포츠카가 잘 달릴 수 있도록 트랙도 정비해야죠. 지금처럼.”

“……?”

“어제는 당시 상황을 목격한 사람들이 너무 많았습니다. 어차피 지켜지지 못할 함구령이라면, 차라리 빨리 퍼트리는 게 나을 것 같더군요.”

머릿속에 떠오른 물음표가 느낌표로 변하기까지는 그리 오랜 시간이 걸리지 않았다.

“팀장님, 혹시?”

입을 딱 벌린 나를 바라보며 최 팀장이 웃었다.

“빠르게 선수를 쳐서 최대한 유리한 소문을 퍼트리는 것. 이정룡 부길드장이 자주 쓰는 방법이죠.”

“……허.”

이제야 얼추 아귀가 맞는다.

어쩐지 함구령이 무색할 만큼 소문이 빨리 퍼진 것 같아 의아했었는데, 최 팀장이 미리 손을 써 둔 것이 분명했다.

공안 무력부 헌터들이야 랴오 상장에게 극심한 반감을 품었으니 움직이기 쉬웠을 것이고, 군인들은……….

‘돈을 풀었군.’

뭐니 뭐니 해도 결국 머니다. 최 팀장은 돈으로 사람들의 입을 샀고, 그들은 최대한 우리에게 유리한 방향으로 소문을 퍼트렸다.

안 그래도 수많은 마이크와 스피커가 우글거리는 곳이 바로 군대 아닌가?

‘소문이 퍼지는 건 금방이지.’

열 명이 입을 열면 백 명이 듣고, 백 명은 천 명에게 그 소문을 알려 줬을 것이다. 그 과정에서 맛깔나게 MSG도 팍팍 치다 보면 부풀려진 소문은 어느새 사실로 알려지기 마련이다.

‘그런데 이걸 바로 생각해서 하룻밤 만에 해냈다고?’

나는 존경이 듬뿍 담긴 시선으로 최 팀장을 바라봤다.

“최 팀장님. 혹시 제갈공명입니까? 장량이에요?”

“이 정도는 별거 아닙니다.”

“쌀 팀장님. 저 최 것 같아요.”

“……그만하십시오.”

그런 대화를 나누는 사이 앞서가던 마이클의 발걸음이 멈췄다.

똑똑.

「존슨. 접니다, 마이클.」

VIP 개인실이라 적혀 있는 문 너머, 각기 크고 작은 두 개의 기운이 반응했다. 굵은 저음이면서도 쾌활한 목소리가 들려왔다.

「오, 어서 들어와.」

「그렇다는군요. 제가 맡은 임무는 여기까지라 이만.」

우리를 향해 어깨를 으쓱해 보인 마이클이 옆으로 물러섰다.

나는 어느새 엉덩이에 힘이 바짝 들어간 최 팀장을 대신해 문고리를 옆으로 밀었다.

드르륵.

부드러운 소리와 함께 두 사람이 모습을 드러냈다.

「하하, 이렇게 다시 보는군. 매력적인 젊은이들!」

성큼 다가와 솥뚜껑만 한 손을 내미는 거구의 흑인, 매직 존슨.

그리고…….

“히익!”

나를 보자마자 질겁하는 포동포동한 돼지 한 마리.

턱살을 파르르 떠는 랴오 상장을 힐끗 바라본 나는 매직 존슨의 손을 맞잡으며 속삭였다.

“언제 오셨어요?”

「한, 삼십 분 전쯤?」

“맡고 계신 전선은 어쩌고 여기에…… 그나저나 왜 바로 안 찾아오시고 저런 인간이랑 같이 계셨습니까?”

「잠깐 기다리게. 차례대로 대답해 줄 테니까. 물론 그전에 최랑 인사부터 하고.」

덥석.

먹이를 노리는 솔개처럼 최 팀장의 손을 낚아챈 매직 존슨이 반갑게 인사를 건넸다.

「잘 지냈나? 내 생각은 많이 했고?」

“……예.”

최 팀장의 대답은 100% 진심일 것이다. 여기까지 오면서도 오만가지 생각을 했을 테니까.

하지만 그 대답이 어떤 의미인지 모르는 매직 존슨을 설레게 만들기에는 충분했다.

「오오. 그 점은 나랑 같군. 우린 참 공통점이 많아. 그렇지?」

“…….”

특정 성별을 좋아한다는 점에서는 매우 다를 것 같은데.

「어쨌든 다시 만나게 돼서 반갑네.」

미련이 뚝뚝 떨어지는 눈빛으로 최 팀장과의 조우를 끝낸 매직 존슨이 조금 전의 질문에 답해 주었다.

「그리고 진, 내가 맡은 남부 전선을 이야기하는 거라면 걱정할 것 없어. 잠깐 자리를 비운 정도로 문제가 생기진 않거든.」

“전황이 상당히 좋게 흘러가고 있는 모양이네요.”

「흠. 글쎄. 당장 모든 전선에서 몬스터 군단이 퇴각하고 있다는 점에서는 고무적이지.」

“아하, 몬스터 군단이 퇴각…… 예?”

나와 최 팀장은 약속이라도 한 것처럼 서로를 바라보며 눈을 깜빡였다.

이게 도대체 뭔 소리야.

나보다 먼저 정신을 수습한 최 팀장이 매직 존슨에게 물었다.

“저희들로서는 처음 듣는 이야기입니다. 미스터 존슨, 혹시 어떻게 된 상황인지 알려 주실 수 있습니까?”

「말 그대로야. 간밤에 몬스터 군단이 꽁무니를 뺐어. 알아보니 모든 전선에서 같은 일이 일어났더군.」

“하지만 저희 측에서는 어떤 움직임도 포착하지 못했는데요.”

「아, 정정하지. 이쪽 서부 전선은 제외야.」

“어째섭니까?”

「뭐? 하하하!」

매직 존슨은 너털웃음과 함께 내 어깨를 두드리며 말을 이었다.

「그야 당연히 이곳, 서부 전선이 적진 가장 깊숙이 들어와 있기 때문이지. 아크 리치가 무슨 수작을 부리려는 건지는 모르겠지만, 서부 전선은 이미 뚫린 고속도로야. 놈들로서는 이미 물러설 만큼 물러섰다고.」

“아.”

잠시 잊었다. 육, 공군의 엄호하에 전투를 치르며 조금씩 전진하는 타 전선과는 달리, 나는 닥치는 대로 죽이고 부수며 진격했다는 것을.

‘일단 파죽지세로 뚫긴 했는데, 이 정도였나?’

얼떨떨해하는 내 모습에 매직 존슨이 껄껄 웃었다.

「21세기의 징기스칸답지 않은 모습이군. 어마어마한 전공을 세웠으니 조금은 웃어 보지 그래?」

“아직 맘 놓고 웃기에는 한참 이르죠. 그런데 몬스터 군단이 전선을 물린 건 둘째 치고, 이곳에는 무슨 일로?”

「최를 만나러 왔지.」

“……!”

“……!”

「농담이야.」

최 팀장 얼굴 핼쑥해진 것 봐라. 농담 한 번만 더 하면 괄약근 파열되겠다.

「아무래도 인원을 잠시 빼 가는 거니, 사령관에게 명령서를 전달해야 했거든.」

“뺀다고요? 어디로?”

「청두(成都). 군사 회의가 소집되었어.」
```

## Final English reading copy

```markdown
# Chapter 394

As expected, the mainland was on an entirely different scale.

I had clearly heard that this was a small provincial city, but once I actually entered it, the area and population were far beyond anything I had expected.

Even after a monster army had swept through the place, quite a few buildings were still standing.

*This one, too.*

At the entrance of the municipal hospital, which was currently being used as a temporary headquarters, a tall white Hunter spotted Team Leader Choi and me before approaching.

“I’ve been waiting for you.”

“Are you the one sent by Magic Johnson…?”

“Yes. My name is Michael Johnson. Please feel free to call me Michael.”

“Ah, yes.”

*Is everyone over there named Johnson? Is there some kind of Johnson family reunion in L.A.?*

I shook Michael’s hand, still puzzled.

After the handshake, he beamed at me.

“What?”

“I’m a huge fan of yours. Lord Fuck.”

“……”

“I’d appreciate it if you called me Jin instead of Lord Fuck.”

“Why? If it were me, I’d love that nickname.”

“Then should I call you Little Johnson?”

Michael answered with a perfectly straight face.

“Nope.”

*Look at how decisive he is.*

I was dumbfounded as I replied.

“It’s the same idea. So please call me Jin.”

“Ah, okay.”

*That Lord Fuck nickname is really spreading to every corner of the globe.*

Cheon Taemin, who had defeated the Demon King and was called the savior of the twenty-first century, had obtained the incredibly cool title Slayer. Even if I beat a Demon God instead of a Demon King, I would probably remain Lord Fuck.

At best, I’d evolve into Lord Fuuuck.

“Don’t take it too hard. Lord Fuck is a warm and friendly nickname, isn’t it?”

“Team Leader. Are you making fun of me?”

“Of course not.”

As Team Leader Choi let out a quiet laugh, Michael recognized him.

“Choi. You came too.”

“Do you know me?”

“Of course. The news of how much Johnson likes you has already spread throughout the Guild.”

“……”

I jabbed Team Leader Choi in the ribs. His expression had darkened in an instant.

“Don’t take it too hard. Johnson’s Johnson likes you, Team Leader.”

“……Mr. Jin. You just said Johnson twice.”

“Did I? I must have misspoken.”

Pretending not to notice Team Leader Choi’s sharp glare, I asked Michael,

“Where is Johnson?”

“Ah, I’ll show you.”

We followed him inside. The moment we entered the lobby, the murmuring noise abruptly vanished, and people’s gazes came flying toward us.

I had heard that several civilians rescued during the night were here, but since this was a temporary headquarters, it seemed to be filled almost entirely with soldiers.

“The atmosphere changes the moment Jin appears.”

“I was already famous, but I’m probably a little more famous after yesterday.”

“Oh, did you kill a Named Monster or something?”

I shrugged at Michael’s question.

“Something like that.”

Considering General Liao’s position within the military, he was a Named Monster in his own right.

The people on that side had issued their own gag order, but somehow the rumor had spread everywhere. Each time I passed by, I heard soldiers whispering under their breath.

“Did you hear? Yesterday, Mr. Jin did something to the commander…”

“If you mean that story, I heard it, but wasn’t it just a rumor?”

“They say it’s not a rumor. It’s true. The Hunters heard it, and apparently even the headquarters operations soldiers confirmed it. They said Rao Yang heard it clearly.”

“Huh. If that’s true, I’m disappointed in Mr. Jin.”

“Me too. I thought he was a hero of the people.”

The reaction was exactly what I had expected.

*Crabs side with crabs, and people’s arms bend inward.*

Naturally, the soldiers wouldn’t be happy about me pulverizing their direct superior…

“He shouldn’t have just broken the man’s limbs. He should’ve ripped his head off.”

“Exactly. How many people died because of that pig bastard?”

“I heard he took a huge cut in the latest defense procurement scandal, too. That’s why he’s keeping quiet and letting it go even after getting his limbs broken. Following Mr. Jin around is the only way he can pick up a few scraps of military glory and save his own skin.”

“That damn thief. Someone like him should be hanged in Tiananmen Square.”

*……What? They seem to like me quite a lot.*

It wasn’t just the ordinary soldiers. Even the officers were whispering among themselves.

They called General Liao an incompetent pig who had sacrificed his troops. Some said they finally understood why they were still using canteens made during the Chinese Civil War.

When the circumstances that had come to light were combined with General Liao’s usual reputation, an endless stream of statements poured out that could have gotten them arrested for insulting a superior.

“The atmosphere is good. At this rate, we won’t have to worry about the aftermath.”

Walking beside me, Team Leader Choi spoke with satisfaction. I answered with a dazed expression.

“Yeah. If I’d known, I should’ve hit him a few more times.”

“Hmm. I still have a few Top-Grade Potions left.”

“Look at you, Team Leader. You’re getting good at jokes.”

“Not entirely a joke.”

“Huh?”

*What got into this guy all of a sudden?*

Team Leader Choi stared straight at me as I struggled to process his unexpected response.

“Mr. Jin is an S-rank Hunter in both name and reality. You’re the dream and symbol of ordinary citizens, as well as a celebrity who enjoys the support of the public. General Liao, on the other hand, is corruption and entrenched privilege personified. Anyone who tries to come after Mr. Jin will have to be prepared to pay an enormous price.”

“So you’re saying it wouldn’t matter if I hit him a little harder?”

“It would matter, but I mean that you won’t be held back by someone like General Liao, who is about to fall.”

“Seriously? You were telling me not to cause trouble just a few hours ago.”

“Even the best sports car will crash if you only step on the accelerator. Someone needs to sit beside you and hit the brakes, like me. And…”

Team Leader Choi continued in a low voice.

“Sometimes you have to maintain the track so the sports car can run properly. Like now.”

“……”

“Yesterday, too many people witnessed what happened. If the gag order was bound to fail anyway, I thought it would be better to spread the story as quickly as possible.”

It didn’t take long for the question marks in my head to turn into exclamation points.

“Team Leader, did you…?”

Team Leader Choi smiled as he looked at me, my mouth hanging open.

“Getting ahead of things and spreading the most favorable rumor possible. That’s a method Vice Guild Master Lee Jungryong uses often.”

“……Huh.”

Everything finally fell into place.

I had wondered why the rumor had spread so quickly that the gag order seemed meaningless. Team Leader Choi had clearly laid the groundwork in advance.

The Hunters from the Public Security Armed Forces Department already hated General Liao intensely, so they would have been easy to mobilize. And the soldiers…

*He opened his wallet.*

In the end, it always came down to money. Team Leader Choi had paid people to talk, and they had spread the rumor in whatever way was most favorable to us.

Besides, wasn’t the military a place crawling with microphones and speakers?

*Rumors spread quickly.*

Ten people opened their mouths, a hundred people heard them, and those hundred people told a thousand more. If you added a generous sprinkling of MSG along the way, the inflated rumor was bound to become accepted as fact before long.

*But he thought of all that and pulled it off in a single night?*

I looked at Team Leader Choi with deep respect.

“Team Leader Choi, are you Zhuge Liang? Zhang Liang?”

“It was nothing special.”

“Team Leader Come. I think I’m about to Choi.”

“……Stop it.”

While we were having that conversation, Michael, who had been walking ahead of us, stopped.

Knock, knock.

“Johnson. It’s Michael.”

Beyond the door marked VIP Private Room, two auras of different sizes reacted. A deep but cheerful voice came from inside.

“Oh, come on in.”

“Apparently so. My assignment ends here, so I’ll be going.”

Michael shrugged at us and stepped aside.

I slid the door open in place of Team Leader Choi, whose butt was clenched tight.

Rattle.

Two people appeared behind the door.

“Haha! So we meet again, charming young men!”

The first was a huge Black man who strode toward us and extended a hand as large as a pot lid—Magic Johnson.

And then…

“Eek!”

A plump pig that shrieked in terror the moment he saw me.

I glanced at General Liao, whose double chin was trembling, then took Magic Johnson’s hand and whispered,

“When did you get here?”

“About… thirty minutes ago?”

“What about the southern front you’re in charge of? And for that matter, why didn’t you come find us right away? Why are you here with this guy?”

“Wait a moment. I’ll answer your questions one at a time. But first, I need to say hello to Choi.”

Snatch.

Magic Johnson caught Team Leader Choi’s hand like a hawk swooping down on its prey and greeted him warmly.

“How have you been? Have you thought about me a lot?”

“…Yes.”

Team Leader Choi’s answer was one hundred percent sincere. He must have thought about all kinds of things on the way here.

But since Magic Johnson had no idea what the answer meant, it was more than enough to set his heart aflutter.

“Oh! Then you’re just like me. We have so much in common, don’t we?”

“……”

*We’re probably very different when it comes to the gender we like.*

“Anyway, it’s good to see you again.”

With his gaze still dripping with longing, Magic Johnson ended his reunion with Team Leader Choi and answered my earlier question.

“And if you’re talking about the southern front I’m in charge of, don’t worry. Nothing will go wrong just because I’ve stepped away for a little while.”

“It sounds like the war is going very well.”

“Hmm. I’m not sure about that. It is encouraging that the monster armies are retreating from every front at the moment.”

“Oh, the monster armies are retreating… What?”

Team Leader Choi and I blinked at each other as though we had planned it.

*What the hell was he talking about?*

Team Leader Choi recovered first and asked Magic Johnson,

“This is the first we’ve heard of this. Mr. Johnson, could you tell us what happened?”

“It’s exactly as I said. The monster armies pulled back during the night. When we looked into it, the same thing had happened on every front.”

“But we didn’t detect any movement on our side.”

“Ah, let me correct that. This western front is the exception.”

“Why?”

“What? Hahaha!”

Magic Johnson slapped my shoulder with a hearty laugh before continuing.

“Because this western front has penetrated deepest into enemy territory. I don’t know what kind of scheme the Arch Lich is plotting, but the western front is already an open highway. They’ve already retreated as far as they can.”

“Oh.”

I had momentarily forgotten.

Unlike the other fronts, which were advancing little by little under Army and Air Force cover, I had simply killed and smashed everything in my way as I pushed forward.

*I did break through with unstoppable momentum, but was it really this much?*

Magic Johnson laughed loudly at my bewildered expression.

“That’s not very Genghis Khan of the twenty-first century. You’ve accomplished an incredible military feat, so why don’t you smile a little?”

“It’s far too early to relax and smile. But putting the monster army’s retreat aside, why are you here?”

“I came to see Choi.”

“……!”

“……!”

“I’m kidding.”

*Look at how pale Team Leader Choi’s face has become. If Magic Johnson makes one more joke, his sphincter might rupture.*

“Since I’m pulling some personnel away for a while, I had to deliver written orders to the commander.”

“You’re pulling them away? Where?”

“Chengdu. A military conference has been convened.”
```

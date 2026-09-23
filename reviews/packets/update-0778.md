<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0778.txt",
      "sha256": "bf10d37f2b23a59fd1f285358ccb70ff35ae3bd41358f6147c1d82383f893fac",
      "bytes": 12770
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "40f4887eb250995bf8c62ff26182527f9357c235ec2d4ec5a4a7efb593b38bcb",
      "bytes": 1160
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "45e50ae77be3c073d1488a74f8e2d08bfe6cbdb99494ab42a6437874780008c2",
      "bytes": 223212
    },
    {
      "path": "characters/Felix.md",
      "sha256": "4b8206a603c098ff94d7ac98ec005ad594cb1aea8105b276c48d7c67869fd1da",
      "bytes": 464
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0d601ee0e39bec0e0f84cc6e508e71ad53b6d12ebbc35a8d3e3cc2d7bf54359c",
      "bytes": 2096
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "30ef2b2681defbcb89419320c012256ac0ae2caf418bc3cca22c65c6c159d6ca",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "af9bebf9eb79b4ec7766bdde616d2637eada08abde0edbc537e64ea04eba051b",
      "bytes": 1384
    },
    {
      "path": "characters/Michael.md",
      "sha256": "f76d9ef77bd6e60f59cceb1fcf0042714efe36414c55ad39e3d386282844b890",
      "bytes": 859
    },
    {
      "path": "characters/Wu Heixing.md",
      "sha256": "69f6d724ae939af1eef656f2b2592544b725636eb842616f091924b82eec90b6",
      "bytes": 533
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "06096479fc323c602e89207b4ac9961607a3c66789752284f1bc07cdd4c1105a",
      "bytes": 241634
    }
  ],
  "estimated_tokens": 10102
}
-->

# Durable State Update — Chapter 778

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 778. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 778. Profile updates may replace only one
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
  "chapter": 778,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 778,
    "continuity_sources": [778],
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
    "Cheon Taemin is in a coma and too ill to join the coming war; Team Leader Choi publicly revealed this at the Federation’s inaugural ceremony, and Magic Johnson confirmed it.",
    "Michael Silbert is positioning himself to lead the World Hunter Federation and intends to eliminate Jin Taekyung as soon as possible.",
    "The Federation’s leadership vote has begun; Jin is silent during it, with the Skeleton King beside him.",
    "Jin plans to take a near-even chance on a dangerous course of action and has asked the Skeleton King to trust him and their friends."
  ],
  "continuity_sources": [
    776,
    777
  ],
  "open_questions": [
    "What dangerous course of action does Jin intend to take, and what will its consequences be?",
    "Who will be elected to lead the World Hunter Federation?",
    "Will Michael act on his intention to eliminate Jin?",
    "Can Cheon Taemin recover from his coma?"
  ],
  "safe_through": 777,
  "temporary_decisions": [
    "Render 도편추방제 as “ostracism by lot” and 도편추첨제 as “ostracism by ballot,” preserving Jin’s uncertainty."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 선배     | **Senior**                                   |
| 일격     | **One Strike**                         |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 우헤이싱 | **Wu Heixing** | Chinese S-rank Hunter who provokes Jin and nearly draws his sword. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 정룡 | **Jungryong** | Cheon Taemin's trusted associate who joined the Peace Guild. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 서울 | **Seoul** | Location announced for the World Hunter Federation's inaugural ceremony. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 우헤이싱 | 진태경 | hostile S-rank Hunter to foreign Hunter and provocation target | peninsula bangzi | insulting and confrontational | Wu repeatedly addresses Jin with anti-Korean slurs. |
| 우헤이싱 | 이정룡 | younger S-rank Hunter to senior Ares Guild authority | Mr. Lee | formal and deferential | Wu addresses Lee respectfully despite his usual hostility toward Koreans. |
| 필릭스 | 이정룡 | British prince to senior S-rank Hunter | Jungryong Lee | formal through a translation device | Felix permits Lee to omit His Highness and gives his own preferred form of address. |
| 진태경 | 필릭스 | Korean S-rank Hunter addressing a British prince | His Highness | mock-formal and sarcastic | Felix demands formal address, and Jin complies by calling him His Highness while continuing to mock him. |
| 진태경 | 우헤이싱 | adversarial S-rank Hunters | you idiot | insulting-casual | Mocks Wu's cowardice and orders him to stop complaining. |
| 이정룡 | 우헤이싱 | senior S-rank Hunter to younger allied S-rank Hunter | Mr. Wu | polished and formally coaxing | Lee publicly draws Wu into agreement with the suicide-squad plan. |
| 필릭스 | 진태경 | British prince and S-rank Hunter to allied Korean S-rank Hunter | Jin | lofty and aristocratic | Felix addresses Jin while discussing royal duty and their teleport. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |
| 필릭스 | 존슨 | prince_to_allied_grand_mage | Mr. Johnson | formal-polite | Felix uses a respectful address while speaking with Magic Johnson. |

## Listed compact profiles

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 776
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty, self-important, and conscious of royal duty.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 777
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 777
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 777
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regarded Cheon Taemin as an older brother despite no blood relation and long held him in respect and fear; secretly supported the orphanage where Lee Dongseok grew up and was regarded by Dongseok as a father; operated as Ares Guild's senior authority beneath its Guild Master; concealed Taemin's condition with Song Cheonwoo and participated in purging aides who knew the truth.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 777
- **Aliases:** None
- **Role:** Michael Silbert is Odin Guild Master and a public hero positioning himself to lead the World Hunter Federation; he intends to eliminate Jin Taekyung as soon as possible.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### Wu Heixing.md

# Wu Heixing (우헤이싱)

- **Safe through:** Chapter 733
- **Aliases:** None
- **Role:** Deceased S-rank Hunter who learned the Wu family's inherited Mana Cultivation Method and joined forces with Lee Jungryong to try to kill Jin Taekyung.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Son of Wu Shaiming and member of the Wu family; his Mana Cultivation Method became the reason Xiao Yang sought to persuade his father.

## Korean source

```text
＃778화



- 너도 내 친구니까.

나직이 흘려보낸 그 한 마디에, 스켈레톤 킹의 눈동자가 잘게 흔들린다. 나는 녀석을 똑바로 응시하며 말을 이었다.

- 단지 그뿐이야. 너도 내 친구라서. 이딴 식으로 잃으면 평생 기분이 더러울 것 같아서. 그래서 포기할 수 없는 거다.

- …….

- 중국에서 아크 리치랑 싸웠을 때. 기억해?

내 물음에 스켈레톤 킹이 말없이 고개를 끄덕였다.

그래, 어찌 잊을 수 있을까.

치열했던 그 날의 기억은 지금도 선명하게 뇌리에 각인되어 있었다.

- 그땐 진짜 죽는 줄 알았다. 아니, 상황이 그대로 흘러갔다면 십중팔구는 죽었을걸.

그만큼 힘든 싸움이었다.

앞길을 가로막은 수많은 몬스터들. 그리고 마침내 배신을 택한 이정룡과 우헤이싱을 처단한 뒤에야 마주한 아크 리치는, 당시의 내게 있어 버거운 상대였으니까.

하지만.

- 네가 날 구했지. 소멸까지 감수하면서.

아직도 눈앞에 선하다. 절체절명의 순간, 감히 허락도 없이 인벤토리에서 뛰쳐나와 아크 리치의 일격을 대신 받아 내었던 녀석의 모습이.

그건 희생이었다.

지극히 순수하며 숭고한 희생.

동시에 평범한 누군가가, 비로소 새로운 존재로 거듭날 수 있는 위대한 행위.

그렇게 검은 숲을 지배하던 스켈레톤 워로드는 왕관을 얻었다.

소멸의 끝자락에서 되돌아와, 찬란한 빛을 뿌리는 [영웅의 검]을 손에 쥐고 아크 리치의 가슴에 박아 넣었다.

- 그때 왜 그런 선택을 했냐.

- ……글쎄. 모르겠군.

문득 허공으로 시선을 돌린 스켈레톤 킹이 뇌까렸다.

- 굉장히 멍청하면서도 사소한 이유가 있었다는 것밖에는.

- 이유?

- 항상 궁금했던 것이 있었다. 나는 누구인가. 어디에서 태어나 무슨 잘못을 저질렀길래 지금 같은 몬스터가 되었을까. 분명 처음부터 이런 모습은 아니었을진대.

공허한 의념이 귓가에 울려 퍼졌다.

- 하지만 아무리 애써 봐도 살아 있던 시절의 기억을 떠올릴 수 없더군. 인간들의 세상에서, 인간들과 함께하는 매 순간에도 나는 혼란스러웠다. 스스로가 몬스터도, 인간도 아닌 무언가처럼 느껴졌으니까. 과거에 지은 죄로 끝나지 않는 형벌을 받는 것 같았으니까.

그래, 그 무렵의 스켈레톤 킹은 그랬다.

항상 심란한 표정으로 생각에 잠겨 있었고, 인벤토리에 들어가면 며칠씩이나 말이 없던 적도 있었다.

그리고 어느 날, 나는 녀석에게 지나가듯 한마디를 건넸다.

너라면 썩 괜찮은 놈이었을 것 같다고.

잘은 몰라도, 분명히 그랬을 거라고.

- 그래서였다. 단순한 위로였을지 모르는 그 말을 믿고 싶었고, 한편으로는 증명하고 싶었다. 만약 정말로 과거의 내가 썩 괜찮은 놈이었다면…….

스켈레톤 킹의 고개가 천천히 기울었다. 허공으로부터 떨어진 시선이 나를 향해 미끄러졌다.

- 다른 누군가를…… 친구를 위해 스스로를 희생할 수도 있을 테니까.

- ……!

- 그래, 맞다. 이 빌어먹게 간악한 인간이여.

스켈레톤 킹의 입가에 희미한 웃음이 맺혔다.

- 네놈은, 이 몸이 세상에 나와 처음으로 사귄 친구였다.

순간, 말문이 막혔다.

무슨 말이라도 해야 하는데. 그래야 할 텐데 머릿속에는 어떤 단어나 표현도 떠오르지 않았다.

그래서 그냥 웃었다.

입꼬리를 올리며 소리 없이 웃다가, 피식피식 실소를 흘리고, 이내 참지 못하고 소리 내어 웃었다.

앞에 놓인 거대한 원탁을 넘어 모두에게 들릴 만큼. 우리를 향해 수백 쌍의 이목이 쏠릴 만큼.

그리고 당황한 듯 눈을 깜빡이는 스켈레톤 킹을 향해 말했다.

“그 간단한 걸 이제야 알았냐. 이 멍청한 새끼야.”

- 모, 목소리 좀 줄여라.

“그냥 시원하게 말을 해. 다른 사람들 몰래 속닥거리지 말고.”

- 아니, 이게 뭔…….

“어차피 늦었어. 이미 다 쳐다보는 거 안 보여?”

내 말에 주위를 둘러본 스켈레톤 킹이 반쯤 자포자기한 목소리로 중얼거렸다.

“미친놈.”

“뭐, 미친놈? 말 다 했냐?”

“아직 다 안 했다. 관심종자 새끼야.”

“이 자식 이거 말하는 본새 봐라. 최 팀장님, 관리 안 하세요?”

“관, 뭐요?”

갑작스럽게 지목당한 최 팀장이 현타가 온 표정으로 이를 악물었다.

“예, 맞습니다. 죄송합니다. 이 모든 것이 진태경 씨를 관리하지 못한 제 잘못입니다.”

“아, 팀장님까지 이렇게 나오면 내가 좀 섭섭한데.”

“섭섭한 건 오히려 이쪽입니다. 원래대로라면 잠시 후에…… 아니, 도대체 이러실 거면 사전 계획이라는 말이 왜 있는 겁니까?”

그러게.

하지만 뭐 어쩌겠나. 일이 이렇게 흘러가 버린걸.

사람 일은 종종 알 수 없는 방향으로 흐른다. 바로 지금처럼.

그럼에도 현재 내 마음에는, 순서가 틀어졌다는 불안감 따위는 조금도 찾아볼 수 없었다.

그래, 그렇다면 된 거다.

다시 한번 크게 웃음을 터트린 나는, 어이없어하는 최 팀장을 향해 짐짓 목소리를 내리깔았다.

“최 팀장님, 모로 가도 서울로만 가면 된다는 말 못 들어 봤어요?”

“듣기 싫습니다. 그리고 이미 서울이에요.”

“그러지 말고 따라 해 보세요. 영. 차. 영. 차.”

“영차고 나발이고 좆 된 것 같습니다만.”

“괜히 튕기는 거 보니까 단단히 삐치셨네. 어차피 이렇게 될 거였잖아요.”

“순서가 다르잖습니까, 순서가! 진태경 씨는 물이 끓기도 전에 라면을 넣습니까?”

“아뇨. 오늘은 안 끓이고 부숴 먹을 건데요.”

“이 개씹……!”

최 팀장이 쌍욕을 할 수 있게 만드는 남자. 그것이 바로 나다.

그리고 눈깔이 뒤집힌 최 팀장이 이성을 상실하고 벌떡 일어나려던 그 순간. 등 뒤에서 불쑥 뻗어 나온 커다란 두 손이 그의 몸을 붙잡았다.

덥석!

“헤이, 최! 진정해!”

“놔! 안 놔? 당장 내 몸에서 손 떼!”

“제발 이성을 되찾아! 내 생각에도 진이 실수하긴 했지만…… 잠깐. 혹시 요새 벌크업 해?”

개판도 이런 개판이 없다.

나는 이때다 싶어 최 팀장의 잔 근육을 더듬는 매직 존슨에게 엄지를 치켜세운 뒤, 자리에서 일어나 주위를 둘러보았다.

딱 벌어진 입. 도대체 이게 뭔가 하는 싶은 표정과 흐려진 동공까지.

인류의 위기에 맞서 세계 헌터 연맹의 대표를 선출하는 이 중요한 자리에서 갑작스럽게 벌어진 소란에, 모두가 예토 전생으로 부활한 마왕 아스모데우스를 목격한 듯한 얼굴들을 하고 있었다.

물론 미리 사정을 알고 있던 몇몇 사람들은 빼고.

“아, 미안합니다. 원래 지금 터트릴 생각은 아니었는데.”

진심을 담아 건넨 정중한 사과였지만, 가끔은 진심이 먹히지 않을 때도 있는 법이다.

“이 빌어먹을 놈. 어쩌면 이게 내 인생 마지막 시가가 될수도 있겠군.”

폐암 말기 환자처럼 착잡하게 대답한 척 헤이글은 두 배나 빨라진 속도로 시가를 피워 댔고.

“괜찮아. 난 널 믿으니까. 하지만 엿 먹어, 진.”

파이 첸은 그윽하게 웃으며 중지를 치켜세웠으며.

“죄송합니다, 국왕 폐하. 저런 미친놈을 믿고 제가 섣부른 선택을…….”

영국 왕위 계승 서열 3위에 빛나는 필릭스 왕자는 회한에 찬 얼굴로 중얼거렸다.

하지만 이 자리에 모인 삼백여 명 중 가장 큰 혼란을 느낀 이를 한 사람 꼽으라면, 그건 바로 미카엘 실베르트였다.

- 도대체…… 무슨 꿍꿍이냐.

공간을 뛰어넘어 귓가를 파고드는 목소리.

그 어느 때보다 딱딱하게 굳어 있는 놈의 얼굴을 보자 나도 모르게 실소가 흘러나왔다.

- 웃어?

궁금해하는 사람에게는 대답해 주는 것이 인지상정.

나는 아랑곳하지 않고 입을 열었다.

“어, 웃었다. 어쩔래?”

- 네놈……!

귓가로 전해지던 목소리가 뚝 끊긴다. 어느덧 이 공간의 모두가, 내 시선을 따라 나와 미카엘 실베르트를 번갈아 바라보고 있었다.

“할 말이 있으면 모두가 들을 수 있게 당당하게 하세요. 그 나이 처먹고 귀 간지럽게 속닥거리지 말고.”

말하고 나니 너무 건방지게 들리는 것 같아서, 수줍게 한 마디를 덧붙였다.

“이 씨벌놈아.”

“……!”

“……!”

마치 수백 발의 핵미사일이 한바탕 휩쓸고 지나간 것처럼 온 사방이 고요해지고 주위를 에워싼 공기가 얼어붙었다.

그리고 그것은 이 믿을 수 없는 상황을 지켜보는 다른 이들과는 달리, 내게는 무언가에 꽉 막혀 있던 목과 가슴이 뻥 뚫릴 만큼 차가운 공기였다.

‘이제야 좀 숨통이 트이네.’

도대체 얼마 만에 느껴보는 후련함인지.

크게 심호흡한 나는 터덜터덜 걷기 시작했다. 원탁 사이사이를 지나쳤고, 몇 걸음 만에 그조차도 귀찮아져 모두의 머리 위를 훌쩍 뛰어넘었다.

쉬익, 탁.

가볍게 내려선 그곳은 텅 비어 있던 원탁의 중심이었다.

마치 보이지 않는 벽에 막히기라도 한 것처럼, 차마 그 공간으로 발을 디디지 못하고 있던 미카엘 실베르트가 이를 악무는 것이 보였다.

“이 무슨…… 무례인가.”

한껏 억눌린 목소리.

지금 이 순간 나를 노려보는 놈의 눈동자에서는 숨길 수 없는 분노가 담겨 있었고, 나는 그 분노의 이유를 매우 잘 알고 있었다.

“왜, 반평생 동안 그토록 바랬던 자리였는데. 뭣도 아닌 놈이 먼저 올라가니까 기분이 더러워?”

“……!”

“사실 어느 정도는 이해해, 나도 전에 비슷한 일을 많이 겪었거든. 어느 날에는 목욕 후에 먹으려고 남겨 놨던 아이스크림을 찾고 있었는데, 막상 나와 보니까 여동생이 다 먹고 껍데기만 남아 있더라고. 상당히 열 받는 상황이었지. 그런데…….”

말꼬리를 흐린 나는 딱딱하게 굳은 미카엘 실베르트의 얼굴을 응시하며, 천천히 말을 이었다.

“문득 그런 생각이 들더라. 겨우 이깟 게 뭐라고 내가 화를 내나. 그 정도까지 지랄 염병을 떨 일인가.”

나는 주위를 둘러보았다. 이미 예상했듯이, 대부분의 사람들이 나를 미친놈 보듯 바라보고 있다.

당연한 일이다. 가장 중요할 때 소란을 일으키지 않나, 대선배를 향해 쌍욕을 내뱉지를 않나. 거기에 더해 이제는 아무도 물어보지 않는 아이스크림 썰이나 풀고 있으니까.

그런데 그 표정들이 너무나도 웃겨서, 나는 그만 웃어 버렸다.

“뭐, 그냥 그랬다고.”

그리고 동시에 공력을 끌어올려, 거칠게 진각(震脚)을 밟았다.

“안……!”

콰직, 우드드득!

미카엘 실베르트의 뒤늦은 외침이 굉음에 파묻힌다.

누구도 말릴 수 없었던 찰나의 순간, 오직 한 사람만을 위해 마련된 원탁의 중심을 완전히 으스러트린 나는 경악에 찬 얼굴들을 바라보았다.

“곰곰이 생각해 봤더니 결국 이 자리도 그 아이스크림 같더라고. 다들 욕심이 없으면 화낼 일도 없는데, 꼭 욕심 있는 놈들이 나서서 문제를 만들어.”

물론 아이스크림과 세계 헌터 연맹 사이에는 비교할 수도 없을 만큼 큰 차이가 있다.

이 세상에서 차지하는 중요성도. 그리고…… 그 욕심이 불러일으킨 여파의 크기도.

바로 그 욕심 때문에 사람이 죽었다.

수십만 명이 넘는 사람들이 가족과 친구를, 집과 희망을 잃었다.

그토록 비싼 값을 치르고 그들이 얻은 것은, 절망과 두려움뿐이다.

그렇다면 저 자리와 아이스크림이 다를 것이 무엇인가.

나는 우스웠고, 허탈했다.

그리고 경악 속에서 나를 바라보는 수백 명을 향해 입을 열었다.

“모두 잘 들어.”

아니. 미카엘 실베르트를 향해.

“스톤 킹은, 몬스터다.”

툭 던진 그 한 마디가, 모두를 집어삼키며 폭발했다.
```

## Final English reading copy

```markdown
# Chapter 778

“Because you’re my friend, too.”

At those quiet words, the Skeleton King’s eyes trembled faintly. I looked straight at him and continued.

“That’s all there is to it. You’re my friend, too. If I lost you like this, I’d feel like shit for the rest of my life. That’s why I can’t give up.”

“……”

“Remember when we fought the Arch Lich in China?”

The Skeleton King silently nodded at my question.

Yeah. How could I forget?

The memory of that fierce day was still etched vividly in my mind.

“I really thought I was going to die. No—if things had kept going the way they were, I’d probably have died nine times out of ten.”

It had been that hard of a fight.

The countless monsters blocking our path—and the Arch Lich we’d finally faced after putting down Lee Jungryong and Wu Heixing, who had chosen to betray us—had been too much for me at the time.

But…

“You saved me. Even knowing you might be erased.”

I could still picture it clearly. In that life-or-death moment, he had leaped out of my Inventory without even asking permission and taken the Arch Lich’s strike in my place.

It was a sacrifice.

A purely selfless and noble sacrifice.

At the same time, it was a great deed that allowed an ordinary someone to finally become a new being.

And so the Skeleton Warlord, who had ruled the Black Forest, received a crown.

He returned from the brink of Erasure, took up the radiant [Hero’s Sword], and drove it into the Arch Lich’s chest.

“Why did you make that choice back then?”

“……Who knows. I don’t.”

The Skeleton King gazed up at empty space and muttered.

“All I know is that I had a very stupid, very trivial reason.”

“A reason?”

“There was something I’d always wondered. Who am I? Where was I born, and what sin did I commit to become the monster I am now? Surely I wasn’t always like this.”

His hollow thoughts echoed in my ears.

“But no matter how hard I tried, I couldn’t remember anything from when I was alive. Even in the human world, every moment I spent with humans left me confused. I felt like something that was neither a monster nor a human. As if I were being punished without end for a sin I’d committed in the past.”

Yeah. Back then, that was how the Skeleton King had been.

He was always lost in thought with a troubled look on his face. Sometimes, he’d go into my Inventory and not say a word for days.

Then one day, I’d casually said to him:

*I bet you were a pretty decent guy.*

I didn’t know for sure, but I was sure he had been.

“That was why. I wanted to believe those words, which might have been nothing more than comfort. And, in a way, I wanted to prove them. If I really had been a decent guy in the past…”

The Skeleton King slowly tilted his head. His gaze dropped from the empty space and slid toward me.

“Then I might be able to sacrifice myself for someone else… for a friend.”

“……!”

“Yes, that’s right, you damn crafty human.”

A faint smile touched the Skeleton King’s lips.

“You were the first friend this body made after coming into this world.”

For a moment, I couldn’t speak.

I had to say something. I should have. But not a single word or phrase came to mind.

So I just smiled.

I lifted the corners of my mouth and laughed silently, then let out a few short chuckles before I couldn’t hold back any longer and burst out laughing.

Loud enough for everyone to hear across the enormous round table. Loud enough for hundreds of pairs of eyes to turn toward us.

Then I looked at the Skeleton King, who was blinking in surprise.

“You only figured out something that simple now, you dumbass?”

“C-Could you keep your voice down?”

“Just say it out loud. Don’t whisper behind everyone’s backs.”

“No, what is this—”

“It’s too late anyway. Can’t you see everyone’s already staring?”

The Skeleton King looked around, then muttered in a half-resigned voice.

“You lunatic.”

“What, a lunatic? Are you finished?”

“I wasn’t finished. Attention-seeking bastard.”

“Listen to the way this guy talks. Team Leader Choi, aren’t you going to manage him?”

“Man—what?”

Suddenly singled out, Team Leader Choi clenched his teeth, looking as if grim reality had just hit him.

“Yes, that’s right. I’m sorry. This is all my fault for failing to manage Jin Taekyung.”

“Come on, Team Leader. You’re going to hurt my feelings if you pile on, too.”

“I’m the one who should be hurt. If things had gone according to plan, in a little while… No, why even call it a plan if you’re going to do this?”

Fair enough.

But what could I do? Things had gone this way.

People’s affairs often took turns no one could predict. Just like right now.

Even so, not a trace of unease crossed my mind about the plan going out of order.

Yeah. If that was how it turned out, then so be it.

I burst out laughing again, then lowered my voice as if I meant business and addressed Team Leader Choi.

“Team Leader Choi, haven’t you heard the saying, ‘It doesn’t matter how you get there as long as you get to Seoul’?”

“I don’t want to hear it. And we’re already in Seoul.”

“Come on, try saying it with me. Heave. Ho. Heave. Ho.”

“To hell with heaving and ho-ing. I think we’re royally fucked.”

“You’re putting up a front for no reason. You’re seriously sulking, aren’t you? This was going to happen anyway.”

“The order is wrong! The order! Do you put the ramen in before the water boils?”

“No. Today, I’m going to crush it up and eat it without boiling it.”

“You little shit—!”

The man who could make Team Leader Choi swear like that.

That was me.

And just as Team Leader Choi’s eyes rolled back and he lost control, about to spring to his feet, two enormous hands reached out from behind him and grabbed him.

“Hey, Choi! Calm down!”

“Let go! You hear me? Get your hands off me right now!”

“Please, get a grip! I know Jin made a mistake, too, but… Wait. Have you been bulking up lately?”

This was a mess beyond all messes.

Seeing my chance, I gave Magic Johnson a thumbs-up as he felt Team Leader Choi’s lean muscles, then stood and looked around.

Wide-open mouths. Faces asking what the hell was going on. Eyes gone unfocused.

A commotion had erupted out of nowhere at this important meeting to elect the World Hunter Federation’s representative as humanity faced a crisis. Everyone looked as if they’d just seen Demon King Asmodeus brought back with Edo Tensei[^1].

[^1]: A technique from *Naruto* that summons the dead back to life.

Except for the few who already knew what was going on.

“Ah, I’m sorry. I wasn’t planning to spring it on you right now.”

It was a sincere, polite apology. But sometimes sincerity just didn’t get through.

“You damn bastard. This might be the last cigar of my life.”

Chuck Hagel pretended to answer with the bleak resignation of a terminal lung cancer patient, all while puffing on his cigar twice as fast.

“It’s okay. I trust you. But go fuck yourself, Jin.”

Faye Chen gave me a warm smile and raised her middle finger.

“I’m sorry, Your Majesty. I trusted that lunatic and made a rash choice…”

Prince Felix, third in line to the British throne, muttered with a look of regret.

But if I had to name the one person among the three hundred gathered here who was the most confused, it would be Michael Silbert.

*What on earth… are you up to?*

His voice slipped through space and into my ear.

Seeing his face, stiffer than I’d ever seen it, I couldn’t help but let out a laugh.

*You’re laughing?*

It was only natural to answer someone who was curious.

I opened my mouth without a care.

“Yeah, I laughed. What are you going to do about it?”

*You…!*

The voice in my ear cut off. By now, everyone in the room was looking back and forth between me and Michael Silbert, following my gaze.

“If you have something to say, say it out loud so everyone can hear. Don’t whisper in people’s ears at your age.”

After saying that, it struck me as a little too rude, so I shyly added one more thing.

“You son of a bitch.”

“……!”

“……!”

The whole room fell silent, as if hundreds of nuclear missiles had swept through it. The air surrounding us froze.

But unlike the others watching this unbelievable scene, to me that cold air felt like it had finally cleared the blockage in my throat and chest.

*I can finally breathe.*

How long had it been since I’d felt this relieved?

After taking a deep breath, I started walking at a leisurely pace. I passed between the round tables, then got tired of even that after a few steps and leaped over everyone’s heads.

*Whoosh. Tap.*

I landed lightly in the empty center of the round table.

I saw Michael Silbert clench his teeth, unable to bring himself to step into that space, as though an invisible wall held him back.

“What… is this insolence?”

His voice was tightly restrained.

In the eyes of the man glaring at me, there was anger he couldn’t hide. And I knew exactly why he was angry.

“What, you spent half your life wishing for that seat, and now some nobody gets there before you? That piss you off?”

“……!”

“Honestly, I understand to some extent. I’ve been through something similar before. One day, I was looking for the ice cream I’d saved to eat after a bath, but when I came back out, my little sister had eaten all of it and left me the wrapper. I was pretty pissed. But…”

I trailed off, gazing at Michael Silbert’s rigid face, and continued slowly.

“Then I suddenly thought, what am I getting so mad about over something this trivial? Is it really worth throwing a fit over?”

I looked around. Just as I’d expected, most people were staring at me like I was crazy.

Naturally. I’d caused a scene at the most important moment, hurled curses at a Senior, and now I was telling an ice cream story nobody had asked for.

But their expressions were so funny that I ended up laughing.

“Anyway, that’s all.”

At the same time, I drew up my internal energy and stamped my foot down hard.

“Don’t—!”

*Crack! Rumble!*

Michael Silbert’s belated shout was swallowed by the roar.

In the split second when nobody could stop me, I completely crushed the center of the round table, a place set aside for just one man. Then I looked at the faces staring at me in shock.

“After thinking about it, I realized that seat was just like that ice cream. If nobody was greedy, there’d be nothing to get angry about. But the greedy ones always step forward and cause trouble.”

Of course, there was an incomparably vast difference between ice cream and the World Hunter Federation.

The importance of each in this world. And…the scale of the fallout caused by that greed.

People had died because of that greed.

Hundreds of thousands of people had lost their families and friends, their homes and their hopes.

After paying such a high price, all they’d gained was despair and fear.

So what was the difference between that seat and ice cream?

It was ridiculous. It was hollow.

Then I spoke to the hundreds of people looking at me in shock.

“Everyone, listen.”

No. I was speaking to Michael Silbert.

“The Stone King is a monster.”

That one casually tossed-out line swallowed everyone whole and exploded.
```

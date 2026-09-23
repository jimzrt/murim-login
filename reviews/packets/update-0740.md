<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0740.txt",
      "sha256": "2a5c934c3eacdac59ed61c5d5ba444f47165bcd00e7ba01d93e1554bd103a130",
      "bytes": 13367
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "17fe5af2dbadb51b94df57a543122c92663618a9f530af1e3c2cd1106a4cf2d3",
      "bytes": 1619
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "cbf4cb565be5dcffbc6361b0c9e148a4c2417112b4a349817c64e36439a46163",
      "bytes": 214177
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "23489e511e6b6d8615ab528ec0eb7ec32b27686a9b6d834acb241c7bf9fe24f3",
      "bytes": 752
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "b214d20a82c7f633a9c25fdb94873613dab3db682c75c83cdd9e05cdd5147b10",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "cceec71d7c6ef6aa5d4448d5bace5feb77cdd193ad3877588d03353038f11cbd",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "4e0eef9836b2d3a233156d8a6081894d4a90678da453afb1418aa5f8fa02184f",
      "bytes": 744
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "1bb3dd0e60e431bf964298673267426277842f2d522427f8f1c0f56667d87968",
      "bytes": 626
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4eb7ae6b7f72df9de6e81f6db97c762f07d9c04a11af54cc3539586facd3838b",
      "bytes": 226542
    }
  ],
  "estimated_tokens": 9840
}
-->

# Durable State Update — Chapter 740

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 740. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 740. Profile updates may replace only one
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
  "chapter": 740,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 740,
    "continuity_sources": [740],
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
    "The ten Monster Waves are publicly established as planned terrorist attacks using bombs and unrefined A-rank Magic Gems near high-mana Gates, with thousands dead.",
    "Michael Silbert has released Odin Guild footage and publicly shaped the narrative that the attacks were deliberate terrorism.",
    "The Prophet has threatened continued attacks, judgment, and punishment after displaying the severed heads of the former IS and Al Qaeda leaders.",
    "A masked figure is being linked by alleged 99.99%-matching video analysis to another identity of a young hero, and public discussion is targeting Jin Taekyung.",
    "The Skeleton King knows the public narrative is false or incomplete and cannot safely reveal the truth yet.",
    "An unidentified person is sitting cross-legged inside the room the Skeleton King enters."
  ],
  "continuity_sources": [
    739
  ],
  "open_questions": [
    "Who is the masked figure shown in the Prophet's transmission?",
    "What does the Prophet mean by saying that all of this began with the audience?",
    "How will the Prophet's promised further judgment and punishment proceed?",
    "Why is the Skeleton King bringing a silver tray to the unidentified person?",
    "What is the identity and condition of the person sitting cross-legged inside the room?"
  ],
  "safe_through": 739,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 인샬라 as Inshallah.",
    "Render 시벌좌 as Lord Fuck.",
    "Render 스켈레톤 킹 as Skeleton King.",
    "Render 조국일보 as Joguk Ilbo."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 도사      | **Daoist**                                                      |
| 방장      | **Abbot**                                                       |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 도사견 | **Tosa mastiff** | Taekyung’s nickname for the veteran third-week trainees. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 황하 | **Yellow River** | River along which civilization began. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 아프리카 | **Africa** | Region where terrorist organizations are reportedly conducting Gate and Magic Gem experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 오딘 | **Odin** | The name of the world's greatest Guild, invoking the Norse god. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 739
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 739
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 739
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 739
- **Aliases:** None
- **Role:** Michael is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, and the hidden architect of a coordinated terrorist campaign designed to isolate Ares Guild.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 739
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of a hidden Middle Eastern terrorist organization whose ten warriors carried out the day's coordinated attacks.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered as a sacred figure by the followers.

## Korean source

```text
＃740화



운기조식(運氣調息)의 묘리는 공력 증진뿐만이 아니다.

자연스럽게 신체 내부에 쌓이는 노폐물을 제거하고, 마음을 평온하게 가다듬는 것 역시 운기조식으로 얻을 수 있는 여러 가지 효능 중 하나였다.

물론, 최고의 집중 상태인 만큼 오감(五感)이 극대화되는 것은 말할 것도 없고.

‘이건…….’

저벅저벅.

누군가의 발소리가 천둥처럼 들려온다.

얼마 지나지 않아 문 앞을 서성이는 불청객의 정체를 깨달은 나는 공력을 갈무리했다.

띠링.

운기조식의 종료를 알리는 시스템 알림이 울려 퍼지기 무섭게 등 뒤에서 문고리가 움직였다.

달칵.

조심스럽게 열린 문 틈새로 풍겨 오는 진한 냄새.

긴 숨을 내뱉는 것으로 모든 것을 마무리한 내가 입을 열었다.

“알아서 나올 때까지 아무도 들어오지 말라고 했던 것 같은데…… 몬스터라 사람 말을 못 알아듣는 거냐. 아니면 아예 알아들을 생각이 없는 거냐?”

잠시 머뭇거리던 불청객, 스켈레톤 킹이 헛기침을 내뱉었다.

“크흠. 이 몸인 줄 어떻게 알았지?”

“기척.”

“기척?”

“어. 이미 죽은 놈이라 그런지 숨을 안 쉬더라고.”

“……묘하게 납득이 가면서도 기분이 나쁜데.”

“굳이 널 기쁘게 해 줄 필요는 없지.”

근처에 대충 벗어 놓았던 추리닝을 걸치고 돌아섰다. 번쩍거리는 은쟁반을 든 스켈레톤 킹이 집사처럼 서 있었다.

“그래서, 뭐 때문에 왔어?”

평소였다면 이미 단단히 삐쳐서 주둥이가 한 댓 발은 나왔을 거다.

그러나 오늘의 스켈레톤 킹은 달랐다. 녀석은 내 눈치를 슬금슬금 살피면서 은쟁반을 바닥에 내려놨다.

“식사해라. 네놈을 위해 이 몸이 친히 가져왔으니.”

“이런 거 가져오지 말라니까.”

“하지만 벌써 사흘 넘게 굶지 않았나.”

사흘 넘게?

뜻밖의 말을 들은 나는 문득 주위를 둘러보았다.

창문 하나 없이 사방이 가로막힌 방. 스마트폰도 없이 들어와서인지, 아니면 그럴 만한 정신도 남아 있지 않아서였는지 시간 가는 줄도 몰랐다.

‘벌써 그렇게 됐나.’

인간이라는 존재는 참 묘하다. 앞서 흘려보낸 날짜를 깨닫자마자 뒤늦은 허기가 찾아온 것을 보면 더더욱 그렇다.

하지만…….

내가 허기를 느낄 자격이나 있는 놈일까.

수천이 죽고 수만이 다쳤다. 그들 개개인이 어떤 삶을 살아왔는지는 알 수 없지만, 아무런 죄도 없는 이들이 대부분일 것이다.

바로 그런 이들이 내가 벌인 일로 말미암아 피해를 입었다. 죽고, 다치고, 소중한 가족과 친구를 잃었다.

불과 얼마 전까지만 하더라도 나를 영웅으로 치켜세우던 사람들은 하나둘씩 돌아섰고, 비난의 화살은 내 주변 사람들에게까지 영향을 미쳤다.

단지 나와 가깝다는 이유 하나만으로.

‘도대체 뭐가, 어디서부터 잘못된 걸까.’

머릿속을 떠나지 않던 그 의문을 해결하기 위해 혼자 방에 틀어박혔다. 먹지도, 자지도 않은 채 운기조식과 상념으로 하루하루를 보냈다.

그리고 마침내 답을 찾았다.

모든 것을 속 시원히 해결해 줄 답이 아니더라도, 잠시 잊을 수 있을 정도의 깨달음을.

“냄새 좋네.”

“어?”

“너 말고. 음식.”

순간 불쑥 꺼낸 말에 버퍼링이 걸린 스켈레톤 킹이 대답했다.

“어어. 된장찌개랑 갈비찜이다.”

냄새만 맡아도 누구 솜씨인지 알 만하다.

며칠 전부터 노심초사하며 식사를 차렸을 어머니의 모습을 떠올리며, 나는 은쟁반 위에 덮여 있던 뚜껑을 열었다.

달칵.

뜨거운 김이 솟아오르는 음식을 물끄러미 바라보다가, 오랜만에 보는 된장찌개를 한술 떴다.

그리고 입안에 넣기가 무섭게 도로 뱉었다.

퉤.

“어? 왜, 왜?”

뭐지, 이거.

당황하는 스켈레톤 킹과 된장찌개를 번갈아 보던 나는, 떨떠름하게 입을 열었다.

“이거 누가 만들었냐?”

“네 동생.”

“……아. 그래.”

“무슨 문제라도 있느냐?”

문제라. 있지. 그것도 심각하게.

하지만 대답 대신 나도 모르게 실소가 흘러나왔다.

이유는 잘 모르겠지만 그냥, 그랬다.

“먹고 갈게.”

“뭐?”

“이것만 먹고 간다고. 아, 샤워도 좀 하고.”

순간 내 말을 이해하지 못했는지, 한동안 눈만 깜빡거리던 스켈레톤 킹이 황급히 고개를 끄덕였다.

“어? 어어, 알았다. 그럼 이 몸은…….”

“그래. 이따 보자.”

도둑처럼 슬금슬금 문을 닫고 사라지는 녀석의 모습에, 다시 한번 이유 모를 실소가 터진다.

수저를 내려놓은 나는 갈비찜을 집고 크게 베어 물었다.

매우 다행스럽게도, 갈비찜은 어머니의 솜씨였다.



* * *



“사람들을 물어뜯고 다니는 사나운 개들이 있어서 쥐어팼는데, 이번에는 웬 미친개 두 마리가 나타났네요.”

며칠 만에 마주한 내 첫마디에, 뭐라 말할 것처럼 입술을 달싹이던 최 팀장이 고개를 끄덕였다.

“맞습니다. 그 미친개 두 마리가 더욱 많은 사람들을 물었고요.”

“최 팀장님도 제 잘못이라고 생각하세요?”

“미친개는 말 그대로 미친개에 불과합니다. 결국 시기와 명분의 차이일 뿐, 반드시 사람들에게 이빨을 드러냈겠죠.”

“하지만 결과적으로 그럴 계기를 준 사람은 저고요.”

“정 자책하고 싶으시다면 우리라고 합시다. 진태경 씨 홀로 한 일이 아니지 않습니까.”

“맞다. 이 몸도 사막에서 아주 큰 공을 세웠지.”

불쑥 끼어든 스켈레톤 킹의 말에, 최 팀장이 어깨를 으쓱해 보였다.

“그렇다는군요.”

“자책이 아닙니다. 그냥, 그것만큼은 분명히 해야 할 것 같아서요.”

모든 사건에는 원인과 결과가 있다.

그리고 수많은 이들이 죽고 다친 이상, 그 원인에서 나 역시 자유로울 순 없다.

그럴 생각도 없고.

“저를 비난하는 사람들을 이해합니다. 응원하는 사람들에게는 그저 감사하고요.”

“그게 끝입니까?”

“아뇨. 아직 가장 중요한 게 남았어요.”

나는 담담하게 말을 이었다.

“세상이 뭐라 하든, 저 미친개들을 잡을 겁니다.”

내 대답을 들은 스켈레톤 킹이 눈을 빛냈고, 최 팀장의 입가에는 희미한 미소가 맺혔다.

“나름대로의 답을 찾으셨군요.”

“완전한 답은 아니겠지만, 계속 나아갈 이유 정도는 되지 않겠어요?”

“그 정도면 충분합니다. 그럼 저도 한결 가벼운 마음으로 몇 가지 소식을 전해 드릴 수 있겠군요.”

“몇 가지 소식이라면…….”

“이번 사건이 일어나기 전부터 미카엘 실베르트와 오딘 길드 등에 관련된 정보를 취합하고 있었습니다. 그 결과가 얼마 전 나왔고요.”

마나 연공법의 공개 이전부터 다른 거대 길드의 동태를 주시하던 최 팀장이다. 빈틈없는 그의 성격을 생각해 보면 당연한 일이었다.

“뭡니까? 가급적 좋은 소식이었으면 좋겠는데.”

“안타깝지만 나쁜 소식도 있는데, 어떤 것부터 들으시겠습니까?”

“지금보다 더 안 좋을 수도 없겠죠. 나쁜 소식부터 말씀해 주세요.”

피식 웃은 최 팀장이 서랍에서 두꺼운 서류 뭉치를 꺼냈다.

“나름대로 정리했는데, 그럼에도 분량이 워낙 방대하더군요.”

“이건?”

“오딘 길드가 보유한 자산 및 사업체에 관련된 정보입니다. 물론 그중 상당수가 드러나지 않았지만요.”

“차명이라는 겁니까?”

“예. 법적으로는 관련이 없지만 사실상 오딘 길드의 자회사나 다름없는 식으로 운영되고 있었습니다. 다른 거대 길드나 기업도 흔히 이용하는 방식이지만…… 규모 자체가 차원이 다르죠.”

이쪽으로는 까막눈이나 다름없는 나지만, 쌓여 있는 서류 두께만 봐도 충분히 감이 왔다.

무슨 소린지 당최 알아들을 수 없는 단어와 문장이 가득한 서류를 훑어보던 나는 가장 가까운 비교군을 찾았다.

“아레스 길드보다?”

“아레스와 평화 길드를 하나로 합치고, 거기에 거대 길드 서너 개는 합쳐야 할 겁니다.”

“미친.”

“이런 식으로 오딘 길드가 맡은 게이트의 숫자만 따져도 전 세계를 통틀어 이백 개가 넘습니다. 영구 임대인 만큼 사실상 소유나 다름없고, 이를 통해 막대한 양의 마정석이 쏟아져 나오죠.”

비록 이중 상당수가 비공식적인 루트를 통했다 하더라도, 이백여 개의 게이트를 보유했다면 어지간한 소국(小國)과 비슷한 수준이다.

아니, 소속된 헌터들의 전력을 따지자면 그 이상일지도 모르지.

‘……차라리 그냥 미친개였다면 좋았을 텐데.’

냉정하게 말해서 미카엘 실베르트는 단순히 미친개가 아니다.

투견 중에서도 도사견이고, 심지어 영리하기까지 한 놈이었다.

‘하지만 반드시 때려죽여야 하는 놈이기도 하지.’

내심 중얼거린 나는 문득 한 가지 생각을 떠올렸다.

“그럼 혹시 그 게이트에서 나온 마정석들이, 정제되지 않은 채로 이번 테러에 이용됐을 가능성은요?”

“없습니다. 적어도 서류상으로는.”

“서류상으로는?”

“진태경 씨도 아시겠지만, 미카엘 실베르트라는 인물은 철두철미한 사람입니다. 마정석 밀반입이라는 위험을 감수할 이유도 없고, 설령 그렇다 하더라도 빈틈을 남겨 두지 않았겠죠. 테러에 이용된 마정석은 중동이나 아프리카 쪽에서 흘러나왔을 가능성이 높습니다.”

설득력이 있는 말이다.

중동과 아프리카는 대격변 이전부터 테러와 내전의 본고장이었고, 지금 이 순간에도 어디선가 피 튀기는 싸움을 이어 나가고 있을 놈들이니까.

테러리스트와 반군이 점령한 게이트에서 몇 개의 마정석이 나오는지, 그중 정제되지 않은 마정석이 얼마나 있는지는 누구도 정확히 알 수 없었다.

더군다나 미카엘 실베르트는 혼자가 아니었다.

놈에게는 자신과 같은 미친개이자, 든든한 조력자가 있었다.

“선지자.”

내가 불쑥 내뱉은 세 글자에, 최 팀장이 굳은 얼굴로 고개를 끄덕였다.

“그렇지 않아도 그에 관한 정보 역시 샅샅이 찾았습니다.”

“어떤 놈입니까?”

진심으로 궁금했다.

두 거대 테러 집단의 우두머리를 참수하고, 사분오열된 테러리스트들을 규합하여 전 세계를 뒤흔든 그 미친놈의 정체가.

그러나 다음 순간 들려온 최 팀장의 목소리는, 내 기대를 한참이나 벗어났다.

“모릅니다.”

“모른다고요?”

“예. 여러 가지 사정을 고려하더라도 선지자에 관해서는 알려진 바가 전무합니다. 심지어는 그날의 선언 이후 완전히 자취를 감췄고요.”

“아니 잠깐. 미국도요?”

“미국뿐만 아니라, 전 세계가 나선 지금도 마찬가집니다.”

나는 눈을 깜빡이며 생각했다.

이게 말이 되나?

스스로를 선지자라 칭한 그 미친놈은 미국뿐만 아니라 전 세계를 들쑤셔 놨다. 그런데 모두의 눈을 피해 자취를 감추다니.

“알면서도 기밀 유지를 위해 숨기는 건 아니고요?”

“얼마 전 척 헤이글과 연락이 닿았습니다. 신께 맹세코, 선지자가 어디 있는지 모른다더군요.”

사막에서도 함께했던 척 헤이글은 S급 헌터이기 이전에 미국의 국방장관.

그가 거짓말을 하지 않는 이상, 국방장관인 그가 모른다면 그건 정말 선지자가 하늘로 솟았다는 뜻이다.

‘도대체 뭐 하는 놈이지?’

내가 눈살을 찌푸린 그때, 최 팀장이 말을 이었다.

“그리고 한 가지 더. 미스터 존슨에게 연락이 왔습니다. 그와 같은 대마도사들 중 미카엘 실베르트와 접촉한 것이 유력한 인물을 찾았다더군요. 아마 그를 통해 더 핵심적인 정보를 알 수 있을 거라고 했습니다.”

다행히 이번에는 좋은 소식이다.

아직 누구인지 이름은 듣지 못했지만, 그 대마도사는 미카엘 실베르트의 실체를 어느 정도는 알고 있을 테니까.

그는 직접 아레스 길드의 A구역을 만들고, 거기에 더해 천태민의 상태를 알고 있던 주요 인물.

전 세계에 단 셋뿐인 대마도사인 그가 새로운 실마리가 될 것이다.

아니, 그럴 것이라고 생각했다.

얼마 지나지 않아 최 팀장에게 걸려온 전화에서 매직 존슨의 목소리를 듣기 전까지는.

- 빌어먹을. 그가 죽었어.
```

## Final English reading copy

```markdown
# Chapter 740

Circulating qi and regulating the breath was not solely about increasing internal energy.

Naturally removing the waste that accumulated inside the body and calming the mind were also among the many benefits of circulating qi.

And since circulating qi brought one into a state of supreme concentration, it went without saying that all five senses were heightened to their limits.

*What is this…?*

Thud. Thud. Thud.

Someone’s footsteps sounded like thunder.

Before long, I realized who the uninvited guest pacing outside the door was and brought my internal energy under control.

*Chime.*

Just as a System notification announcing the end of my qi circulation rang out, the doorknob behind me began to turn.

*Click.*

A strong scent wafted through the narrow gap as the door opened cautiously.

After finishing everything with a deep exhale, I spoke.

“I thought I said no one was to come in until I came out on my own… Are you unable to understand human speech because you’re a monster? Or do you just have no intention of understanding it?”

The uninvited guest hesitated before clearing his throat. It was the Skeleton King.

“Ahem. How did you know it was this body?”

“Your presence.”

“My presence?”

“Yeah. Maybe because you’re already dead, but you don’t breathe.”

“…That makes a strange amount of sense, but it’s still unpleasant.”

“There’s no reason for me to go out of my way to make you happy.”

I pulled on the tracksuit I had carelessly taken off nearby and turned around. The Skeleton King stood there like a butler, holding a gleaming silver tray.

“So why are you here?”

Normally, he would have been sulking hard by now, his pout stretching a good thirty feet.

But today, the Skeleton King was different. He kept glancing at me nervously as he lowered the silver tray to the floor.

“Eat. This body personally brought it for you.”

“I told you not to bring me things like this.”

“But you have been fasting for more than three days.”

More than three days?

Taken aback by his unexpected words, I looked around.

It was a room sealed off on all sides, without even a window. I had come in without my smartphone, and whether because of that or because I had not had the energy to care, I had completely lost track of time.

*Has it already been that long?*

Humans were strange creatures. They were even stranger when belated hunger struck the moment you realized how many days had passed.

But…

Did I even have the right to feel hungry?

Thousands had died, and tens of thousands had been injured. I did not know what kind of lives they had led, but most of them must have been innocent people.

Those very people had suffered because of what I had done. They had died, been injured, and lost their precious families and friends.

Until only a short while ago, the people who had raised me up as a hero had turned away one by one, and the arrows of condemnation had reached the people around me as well.

All because they were close to me.

*What exactly went wrong? And where did it begin?*

I had shut myself away in this room to find the answer to that question, which refused to leave my mind. Without eating or sleeping, I had spent each day circulating qi and lost in thought.

And at last, I had found an answer.

It was not an answer that could neatly resolve everything, but it was an insight that allowed me to forget it for a while.

“Smells good.”

“Huh?”

“Not you. The food.”

The Skeleton King froze as if he were buffering before answering.

“Uh, yeah. It’s doenjang jjigae and braised short ribs.”

Even from the smell alone, I could tell who had made it.

I pictured my mother anxiously preparing meals for me over the past several days and lifted the lid covering the silver tray.

*Click.*

I stared blankly at the food as steam rose from it. Then I scooped up a spoonful of doenjang jjigae, something I had not seen in a long time.

The moment I put it in my mouth, I spat it right back out.

*Ptooey.*

“Wh—what? Why?”

What the hell was this?

I looked back and forth between the flustered Skeleton King and the doenjang jjigae before opening my mouth hesitantly.

“Who made this?”

“Your younger sister.”

“…Ah. Right.”

“Is something wrong?”

A problem? There was one. A serious one.

But instead of answering, a quiet laugh escaped me.

I did not know why. It just did.

“I’ll eat and then go.”

“What?”

“I’ll just eat this and go. And I’ll take a shower, too.”

The Skeleton King blinked for a while, as though he had not understood me, then hurriedly nodded.

“Oh? Oh, understood. Then this body will…”

“Yeah. See you later.”

He slowly closed the door and disappeared like a thief, and another inexplicable laugh escaped me.

I set down my spoon, picked up a piece of braised short rib, and took a large bite.

Fortunately, the braised short ribs had been made by my mother.

* * *

“There were vicious dogs going around biting people, so I beat them senseless. But this time, two mad dogs showed up.”

At my first words after several days apart, Team Leader Choi nodded after briefly moving his lips as though he had been about to say something.

“That’s right. And those two mad dogs bit even more people.”

“Do you think it’s my fault too, Team Leader Choi?”

“Mad dogs are nothing more than mad dogs. In the end, it is only a matter of timing and pretext. They would have bared their fangs at people sooner or later.”

“But I’m the one who gave them the opportunity to do it.”

“If you insist on blaming yourself, then say ‘we.’ This wasn’t something Jin Taekyung did alone.”

“That’s right. This body also achieved a great feat in the desert.”

At the Skeleton King’s sudden interruption, Team Leader Choi shrugged.

“That’s what he says.”

“I’m not blaming myself. I just thought I needed to make that much clear.”

Every incident had a cause and an effect.

And since so many people had died or been injured, I could not claim to be free of responsibility for the cause.

Nor did I intend to.

“I understand the people who condemn me. And I’m simply grateful to those who support me.”

“Is that all?”

“No. The most important thing is still left.”

I continued speaking calmly.

“No matter what the world says, I’m going to catch those mad dogs.”

The Skeleton King’s eyes gleamed at my answer, while a faint smile appeared around Team Leader Choi’s mouth.

“You found an answer of your own.”

“It may not be a complete answer, but isn’t it enough of a reason to keep moving forward?”

“That is enough. Then I can deliver some news with a lighter heart.”

“News?”

“Even before this incident occurred, I had been gathering information related to Michael Silbert and Odin Guild. The results came in recently.”

Team Leader Choi had been monitoring the movements of the other major Guilds since before the Mana Cultivation Method was released. Given his meticulous nature, that was only natural.

“What is it? I’d prefer good news, if possible.”

“Unfortunately, there is bad news as well. Which would you like to hear first?”

“It can’t get any worse than this. Tell me the bad news first.”

Team Leader Choi gave a short laugh and pulled a thick bundle of documents from a drawer.

“I organized them as best I could, but there was an enormous amount of information.”

“What is this?”

“Information regarding the assets and businesses owned by Odin Guild. Of course, a considerable portion of them have not been exposed.”

“You mean they’re in other people’s names?”

“Yes. Legally, they have nothing to do with Odin Guild, but in practice, they were operated as though they were subsidiaries of the Guild. Other major Guilds and corporations commonly use the same method, but the scale itself is on another level.”

I was practically illiterate in this area, but even the thickness of the documents piled up before me gave me a sense of the scale.

I skimmed through the pages, which were filled with words and sentences I could barely understand, until I found the closest comparison.

“More than Ares Guild?”

“You would have to combine Ares Guild and Peace Guild, then add three or four major Guilds on top of that.”

“Holy shit.”

“Just counting the number of Gates Odin Guild has taken charge of, there are more than two hundred across the world. Since they are permanent leases, they are effectively the same as ownership, and an enormous quantity of Magic Gems pours out of them.”

Even if a considerable number of those holdings were controlled through unofficial channels, having control of around two hundred Gates put Odin Guild on the level of a small country.

No—considering the strength of the Hunters belonging to it, perhaps it was even more than that.

*It would have been better if he were just a mad dog.*

To put it coldly, Michael Silbert was not simply a mad dog.

He was a Tosa mastiff among fighting dogs—and he was clever, too.

*But he was also a bastard I absolutely had to beat to death.*

I muttered inwardly, then suddenly thought of something.

“Then is it possible that the Magic Gems from those Gates were used in this terrorist attack without being refined?”

“No. At least not according to the documents.”

“Not according to the documents?”

“As you know, Michael Silbert is an extremely thorough person. He had no reason to take the risk of smuggling Magic Gems, and even if he had, he would not have left any gaps in the records. The Magic Gems used in the terrorist attacks most likely came out of the Middle East or Africa.”

It was a convincing explanation.

The Middle East and Africa had been hotbeds of terrorism and civil war even before the Great Cataclysm, and even now, people there were continuing bloody battles somewhere or other.

No one could know exactly how many Magic Gems came from Gates occupied by terrorists and rebels, or how many of them had been left unrefined.

Moreover, Michael Silbert was not alone.

He had a reliable accomplice who was just as much a mad dog as he was.

“The Prophet.”

At the name that slipped from my mouth, Team Leader Choi nodded with a grim expression.

“I searched thoroughly for information on the Prophet as well.”

“What kind of bastard is the Prophet?”

I was genuinely curious.

Who was the madman who had beheaded the leaders of two massive terrorist organizations, rallied the scattered terrorists, and shaken the entire world?

But the answer I heard from Team Leader Choi fell far short of my expectations.

“We don’t know.”

“You don’t know?”

“No. Even after taking every circumstance into account, there is absolutely no information about the Prophet. The Prophet completely vanished after that declaration as well.”

“Wait. Even the United States?”

“Not just the United States. Even with the entire world searching, the situation is still the same.”

I blinked and thought.

*How was that possible?*

The madman who called himself the Prophet had stirred up not only the United States but the entire world. And yet he had disappeared without a trace, evading everyone’s eyes.

“You’re not hiding what you know to protect classified information, are you?”

“I recently managed to contact Chuck Hagel. He swore to God that he didn’t know where the Prophet was.”

Chuck Hagel, who had fought alongside us in the desert, was not only an S-rank Hunter but also the United States Secretary of Defense.

Unless he was lying, if even the Secretary of Defense did not know, then the Prophet really must have shot straight up into the sky.

*Who the hell is this guy?*

Just as I furrowed my brow, Team Leader Choi continued.

“And there’s one more thing. Mr. Johnson contacted us. He said he had found someone among the other Grand Mages who was likely to have been in contact with Michael Silbert. He said we would probably be able to learn more vital information through that person.”

Fortunately, this time, it was good news.

I had not yet heard the person’s name, but that Grand Mage would have to know something about Michael Silbert’s true nature.

He was a key figure who had personally created Ares Guild’s A Area and knew about Cheon Taemin’s condition.

As one of only three Grand Mages in the entire world, he would become a new clue.

Or so I thought.

That was before I heard Magic Johnson’s voice on a call that came to Team Leader Choi not long afterward.

—Damn it. He’s dead.
```

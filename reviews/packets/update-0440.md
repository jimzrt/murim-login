<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0440.txt",
      "sha256": "a91258c72ebc8bbd4882de66ff1cc04b91e7f52ddece04dfcff84eeadc4bf1b7",
      "bytes": 12907
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "56ac3a7be2b832c255bca0506ef994c62ca6c9acdb4af6224628c0b18efb75d0",
      "bytes": 1975
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "680d679df3c0c9c664a8b1bfbd5f20a8e2ae6f57802f97dc970ebd023a23fb77",
      "bytes": 143840
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0e21a6d58d25ff768d8d9b3fdc660104c697672350f7366a417cebf670aebf43",
      "bytes": 553
    },
    {
      "path": "characters/Go Jun.md",
      "sha256": "349bca1e36708594611e32b5b09ae7137f64b9321f5058b78b20d9fae8fc9976",
      "bytes": 800
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d99e7f9b2044441f12bd09e0d65483748cad71c7cb2bbf4270999a0b19283868",
      "bytes": 1473
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "343b19bc3f972cbeec93b92708d3fd43434a114ede03e1138e8d3baf8dd08307",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "765de592675b0c1402a227728d36853ac88b77a974ba3a46034972fae119a802",
      "bytes": 137572
    }
  ],
  "estimated_tokens": 9727
}
-->

# Durable State Update — Chapter 440

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 440. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 440. Profile updates may replace only one
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
  "chapter": 440,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 440,
    "continuity_sources": [440],
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
    "The Skeleton King's undead identity remains concealed from the public, and he has agreed to exercise restraint.",
    "The Skeleton King uses Stone-King as his claimed identity and wants to be addressed as Mr. King.",
    "Magic Johnson supplied the Skeleton King with a translation-magic ring and a Magic Gem-powered smartphone; his social-media account has 5,134 followers.",
    "Jin Taekyung is Korea's publicly recognized representative S-rank Hunter after returning from China.",
    "Tens of thousands gathered at Incheon Airport, where traffic was halted and a military- and police-controlled car parade was prepared.",
    "The President greeted Taekyung and posed with him at the airport photo line.",
    "The fifty-trillion Arch Lich bounty may produce several trillion in Korean taxes, and Taekyung intends to pay them rather than enter politics for tax relief.",
    "Team Leader Choi manages Taekyung's media and official arrangements but must consult him before making political commitments."
  ],
  "continuity_sources": [
    439
  ],
  "open_questions": [
    "Why does Mungyeong continue accompanying Jin Taekyung's group despite being unable to explain the impulse?",
    "How did Jin Taekyung actually open his Middle Dantian?",
    "What confidential matter is Jin Wikyung withholding?",
    "Are Taekyung's suspicions about the mysterious patterns and symbols found in both worlds correct?",
    "How will Taekyung's public status and the Arch Lich bounty affect his future dealings with Korea's political establishment?"
  ],
  "safe_through": 439,
  "temporary_decisions": [
    "Render 스톤 킹 as “Stone-King” and use “Mr. King” when others address him.",
    "Preserve the Skeleton King's grandiose “this king” voice and Taekyung's profane modern humor.",
    "Keep Arch Lich, S-rank Hunter, Magic Gem, Inventory, Blue House, Peace Guild, and Demon Realm as established terms."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 청해     | **Qinghai**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아이튜브 | **iTube** | Live-streaming platform hosting the Hunter Association ceremony. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 킹태경 | **King Taekyung** | Online nickname praising Taekyung. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 인천 | **Incheon** | Location of the airport welcome and presidential greeting. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 고준 | 진태경 | Ares Guild combatant confronting the killer of his Master | you | hostile and informal | Go Jun uses 너 while demanding Jin confess to Lee Jungryong's death and threatening retaliation. |
| 진태경 | 고준 | dominant adversary confronting Lee Jungryong's Disciple | you | contemptuous and informal | Jin uses 너 and 놈 while overpowering Go Jun and ordering him to end the conflict with Lee Jungryong. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 439
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Go Jun.md

# Go Jun (고준)

- **Safe through:** Chapter 432
- **Aliases:** Team Leader Seok
- **Role:** Leader of Lee Jungryong's security team, an Ares Guild combatant, and Lee's disciple and right-hand man who remains alive after Jin Taekyung grievously mutilated him.
- **Personality:** Highly disciplined, fiercely loyal to Lee Jungryong, confident in his abilities, and capable of suppressing his anger and killing intent under provocation.
- **Voice:** Dry, controlled, and formal with subordinates; deferential when addressing his Master.
- **Relationships:** Disciple and direct protégé of the late Lee Jungryong, Go Jun confronted Jin Taekyung over Lee's death and was forced to accept Jin's demand that the conflict end with Lee.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 439
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, and is Korea's publicly recognized representative S-rank Hunter.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and student, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 439
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃440화



진태경이 탄 전용기가 인천 국제공항에 착륙한 그 날, 전 세계의 카메라는 대한민국을 향했다.

쉬지 않고 터져 나오는 수많은 플래시는 해 질 녘이라는 사실을 잊게 할 정도였다. 한겨울의 추위에도 인근을 가득 메운 수십 만의 인파가 기다리던 영웅의 귀환에 뜨거운 환호를 보냈다.

그리고 이 모든 것들의 중심에 선 한 사람은, 자신의 예상을 훌쩍 벗어난 규모에 멍하니 중얼거렸다.

“……이게 다 뭐여, 시부럴.”

개미만큼 작은 목소리였지만 최고의 장비를 투입한 세계 각국의 언론사는 이 젊은 영웅이 무심코 흘린 한마디를 놓치지 않았다.

“What the sibu-leol?”

“Que veut-elle dire par là?”

“Was meint sie damit?”

대한민국의 욕설이 통역기도 버벅거릴 정도로 다채롭다는 것은 이미 유명한 사실.

시부럴의 찰진 의미를 제대로 이해하지 못한 서구권 기자들은 멈칫했지만, 학창시절부터 온갖 기상천외한 욕설을 섭렵한 한국인 기자들은 번개처럼 움직였다.

“기사! 빨리 기사 올려! 우리가 제일 먼저 올려야 해!”

“이, 이걸로 말입니까?”

“인마, 지금 진태경은 숨만 쉬어도 특종인 거 몰라? 헛소리할 시간에 욕하는 입 모양이랑 오디오 따서 당장 올려!”

“네, 넵! 그런데 선배님. 이거 괜히 문제 되진 않을까요?”

“문제? 무슨 문제?”

“아무래도 저희가 진태경 까는 것처럼 보이면 역풍 맞을 수도 있을 것 같은데. 진태경 욕설 파문, 뭐 그런…….”

고참 기자는 후배의 말에 인상을 찡그렸다.

저놈이 이제 2년 차던가, 3년 차던가? 이쯤 굴러 봤으면 생각이란 걸 할 법도 한데 여전히 어리바리하기 짝이 없다.

고참 기자는 눈앞의 얼간이가 국장의 외조카라는 사실을 떠올리며 간신히 욕설을 참았다.

“야. 홍 기자야.”

“예.”

“진태경은 쌍욕을 해도 돼.”

“네?”

“우리나라에서 정치인이나 연예인이 공적인 자리에서 욕하면 천하의 죽일 놈이 되지만, 진태경이 시벌거리면 좋아 죽으려고 한다고. 알아듣겠냐?”

“예, 옙!”

그제야 고개를 끄덕이는 후배의 모습에, 한숨을 푹 내쉰 고참 기자가 자신의 스마트폰을 바라보았다.

세계 최대 규모의 동영상 공유 웹사이트, 아이튜브에서 진행 중인 실시간 스트리밍 방송의 채팅방은 이미 미친 듯이 폭주하고 있었다.



ㅅㅂㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ시부럴.

시벌좌…… ‘그’가 돌아왔다.

불알좌도 있음. 아까 중국 뉴스에서 불알 건다는 거 보고 미친 듯이 웃었는데 진짜ㅋㅋㅋㅋㅋ

킹태경. 엄청난 업적을 세우고도 인터뷰 다 좆 까고 공식 기자 회견 30분으로 끝내 버린 놈…….

그러면서도 마지막까지 생존자들을 구출하기 위해 고군분투한 놈…….

최소 천만 명이 시청하는 중국 공영방송에서 판돈 대신 불알을 거는 놈…….

전 세계가 지켜보는 앞에서 시부럴거리는 놈…….

킹태경, 한없이 따뜻하지만 미친놈…….

ㅋㅋㅋㅋㅋㅋ이 정도면 헌터가 아니라 기인 아니냐.

ㄴㄴ시부럴좌임.

ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ시부럴좌 괜찮네.

ㅋㅋㅋㅋㅋㅋㅋㅋ안 그래도 킹태경이 전에 했던 인터뷰 중에 그런 거 있더만. 시벌좌라고 부르는 거 좀 자제해 주면 안 되겠냐고.

그래? 알겠어, 형! 오늘부터 시부럴좌라고 부를게!

시벌좌가 싫어? 그럼 지금부터 시부럴좌 해야지ㅋㅋㅋㅋㅋㅋㅋㅋ

시벌좌+불알좌=시부럴좌.

빌드업 보소ㅋㅋㅋㅋ이 정도면 노린 거 아니냐.

안녕. 모두들 진 선생이 명나라 장군이었던 진취의 후손이라는 것에 대해 어떻게 생각해? 중국은 크고 위대한 나라니까 만약 그가 귀화한다면 더욱 좋은 기회가 될 거야. 아, 참고로 나는 한국인이야.

??????

아니, 여기서 갑자기 짜장을 끼얹네…….

왕 서방 조심히 들어가고.

저 새끼가 한국인이면 난 아스가르드인임. 어제 토르랑 발할라에서 맥주도 마심.

헤에, 역시 중국인. 멍청해서 바로 티가 나는 걸wwwww 물론 진태경도 멍청하지만 말이야. 나도 한국인이지만, 오늘처럼 공식적인 자리에서 저런 상스러운 말을 하는 건 모두에게 민폐라고 생각해. 최소한 민족성만큼은 이웃 나라인 일본에서 배울 점이 있어.

????

짜장으로도 부족해서 와사비까지 끼얹네…….

헤에 ㅇㅈㄹㅋㅋㅋㅋㅋ 킹태경 보고 부들거리는 일본 우익 같은데 왜 이렇게 멍청하냐.

??? : 매그도나르도. 쌍큐!

제발 너희 나라 방송 봐라. 한국 공식 채널 와서 어쭙잖게 한국인 흉내 내지 말고.

wwwww 현실 부정하는 게 웃기네. 나 진짜 한국인 맞아.

너 어디 사는데.

서울시 부산구.

하…….

괜히 헬조선이라고 부르는 게 아니다. 무슨 좌청룡 우백호도 아니고 좌짜장 우와사비여.

북쪽에는 악마의 열매 능력자도 있음.

??? : 고모부고모부 총난타!

님들 이상한 애들한테 어그로 끌리지 말고 방송 보세요. 이제 막 카 퍼레이드 시작하려고 함.

진짜네. 형들 쓸데없이 화내지 말고 킹태경이나 보자.



지상파와 케이블 및 종편 방송. 거기에 더해 아이튜브 실시간 스트리밍으로 전 세계 각국에서 이 광경을 지켜보던 시청자들까지.

헤아릴 수 없을 만큼 많은 이들이 지켜보는 가운데, 진태경과 그 일행을 실은 대형 리무진 버스가 움직이기 시작했다.

더욱 커지는 환호와 번쩍이는 플래시. 그리고 상공을 가득 메운 드론이 밤하늘을 수놓았다.



와, 미쳤다. 카메라가 사람들을 다 못 담을 정도임 ㄷㄷ;

올림픽 개최 때보다 더한데. 도대체 드론이 몇 개냐.

많을걸?

아니 그건 나도 알지…….

버스 출발하는 순간 나도 모르게 소름 돋았다. 가슴 웅장해지는 거 실화냐.



진태경과 그 일행을 실은 리무진 버스는 시속 10km로 움직이며 인의 장막을 가로질렀다.

화려한 폭죽이 쉼 없이 터져 나왔고 사람들이 뿌린 꽃잎이 바람을 타고 휘몰아쳤다.

처음에는 어색하게 굳은 채 상황을 바라보던 진태경도 이내 웃으며 인파를 향해 손을 흔들었다.

‘나를 좋아해 주는 사람들이니까.’

반년 전의 진태경은 백사장의 모래알 같은 존재였다.

누구도 관심을 기울이지 않으며 한바탕 파도가 지나가면 쓸려 나가는, 어디에서나 흔히 찾아볼 수 있는 F급 헌터.

그랬던 자신에게 오늘 같은 날이 찾아올 것이라고는 단 한 번도 생각해 본 적이 없었다.

‘그저 죽지 않고 은퇴하는 것이 꿈이었는데…….’

너무나도 많은 것을 손에 넣었다. 죽음이 사방에 깔린 가시밭길을 걸어야 했지만 중간중간 매달려 있는 과실은 달콤했다. 상상도 할 수 없던 힘과 막대한 부, 명예까지.

그리고…….

“고생했어. 우리 아들.”

“나도 진태경 씨가 무지 자랑스럽긴 한데, 지금 눈이 부셔서 얼굴도 잘 안 보여. 저 기자들은 언제까지 저러고 있을 거래?”

언제나 함께했던 가족들.

등을 쓰다듬는 어머니의 따뜻한 손길에 울컥하고, 플래시로 인해 오만상을 찡그리는 동생의 모습에 피식 웃음이 터져 나온다.

“저보다는 엄마가 더 고생하셨죠. 하연이 너도.”

“나도 알거든. 엄마랑 오빠가 더 고생한 거.”

“인간 언저리인 줄 알았는데, 그래도 일말의 양심은 있구나.”

“와, 말하는 것 봐.”

“웃어. 인마. 지금 찍고 있는 카메라가 몇 대인데.”

농담 같은 한 마디와 함께 두 사람을 끌어안은 진태경은, 가족의 뒤에서 자신을 바라보는 한 쌍의 눈동자와 마주쳤다.

“정말 고생 많으셨습니다. 진태경 씨.”

“최 팀장님도요. 저야 힘만 센 무식한 놈이라 팀장님 없었으면 정말 힘들었을 거예요.”

“해야 할 일을 한 것뿐입니다. 앞으로도 마찬가지고요.”

“무서운 말씀을 웃으면서 하시네.”

“알고 계시잖습니까. 이게 끝이 아니라는 걸.”

안다. 그렇기에 더욱 결심을 굳혔다.

지금까지 위태로운 가시밭길을 지나온 진태경이다. 소중한 가족과 친구들이 같은 길을 걷게 할 수는 없었다.

발이 피투성이가 되고 고통으로 쓰러지더라도 성큼 다가오는 위협으로부터 그들을 보호할 것이다.

때로는 함께 힘을 합치고, 자신이 희생하는 한이 있더라도.

“잘 부탁할게요. 앞으로도 쭉.”

진태경이 내민 손을 물끄러미 바라보던 최 팀장의 입가에 보조개가 움푹 팼다.

“네. 언제까지나.”

두 사람이 손을 굳게 맞잡은 그때, 툴툴거리는 목소리가 진태경의 머릿속에서 울려 퍼졌다.

- 아주 잘들 노는구나.

‘아직도 삐져 있냐?’

- 삐지긴 누가! 위대한 왕으로 거듭난 이 몸이 그런 하찮은 인간의 감정을 느낄 것 같은가!

‘삐진 거 맞네.’

- 아니라고!

사정상 인벤토리에 숨을 수밖에 없었던 관종, 아니 스켈레톤 킹은 아까부터 단단히 토라진 상태였다.

슬쩍 웃은 진태경이 마음속으로 중얼거렸다.

‘야.’

- 말 걸지 마라!

‘지금까지 고마웠고, 앞으로도 잘 부탁한다.’

- 흐, 흠.

헛기침을 내뱉은 스켈레톤 킹이 머뭇거리는 목소리로 말을 이었다.

- 그, 그렇게까지 말하니 고려해 보도록 하지.

‘뭘 고려해?’

- 너, 간악한 인간과 함께하는 것 말이다.

‘아, 그건 고려할 필요 없어.’

- 응?

‘너 무조건 평화 길드 들어와야 해. 이미 계약서 작성해 놨으니까 가서 지장 찍어. 아니다, 지문 조회해 봤자 나오지도 않으니까 두개골로 찍어야겠다.’

- 이 무슨! 자유 민주주의 국가 아닌가!

‘응. 아냐. 노예처럼 골수까지 뽑아먹을 거야.’

- 당장 이 몸을 내보내라! 차 돌려!

참지 못하고 소리 내어 웃은 진태경이 운전석을 향해 몸을 기울였다.

“이대로 다음 목적지까지 이동할 수 있을까요?”

“예?”

화들짝 놀란 운전기사가 더듬더듬 대답했다.

“사, 사전에 전달받은 지시와는 다른데요.”

“안 돼요?”

“죄송하지만 그렇습니다.”

“정말 안 돼요?”

“아무래도…….”

“진짜, 정말 안 돼요?”

운전기사가 반쯤 포기한 목소리로 대답했다.

“……될 것 같습니다.”

“그럼 평화 길드의 길드 하우스로 가 주세요.”

운전기사는 자신의 상관에게 이 사실을 전달했고, 몇 계단을 거쳐 보고를 받은 상부는 당황했지만 흔쾌히 수락했다. 그리고 3천여 대에 달하는 드론은 끝나지 않는 카 퍼레이드를 따라 이동했다.

드론은 진태경 일행을 실은 리무진 버스가 평화 길드의 길드 하우스 앞에서 멈추었다.

그곳에서 기다리고 있던 길드원들과 조우하는 모든 장면은 카메라에 담겨 전 세계 곳곳으로 송출됐다.

그렇게 자정이 지나고, 날이 저물어 많은 이들이 고대하던 크리스마스이브가 찾아왔음에도 열기는 사그라지지 않았다.

아니, 오히려 경쟁하듯 꺼져 가는 불길에 새로운 장작과 바람을 불어넣었다.

사람들은 진태경이라는 이름을 어디에서나 볼 수 있었고, 그것은 아직도 심각한 후유증에 시달리는 누군가에게는 엄청난 고통이었다.

- 금일 오전, 미국의 S급 헌터 매직 존슨은 공식 SNS 계정을 통해 평화 길드와 모종의 협약을 추진 중…….

쾅!

홀로그램 TV속 아나운서의 얼굴이 사라졌다. 기계를 박살 낸 사내가 비명처럼 울부짖었다.

“진태경, 진태경, 진태경!”

쾅! 콰과광!

벌겋게 충혈된 눈. 난폭하게 휘두르는 주먹 끝에서 쏘아진 강대한 기운이 주위를 박살 내고 가루로 만든다.

누구보다 증오스러운 그 이름. 동시에 잊을 수 없는 공포를 알려 준 그의 이름!

“으아아아아!”

사내, 석고준이 초토화된 공간에서 울부짖던 바로 그때, 작은 인기척과 함께 조심스러운 목소리가 그의 귓가를 파고들었다.

“티, 팀장님.”
```

## Final English reading copy

```markdown
# Chapter 440

The day Jin Taekyung’s private jet landed at Incheon International Airport, cameras from around the world turned toward Korea.

The countless flashes erupting without pause were bright enough to make people forget that the sun was already setting. Despite the midwinter cold, hundreds of thousands of people packed the surrounding area and sent up a blazing cheer for the hero’s return.

And at the center of it all stood one man, staring blankly at the scale of the welcome, which had far surpassed anything he had expected.

“...What the hell is all this, goddammit?”

His voice was as small as an ant, but the news outlets from around the world had brought in their best equipment. They didn’t miss the young hero’s offhand remark.

“What the sibu-leol?”

“Que veut-elle dire par là?”

“Was meint sie damit?”

It was already famous that Korean profanity was so diverse that even translation devices struggled with it.

Western reporters who failed to properly understand the rich meaning of *sibu-leol* hesitated, but Korean reporters who had mastered every bizarre curse imaginable since their school days moved like lightning.

“Write it up! Hurry and get the article online! We have to be first!”

“W-With this?”

“You idiot, don’t you know that everything Jin Taekyung does is breaking news right now? Stop wasting time talking nonsense. Get a shot of the way his mouth moved when he cursed, grab the audio, and upload it immediately!”

“Yes, Senior! But, Senior… won’t this cause trouble?”

“Trouble? What trouble?”

“If it looks like we’re attacking Jin Taekyung, we could suffer a backlash. You know, the Jin Taekyung profanity controversy or something…”

The veteran reporter scowled at his junior.

*Was that kid in his second year now, or his third? After working in the field this long, he should have learned to think, but he was still hopelessly slow on the uptake.*

The veteran reporter barely held back a curse when he remembered that the idiot in front of him was the bureau chief’s nephew.

“Hey. Reporter Hong.”

“Yes.”

“Jin Taekyung is allowed to swear.”

“What?”

“Politicians and celebrities become the worst people alive if they curse at a public event in this country. But when Jin Taekyung starts swearing, people nearly die of happiness. Do you understand?”

“Yes, yes, Senior!”

Only then did the junior nod. The veteran reporter let out a deep sigh and looked at his smartphone.

The chatroom for the live stream currently airing on iTube, the world’s largest video-sharing website, was already exploding out of control.

ㅅㅂㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋSibu-leol.

Lord Fuck… *he* is back.

Lord Balls is here too. I saw him say he’d bet his balls on the Chinese news earlier and laughed my ass off, seriously lmao.

King Taekyung. The bastard who accomplished something incredible, told every interview to fuck off, and wrapped up his official press conference in thirty minutes…

And yet he fought like hell to rescue the survivors until the very end…

The bastard who bet his balls instead of money on a Chinese state-run broadcast watched by at least ten million people…

The bastard who kept saying *sibu-leol* in front of the entire world…

King Taekyung. Infinitely warmhearted, but completely insane…

ㅋㅋㅋㅋㅋㅋ Is he even a Hunter, or is he some kind of eccentric?

Nope, he’s Lord Sibu-leol.

ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ Lord Sibu-leol is pretty good.

ㅋㅋㅋㅋㅋㅋㅋㅋ Actually, didn’t King Taekyung say something like that in one of his earlier interviews? He asked people to stop calling him Lord Fuck.

Really? Got it, hyung! From today on, I’ll call him Lord Sibu-leol!

He doesn’t like Lord Fuck? Then we have to call him Lord Sibu-leol from now on lmao.

Lord Fuck + Lord Balls = Lord Sibu-leol.

Look at that buildup lmao. At this point, was it intentional?

Hello, everyone. What do you think about the fact that Mr. Jin is a descendant of Jin Chui, who was a Ming dynasty general? China is a great and powerful country, so if he were to become a naturalized citizen, it would be an even better opportunity for him. Oh, and for the record, I’m Korean.

??????

Why are you suddenly dumping jajang sauce in here…

Take care on your way home, Wang.

If that bastard is Korean, then I’m an Asgardian. I drank beer with Thor in Valhalla yesterday.

Heh, Chinese as expected. You give yourself away immediately because you’re an idiot lmao. Of course, Jin Taekyung is an idiot too. I’m Korean as well, but I think it’s a nuisance to everyone when he uses such vulgar language at an official event like today. At the very least, there’s something to learn from our neighboring country Japan when it comes to national character.

????

Jajang sauce wasn’t enough, so now you’re dumping wasabi on us too…

Heh, that sounds like some Japanese right-winger trembling with rage at King Taekyung. Why are you so stupid?

??? : Magdonaldo. Ssankyu!

Please watch your own country’s broadcasts. Stop coming to Korea’s official channel and pretending to be Korean.

Lmao, it’s hilarious how hard you’re denying reality. I really am Korean.

Where do you live?

Seoul City, Busan District.

Ha…

There’s a reason people call this place Hell Joseon.[^1] What is this, left Azure Dragon and right White Tiger? We’ve got left jajang and right wasabi.

There’s even a Devil Fruit user up north.

??? : Uncle-in-law, uncle-in-law, total barrage!

Don’t get baited by weirdos. Watch the broadcast. The car parade is just about to start.

It really is. Don’t get angry over pointless stuff, hyungs. Let’s just watch King Taekyung.

[^1]: “Hell Joseon” is a cynical nickname for South Korea, comparing modern society to the rigid and oppressive Joseon era.

Broadcast networks, cable channels, and general programming channels were all showing the scene. On top of that, viewers around the world were watching through iTube’s live stream.

With an uncountable number of people watching, the large limousine bus carrying Jin Taekyung and his companions began to move.

The cheers grew louder, flashes burst everywhere, and drones filled the sky overhead, painting patterns across the night.

Wow, this is insane. There are so many people that the cameras can’t even fit them all in the frame ㄷㄷ;

This is bigger than the Olympics. How many drones are there, anyway?

A lot, I guess?

I know that much…

I got goose bumps when the bus started moving without me even realizing it. Is it really possible for your heart to feel this grand?

The limousine bus carrying Jin Taekyung and his companions moved at ten kilometers per hour through a wall of people.

Brilliant fireworks exploded without pause, and flower petals scattered by the crowd whirled through the air on the wind.

At first, Jin Taekyung watched the situation with an awkwardly stiff expression. Before long, however, he smiled and waved at the crowd.

*They’re people who like me.*

Six months ago, Jin Taekyung had been no more than a grain of sand on a beach.

An F-rank Hunter who could be found anywhere, unnoticed by anyone and swept away when a wave passed over him.

He had never once imagined that a day like this would come.

*I only dreamed of retiring without dying…*

He had gained far too much. He had been forced to walk a thorny path with death spread out in every direction, but the fruit hanging along the way had been sweet. Power beyond his wildest imagination, enormous wealth, and even fame.

And…

“You’ve worked hard, my son.”

“I’m incredibly proud of you too, Mr. Jin Taekyung, but these flashes are so bright that I can barely see your face. How long are those reporters planning to keep doing this?”

His family, who had always been with him.

His mother’s warm hand stroking his back made his throat tighten, while the sight of his sister scrunching up her face against the flashes made him let out a quiet laugh.

“Mom worked harder than I did. You too, Sis.”

“I know. I know Mom and Oppa worked harder.”

“I thought you were barely human, but you have a shred of conscience after all.”

“Wow, listen to him.”

“Smile, you idiot. Do you have any idea how many cameras are filming us right now?”

After hugging the two of them with that joking remark, Jin Taekyung met a pair of eyes watching him from behind his family.

“You’ve truly worked incredibly hard, Mr. Jin Taekyung.”

“You too, Team Leader Choi. I’m just a big, dumb brute who’s good at using strength. I would’ve had a really hard time without you.”

“I only did what I had to do. And I will continue to do the same.”

“You’re saying something scary with a smile.”

“You know, don’t you? That this isn’t the end.”

He knew.

That was why he hardened his resolve even further.

Jin Taekyung had made it this far after crossing a perilous field of thorns. He couldn’t allow his precious family and friends to walk the same path.

Even if his feet became covered in blood and he collapsed from the pain, he would protect them from the threats drawing ever closer.

Sometimes they would join forces. And even if it meant sacrificing himself…

“Please take care of me. From now on, too.”

Team Leader Choi stared at the hand Jin Taekyung extended. Then a deep dimple appeared beside his mouth.

“Yes. Always.”

Just as the two clasped hands firmly, a grumbling voice rang out inside Jin Taekyung’s head.

—You’re all having a grand old time.

*Are you still sulking?*

—Who is sulking?! Does this body, reborn as the great king, look like it would feel such a worthless human emotion?

*You’re definitely sulking.*

—I am not!

The attention seeker—no, the Skeleton King—who had been forced to hide in the Inventory for the time being had been sulking bitterly for quite a while.

Jin Taekyung smiled faintly and muttered inwardly.

*Hey.*

—Do not speak to me!

*Thanks for everything up to now. I’m counting on you from here on out, too.*

—H-Hmm.

After letting out a fake cough, the Skeleton King continued in a hesitant voice.

—Since you put it that way, I shall consider it.

*Consider what?*

—Going with you, you vile human, of course.

*Oh, you don’t need to consider that.*

—What?

*You have to join Peace Guild no matter what. I’ve already had the contract drawn up, so go put your thumbprint on it. No, wait. Your fingerprints won’t turn up in a records check, so I guess you’ll have to stamp it with your skull.*

—What is this?! Is this not a liberal democratic country?!

*Yeah. No. I’m going to milk you like a slave, right down to your marrow.*

—Release this body immediately! Turn the car around!

Unable to hold it in any longer, Jin Taekyung burst out laughing and leaned toward the driver’s seat.

“Could we go to the next destination like this?”

“Pardon?”

The startled driver stammered out a reply.

“That’s different from the instructions we received beforehand.”

“Can’t we?”

“I’m sorry, but we can’t.”

“We really can’t?”

“I’m afraid not…”

“Seriously, truly, we can’t?”

The driver answered in a voice halfway to giving up.

“…It seems we might be able to.”

“Then please take us to Peace Guild’s guild house.”

The driver relayed the information to his superior. After passing through several levels of reporting, the higher-ups were bewildered but readily agreed.

And the roughly three thousand drones moved along with the seemingly endless car parade.

The limousine bus carrying Jin Taekyung and his companions eventually came to a stop in front of Peace Guild’s guild house.

Every moment of their meeting with the Guild members waiting there was captured by cameras and broadcast across the world.

Even after midnight passed and the long-awaited Christmas Eve arrived, the fervor did not die down.

No. The dying flames only received fresh firewood and a new gust of wind, as though competing with one another.

People could see the name Jin Taekyung everywhere, and for someone still suffering from severe aftereffects, it was an unbearable torment.

—This morning, the United States’ S-rank Hunter Magic Johnson announced through his official social-media account that he is pursuing some kind of agreement with Peace Guild—

*Bang!*

The announcer’s face vanished from the holographic television. The man who had smashed the machine let out a scream.

“Jin Taekyung, Jin Taekyung, Jin Taekyung!”

*Bang! Crash!*

His eyes were bloodshot. Powerful qi fired from the ends of his wildly swinging fists smashed everything around him and reduced it to dust.

That name was more hateful than any other.

At the same time, it was the name of the man who had shown him a fear he could never forget!

“Aaaaaaaagh!”

Just as the man, Go Jun, was howling in the devastated space, a faint stir accompanied by a cautious voice reached his ears.

“T-Team Leader.”
```

<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0774.txt",
      "sha256": "a7000b0544a979c534f7ce13f256c57fa9bff5115a9adc0ba6c688a8d4d532e2",
      "bytes": 13037
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9dff5dcf7f5d218be5b13651c8b4ec78f81ca69c36d6c8fb1ed0679c7d334d6f",
      "bytes": 2291
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7f1782ba7a45fb761291534917139ffcb877474998bbbfbd616a9476b54249d7",
      "bytes": 222793
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "714372438aae89487f528096d47c827d1eac2ce8585b20f86c6e40e2e1fb333f",
      "bytes": 752
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "341d2a5d908712fb14b2a770738d276c24a604e51d5998167efc29085deca90f",
      "bytes": 553
    },
    {
      "path": "characters/Hong Cheonsu.md",
      "sha256": "5b760c32702050e73b00cfb12d602b299c75b2016f99f22aae0c75fafd5978e4",
      "bytes": 681
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "7f0e14473591ce7081373539655d74f5df0c8b78981390fab52f43674bbcbf89",
      "bytes": 667
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3427a572c0b3a5e4e80e5110d01754293ac5fbec347492f2474a9eb0222c934b",
      "bytes": 2096
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "dc336607d93c5c0973cc42ca643fe1b5ab7ec1eae11811ede305e4c9bd4faa4b",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "91e4348e6d4f4cbafbf5a9becc92622497abcf7c75d28b8293c79bf55770b55d",
      "bytes": 1015
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "89b7ab9a90f3f13c0775e001839241b2d76eb63d0266d0007ac3e4eaf6548051",
      "bytes": 241081
    }
  ],
  "estimated_tokens": 10347
}
-->

# Durable State Update — Chapter 774

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 774. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 774. Profile updates may replace only one
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
  "chapter": 774,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 774,
    "continuity_sources": [774],
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
    "Jin and Team Leader Choi have returned to Korea and are operating under heightened security before the World Hunter Federation's inaugural ceremony.",
    "Song Song delivered Choi's covert instructions to fewer than ten trusted senior members of the Peace and Ares Guilds, whose families remain in Korea.",
    "Choi will personally issue further covert instructions as a safeguard unrelated to the clue Jin and his allies discovered.",
    "Baek Hanseong has designated the National Assembly as the ceremony venue and is protecting Jin's mother and Hayeon under heavy security.",
    "Jin is withholding the discovered clue from Baek because Michael Silbert may have a mole or surveillance near the President, and the clue may not be genuine.",
    "Jin will not see his mother and Hayeon until after the ceremony because he fears losing his composure before the crisis is resolved.",
    "The Skeleton King is concealed with Jin inside an unknown space that others cannot perceive and has remained completely silent.",
    "The inaugural ceremony is less than twenty-four hours away, its attendee list is secret, and it will not be broadcast live.",
    "Cheon Taemin remains absent while the public speculates that he, Michael Silbert, or Jin may become the Federation's representative.",
    "Felix, Magic Johnson, Chuck Hagel, Faye Chen, and Team Leader Choi are gathered for a secret meeting before the ceremony."
  ],
  "continuity_sources": [
    773
  ],
  "open_questions": [
    "Is the clue discovered by Jin and his allies genuine, and is their fourth path viable?",
    "What will the secret meeting involving Choi, Felix, Magic Johnson, Chuck Hagel, and Faye Chen decide before the ceremony?",
    "Who will become the World Hunter Federation's representative while Cheon Taemin remains absent?",
    "What coordinated plan do Michael and The Prophet have for the Federation and the coming crisis?",
    "Why has the Skeleton King remained silent inside the concealed space?"
  ],
  "safe_through": 773,
  "temporary_decisions": [
    "Render 파이 첸 as Faye Chen.",
    "Render 척 헤이글 as Chuck Hagel.",
    "Retain World Hunter Federation and inaugural ceremony.",
    "Render 왕자 전하 as Your Highness."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 무인     | **martial artist**                               | Default term                                          |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍천수 | **Hong Cheonsu** | Ten-year veteran Hunter and deceased comrade who saved Taekyung from goblins. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 평화 | **Peace Guild** | Guild name. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 홍천 | **Hongcheon** | Given name of the newly appointed Hubei Provincial Administration Commissioner. |
| 초인 | **superhuman** | A being who has surpassed ordinary human limits. |
| 국회의사당 | **National Assembly** | Government building visible from the skyscraper. |
| 대전쟁 | **Great War** | The long war that ended after the Great Cataclysm. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍천수 | 진태경 | older_comrade_to_younger_comrade | Taekyung | affectionate-casual | His remembered final words address Taekyung familiarly while ordering him to go ahead. |
| 진태경 | 홍천수 | younger_comrade_to_older_comrade | Cheonsu hyung | casual-but-junior | Taekyung called Hong Cheonsu hyung after being saved from goblins. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 773
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 772
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hong Cheonsu.md

# Hong Cheonsu (홍천수)

- **Safe through:** Chapter 220
- **Aliases:** Cheonsu hyung
- **Role:** Deceased ten-year veteran Hunter and Jin Taekyung’s senior comrade; saved Taekyung from goblins before dying in the incident three years earlier.
- **Personality:** Kind and protective toward younger Hunters; treated Taekyung well because he was reminded of his youngest sibling.
- **Voice:** Rough, affectionate, and protective in his remembered final words.
- **Relationships:** Jin Taekyung’s senior comrade, whom Taekyung called hyung; grew up in an orphanage and left behind a spouse and three children.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 763
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 773
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 773
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 773
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, the hidden architect of a coordinated terrorist campaign, and a feared rival whose warning about a second Great Cataclysm triggered worldwide panic and led the UN to approve the World Hunter Federation's reestablishment.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

## Korean source

```text
＃774화



초짜 헌터 시절. 나는 종종 울곤 했다.

아니, 솔직히 고백하건대 꽤 자주.

지금 돌이켜보면 그 모든 것이 성장통이었겠지만, 그땐 그랬다.

당연한 일이다. 그 당시의 나는 갓 성인이 된 애송이였고 헌터 훈련소는 말 그대로 훈련소에 불과했다.

첫 실전이 어땠더라?

그때의 기억은 아무리 떠올리려 애써 봐도 안개처럼 흐릿하다.

기억의 유통기한이 지나서가 아니라, 전투가 시작하자마자 반쯤 정신이 나갔기 때문이었다.

물론 또렷하게 남아 있는 몇 조각의 기억들도 있다.

몬스터들의 물량 공세를 이기지 못하고 허물어지는 탱커들의 뒷모습. 짙은 피비린내와 이 세상의 것이 아닌 괴물들의 악취.

그 어느 때보다 무겁게 느껴졌던 창의 무게와 땀이 흥건하게 고인 손아귀…….

그게 전부다. 격돌하던 그 순간 주위의 모든 것이 멀어졌고, 다시 눈을 떴을 때는 사방이 피바다였다.

그리고 담배를 문 채 내가 깨어나길 기다리던 팀장은 대뜸 이렇게 말했다.



‘야. 신입아.’

‘예, 예.’

‘이 씨발럼아.’

‘예?’

‘너 구하느라 나까지 뒈질 뻔했다. 우리 와이프가 시키던? 나 죽이고 같이 보험금 뿜빠이 치자고?’

‘아, 아뇨.’

‘정신 나간 것 치고는 잘 싸우긴 했는데, 다음에도 또 그러면 죽는다, 진짜.’

‘……죄송합니다.’

‘그런데 너, 이름이 뭐야?’

‘진태경. 진태경인데요.’

‘몇 년 생?’

‘20년생이요.’

‘시바, 20년에도 사람이 태어났어?’



담배를 뻑뻑 피워 대며 나를 노려보던 팀장은 그제야 자신의 이름을 밝혔다.



‘난 홍천수다.’

‘아, 예.’

‘앞으로 사석에서는 삼촌……은 좀 그렇고. 형이라고 불러라. 천수 형.’

‘네, 천수 형.’

‘이놈 이거 예의상 거절 한 번이 없네. 그리고 아직 게이트 안이야, 이 자식아.’



그때는 몰랐다.

저 성질 더러워 보이는 팀장과 형제처럼 동고동락하게 될 줄은. 불과 몇 년 후, 그가 나를 대신해서 희생하게 될 줄은.



‘고생했다. 여기 정산금.’



세금과 길드 수수료를 뗀, 오만 원짜리 지폐 여섯 장. 그날 하루 목숨을 건 대가를 받아 든 채 나는 고시원으로 돌아왔다.

문을 열자 4평도 되지 않는 방에서는 곰팡내가 풍겼고, 끄트머리가 부서진 탁자 위에는 가족사진이 놓여 있었다.

그리고 나는 울었다.

처음에는 작게 흐느끼다가, 이내 어린아이처럼 두 무릎 사이에 얼굴을 파묻고 엉엉 울어 버렸다.

아마 누군가 잠겨 있던 방문을 열지 않았다면, 그날 밤 내내 고시원을 시끄럽게 했을지도 모른다.



‘저기, 새로 온 친구. 허락도 안 받고 막 들어와서 미안해요. 나 여기 고시원 총무인데 자꾸 민원이 들어와서 어쩔 수 없이 마스터키를 썼…….’



엉망이 된 내 얼굴을 바라본 총무는 말꼬리를 흐렸고, 떡진 머리를 긁적이다가 문을 닫았다.

나는 저 아저씨처럼 생긴 총무가 다시 돌아오지 않을 거라 생각했다.

잠시 후, 양손에 소주와 라면 봉지를 든 그의 모습을 보기 전까지는.



‘한잔할래? 아, 혹시 미성년자……는 아니겠구나. 딱 봐도 덩치가 아주, 어후.’



벌써 10년에 가까워지는 과거의 기억들.

시간이 흐름에 따라 나는 변했다. 몬스터에 대한 두려움도, 가족들과 떨어져 느끼는 외로움도 조금씩 잊었다.

아니, 무뎌졌다.

쳇바퀴 위에 올려진 햄스터처럼, 그저 달리고 또 달렸다.

앞으로는 나아가지 못하더라도 멈추는 것보다는 나았다. 이 쳇바퀴를 굴려야만 지킬 수 있는 것들이 있었으니까.

가족. 친구. 동료.

이제는 멈출 수 없었다.

나를 가둔 사육장 안의 조그맣던 쳇바퀴는 어느새 거대한 운명의 수레바퀴로 변해 있었고, 마음속에 간직한 의무감이라는 단어는 점점 선명하고 무거워졌다.

아마 그래서였을지도 모른다.

흐릿해진 그 날의 기억을 꿈속에서나마 들여다볼 수 있었던 것은.

날 흔들어 깨우는 누군가의 손길에 눈을 떴을 때, 두 뺨이 축축해져 있던 것은.

“……경 씨. 진태경 씨.”

나는 눈을 깜빡였다. 흐릿하던 시야에 비로소 초점이 잡힌다.

별다른 표정 변화는 없지만, 그렇기에 작은 감정조차 유난히 돋보이는 낯익은 얼굴이 나를 걱정스럽게 내려다보고 있었다.

“괜찮으십니까?”

나는 젖어 있는 눈가를 문지르며 대답했다.

“모르겠어요.”

“안 좋은 꿈을 꾸신 겁니까?”

“글쎄요.”

나는 갈라진 목소리와 함께 상반신을 일으켰다.

이제 막 정오를 지났음을 알리는 시계와 창가에 드리워진 커튼 틈새 사이로 어두컴컴한 바깥 풍경이 보였다.

“흉몽(凶夢)인지 길몽(吉夢)인지…… 모르겠어요. 저도.”

말없이 나를 바라보던 최 팀장이 침착한 어조로 입을 열었다.

“연연하지 마십시오. 단지 꿈이었을 뿐입니다.”

맞는 말이다. 꿈은 그저 꿈일 뿐이다. 일의 길흉(吉凶)을 결정하는 것은 사람에게 달렸고, 그것이 바로 오늘 내 역할이었다.

아니, 우리 모두의.

“지금 잠이 덜 깨서 그런데, 혹시 어젯밤 일도 꿈이었습니까?”

“어젯밤이요?”

“네. 낯익은 얼굴들이 많이 나왔거든요. 마지막에는 호텔 벨보이 복장을 한 영국 왕자님도 봤었는데.”

내 너스레에 그제야 최 팀장의 입가에 희미한 웃음이 맺혔다.

“희한하네요. 저도 같은 꿈을 꿨지 뭡니까.”

“아, 그러셨구나. 개인적으로는 꽤 괜찮은 꿈이었어요.”

“저도 그렇게 생각합니다.”

당연하게도 그것만큼은 꿈은 아니다.

비밀리에 시작된 대화는 깊은 새벽까지 이어졌고, 나는 지난 며칠 간의 피로를 끌어안은 채 기절하듯 잠이 들었었다.

그 덕분일까. 정신은 맑았고 몸은 가벼웠다.

이래도 되나 싶을 만큼.

‘물론 약간의 하자는 있지만.’

나는 몸속 깊은 곳에서 느껴지는 희미한 통증에 집중했다.

아직까지 치유되지 않은 [망가진 신체]의 영향은 단순히 시스템 상의 숫자로만 표시되는 것이 아니라, 숙주에게 달라붙은 기생충처럼 내 힘의 일부를 갉아먹고 있었다.

‘할 수 있을까? 지금 이 상태로도?’

순간 뇌리를 스치는 한 줄기의 의문.

그러나 나는 이내 고개를 저었다. 이건 할 수 있느냐, 없느냐의 문제가 아니다.

반드시 해내야 한다.

나와 내 사람들을 비롯한 모두를 위해서라도.

“준비는?”

최 팀장이 망설임 없이 대답했다.

“모두 끝마쳤습니다.”

그의 목소리에 담긴 것은 확신이었다. 할 수 있는 모든 것을 준비한 사람만이 보일 수 있는 태도.

하지만 나는 다시 물었다.

최 팀장이 아닌, 보이지 않는 어딘가에서 웅크리고 있을 또 다른 누군가에게.

“넌?”

이번에도 대답은 없었다.

분명 이 모든 상황과 대화를 보고 들었음에도, 녀석은 또 다시 침묵을 택했다.

마치 그간의 정을 한 톨도 남김없이 떼어 내려는 사람처럼. 곧 떠날 준비를 끝마친 여행자처럼.

그러나…… 나는 녀석을 떠나보낼 생각이 없었다.

이런 개 같은 이유 때문이라면 더더욱.

“갑시다.”

나는 담담한 목소리와 함께 방을 나섰다.

최 팀장이 곧장 뒤를 따랐고, 복도를 가득 채운 평화와 아레스 길드의 헌터들이 용의 꼬리처럼 이어졌다.

이제, 거대한 수레바퀴를 굴리러 갈 시간이었다.



* * *



그날의 하늘은 잿빛이었다.

새벽을 틈타 수도권 일대를 뒤덮은 먹구름은 부슬비를 쏟아냈고, 피부에 와닿는 공기는 서늘했다.

그러나 사람들에게 있어 날씨 따위는 아무래도 상관없었다.

그들에게는 곧 먹구름이 흩어지고 햇빛이 비치리라는 기대감이 있었으니까.

아니, 기대감보다는 확신이라는 단어가 더욱 정확할지도 몰랐다.

신(新) 세계 헌터 연맹의 역사적인 첫 발족식.

그것이 바로 사람들이 기다리는 햇빛이었다. 머지않아 들이닥칠, 어쩌면 이미 시작된 두 번째 대전쟁으로부터 자신들을 구원할 초인들의 연합 집단.

과거, 현재, 그리고 미래의 영웅들이 한자리에 모여 진정한 의미의 헌터로 거듭날 것이다.

인류의 검과 방패가 되어, 저 먹구름을 걷어 내고 파도처럼 밀려오는 괴물들로부터 이 세상을 지켜 낼 터였다.

바로 오늘.

이곳에서.

‘새로운 역사가 시작된다.’

스륵.

미카엘 실베르트는 손끝으로 테이블을 쓸었다.

거대한 원형(圓形)의 형태를 갖춘 테이블은 총 삼백 개의 좌석으로 이루어져 있었고, 그 표면에는 예리한 병장기가 만들어 낸 흔적이 곳곳에 가득했다.

‘영웅들이 남긴 기록.’

아직도 또렷하게 기억난다.

세계 헌터 연맹이라는 사상 초유의 연합이 탄생하던 그 날, 미카엘 실베르트 역시 그 영광의 순간과 함께했다.

이제는 죽고 없는 그들의 곁에서 피 끓는 외침을 토해 내고, 각자의 무기를 뽑아 허공을 겨누고, 거대한 원탁(圓卓)에 검을 박아넣으며 인류의 검과 방패가 될 것을 맹세했다.

‘그래, 바로 이 자리에서.’

잊을 수 없는 기억이다.

미카엘 실베르트는 과거 자신이 앉았던 그 의자를 가만히 쓰다듬었다.

세월의 흔적을 고스란히 담은 그것은 거칠고 삐걱거렸으나, 그것만으로도 묘한 감흥을 불러일으켰다.

하지만 그뿐이었다.

미카엘 실베르트는 과거의 추억을 간직한 그것을 그저 말없이 내려다보기만 할 뿐, 앉거나 등을 기대지 않았다.

어느샌가 의자에서 떨어져 나간 그의 시선은, 원탁의 중심을 향하고 있었다.

유일하게 텅 비어 있는 공간.

그곳에는 의자도 없고, 단상도 없다. 삼백 개의 좌석에 의해 고립된 무인도처럼 황량하게 느껴지기도 했다.

그러나 과거에는 미카엘 실베르트를 비롯한 누구도 그렇게 생각하지 않았다.

언제나 저 자리를 가득 채웠던 한 사람이 있었으니까.

누구보다 강하고 누구보다 빛났던. 그렇기에 그를 시기하는 적들조차 경외와 두려움을 품을 수밖에 없었던 영웅들의 영웅이.

‘스카이(Sky).’

미카엘 실베르트는 문득 고개를 들어 주위를 둘러보았다.

이제는 세계 문화유산이 되어 버린 제1 국회의사당.

종전 직후, 대격변의 승리 과정을 담아 그려낸 스테인 글라스(Stained glass)가 사방에서 반짝거렸다.

치열한 전투를 치르는 몬스터와 인간의 모습. 강이 되어 흐르는 핏물과 곳곳에 쌓여 있는 시체들…….

눈부신 활약으로 역사에 이름을 남긴, 불행히도 이제는 대부분 죽고 없는 옛 영웅들의 흔적을 스쳐 지나간 시선이 한곳에 머물렀다.

이 영광스러운 기록 속에서도 가장 높은 곳. 천장에 아로새겨진 두 존재를 향해.

‘이런, 아직도 그곳에서 저를 내려다보시는군요.’

미카엘 실베르트는 실소를 흘렸다.

인류를 불구덩이로 밀어 넣은 악마, 마왕 아스모데우스의 심장에 검을 박아 넣은 구세주가 아래를 굽어보고 있었다.

마치 자신의 존재를 잊지 말라는 듯이.

당장이라도 내려와 신처럼 천벌(天伐)을 내릴 것처럼.

하지만…….

‘이제는 아닙니다, 스카이.’

미카엘 실베르트는 부드럽게 미소지었다.

다른 영웅들에 비하여 특별히 강하지도, 그렇다고 약하지도 않았던 젊은 시절의 그는 이제 누구도 부정할 수 없는 강자가 되어 돌아왔다.

‘반면 당신은 어떻습니까.’

그가 경외하고, 두려워하고, 눈에 띄지 않기 위해 숨죽여 엎드릴 수밖에 없었던 천태민은 이제 없다.

그저 이곳의 기록으로 남아, 곧 왕좌에 오를 자신을 지켜보는 것이 인류의 구세주가 할 수 있는 전부였다.

“당신이 서 있던 그 자리를…… 이제 내가 채우겠습니다.”

그리고 환희 어린 목소리가 흘러나온 그 순간.

그그긍.

굳게 닫혀 있던 문이 열리고, 그 틈새로 빛과 함께 한 사람의 목소리가 스며들었다.

“지랄을 한다, 지랄을.”
```

## Final English reading copy

```markdown
# Chapter 774

Back when I was a rookie Hunter, I used to cry sometimes.

No—if I’m being honest, pretty often.

Looking back now, I suppose all of it was just growing pains. But that was how it was back then.

It was only natural. At the time, I was a newly minted adult still wet behind the ears, and the Hunter training camp was literally nothing more than a training camp.

What had my first real mission been like?

No matter how hard I tried to remember, the memory remained hazy as fog.

Not because it had passed its expiration date, but because I had half-lost my mind the moment the battle began.

Of course, a few fragments had remained clear.

The backs of the tanks collapsing beneath the monsters’ overwhelming numbers. The thick stench of blood and the foul odor of creatures that did not belong to this world.

The weight of the spear that had felt heavier than ever, and my sweat-soaked grip around it…

That was all.

At the moment of impact, everything around me had grown distant. When I opened my eyes again, the world was a sea of blood.

And the Team Leader, who had been waiting for me to wake up with a cigarette between his lips, had immediately said this:

“You. Rookie.”

“Y-Yes.”

“You fucking bastard.”

“Excuse me?”

“I almost died saving your ass. Did my wife put you up to it? Tell you to kill me and split the insurance payout with her?”

“N-No.”

“You fought pretty well for someone who’d lost his mind, but if you pull that shit again, you’re going to die. Seriously.”

“…I’m sorry.”

“By the way, what’s your name?”

“Jin Taekyung. Jin Taekyung, sir.”

“What year were you born?”

“2020.”

“Holy shit. People were born in 2000?”

The Team Leader had glared at me while puffing furiously on his cigarette. Only then did he tell me his name.

“I’m Hong Cheonsu.”

“Oh. Yes, sir.”

“From now on, when we’re off duty, calling me uncle would be a little weird. Call me hyung instead. Cheonsu hyung.”

“Yes, Cheonsu hyung.”

“This kid doesn’t even know how to refuse politely. And we’re still inside the Gate, you little shit.”

I didn’t know it at the time.

I didn’t know that I would share thick and thin like brothers with that Team Leader who looked so foul-tempered.

I didn’t know that, only a few years later, he would sacrifice himself in my place.

“You did good. Here’s your payout.”

Six 50,000-won bills, after taxes and the Guild’s fee had been deducted.

I took the payment for risking my life that day and returned to my goshiwon.[^1]

When I opened the door, the room—less than four pyeong—smelled of mold. A family photograph sat on a table with a broken corner.

And I cried.

At first, I only sobbed quietly. But before long, I buried my face between my knees and wailed like a little child.

If someone hadn’t opened the locked door, I might have kept the entire goshiwon awake all night.

“Hey, new guy. Sorry for barging in without permission. I’m the manager here, but I kept getting complaints, so I had no choice but to use the master key—”

The manager stared at my tear-streaked face, let his voice trail off, scratched his greasy hair, and closed the door.

I thought that the manager, who looked like some middle-aged man, would never come back.

At least, not until I saw him again a little later, carrying soju and a bag of ramen in his hands.

“Want a drink? Oh, wait. You’re not a minor… obviously. Look at the size of you. Whew.”

Memories from nearly ten years ago.

As time passed, I changed. My fear of monsters and the loneliness I felt being separated from my family gradually faded.

No.

I became numb to them.

Like a hamster placed on a wheel, I simply ran and ran.

Even if I couldn’t move forward, it was better than stopping. There were things I could protect only by keeping that wheel turning.

Family.

Friends.

Companions.

By then, I couldn’t stop anymore.

The tiny hamster wheel inside the cage that had confined me had, at some point, transformed into the enormous wheel of fate. And the word *duty* I carried in my heart had grown increasingly clear—and increasingly heavy.

Maybe that was why.

Maybe that was why I had been able to look into that fading memory, if only in a dream.

Maybe that was why my cheeks had been wet when I opened my eyes to someone shaking me awake.

“…Gyeong. Mr. Jin Taekyung.”

I blinked. At last, my blurry vision came into focus.

The familiar face looking down at me with concern showed no noticeable change in expression. Perhaps because of that, even the smallest emotion stood out all the more.

“Are you all right?”

I rubbed the dampness from the corners of my eyes and answered.

“I don’t know.”

“Were you having a bad dream?”

“I couldn’t say.”

I sat up, my voice hoarse.

Through the gap between the curtains hanging by the window, I could see the dark landscape outside. The clock showed that it had only just passed noon.

“I don’t know whether it was a nightmare or a good dream. I don’t know either.”

Team Leader Choi watched me in silence before speaking in a calm voice.

“Don’t dwell on it. It was only a dream.”

He was right. A dream was only a dream. People were the ones who determined whether something would bring good or bad fortune—and that was my role today.

No.

Our role.

“I haven’t fully woken up yet, so let me ask you something. Was what happened last night also a dream?”

“Last night?”

“Yes. A lot of familiar faces appeared. At the end, I even saw a British prince dressed as a hotel bellboy.”

Only then did a faint smile appear at the corners of Team Leader Choi’s mouth.

“How strange. I had the same dream.”

“Oh, you did? Personally, I thought it was a pretty nice dream.”

“I thought so, too.”

Naturally, that part had not been a dream.

The conversation that had begun in secret had continued until deep into the night, and I had collapsed into sleep beneath the weight of the exhaustion I had accumulated over the past few days.

Perhaps thanks to that, my mind was clear and my body felt light.

Almost unnaturally so.

*Of course, there are a few flaws.*

I focused on the faint pain deep within my body.

The effects of **Broken Body**, which had yet to be healed, were not merely represented as numbers on the System. Like a parasite clinging to its host, they were eating away at part of my strength.

*Can I do it? Even in this condition?*

A single question flashed through my mind.

But I soon shook my head.

This was not a matter of whether I could do it or not.

I had to do it.

For everyone—including me and my people.

“What about the preparations?”

Team Leader Choi answered without hesitation.

“Everything is ready.”

The conviction in his voice was unmistakable—the attitude of someone who had prepared everything he possibly could.

But I asked again.

Not Team Leader Choi, but another person crouching somewhere out of sight.

“What about you?”

Once again, there was no answer.

Even though he had clearly seen and heard everything happening here, he chose silence once more.

As though he were someone trying to sever every last shred of affection between us. As though he were a traveler who had finished preparing to leave.

But…

I had no intention of letting him go.

Especially not for some fucking reason like this.

“Let’s go.”

I left the room in a calm voice.

Team Leader Choi followed immediately, and the Hunters from the Peace and Ares Guilds filled the hallway behind us, trailing after us like a dragon’s tail.

It was time to set the enormous wheel in motion.

* * *

The sky was gray that day.

Dark clouds had spread across the capital region under cover of dawn, spilling a light drizzle, and the air against my skin was chilly.

But to the people, the weather was irrelevant.

They had hope that the clouds would soon scatter and sunlight would shine through.

No.

Perhaps *conviction* was a more accurate word than hope.

The historic inaugural ceremony of the new World Hunter Federation.

That was the sunlight everyone had been waiting for—the alliance of superhumans that would save them from the second Great War that was about to descend upon them, or perhaps had already begun.

The heroes of the past, present, and future would gather in one place and be reborn as Hunters in the truest sense of the word.

They would become humanity’s sword and shield, clearing away those dark clouds and protecting the world from the monsters surging in like waves.

Today.

Here.

*A new history begins.*

Swish.

Michael Silbert ran his fingertips across the table.

The enormous round table had three hundred seats, and its surface was covered in marks left by sharp weapons.

*Records left behind by heroes.*

He still remembered it clearly.

On the day the unprecedented alliance known as the World Hunter Federation was born, Michael Silbert had stood alongside them in that glorious moment.

Beside those who were now dead, he had shouted until his blood ran hot. They had drawn their weapons and pointed them at the sky, then driven their swords into the enormous round table and sworn to become humanity’s sword and shield.

*Yes. Right here.*

It was an unforgettable memory.

Michael Silbert gently stroked the chair where he had once sat.

It carried every mark left by the years. It was rough and creaked beneath his touch, but even that stirred a strange emotion within him.

But that was all.

Michael Silbert merely looked down at the object that held his memories of the past. He did not sit in it or lean against it.

At some point, his gaze had left the chair and turned toward the center of the round table.

The only empty space.

There was no chair there, nor any platform. Isolated by the three hundred seats, it almost seemed as desolate as an uninhabited island.

But in the past, neither Michael Silbert nor anyone else had thought of it that way.

There had always been one person who filled that space.

The strongest and brightest of them all. The hero among heroes, whom even those who envied him had no choice but to regard with awe and fear.

*Sky.*

Michael Silbert suddenly raised his head and looked around.

The First National Assembly Hall, which had since become a World Heritage site.

Stained glass created just after the war ended, depicting the course of humanity’s victory in the Great Cataclysm, glittered on every side.

Monsters and humans locked in fierce battle. Blood flowing like rivers, and corpses piled up in every direction…

His gaze passed over the traces of the old heroes who had etched their names into history with their dazzling accomplishments—heroes who, unfortunately, were now mostly dead.

Then it came to rest on one place.

The highest point within those glorious records.

The two figures carved into the ceiling.

*My, my. You’re still looking down at me from up there.*

Michael Silbert let out a quiet laugh.

The savior who had driven a sword into the heart of Asmodeus, the Demon King who had cast humanity into a pit of flames, was looking down at him.

As though warning him never to forget his existence.

As though he might descend at any moment and pass divine judgment like a god.

But…

*Not anymore, Sky.*

Michael Silbert smiled gently.

In his youth, he had been neither particularly strong nor particularly weak compared to the other heroes.

Now, he had returned as a powerhouse no one could deny.

*But what about you?*

Cheon Taemin—the man Michael had revered, feared, and been forced to keep his head down to avoid drawing attention from—was gone.

All he could do now was remain as a record in this place and watch Michael, who would soon ascend the throne.

That was all the savior of humanity could do.

“I’ll fill the place where you once stood.”

And the moment those words left his mouth in a voice brimming with joy—

Grrrnnng.

The tightly closed door opened, and a voice seeped through the gap along with the light.

“What a load of bullshit. What a load of bullshit.”

[^1]: A *goshiwon* is a very small, inexpensive room-for-rent housing arrangement, often used by students and people with limited means.
```

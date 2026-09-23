<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0771.txt",
      "sha256": "06d9403df16b7702f2ae1127f055b571234606d613dda8d94a164ce8b5bc50fb",
      "bytes": 14488
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e7d632e2eb6052df8c2659e38f24ea2a59487331a9176150cf94d726a7ce91a7",
      "bytes": 1683
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "020195aeee3920f401f4260c4ea8d0bd4e737aa2170751aa5d731aea7d0b81ed",
      "bytes": 222073
    },
    {
      "path": "characters/Cheon Taemin.md",
      "sha256": "249e62de2da1da02d6abaf6e9751d485eb99f86ef9d4f89dc1c0e495405d9a75",
      "bytes": 752
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0a8a27d1dcac7531981eedd50cf0b8c01ac80e895a0b609edfbecf2431d5ff05",
      "bytes": 2017
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "80fa5a758a9ea984fc395e43e9e173601e3d24c2147de352fdacd18a84e73244",
      "bytes": 622
    },
    {
      "path": "characters/Michael.md",
      "sha256": "e80e6eb3baec6f21a48e6f20501c92d914317966217a4f3d3b3e731c777a1b76",
      "bytes": 951
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "a3aed6aeb4792bf09b159db4922fa418aed823f0a7f2e7cfe30fdd558bad2f38",
      "bytes": 644
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9d02ded1ec3e5fbb000406fbf261c23360dd3c860c8f046b9a15e919d7892219",
      "bytes": 239838
    }
  ],
  "estimated_tokens": 10459
}
-->

# Durable State Update — Chapter 771

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 771. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 771. Profile updates may replace only one
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
  "chapter": 771,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 771,
    "continuity_sources": [771],
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
    "The Skeleton King has accepted that humanity will reject him as a monster and has asked Jin Taekyung to erase him publicly.",
    "Jin Taekyung considers the Skeleton King a trusted comrade and friend and cannot willingly sacrifice him.",
    "Team Leader Choi believes Jin must choose a course of action and refuses to let Jin confront Michael Silbert alone.",
    "Jin Taekyung has chosen to kill Michael Silbert as a third path instead of sacrificing the Skeleton King or surrendering the world to Michael.",
    "Jin intends for Team Leader Choi to lead or control the reestablished World Hunter Federation with support from their international allies.",
    "The Login function remains blocked by the main Quest, preventing Jin from gaining more time to deliberate in Murim.",
    "Team Leader Choi has drawn the Hero's Sword and begun confronting Jin to stop him from leaving.",
    "A mysterious faint vibration interrupts the confrontation."
  ],
  "continuity_sources": [
    770
  ],
  "open_questions": [
    "What caused the faint vibration that interrupted Jin and Choi?",
    "Can Jin kill Michael Silbert and can Choi secure control of the reestablished World Hunter Federation?",
    "What will ultimately happen to the Skeleton King if Jin's alternative plan fails?"
  ],
  "safe_through": 770,
  "temporary_decisions": [
    "Render 스켈레톤 킹 as Skeleton King.",
    "Render 세계 헌터 연맹 as World Hunter Federation.",
    "Render 영웅의 검 as Hero's Sword.",
    "Retain Erasure for 소멸.",
    "Use Magic Johnson, Chuck Hagel, Pai Chen, and Prince Felix as the established English names."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 천태민    | **Cheon Taemin**  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 슬레이어 | **Slayer** | Cheon Taemin's title after killing the Demon King. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 스카이 | **Sky** | American epithet for Cheon Taemin. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 미카엘 | 진태경 | rival_to_target | you | quietly polite but threatening | Michael warns Jin to reconsider for the sake of Jin's monster friend. |
| 진태경 | 미카엘 | target_to_rival | Go fuck yourself | blunt and profane | Jin rejects Michael's proposal to resurrect the World Hunter Federation. |

## Listed compact profiles

### Cheon Taemin.md

# Cheon Taemin (천태민)

- **Safe through:** Chapter 770
- **Aliases:** Slayer; Sky (the American epithet used for him)
- **Role:** Cheon Taemin is Ares Guild Master and the world's greatest Hunter, known as the Slayer for killing the Demon King and creating the first Mana Cultivation Method during the Great Cataclysm, and he remains unconscious after more than twenty years in a wired mechanical capsule at his former mansion.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** Maternal grandfather of Team Leader Choi and Jin Taekyung and father of Soyeong; regarded by Lee Jungryong as an older brother despite their lack of blood relation.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 770
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, and a publicly recognized S-rank-level Hunter who formally retains an A-rank license, as well as a traveler between Murim and another world resembling the realm of immortals and the principal Hunter opposing Michael Silbert's terrorist campaign.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real; treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 770
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 770
- **Aliases:** None
- **Role:** Michael Silbert is the Guild Master of Odin Guild, a public hero who helped suppress five Monster Waves, the hidden architect of a coordinated terrorist campaign, and a feared rival whose warning about a second Great Cataclysm triggered worldwide panic and led the UN to approve the World Hunter Federation's reestablishment.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, and regards Jin Taekyung as a serious adversary.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 769
- **Aliases:** None
- **Role:** The Prophet is the mysterious leader of the revived Hasasin, a Middle Eastern terrorist organization preparing further attacks against apostates and Western heretics.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors and is revered as a sacred figure by the followers.

## Korean source

```text
＃771화



지이잉.

진동음의 정체를 알아차리는 건 그리 어렵지 않았다. 당장 내 주머니에도 비슷한 소리를 내는 물건이 하나 들어 있었으니까.

“팀장님, 전화 온 것 같은데 안 받아요?”

“신경 쓰지 마십시오. 지금은 그게 중요한 게 아니니까요.”

“왜, 내가 전화 받는 틈을 타서 기습이라도 할까 봐?”

“그건…….”

최 팀장은 말꼬리를 흐렸다.

사실 우리가 이렇게 대치하고 있다는 것 자체부터가 어불성설이다.

최 팀장이 제아무리 타고난 재능이 뛰어나고, 실력이 일취월장했어도 나를 막아서는 건 불가능하니까.

그럼에도 지금까지 그가 서 있을 수 있는 이유는, 온전히 내 배려 때문이었다.

어쩔 수 없이 쓰러트려야만 하는 친구를 향한 배려.

그리고 한편으로는 그럴 만한 이유가 있는 배려이기도 하다.

“직통으로 걸려 올 정도면 제법 중요한 전화 같은데, 그냥 받으시죠. 어차피 나도 목격자들이 충분히 모일 때까지 기다려야 하는데.”

“목격자…… 말입니까?”

“네. 목격자.”

그 세 글자의 의미를 곱씹는 최 팀장을 바라보며, 나는 천천히 말을 이었다.

“앞으로 벌어지는 일은, 지켜보는 사람들이 많을수록 좋을 겁니다. 우리 모두를 위해서라도.”

어쩔 수 없다.

최 팀장과 나는 이미 오래전부터 같은 배를 탄 몸. 내가 미카엘 실베르트를 죽이게 된다면 최 팀장 역시 한 패거리로 엮여 들어갈 것이 뻔하다.

그뿐인가. 평화 길드도, 아레스 길드도. 가족과 친구, 나와 연관된 사람들 모두가 다치게 된다.

그렇게 되면 모든 게 끝장이다.

‘최악의 상황을 막기 위해서라도, 많은 이목이 지켜보는 앞에서 선을 그어야 한다.’

이제 곧 나는 선지자와 버금가는, 혹은 그 이상으로 악명 높은 범죄자가 된다.

한솥밥을 먹던 동료에 의해 언데드 몬스터와 손을 잡았다는 사실을 추궁당하자, 주저 없이 그를 쓰러트리고 몬스터와 함께 도망친 인류의 배신자.

그리고…… 희대의 영웅. 미카엘 실베르트를 대낮에 죽인 희대의 살인범.

“뼈 한두 개 부러트리는 정도로는 안 끝날 겁니다. 전화 받는 김에 포션도 체크해 두세요.”

내 담담한 제안에 최 팀장이 입술을 깨물었다.

“……진심이시군요.”

“이미 고민은 끝났고, 가야 할 길은 정해졌으니까요.”

어느 순간부터 지켜야 할 것들이 많아진 나는 선택에 앞서 늘 고민에 고민을 거듭해야 했다.

그러나 한번 결정을 내렸다면 망설임 따위는 집어던져야 한다.

뒤를 돌아보는 순간 망설임이, 빈틈이 생기고 만다.

그렇게 나는 돌아보지 않는 법을 조금씩 배웠다.

무림에서. 현대에서.

날 죽이려 달려드는 온갖 괴물들과, 그 괴물보다도 더한 혐오스러운 인간군상의 틈바구니에서.

“이게 내가 선택한 길이고, 지금으로서는 최선입니다,”

스켈레톤 킹을 희생시키는 것과, 미카엘 실베르트에게 이 세상을 들어 바치는 것.

무엇하나 결정할 수 없는 그 양자택일(兩者擇一)의 상황 속에서 나는 결정했다.

이대로 허수아비처럼 조종당하느니, 차라리 영웅을 죽이고 몬스터와 결탁한 배신자가 되겠다고.

그렇게 해서라도 화근(禍根)을 뿌리 뽑겠다고.

‘놈은…… 오늘 내 손에 죽는다.’

화악.

뜨거운 열기가 전신으로 번진다. 씹어뱉듯 한 마디를 토해 낸 나는 한껏 끌어올린 기파(氣波)를 사방으로 퍼트렸다.

구구구궁!

건물 전체를 넘어, 인근을 뒤흔드는 거센 진동.

최 팀장의 발산한 것과는 비교도 되지 않는 그 거대한 힘에 소리 없이 틀어져 있던 홀로그램 TV가 치직거리며 꺼지고, 건물 곳곳에 설치되어 있던 경보 장치가 커다란 울음소리를 토해 냈다.

삑, 삑! 위이이이잉!

“도대체 이게 뭐…… 헉!”

“꺄아아악!”

“비상! 비상 상황입니다! 모두 대피해 주십시오!”

이미 앞서 최 팀장에 의한 진동에 웅성거리던 사람들의 목소리가 순식간에 비명으로 돌변했다.

문밖을 오가는 수많은 인기척과 그들이 토해 내는 다급한 외침 속, 허탈한 표정으로 나를 바라보던 최 팀장이 돌연 [영웅의 검]을 치켜세웠다.

푹!

바닥을 두부처럼 가르며 파고든 은빛 검신. 눈을 질끈 감았다가 뜬 그가 자포자기한 듯 품에서 스마트폰과 포션을 꺼내 들었다.

그리고 다음 순간, 나는 볼 수 있었다.

크게 뜨여진 최 팀장의 눈과 얼마 지나지 않아 빠르게 화면을 터치하는 그의 손길을.

파앗.

홀로그램 특유의 빛과 함께 허공에 나타난 거구의 사내. 매직 존슨이 그 어느 때보다 다급한 표정으로 입을 열었다.

- 젠장. 왜 이렇게 연락을 늦게 받는 거야? 내가 보낸 자료는 봤어? 조금 전에 뭔가 이상한 점을 발견했…… 잠깐, 이건 또 무슨 상황이지?

횡설수설하던 매직 존슨이 이상함을 눈치채고 우리를 번갈아 봤지만, 나는 대답 대신 그를 향해 성큼 다가갔다.

정확히 말하자면, 그의 손에 들린 서류를 향해.

‘이건.’

몇 장의 사진과 깨알 같은 글자들로 가득한 서류.

그러나 나는 무시무시한 동체 시력으로 불과 십여 초 만에 모든 내용을 파악했고, 동시에 단 한 번도 생각해 본 적 없던 가설들을 떠올렸다.

‘도대체 이게 왜…… 잠깐. 그렇다면?’

꼬리에 꼬리를 물고, 뒤죽박죽으로 섞여 들어가는 생각들.

순식간에 머릿속을 가득 메운 희뿌연 안개와 그 안에 숨어 있는 실체를 더듬고 있던 그때.

“아.”

입술을 비집고 흘러나온 외마디 탄성과 함께, 금방이라도 폭발할 듯이 들끓던 몸속 기운이 가라앉기 시작했다.

솨아아아.

흩어지는 기파와 순식간에 서서히 잦아드는 진동.

하지만 내 눈은, 뇌리를 채운 안개 너머로 언뜻 무언가의 실체를 확인한 마음은 그 어느 때보다 흔들리고 있었다.

‘만약 이게 사실이라면.’

그래, 정말 그렇다면…….

입안에서만 맴도는 말꼬리를 흐린 나는 멍하니 매직 존슨을 바라보다, 이내 최 팀장을 향해 고개를 돌렸다.

그의 앞에 마치 엑스칼리버처럼 꽂혀 있는 [영웅의 검]도 함께.

“최 팀장님.”

“네.”

“왜 다짜고짜 검을 뽑고 그러세요, 무섭게.”

“네?”

“생각 좀 해야 하니까 우선 검부터 집어넣고, 사람들 진정시키세요. 바깥에 엄청 시끄럽네.”

“……네?”

뭐지, 미친놈인가?

최 팀장의 눈빛에서 고스란히 전해지는 그 생각을 읽자 헛웃음이 흘러나왔다.

주위에서 어떻게 쳐다보던, 한참을 정신 나간 놈처럼 혼자 피식거리던 나는 두 뺨을 강하게 후려쳤다.

짝!

너무 세게 때렸나.

온 힘을 다한 셀프 싸대기에 골이 흔들렸지만, 덕분에 잠깐 무단 탈영했던 정신이 위수지역을 벗어나기 전에 돌아왔다.

‘좋아.’

비로소 완전히 현실로 돌아온 나는, 얼떨떨한 표정을 짓고 있는 두 사람을 보며 입을 열었다.

“자, 여러분. 그럼 이제부터 다 함께…….”

호흡 좋고. 감정 좋고.

마지막은 엄숙하게.

“씨벌놈들은 싹 다 뒈지고, 우리는 살아남을 수 있는 네 번째 길을 뚫어 봅시다.”

그리고 이 장엄하고도 엄숙한 선언에, 최 팀장과 매직 존슨의 눈가가 파르르 떨렸다.

“진태경 씨…….”

- 헤이, 진…….

더 무슨 말이 필요할까.

나는 다 안다는 듯이 희미하게 웃으며 고개를 끄덕였다.

마지막 순간에 엿본 새로운 희망에, 열양지기와는 다른 뜨거운 열기가 몸속 어딘가에서 끊임없이 샘솟고 있었다.

아니, 샘솟다 못해 흘러넘칠 정도다.

주르륵. 촤아악.

“……뭐여, 시벌.”

이게 진짜 흘러넘친다고?

네 번째 길보다 먼저 시원하게 뻥 뚫린 콧구멍으로 열기를, 아니 붉은 액체를 콸콸 쏟아내는 내 모습에 두 사람의 눈빛이 짜게 식었다.

“코피 납니다. 진짜 많이 납니다.”

- 마치 내 저택 광장에 설치된 분수를 보는 것 같군. 정확히는 분수에 포함된 아기 천사가 오줌을 저렇게 싸.

“그러니까 살살 좀 때리시지.”

- 이러다 과다 출혈로 쓰러지겠는데. 최, 포션 있어?

“안 그래도 방금 전에 하나 꺼내 놓은 거 있습니다. 이런 상황에서 쓰게 될 줄은 몰랐지만…….”

- 잘됐군. 얼른 진에게 줘. 그런데 아까 네 번째 길 운운했던 건 무슨 뜻이야? 아냐, 됐으니까 우선 코피부터 어떻게 하고 다시 설명해 봐.

“여기 받으십시오. 아, 피 튀니까 한 걸음만 좀 뒤로 물러나서요.”

“…….”

나는 최 팀장이 건네는 포션을 받아들며 생각했다.

어쩌면 곧장 미카엘 실베르트와 싸우러 가는 편이, 지금보다는 훨씬 멋있었을 거라고.

하지만 그래도 이게 나다.

당장은 멋없고, 더럽게 모양 빠지더라도 어떻게든 최선의 결과를 위해 발버둥 치는 남자.

남들이 모르는 곳에서 이 세상을 위해 불철주야 뺑이치는 현실적인 이 시대의 진정한…….

“뭐 합니까. 얼른 삼키십시오. 한입에 꿀꺽.”

- 진, 혹시 포션 잘 못 먹어? 원한다면 내가 도와줄까?

나는 시어머니처럼 구박하는 최 팀장과, 왠지 모르게 갑자기 입술을 핥는 매직 존슨을 두려운 눈빛으로 바라보다 후다닥 포션을 입에 털어 넣었다.

스아아.

그리고 얼음장처럼 차가운 치유의 기운이 몸속을 한 바퀴 돌았을 때, 거짓말처럼 멈춘 진동과 함께 정상으로 돌아온 홀로그램 TV에서 익숙한 얼굴을 발견할 수 있었다.

회색빛 머리카락. 회색빛 눈동자.

빛과 어둠. 그 사이 어딘가에서 태어난 것 같은 사내는 무수한 카메라 플래시와 카메라 앞에 서 있었고, 소리 없이 말을 이어 가는 그의 모습 아래로는 딱딱한 자막이 흐르고 있었다.



Live) [UN 긴급 총회, 압도적인 표결로 세계 헌터 연맹 재설립 승인.]

[미카엘 실베르트 : 인류를 위한 UN의 결정에 아낌없는 찬사를 보내며, 새롭게 설립될 세계 헌터 연맹의 첫 발족식을 제안하는 바입니다.]



“음소거 모드 해제!”

삑.

최 팀장의 다급한 명령어에, 스피커에 갇혀 있던 소음이 물밀 듯이 흘러나왔다.

- 지금 하신 발언은, 스스로 세계 헌터 연맹의 대표가 되시겠다는 뜻입니까?

- 미카엘! 지금 같은 상황에서 발족식이 열릴 수 있겠습니까?

- 언제, 어디에서 열리길 바라십니까!

- 워싱턴 포스트지에서 나왔습니다. 한 말씀만 부탁드립니다!

비명과도 같은 외침들.

카메라에도 채 담기지 않을 만큼 수많은 취재진이 그를 중심으로 에워싼 채 질문을 던지고 있었고, 미카엘 실베르트는 대답 대신 무거운 표정으로 손을 내저었다.

슥.

분명 홀로그램인데도, 실제로는 적어도 수 킬로미터 밖에 있을 그였음에도 모든 것이 생생하게 느껴졌다.

한 사람을 에워싼 공기. 한 사람만을 위해 마련된 현장의 분위기.

그저 보고 듣는 것만으로도 숨 막히는 위엄을 뿜어내는 놈의 존재감이.

이제 저곳에서 자유롭게 입을 열고닫을 수 있는 것은, 오직 미카엘 실베르트 한 사람뿐이었다.

- 하느님께 맹세컨대, 본인이 사흘 전 세계 헌터 연맹의 재설립을 제안했던 것은 단 하나. 이 세상을, 우리 인류를 위해서였습니다.

- ……!

느껴진다. 저들을 휘감은 격동이.

그리고 생애 어느 순간보다 화려하게 빛나는 스포트라이트 앞에 선, 타고난 선동가이자 연설가가.

- 세계 헌터 연맹의 대표는 본인이 아닌 다른 이에게 돌아가야 합니다. 이미 한 차례 마왕으로부터 인류를 구한 대격변의 영웅, 살아 있는 구세주!

공력이 실린 목소리가 끝도 없이 뻗어 나갔다. 격동을 이기지 못한 사람들이 하늘을 보며 부르짖었다.

스카이. 슬레이어. 천태민.

한 사람에게 주어진 여러 개의 이름. 하지만 동시에 적지 않은 숫자가 다른 누군가의 이름을 연호하고 있었다.

바로 미카엘 실베르트의 이름을.

그리고 그렇게 불길이 타오르듯 번지는 열기 속, 놈은 거침없이 말을 이어 갔다.

- 발족식은 반드시 열릴 것입니다. 스스로를 선지자라 칭한 미친 테러리스트도, 그 어떤 몬스터도, 설령 마왕이 돌아온다 해도 세계 헌터 연맹의 헌터들은 한자리에 집결하여 자신들의 대표를 뽑고 인류의 검과 방패가 되었음을 맹세할 것입니다!

- 와아아아아아!

귀가 먹먹하다. 이제 스피커가 아닌 두 귀로도 저들의 함성을 들을 수 있었다.

굳게 닫힌 문틈 사이로, 이 도시의 모든 이들이 하나가 되어 외쳤다.

아니, 어쩌면 전 세계 곳곳에서.

빛이 스며들고 전기가 통하는 그 모든 장소에서.

수많은 환호에 둘러싸여 홀로 빛나고 있는 저 영웅이, 이 모든 일의 배후라는 사실을 짐작조차 하지 못한 채.

그리고 타오르다 못해 터져 나오는 엄청난 열기 속, 미카엘 실베르트는 어느 때보다 힘 있는 눈빛과 목소리로 입을 열었다.

열광하는 사람들을 향해. 자신을 비추는 카메라를 향해.

혹은…….

- 이틀 후. 대한민국의 서울.

이곳에서 놈을 지켜볼 수밖에 없는, 나를 향해.

미카엘 실베르트는 전 세계에 선언했다.

- 구원자의 고향이자 세계 헌터 연맹이 처음 시작되었던 그곳에서, 우리는 다시 한번 그때와 같이 일어날 것입니다.
```

## Final English reading copy

```markdown
# Chapter 771

Bzzzt.

It wasn’t difficult to figure out what the vibration was. I had something in my own pocket that made a similar sound, after all.

“Team Leader, it looks like you’re getting a call. Aren’t you going to answer it?”

“Don’t concern yourself with it. That is not what matters right now.”

“What, are you afraid I’ll ambush you while you take the call?”

“That…”

Team Leader Choi let his voice trail off.

The fact that we were standing off against each other like this was absurd to begin with.

No matter how outstanding his natural talent was or how quickly his skills had improved, there was no way he could stop me.

The only reason he was still standing there was entirely because I was holding back.

Holding back for a friend I would have no choice but to bring down.

And, in a way, it was restraint for a reason that made sense.

“A call coming through on a direct line must be pretty important. Go ahead and answer it. I have to wait until enough witnesses gather anyway.”

“Witnesses…?”

“Yes. Witnesses.”

As I watched Team Leader Choi mull over those three syllables, I continued slowly.

“Whatever happens from here on, the more people watching, the better. For everyone’s sake.”

There was no other way.

Team Leader Choi and I had been in the same boat for a long time. If I killed Michael Silbert, it was obvious that Team Leader Choi would be dragged into it as one of my accomplices.

And it wouldn’t stop there. The Peace Guild. The Ares Guild. My family, my friends, everyone connected to me would be hurt.

If that happened, everything would be over.

*To prevent the worst-case scenario, I have to draw the line in front of as many eyes as possible.*

Soon, I would become a criminal as notorious as The Prophet—or perhaps even more so.

A traitor to humanity who, when a longtime comrade confronted him about joining forces with an undead monster, took him down without hesitation and fled alongside the monster.

And… the infamous murderer who killed the hero of the age, Michael Silbert, in broad daylight.

“This won’t end with one or two broken bones. Since you’re taking the call anyway, check that you have a potion ready.”

At my calm suggestion, Team Leader Choi bit his lip.

“…You’re serious.”

“I’ve finished thinking about it. The road I have to take has already been decided.”

At some point, I had gained too many things to protect. Before every choice, I had to think, and then think again.

But once I made a decision, I had to throw hesitation away.

The moment I looked back, hesitation would create an opening.

That was how I gradually learned not to look back.

In Murim. In the modern world.

Amid all the monsters that charged at me intent on killing me, and all the loathsome human crowds even worse than those monsters.

“This is the path I chose, and for now, it’s the best one.”

Sacrifice the Skeleton King, or hand this world over to Michael Silbert.

Faced with that impossible either-or, where I could not choose either option, I had made my decision.

Rather than being manipulated like a puppet, I would become a traitor who killed a hero and joined forces with a monster.

Even if that was what it took, I would uproot the source of this disaster.

*He’s going to die by my hand today.*

Whoosh.

A scorching heat spread throughout my body. Spitting out a single word as though I were chewing it to pieces, I unleashed the qi wave I had drawn up to its limit in every direction.

Rumble!

A violent tremor shook the surrounding area, extending beyond the entire building.

The enormous power was incomparable to what Team Leader Choi had released. The hologram television, which had been playing silently, crackled and shut off, while the alarm devices installed throughout the building let out an enormous wail.

Beep, beep! Weeeeee-oo!

“What the hell is this…? Gasp!”

“Aaaah!”

“Emergency! This is an emergency! Everyone, please evacuate!”

The people who had already been murmuring at the vibration caused by Team Leader Choi instantly broke into screams.

Amid the countless footsteps passing outside the door and the desperate shouts they were vomiting out, Team Leader Choi, who had been staring at me with a hollow expression, suddenly raised the *Hero’s Sword*.

Thunk!

The silver blade plunged into the floor, slicing through it like tofu. He squeezed his eyes shut, then opened them and pulled a smartphone and a potion from inside his clothes as though he had resigned himself to everything.

And then I saw it.

Team Leader Choi’s eyes widening, followed moments later by his fingers rapidly tapping the screen.

Flash.

With the characteristic glow of a hologram, the huge figure of a man appeared in midair. Magic Johnson opened his mouth with a more frantic expression than ever.

—Damn it. Why are you taking so long to answer? Did you look at the materials I sent? I found something strange a little while ago—wait, what the hell is going on here?

Magic Johnson had been babbling until he noticed that something was wrong and looked back and forth between us. But instead of answering him, I strode toward him.

More precisely, toward the documents in his hand.

*This is…*

The documents were filled with several photographs and tiny text.

But with my terrifying visual acuity, I grasped all their contents in barely a dozen seconds. At the same time, I thought of hypotheses I had never once considered before.

*Why the hell is this…? Wait. If that’s true…?*

Thoughts chased after one another, mixing together in a tangled mess.

Just as I was groping through the pale fog that had instantly filled my mind, searching for the truth hidden inside it—

“Ah.”

With that short exclamation escaping between my lips, the energy roiling inside my body as though it were about to explode began to settle.

Fwoosh.

The qi wave dispersed, and the vibration gradually died down.

But my gaze wavered more than ever, as did my mind after glimpsing the true shape of something beyond the fog filling my head.

*If this is true…*

Yes. If it really was…

I let the unfinished words circle inside my mouth, stared blankly at Magic Johnson, and then turned toward Team Leader Choi.

The *Hero’s Sword* was still stuck in the floor in front of him, like Excalibur.

“Team Leader Choi.”

“Yes?”

“Why did you suddenly draw your sword like that? You’re scaring me.”

“What?”

“I need to think, so put the sword away first and calm everyone down. It’s incredibly noisy outside.”

“…What?”

*What the hell? Is he insane?*

Reading the thought plainly conveyed through Team Leader Choi’s eyes, I let out a hollow laugh.

No matter how people around us looked at me, I continued to quietly chuckle to myself like a madman for quite some time before suddenly slapping both cheeks hard.

Smack!

Maybe I had hit myself too hard.

My head rattled from the full-force self-inflicted slap, but thanks to that, my mind—which had briefly gone AWOL—returned before it could make it beyond the garrison limits.

*All right.*

Only after I had completely returned to reality did I open my mouth while looking at the two men staring at me with dazed expressions.

“All right, everyone. From here on, let’s all…”

Good breathing. Good emotion.

I had to make the ending solemn.

“Let’s carve out a fourth path where every last fucking bastard dies and we survive.”

Team Leader Choi and Magic Johnson’s eyes began to twitch at this grand and solemn declaration.

“Mr. Jin Taekyung…”

—Hey, Jin…

What more needed to be said?

I gave a faint smile and nodded as though I understood everything.

At the new hope I had glimpsed in the final moment, a heat different from the Scorching Yang Qi continued to well up from somewhere inside my body.

No—it wasn’t merely welling up. It was overflowing.

Trickle. Splash!

“…What the fuck?”

Was it really going to overflow?

Heat—or rather, a torrent of red liquid—gushed from my nostrils, which had opened up with refreshing force before the fourth path even had a chance to do so. The two men’s gazes went cold.

“You have a nosebleed. A really bad one.”

—It reminds me of the fountain in the plaza of my mansion. More precisely, it looks like the baby angel built into the fountain is pissing like that.

“So you should have hit yourself more gently.”

—I think he’s going to collapse from blood loss. Choi, do you have a potion?

“I already took one out. I didn’t expect to use it in a situation like this, though…”

—Good. Hurry and give it to Jin. By the way, what did you mean earlier about a fourth path? No, never mind. Deal with the nosebleed first, then explain it again.

“Here. Take it. And move back one step, please. Your blood is splattering.”

“…”

As I accepted the potion Team Leader Choi handed me, I thought that perhaps going straight to fight Michael Silbert would have looked much cooler than this.

But this was still me.

A man who struggled somehow toward the best possible result, even if he looked uncool for now and was horribly undignified.

A realistic man busting his ass for the sake of this world where no one could see him, the true man of this era who was—

“What are you doing? Hurry up and swallow it. All at once.”

—Jin, do you have trouble taking potions? If you want, I can help you.

I looked at Team Leader Choi, who was scolding me like a mother-in-law, and Magic Johnson, who had suddenly started licking his lips for some reason, with frightened eyes before hurriedly emptying the potion into my mouth.

Ssshhh.

Then, as the ice-cold energy of healing made a circuit through my body, I found a familiar face on the hologram television, which had returned to normal as the vibration stopped as though it had never happened.

Gray hair. Gray eyes.

The man looked as though he had been born somewhere between light and darkness. He stood before countless camera flashes and cameras, continuing to speak without sound. Stark subtitles ran beneath him.

> **Live:** UN Emergency General Assembly Approves the Reestablishment of the World Hunter Federation by an Overwhelming Vote.
>
> **Michael Silbert:** “I offer my wholehearted praise for the UN’s decision on behalf of humanity, and I propose the first inaugural ceremony of the newly established World Hunter Federation.”

“Disable mute mode!”

Beep.

At Team Leader Choi’s urgent command, the noise trapped inside the speakers rushed out like a flood.

—Does that statement mean that you intend to become the representative of the World Hunter Federation yourself?

—Michael! Can an inaugural ceremony really be held in a situation like this?

—When and where would you like it to be held?

—We’re from the *Washington Post*. Please give us a statement!

Shouts like screams.

So many reporters had surrounded him that the cameras could not even capture them all, throwing questions at him from every direction. Instead of answering, Michael Silbert waved them away with a solemn expression.

Swish.

Even though it was a hologram, and even though he was actually several kilometers away at the very least, everything felt vivid.

The air surrounding a single person. The atmosphere of a scene prepared for one person alone.

The presence of that man, radiating suffocating majesty simply by being seen and heard.

Only Michael Silbert had the freedom to open and close his mouth there now.

—I swear to God, the only reason I proposed the reestablishment of the World Hunter Federation three days ago was for this world—for humanity.

—…!

I could feel it. The tumult wrapping around them.

And there he stood before a spotlight shining more brilliantly than at any moment in his life—a born agitator and orator.

—The representative of the World Hunter Federation should go to someone other than me. A living savior, the hero of the Great Cataclysm who already saved humanity from the Demon King once before!

His voice, infused with internal energy, stretched endlessly outward. Unable to contain their excitement, people looked to the sky and cried out.

Sky. Slayer. Cheon Taemin.

One man, given many names. But at the same time, a considerable number of people were chanting someone else’s name.

Michael Silbert’s name.

And amid the heat spreading like flames, he continued without hesitation.

—The inaugural ceremony will be held without fail. Whether it is the mad terrorist who calls himself The Prophet, any monster whatsoever, or even the return of the Demon King, the Hunters of the World Hunter Federation will gather in one place, choose their representative, and swear that they have become humanity’s sword and shield!

—Hurrayyyyy!

My ears rang. I could hear their roar even without the speakers now.

Through the cracks beneath the tightly closed doors, everyone in the city cried out as one.

No—perhaps from every corner of the world.

From every place where light seeped in and electricity flowed.

Surrounded by countless cheers, that hero shone alone, with no one even guessing that he was behind all of this.

And amid the immense heat that burned so fiercely it burst forth, Michael Silbert opened his mouth with a more powerful gaze and voice than ever.

Toward the frenzied people. Toward the cameras focused on him.

Or…

*Toward me—the one who could do nothing but watch him from here.*

Michael Silbert made a declaration to the entire world.

—Two days from now. Seoul, Korea.

—In that place, the savior’s homeland and where the World Hunter Federation first began, we will rise once again, just as we did then.
```

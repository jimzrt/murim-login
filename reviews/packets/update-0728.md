<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0728.txt",
      "sha256": "a1d57de48b84a6d4debbb6061b91ea3d0e4cdf5a5d5879d56232c6b1f6f1ac7b",
      "bytes": 15958
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ae469334fc2ba7660c954b31f3ce8360b082b7a2bb89f1508895a8e8b638d3a9",
      "bytes": 1579
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "dee3bec6a97af10fede2014d3d601ec9e3bcc585839a348b3bcdba34f55ec2bd",
      "bytes": 209972
    },
    {
      "path": "characters/Baek Hanseong.md",
      "sha256": "ee9adc84560f4efd9ba1dfbda30a514b129d0c056e979cbd0d1ce19699c9d51b",
      "bytes": 770
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "4e6fa6f088798a98f61fd8a8f72b8eaa1d5ed88e58019aa41b1612c529d4bc73",
      "bytes": 698
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "b74a242e36ed255f115979bd0296aeb02f8a9e53d0f461f0e89a7e746bc603a7",
      "bytes": 1774
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "efda6ae497f2bc331d05ce7e054a5cf8b4be3c4b05cdc989679c1ea1038aa018",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "eb365b588c8f419472faf5ae3d03f2fc09e1f1d44c806b8b40dd3a4a8fb09d96",
      "bytes": 622
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "beba0dfd81f6e91d4bbd9083abc8a3d0baa6f93d29583854bf72fafb03e8ac7a",
      "bytes": 939
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "77a1af6702369bd34848af1d07d41d67810d45567369af3d54b0fca4f77a12b4",
      "bytes": 220286
    }
  ],
  "estimated_tokens": 11928
}
-->

# Durable State Update — Chapter 728

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 728. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 728. Profile updates may replace only one
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
  "chapter": 728,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 728,
    "continuity_sources": [728],
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
    "Jin Taekyung created the stable, beginner-accessible Smiling Mana Cultivation Method and intends to make it publicly available.",
    "The world's increasing mana is strengthening monsters and producing mutation Gates and monster waves.",
    "Jin suppressed rebel groups and terrorist organizations to reduce the danger of the cultivation method being misused.",
    "Major Guilds worldwide are watching Jin and Choi Minwoo, and invisible pressure has delayed Peace Guild's additional overseas expansion.",
    "Choi Minwoo is the Peace Guild Master and has taken control of the Ares Guild.",
    "Jin may reveal the Jin Family's Cultivation Technique if the situation worsens substantially."
  ],
  "continuity_sources": [
    727
  ],
  "open_questions": [
    "How will the major Guilds respond when the Smiling Mana Cultivation Method is made public?",
    "Will Jin and Choi be able to release the method without provoking direct interference or retaliation?",
    "How much will public access to the method improve Hunters' ability to resist stronger monsters and mutation Gates?",
    "Will worsening conditions force Jin to reveal the Jin Family's Cultivation Technique as well?"
  ],
  "safe_through": 727,
  "temporary_decisions": [
    "Render 싱글벙글 마나 연공법 as The Smiling Mana Cultivation Method.",
    "Render 심판의 일주일 as The Week of Judgment.",
    "Render 구세주 코인 as the Savior coin.",
    "Preserve Jin's profane comic banter and Choi Minwoo's formal, controlled speech."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 송송이    | **Song Song**     |
| 무림맹    | **Murim Alliance**               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 지부장    | **Branch Leader**                            |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마정석     | **Magic Gem**         |
| 도사      | **Daoist**                                                      |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 황소자리 | **Taurus** | Zodiac sign Song Song uses as a nickname for Taekyung. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 똥개 | **Ddong Gae** | Taekyung's mocking misremembering of Hwang Gae's name. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |

## Listed compact profiles

### Baek Hanseong.md

# Baek Hanseong (백한성)

- **Safe through:** Chapter 613
- **Aliases:** None
- **Role:** Twenty-seventh President of Korea and the youngest president elected in Korean history; leads the government's public response to the Mutated Gate crisis and supports Jin Taekyung in public appearances.
- **Personality:** Confident, politically shrewd, composed, and willing to needle Lee Jungryong while advancing his anti-Ares stance.
- **Voice:** Polite, self-assured, calm, and lightly teasing.
- **Relationships:** Political counterpart to Lee Jungryong who has established a cooperative relationship with Jin Taekyung and Choi Minwoo while seeking to restrain the power concentrated in their two Guilds.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 639
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 613
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter and veteran tank in the Peace Guild; after recovering from the Black Hunters’ attack and having both arms reattached, he continues as a Hunter while nearing the end of rehabilitation.
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 727
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 727
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 613
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's; Healer Team Leader and temporary head of the Peace Guild's emergency rescue team, which is piloting free public-safety rescues for medium- and low-grade Gates in the capital region.
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; Jin recruited her to help run its emergency rescue team, while she remains his same-age friend and guildmate after rejecting his confession.

## Korean source

```text
＃728화



사람이란 동물은 누구나 그렇다.

성공이 계속되면 자신감이 높아지고, 활짝 열어 두었던 눈과 귀를 슬그머니 닫기 마련이다.

하지만 최 팀장은 뛰어난 헌터이자 경영자이기 이전에, 인간적으로도 썩 괜찮은 사람이었다.

스스로 결정권을 쥐고 있음에도, 언제나 모두의 양해를 구한다는 부분에서 더더욱.

“……해서 여러분들의 의견을 듣고 싶습니다.”

나직한 한마디와 함께 최 팀장의 이야기가 모두 끝나자, 소파에 앉아 있던 사람들은 잠시 침묵했다.

아니, 정확히 말하자면 사람‘들’은 아니다. 언제부턴가 자연스럽게 자리를 차지한 몬스터 한 마리가 끼어 있으니까.

그리고 그 몬스터의 얼굴은, 어느 때보다 심각하게 굳어 있었다.

“이 몸은 반대다.”

한 치의 망설임도 없는 단호한 거절에 쏠리는 시선들.

그러나 스켈레톤 킹은 아랑곳하지 않고 말을 이어 갔다.

“그 이유는 이 자리의 모두가 아는 그대로지. 과한 세력 확장은 경계를 사기 마련이고, 인간의 시기 질투는 위험을 불러일으킬 수밖에 없으니까. 내 말이 틀렸나?”

새삼 느끼는 거지만, 이 새끼 진짜 사람 다 됐네.

내가 떨떠름하게 고개를 젓자, 스켈레톤 킹의 목소리에 한층 힘이 실렸다.

“더 이상의 주목은 이 몸도 피하고 싶군. 다른 인간들이 내 진짜 정체에 알게 되면 너희 역시 곤란해진다. 그러니 멍청한 소리는 이만 집어치우거라.”

준엄한 일갈과 함께 끝난 연설. 나를 비롯한 모두는 약속이라도 한 것처럼 서로를 바라보았다.

어느 정도 일리 있는 말이긴 하다.

분명히 일리 있는 말이긴 한데…….

“그렇게 주목을 피하고 싶은 새끼가, 폰 생기자마자 SNS 계정부터 만들었냐?”

내 예리한 일침에 최 팀장과 임꺽정, 그리고 송송이가 차례대로 고개를 끄덕였다.

“진태경 씨께서 하신 말씀에 동의합니다.”

“그것도 그러네. 난 그런 거 안 해서 잘 몰랐는데, 저 친구 은근히 유명한 것 같더라고.”

“은근히 유명한 정도가 아니에요. 만든 지 얼마 되지도 않았는데 벌써 팔로워 수가 10만이 넘었다고요.”

정곡을 찔려 주춤하던 스켈레톤 킹이 송송이의 말에 가슴을 쭉 폈다.

“오늘부로 12만이다.”

“그래?”

“당연하지. 광고 제의가 사방에서 빗발치고 있다.”

나는 뿌듯해하는 녀석의 모습을 보며 허허 웃었다.

“이 시벌놈 보게. 12만 개의 뼛조각으로 나뉘고 싶니?”

“…….”

“당장 계정 지워라. 마지막 경고다.”

내 으름장에, 잠시 머뭇거리던 스켈레톤 킹이 침울한 목소리로 대답했다.

“……알겠다.”

“그나마 고분고분해서 다행이긴 한데, 설마 SNS에 이상한 헛소리 적어 놓은 건 아니겠지?”

현대 사회에서 인터넷의 파급력은 그야말로 어마어마한 수준이다.

기껏해야 전서구나 띄우는 무림과는 달리 손가락 몇 번 움직이면 전 세계로 퍼져나가는 것이 이 동네 국룰 아닌가.

‘저놈이 똥이라도 싸 놨으면 골치 아픈데.’

그리고 내 근거 있는 우려에, 송송이가 대수롭지 않은 어투로 불쑥 끼어들었다.

“다행히 별다른 건 없어. 그렇지 않아도 내가 한번 쭉 훑어봤는데, 그냥 지 얼굴 사진만 잔뜩 올려놨더라.”

“그래?”

“응. 그리고 팔로워 대다수가 해외 쪽이야. 그중에서도 특히 남성들 비율이 압도적이고.”

“그렇다면 다행이긴 한데, 도대체 왜 남자들이…… 아.”

순간 뇌리를 스치는 깨달음.

나는 스켈레톤 킹의 저 잘생긴 얼굴이, 어떤 사람의 손을 거쳐 탄생했는지 떠올렸다.

‘매직 존슨.’

세기의 대마도사. 그리고 세기의 게이.

두 개의 지팡이로 믿을 수 없는 마법을 부린다는, 바로 그 매직 존슨의 취향이 듬뿍 반영된 것이 바로 현재의 스켈레톤 킹이다.

그냥 대충 봐도 잘생기긴 했지만, 그중에서도 특정 분야에 속한 이들의 니즈를 완벽히 충족시켜 주는 얼굴과 체형인 것이다.

그렇게 모인 숫자가 무려 12만.

이 정도면 십만 마도가 다시 몰려와도 엉덩이를 걷어차 줄 수 있는 머릿수다. 물론 그들이 걷어차기만 할지는 의문이지만.

‘그나저나 이거 대단한 놈이었네.’

이름도, 얼굴도 전혀 알려지지 않은 상황에서도 단기간에 저만큼의 추종자들을 끌어모으다니. 무림맹주도 저렇게는 못한다.

그리고 새삼스럽게 바라보는 내 모습을 눈치채지 못한 채, 스마트폰을 만지작거리던 스켈레톤 킹이 침통한 얼굴로 입을 열었다.

“차마 계정을 삭제할 엄두가 나지 않는군. 넌 세상 누구보다 간악하고 잔인한 인간이다.”

“내가 전생에 무슨 죄를 지어서 몬스터 새끼한테 잔인하다는 소리까지 들어야 하냐.”

“아아, 이토록 갑작스러운 이별이라니. 이 몸의 눈부신 얼굴을 더 이상 볼 수 없게 될 어느 이름 모를 여인은, 하염없이 눈물을 흘리고 말겠지.”

“…….”

“뭐냐, 그 이상한 표정은.”

“아냐. 모르는 게 나아.”

진실은 간혹 드러나지 않는 것이 아름다운 법.

눈빛 교환을 통해 송송이와의 암묵적 합의를 끝낸 나는 주위를 둘러보며 입을 열었다.

“어쨌든, 다들 동의하시는 거죠?”

임꺽정이 당연하다는 듯 고개를 끄덕였다.

“나야 뭐, 태경이 너랑 최 팀장님이 그렇게 결정했으면 따라야지.”

“송이, 너는?”

“글쎄.”

송송이가 비스듬히 다리를 꼬며 말을 이었다.

“들어 보니까 결국 모두를 위해서 하는 일인데, 싫다고 하면 나만 나쁜 년 되는 거 아냐?”

“아니지.”

“그래?”

“응. 원래도 그렇게 착한 편은 아니었으니까.”

“어머, 이 새끼 말하는 것 좀 봐.”

싱긋 웃으며 중지를 치켜세운 송송이가 문득 한숨을 내쉬었다.

“참 스펙타클하네. 처음 최 팀장님한테 이적 제의받고 아레스 길드 나올 때만 해도 이렇게 될 줄은 몰랐는데.”

“그러게. 차라리 그냥 거기 있지 그랬냐.”

“야, 나도 어쩔 수 없었어. 그러기에는 지부장이라는 새끼가 너무 변태였거든. 차라리 젊고 잘생긴 데다 돈까지 많은 누구 밑에 들어가는 게 좋겠다 싶었지. 근데 첫날부터 감이 좀 안 좋더라?”

“첫날?”

“응. 변태 새끼 피해서 왔는데, 웬 이상한 새끼가 하나 있는 거야. 배고파 죽겠는데 고기는 죄다 태워 먹고, 갑자기 지 별자리가 황소자리래. 이거 완전히 미친놈 아니야?”

“아하.”

피식 웃은 나는 별다른 말 없이 그녀를 바라보았다.

솔직히 임꺽정과 송송이에게는 미안한 감정이 존재한다. 평화 길드가 설립된 이래 그들이 원치 않았을 온갖 평지풍파를 겪어야 했으니까.

“음.”

“뭐야? 그 반응.”

“그냥. 아직 늦지 않았다는 말을 해 주고 싶어서.”

“뭐?”

“이번 일, 어쩌면 너나 꺽정 아저씨가 생각하는 것보다 훨씬 위험할 수도 있어.”

평소와는 달리 웃음기 쏙 뺀 목소리에, 송송이의 눈빛이 깊게 가라앉았다.

“어느 정도길래?”

“이제 국내 스케일은 벗어났다고 봐야지.”

“스스로를 과소평가하는 경향이 있는 것 같은데, 너나 최 팀장님 정도면 이미 오래전에 국내는 벗어났어.”

조금도 과장되지 않은 사실이었다.

나는 중국에서 아크 리치를 때려잡은 후부터 전 세계에 이름을 알렸고, 최 팀장은 아레스 길드의 새로운 성주이자 살아 있는 구세주의 후계자로 매스컴을 탔으니까.

하지만 이건 또 다른 이야기다. 아니, 오히려 지금껏 이룬 모든 것을 말미암아 생겨난 문제이기도 하다.

나는 어깨를 으쓱해 보였다.

“누가 그러더라. 몸집이 커지면 뜯어먹을 것도 많아지는 법이라고.”

“그래서. 얼마나 뜯어먹히려고?”

“그럴 계획은 없는데. 앞으로도 쭉 그럴 거고.”

나를 물끄러미 바라보던 송송이가 문득 입을 열었다.

“그거 알아?”

“뭘?”

“이미 발 빼기에는 한참 늦었다는 거. 여기 계신 꺽정 아저씨도, 나도.”

임꺽정이 조용한 목소리로 송송이의 말을 받았다.

“그전에 빠질 생각도 없지.”

“아저씨.”

“늦었고 아니고를 떠나서, 한번 시작한 이상 끝까지 함께 가야 하는 거야. 먼저 떠난 사람을 생각해서라도.”

“……!”

“안 그래, 최 팀장?”

임꺽정의 나직한 물음과 함께, 모두의 시선이 한 방향을 향해 쏠렸다.

언제부턴가 말을 잃어버린 최 팀장은 누군가의 빈자리를 바라보고 있었다.

얼마 전까지만 해도 온기가 남아 있던, 이제는 무엇으로도 채워 넣을 수 없는 한 사람의 빈자리를.

그리고 입을 열었다.

“오늘 산소에 다녀왔습니다. 그런데 묘비 옆에 누군가 글을 새겨 놨더군요. 와 줘서 고맙다고. 사랑한다고. 다음에 또 와 달라고.”

그 누구도 입을 열지 않았고, 최 팀장은 담담하게 말을 이었다.

“해서 다음에는 모두 함께 그분을 뵈러 갔으면 합니다. 내년에도, 내후년에도…… 그리고 수십 년 뒤에도.”

그건 소중한 사람을 먼저 떠나보낼 수밖에 없었던 그의 각오였다.

‘모두 함께’라는 네 글자에는, 두 번 다시 같은 일이 벌어지지 않도록 하겠다는 의지가 스며들어 있었다.

‘수십 년 뒤라.’

그래, 그거면 됐다.

그때의 우리가 어떤 모습일지는 모르겠지만, 지금 당장은 함께 가겠다는 것만으로도 충분하다.

“최 팀장님.”

내 나직한 부름에, 그가 무겁게 고개를 끄덕였다.

“알겠습니다. 시작해 보죠.”

말하기에 앞서 이미 대강의 논의는 끝내 놓은 상태. 최 팀장은 스마트폰을 꺼내 첫 상대에게 전화를 걸었다.

뚜우, 뚜. 달칵.

불과 세 번의 신호음이 울려 퍼지기도 전에 통화가 연결된다. 숨 가쁜 정치 생활로 연마된 중후한 목소리가 저 너머에서 들려왔다.

- 전화 받았습니다. 백한성입니다.

백한성이라는 이름은 대한민국에도 많다. 그러나 이런 상황에서 최 팀장이 가장 먼저 연락할 만한 백한성은, 단 한 사람뿐이다.

“네, 대통령님. 중요한 일로 연락드렸습니다.”

- 하하, 음. 그렇게 말씀하시니 벌써부터 기분이 묘하네요. 기대도 되고, 한편으로는 불안해지기도 하고.

한 나라를 움직이는 거물의 등장에 임꺽정과 송송이는 입을 다물었고, 눈을 부릅뜬 스켈레톤 킹은 나를 향해 속삭였다.

“백한성 대통령이라면 혹시 그.”

“맞아. 우리나라 대통…….”

“안다. 천만이 넘는 팔로워를 보유한 인기 셀럽이 아니더냐.”

“…….”

“젠장. 인간 주제에 무려 이 몸의 백 배라니.”

나는 분통을 터트리는 스켈레톤 킹을 보며 생각했다.

‘제발 꼭 뒈졌으면…….’

생각해 보니 이미 뒈져 있긴 하다.



* * *



복도는 눈이 부시도록 환했다. 거대한 기운이 담긴 A급 마정석은 건물 전체에 끊임없이 에너지를 공급했고, 층층을 가득 메운 사람들은 저마다의 업무로 바빴다.

어느 순간, 갑작스러운 어둠이 찾아오기 전까지는.

파직. 쉬우우우.

전등에서 흘러나오던 불빛이 사그라지고, 모든 기계가 움직임을 멈추었다.

곳곳에서 튀어나온 당황한 외침들이 찰나의 침묵을 깨트리며 울려 퍼졌다.

“뭐야 이거?”

“어, 정전인 것 같은데요.”

“그걸 대답이라고 하냐? 아니, 씨바…… 그러니까 마정석 좀 미리 교체해 달라니까. 이십 년 넘게 빨대 꽂고 쪽쪽 빨아먹으니까 쟤도 차라리 죽여 달라고 호소하는 거 아니냐고. 이거.”

“그러게요. A급 마정석이면 전문가들 의견으로는 최소 삼십 년은 버틴다고 했는데.”

“그래서. 왜 마정석이 십 년 일찍 오링났는지가 중요하냐? 아주 궁금해서 미치겠어?”

“아, 아닙니다.”

“됐고, 다들 집중해! 2분 내로 보안팀이랑 기술팀 올 테니까 다들 손 하나 까딱하지 말고 그대로 있어! 예비용 마나 랜턴 있는 놈들은 얼른 가져오고.”

그러나 부서장의 외침이 무색하게도, 채 1분도 되지 않아 사방이 환해졌다. 잠시 끊겼던 전력이 돌아온 것이다.

“젠장. 이건 뭐 똥개 훈련도 아니고…….”

투덜거린 부서장은 한발 늦게 도착한 보안팀을 향해 손을 내저었다.

“아, 보시다시피 다 괜찮아요. 그런데 갑자기 웬 정전이래?”

“안 그래도 저희 팀장님께 여쭤봤는데, 드물긴 하지만 몇 년에 한 번 정도는 있는 일이랍니다. 정확한 원인은 기술팀에서 확인해 봐야겠지만요.”

“하긴, 뭐. 그거야 그쪽 소관이니까.”

멋쩍게 웃은 보안팀 소속 헌터는 여러 가지 사항을 확인했다.

정전되는 동안 분실된 물건은 없는지. 혹여 다친 이가 있는지. 이번 사태 중 느낀 수상한 점 등등.

하지만 간단한 절차에 불과했고, 고작해야 일 분 남짓한 정전에 신경과 성의를 쏟기에는 당장 처리해야 할 일들이 산더미였다.

“저기 미안한데, 더 물어볼 거 있으면 나중에 하면 안 될까? 지금 우리 사정이 좀 그러네.”

부서장의 말에 보안팀 직원이 고개를 끄덕였다.

“그거야 어려울 거 없죠. 그런데 평소보다 훨씬 바쁘신 걸 보니, 무슨 일이 생겼나 봐요?”

“위쪽에서 공문 내려왔어. 당장 오늘 중으로 큰 거 한 건 터진다고.”

“큰 거요?”

“어. 자세한 사항은 우리도 잘 모르는데 청와대 쪽에서 내려온 것 같더라고. 그거 때문에 다들 초긴장 상태야. 이대로면 칼퇴근도 글렀어.”

“아이고, 괜히 시간만 뺏었네요.”

“뭘 또 그렇게까지. 어차피 다 같이 나랏일 하는 사람들인데. 그럼 고생하고, 나중에 또 봅시다.”

“예, 고생하십시오.”

하지만 각자의 자리로 향하는 그들은 알지 못했다.

일 분도 되지 않았던 그 짧은 시간 동안, 유령 같은 어떤 존재가 짙은 어둠을 타고 건물 곳곳을 누볐음을.

그리고 지하 깊숙한 곳에 위치한 증거 보관실에서 한 가지 물건이 사라졌음을.

각자의 업무를 보던 수백여 명의 직원도, 뛰어난 실력을 지닌 보안팀의 헌터들도, 심지어는 경보 마법조차 그 사실을 인지하지 못했고, 모든 일을 손쉽게 끝마친 어느 존재는 유유히 건물 밖을 빠져나갔다.

저벅. 저벅.

누군가의 발걸음과 함께.

“세환이, 3층 체크했어?”

“예. 팀장님. 별다른 문제는 없었습니다. 그런데 기술팀 쪽은 뭐랍니까?”

“끽해야 십 분도 안 된 일인데, 벌써 원인이 밝혀졌겠냐.”

“그것도 그러네요. 그나저나 오늘 날씨 진짜 좋지 않습니까?”

스륵.

상관을 향해 너스레를 떠는 보안팀 직원의 등 뒤로, 짙은 그림자가 작게 일렁였다.
```

## Final English reading copy

```markdown
# Chapter 728

Humans are all the same.

When success keeps coming, their confidence grows, and they inevitably begin quietly closing the eyes and ears they once kept wide open.

But before being an excellent Hunter and manager, Team Leader Choi was also a pretty decent person on a human level.

Even more so because, despite holding the decision-making authority himself, he always asked for everyone's understanding.

“……That’s why I’d like to hear everyone’s opinions.”

When Team Leader Choi finished speaking in a low voice, the people sitting on the sofa fell silent for a moment.

No, to be precise, it wasn’t *people*. At some point, a monster had naturally claimed a seat among them.

And that monster’s face was more solemn than ever.

“This body is opposed.”

Every gaze turned toward him at the firm refusal, delivered without a hint of hesitation.

But the Skeleton King continued without a care.

“The reason is obvious to everyone here. Excessive expansion of one’s forces is bound to attract suspicion, and human envy and jealousy can only invite danger. Am I wrong?”

I’d been thinking it for a while, but this bastard had really become just like a person.

When I awkwardly shook my head, the Skeleton King’s voice gained even more force.

“This body would also like to avoid attracting any more attention. If other humans learn my true identity, you will be in trouble as well. So stop spouting foolishness.”

The speech ended with that stern denunciation. Everyone, myself included, looked at one another as if we had made a pact.

He did have a point.

He definitely had a point, but…

“The bastard who wants to avoid attention made an SNS account the moment he got a phone?”

At my sharp retort, Team Leader Choi, Im Kkeokjeong, and Song Song nodded one after another.

“I agree with what Mr. Jin Taekyung said.”

“That’s true. I don’t use that sort of thing, so I didn’t know, but this fellow seems to be pretty famous.”

“Not just pretty famous. He hasn’t even had the account for very long, and he already has more than a hundred thousand followers.”

The Skeleton King, who had faltered after being struck in the heart of the matter, thrust out his chest at Song Song’s words.

“As of today, it is one hundred and twenty thousand.”

“Really?”

“Of course. Advertising offers are pouring in from every direction.”

I let out a hollow laugh as I watched him bask in his pride.

“You fucking bastard. Do you want me to split you into a hundred and twenty thousand pieces of bone?”

“……”

“Delete the account right now. This is your final warning.”

After hesitating for a moment at my threat, the Skeleton King answered in a depressed voice.

“……Understood.”

“At least you’re obedient. But you didn’t post any strange nonsense on SNS, did you?”

The reach of the internet in modern society was truly staggering.

Unlike the Murim, where people had to send messenger pigeons, wasn’t the standard around here for something to spread across the entire world with just a few movements of one’s fingers?

*It’ll be a pain in the ass if that bastard left some shit on there.*

And in response to my well-founded concern, Song Song casually cut in.

“Fortunately, there’s nothing much. I looked through everything just in case, and he’s only posted a ton of pictures of his own face.”

“Really?”

“Yeah. And most of his followers are from overseas. Men make up an overwhelming majority of them, too.”

“That’s a relief, but why are so many men following him—ah.”

An insight flashed through my mind.

I remembered whose hands had created the Skeleton King’s handsome face.

*Magic Johnson.*

The Grand Mage of the century. And the century’s gayest man.

The Skeleton King as he currently existed was the result of Magic Johnson’s taste being thoroughly reflected in his work—the very Magic Johnson who had performed unbelievable magic with two staffs.

He was handsome at a glance, but his face and physique were especially perfect for satisfying the needs of people in a certain niche.

And there were no fewer than a hundred and twenty thousand of them.

That was enough people to kick the asses of a hundred thousand practitioners of the Demonic Path, even if they came swarming back. Of course, I had to wonder whether kicking was all they would do.

*This guy was more impressive than I thought.*

To draw in that many followers in such a short time despite having no known name or face. Even the Murim Alliance Leader couldn’t do that.

Unaware of the way I was looking at him, the Skeleton King fiddled with his smartphone before opening his mouth with a mournful expression.

“I cannot bring myself to delete the account. You are the most wicked and cruel human in the world.”

“What crime did I commit in my previous life to deserve being called cruel by a monster bastard?”

“Ah, such a sudden parting. Some nameless woman who can no longer gaze upon this body’s dazzling face will surely shed endless tears.”

“……”

“What is with that strange expression?”

“Nothing. It’s better if you don’t know.”

Sometimes, the truth was more beautiful when left unrevealed.

After reaching a tacit agreement with Song Song through an exchange of glances, I looked around and spoke.

“Anyway, everyone agrees, right?”

Im Kkeokjeong nodded as though it were obvious.

“Well, if you and Team Leader Choi decided that’s what you’re going to do, I’ll follow along.”

“Song-i, what about you?”

“Hmm.”

Song Song crossed her legs at an angle and continued.

“From what I’ve heard, it’s ultimately something we’re doing for everyone. If I say I don’t want to, doesn’t that make me the only bitch here?”

“No.”

“Really?”

“Yeah. You were never particularly nice to begin with.”

“Oh, listen to this bastard.”

Song Song smiled sweetly and raised her middle finger before suddenly sighing.

“What a spectacle. When Team Leader Choi first offered me a transfer and I left the Ares Guild, I never imagined things would turn out like this.”

“You should’ve just stayed there.”

“Hey, I couldn’t. The Branch Leader was such a pervert that there was no way I could stay. I figured it would be better to work under someone young, handsome, and rich. But I had a bad feeling from the very first day, didn’t I?”

“The first day?”

“Yeah. I came here to get away from a pervert, but there was another weird bastard waiting for me. I was starving to death, and he burned every piece of meat he cooked. Then he suddenly announced that his zodiac sign was Taurus. Wasn’t he completely insane?”

“Ah-ha.”

I let out a short laugh and looked at her without saying anything else.

To be honest, I did feel sorry for Im Kkeokjeong and Song Song. Ever since the Peace Guild was founded, they had been forced to endure all sorts of turmoil they had never wanted.

“Hmm.”

“What’s with that reaction?”

“Nothing. I just wanted to tell you that it isn’t too late yet.”

“What?”

“This may be far more dangerous than you or Uncle Kkeokjeong think.”

Unlike usual, my voice held no trace of laughter. Song Song’s eyes grew serious.

“How dangerous are we talking?”

“We have to consider this beyond a domestic scale now.”

“You seem to have a tendency to underestimate yourself. You and Team Leader Choi left Korea behind a long time ago.”

That was an entirely accurate statement.

Ever since I took down the Arch Lich in China, my name had become known throughout the world. Meanwhile, Team Leader Choi had appeared in the media as the new City Lord of the Ares Guild and the successor to the living Savior.

But this was a different matter.

No, it was a problem created by everything we had achieved until now.

I shrugged.

“Someone once said that the bigger you get, the more there is to take a bite out of.”

“So how much are you planning to let people take from you?”

“I have no plans to let that happen. And I intend to keep it that way.”

Song Song stared at me for a moment before suddenly speaking.

“Do you know something?”

“What?”

“It’s already far too late for us to pull out. For both me and Uncle Kkeokjeong.”

Im Kkeokjeong quietly added to her words.

“I never intended to pull out in the first place.”

“Uncle.”

“Whether it’s too late or not doesn’t matter. Once you start something, you have to see it through to the end. At least for the sake of the one who left us first.”

“……!”

“Isn’t that right, Team Leader Choi?”

At Im Kkeokjeong’s quiet question, everyone’s gazes turned in one direction.

Team Leader Choi had fallen silent at some point. He was looking at the empty seat of someone who had been there.

A seat that had still held warmth until not long ago. The empty place left by someone who could no longer be replaced by anything.

Then he opened his mouth.

“I visited the grave today. Someone had carved words beside the gravestone. ‘Thank you for coming. I love you. Please come again.’”

No one said a word, and Team Leader Choi continued calmly.

“So next time, I’d like all of us to go visit that person together. Next year, the year after that……and even decades from now.”

It was the resolve of a man who had been forced to send someone precious on ahead.

The four words *all of us together* carried his determination not to let the same thing happen again.

*Decades from now.*

Yes. That was enough.

I didn’t know what we would look like then, but for now, the fact that we would move forward together was enough.

“Team Leader Choi.”

At my quiet call, he gave a heavy nod.

“Understood. Let’s begin.”

We had already worked out the broad strokes beforehand. Team Leader Choi took out his smartphone and called the first person.

Beep. Beep. Click.

The call connected before even three rings had sounded. A deep voice, honed by a hectic political life, came from the other end.

—You’ve reached me. This is Baek Hanseong.

There were plenty of people named Baek Hanseong in Korea. But in a situation like this, there was only one Baek Hanseong Team Leader Choi would contact first.

“Yes, Mr. President. I’m calling about something important.”

—Ha-ha. Well, putting it that way already makes me feel a little strange. I’m looking forward to it, but at the same time, I’m starting to feel uneasy.

At the appearance of a major figure who moved an entire country, Im Kkeokjeong and Song Song fell silent. The Skeleton King’s eyes widened as he whispered to me.

“If you mean President Baek Hanseong, then could it be that—”

“That’s right. Our country’s pres—”

“I know. Isn’t he the popular celebrity with more than ten million followers?”

“……”

“Damn it. A human has a hundred times this body’s following.”

As I watched the Skeleton King vent his frustration, I thought:

*Please just fucking die already…….*

Come to think of it, he already had.

* * *

The hallway was bright enough to dazzle the eyes. An A-rank Magic Gem filled with tremendous energy continuously supplied power to the entire building, while people filling every floor bustled about with their respective work.

At least, that was how things had been until sudden darkness descended.

Crackle. Whoooosh.

The light flowing from the ceiling lamps faded, and every machine stopped moving.

Confused shouts erupted from all around, shattering the momentary silence.

“What the hell is this?”

“Uh, it looks like a power outage.”

“Is that supposed to be an answer? No, fuck…… This is why I said we should replace the Magic Gem ahead of time. After sticking a straw in it and sucking it dry for more than twenty years, isn’t it practically begging us to put it out of its misery?”

“That’s what I thought, too. The experts said an A-rank Magic Gem would last at least thirty years.”

“So what, does it matter why the Magic Gem ran out ten years early? Are you so curious you’re about to go insane?”

“N-No, sir.”

“Enough. Everyone, focus! The Security Team and Technical Team will be here within two minutes, so don’t move a finger—stay exactly where you are! Anyone with spare mana lanterns, go get them right now.”

But despite the department head’s shout, the entire building lit up again before even a minute had passed. The power had returned.

“Damn it. They’ve got us running around in circles……”

The department head grumbled before waving away the Security Team, who had arrived a step too late.

“Ah, as you can see, everything’s fine. What caused the sudden outage?”

“I asked our team leader, too, and apparently it happens once every few years, although it’s rare. The Technical Team will have to investigate to find the exact cause.”

“Well, I suppose that’s their department.”

The Security Team Hunter gave an awkward smile and checked several things.

Whether anything had gone missing during the blackout. Whether anyone had been injured. Whether anyone had noticed anything suspicious during the incident, and so on.

But it was little more than a simple procedure, and there were mountains of work waiting to be handled. No one had the time or energy to devote to a blackout that had lasted barely a minute.

“Sorry, but if you have anything else to ask, can’t you do it later? Things are a little hectic for us right now.”

The Security Team employee nodded at the department head’s words.

“That shouldn’t be a problem. But you’re all much busier than usual. Did something happen?”

“A notice came down from above. Apparently, something big is going to happen sometime today.”

“Something big?”

“Yeah. We don’t know the details either, but it seems to have come down from the Blue House. Everyone’s on high alert because of it. At this rate, there’s no chance we’ll be leaving on time.”

“Oh dear. I took up your time for nothing.”

“It’s not that serious. We’re all working for the country, after all. Take care, and I’ll see you later.”

“Yes, you too.”

But as they returned to their respective positions, none of them knew.

During that short span of less than a minute, some ghostlike entity had moved through every part of the building, riding the thick darkness.

And that one item had disappeared from the evidence storage room deep underground.

The hundreds of employees going about their work, the highly skilled Hunters of the Security Team, and even the alarm magic had failed to notice.

The entity that had completed everything with ease leisurely slipped out of the building.

Step. Step.

Along with someone’s footsteps.

“Sehwan, did you check the third floor?”

“Yes, Team Leader. There were no problems. What did the Technical Team say?”

“It hasn’t even been ten minutes. Do you really think they’ve already found the cause?”

“That’s true. By the way, isn’t the weather really nice today?”

Sssrk.

A dark shadow stirred faintly behind the Security Team employee as he chatted idly with his superior.
```

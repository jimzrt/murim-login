<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0558.txt",
      "sha256": "c8e83fac80e090d65189cab0692ed525756f410c1b7d77cc07ad7ee92f97b609",
      "bytes": 14671
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4a1b69349cf1504eeb254503f9dada24d16f41fe822b3d2ab3532183fab6e92b",
      "bytes": 4585
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e722dc8fe0a74c5462125c55c13dcd103df843b96ce9e356227b1e742b88dde1",
      "bytes": 176766
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7fdbd090ef9381a2189e894d1c8f0f7deb8f62b5df04bde530cb2778ed3c380e",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "2eae724e98849dc3ec984d6456add73648c933ad52b65369142b0bd5f9734648",
      "bytes": 667
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "1def262f563bcf42df627b47a778d6dea618031e7ab0a8603681fc30cb64886f",
      "bytes": 698
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "f7b58dab459ad3c4ac5806308db638e2180016233a54a9084b28e4191bf72b1a",
      "bytes": 2367
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "78c9ec17f310becdc3c19c00a07efaa320b4fc3afaa3a486014b303e59c32a98",
      "bytes": 2292
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "daa114b6272ba1b8294132f38a64a0dd08f40d032024b3746163e97c053bbe72",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "9767365c03c5a60e55c742d43666dd42515f298195fd8162fd5f583c1e62cab7",
      "bytes": 1182
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "55f27ac9db835fa61bb65587d6efaf8c186cc4deefe27449d07862e2d7ac3dfe",
      "bytes": 770
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61693795214a59a9409884bd5cc353de2fc1d37ea4cc5382d289182b76afcd28",
      "bytes": 168779
    }
  ],
  "estimated_tokens": 12566
}
-->

# Durable State Update — Chapter 558

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 558. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 558. Profile updates may replace only one
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
  "chapter": 558,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 558,
    "continuity_sources": [558],
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
    "The Fire Dragon Pavilion’s six-member first mission is to enter Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can’t Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, and leadership of the Fire Dragon Pavilion’s first mission to Nanman.",
    "Mungyeong ended Taekyung’s direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven’s second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam’s transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon’s remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho’s dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi’s mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Lee is being honored as a Great Cataclysm hero, while Taekyung knows the actual deaths were caused by him.",
    "Go Jun is now Ares Guild’s Vice Guild Master and chief mourner for Lee Jungryong, with dozens of A-rank Hunters serving as his new subordinates; he intends to preserve Lee’s legacy and regards Jin Taekyung and Choi Minwoo as its enemies.",
    "Team Leader Choi deliberately revealed his connection to Cheon Taemin as the old hero’s only living blood relative and intends to acquire the Ares Guild with its influence intact before removing Lee’s corruption.",
    "Go Jun possesses a battered necklace recovered from the ruins of the Arch Lich’s former stronghold; it is not Lee Jungryong’s keepsake, but Go Jun bribed an investigation leader to obtain it because he considers it meaningful.",
    "In the Mutated Gate’s Forest of Giants, Taekyung has destroyed many corrupted Ents and is attacking the Level 130 Named Monster ‘Red Eye’ Cyclops, while the Skeleton King battles Ents and twenty low-level Hunters remain unconscious inside his reinforced bone barrier."
  ],
  "continuity_sources": [
    557,
    556
  ],
  "open_questions": [
    "What is the Lord of Heaven’s identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung’s party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo’s political engagement end?",
    "What process created Jang Sam’s mutant form, whether Dark Heaven’s mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What did Lee Jungryong leave Go Jun beyond his dying wish, what is the necklace recovered from the Arch Lich’s ruins, and what is the outcome of the battle against the Red Eye Cyclops?"
  ],
  "safe_through": 557,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can’t Go to Nanman.",
    "Render 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant’s Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, and 치코리타 as Chikorita; retain the established renderings for Small Cataclysm, Arch Lich, Skeleton King, Forest of Giants, Cyclops, and Ent."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 송송이    | **Song Song**     |
| 이정룡    | **Lee Jungryong** |
| 상태               | **Status**                     |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 탱커      | **tank**              |
| 힐러      | **healer**            |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 황소자리 | **Taurus** | Zodiac sign Song Song uses as a nickname for Taekyung. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 국가장 | **national funeral** | State funeral held for Lee Jungryong. |
| 이승엽 | **Lee Seungyeop** | Hunter whose autograph the Team Leader requests. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 힐러 | 진태경 | healer addressing the rescuer who stabilized the survivor | sir | deferential and grateful | The healer thanks Jin as 선생님 after witnessing his rescue and treatment. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 557
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 550
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 521
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 303
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild; attacked by three Black Hunters following a solo drinking outing, with both arms severed below the elbows; his wounds were treated with high-ranking healer recovery magic and advanced potions, his arms were reattached, and he regained consciousness after three days; he has chosen to continue as a Hunter and remain with the Peace Guild after recovering; after beginning the Jin Family’s Cultivation Technique, he completed a complete circulation and learned to perform the Small Circulation independently on the first day, adapting unexpectedly quickly; repeated circulation is expected to improve his physical foundations, and resolving his trauma may allow an early return to Guild work
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 556
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, and now serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion while holding its unique Title, Fire Dragon Pavilion Master and leading its first mission to Nanman.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 556
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 555
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 303
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; B-rank healer whose buff magic is powerful enough to be mistaken for an A-rank healer's
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild; rejected Taekyung’s confession without changing her attitude for money or fame, then accepted a same-age friendship and guildmate relationship with him.

## Korean source

```text
＃558화



번쩍.

남자는 불현듯 눈을 떴다. 몽롱한 눈동자가 허공을 응시하길 잠깐. 그는 천천히 지나간 기억을 되짚기 시작했다.

‘F급 게이트, 고블린, 지진, 그리고…….’

진태경.

모든 것을 일깨우는 마지막 키워드에, 마침내 모든 기억을 떠올린 남자가 누워 있던 자리에서 용수철처럼 튕겨 올랐다.

“으어어어!”

한 가지 문제는, 탱커답게 큰 체격을 지닌 남자가 요란하게 움직이기에는 공간이 그리 넓지 않다는 것이었다.

벌떡. 쾅!

“으억! 어?”

천장에 머리를 박은 남자가 비명을 지르다 말고 눈을 동그랗게 떴다.

아프다. 진짜 아프다. 하지만 고통을 느낀다는 것은…….

‘사, 살았다!’

웹소설 주인공이나 하던 생각을 자신이 하게 될 줄이야.

비로소 긴장의 끈이 탁 풀린 남자는 그제야 자신이 누워 있던 곳이 차량 내부라는 것을 깨달았다. 정확히는, 구급차.

‘구급차라니.’

죽음의 위기에서 벗어난 것은 다행이지만, 과히 좋은 징조는 아니다. 살아난 대신 불구가 되었다면 그 또한 불행이니까.

퍼뜩 정신을 차린 남자가 정신없이 자신의 전신을 살피고 있던 그때였다.

벌컥. 드르륵.

활짝 열린 문과 함께 쏟아지는 빛에, 남자는 두 팔로 얼굴을 가렸다.

아니, 어쩌면 그건 문을 연 여자의 눈부신 미모 때문인지도 모른다.

“아, 일어나셨구나. 어쩐지 지나가는데 무슨 소리가 들리길래.”

남자는 갑작스럽게 등장한 미인을 향해 더듬더듬 입을 열었다.

“누, 누구세요?”

“이승엽 팀장님, 맞죠? 소속 길드 없는 프리 상태시고, 나이는 서른셋.”

“저, 절 어떻게 아십니까?”

“아, 질문은 잠시 후에. 우선 몸은 괜찮으시죠?”

부드러우면서도 단호하게 말을 가로막는 태도에, 남자는 엉겁결에 고개를 끄덕였다.

“하긴, 괜찮을 거예요. 부상이라고 하기에도 민망할 정도의 찰과상이 전부였으니까. 다른 분들도…….”

다른 분들?

흘리듯 언급한 그 단어에, 남자의 눈이 번쩍 뜨였다.

“그, 그렇지! 우리 팀원들! 팀원들은 무사합니까? 혹시 죽거나 다친 사람 없어요?”

“음. 팀원분들은 모두 무사한데, 그렇게 소리 지르시면 제 귀가 무사하지 못하겠죠?”

“정말입니까? 크흑, 정말 사실이에요?”

“제가 아는 어떤 사람은 이럴 때 꼭 더러운 뭔가를 걸던데. 전 불알이 없으니까 난소를 걸게요. 됐죠?”

쿨내가 진동하는 대답과 함께 목소리가 이어졌다.

“그리고 앞의 질문에 대답하자면, 소지품을 봤어요. 덕분에 가장 빨리 신분 확인 절차가 끝났고요.”

툭.

그녀가 내려놓은 것은 소형 아공간 포켓(Pocket)과 브리핑용 보드판이었다.

새하얀 표면에는 개발새발인 글씨체로 짤막한 사인이 적혀져 있었다.



이승엽 헌터님 파이팅

-진태경-



미인이 피식 웃었다.

“사실 그건 떨어져 있던 건데, 어떤 사람이 직접 건네주더라고요. 한 집안의 가보가 될 물건인데 잃어버리면 안 된다고.”

남자, 이승엽 팀장이 눈을 크게 떴다.

“예에? 그럼 이걸 전해 준 분이 혹시…….”

“지금 머릿속에 떠오른 이름이 있다면, 정답.”

잔털 하나 없이 가지런한 눈썹이 들썩였다. 이목구비처럼 시원시원한 목소리가 뒤를 이었다.

“아, 그러고 보니 자기소개가 늦었네요. 전 송송이라고 합니다.”

“예? 뭔 송이요?”

“……그냥 처음부터 명함을 주는 게 빠르겠네. 여기요.”

슥.

길고 새하얀 손가락에 들린 명함을 받아 든 팀장이 눈을 크게 떴다.

“평화 길드?”

“정식 직함은 힐러팀 팀장이죠. 임시지만 긴급 구조팀을 맡고 있기도 하고.”

“……헙.”

팀장은 헛숨을 삼켰다. 제아무리 먹고 사느라 바쁜 그라고 해도 평화 길드가 어떤 곳인지는 충분히 알고 있었다.

‘모르면 몬스터지.’

다른 사람도 아닌 바로 그 진태경이 속한 길드가 아닌가.

엄청난 자본력과 세간의 관심을 끌어모을 화제성으로 몇 달 사이 급격한 성장을 이룩한 평화 길드는 더 이상 고만고만한 중소 길드가 아니었다.

‘요새는 평화 길드가 아레스 길드보다 들어가기 힘들다던데.’

헌터 대우도 업계 최상위권인 데다, 앞으로의 성장 가능성도 무궁무진한 블루칩이니 인재들이 쏠리는 건 당연했다.

일주일 전 이정룡의 국가장이 치러진 뒤에는 무려 그 아레스 길드의 헌터들도 계약을 연장하는 대신 평화 길드로 이적했다고 했다.

그런데 눈앞의 미인이 그 평화 길드의 팀장급이라니. 기껏해야 20대로 보이는 나이에 비해 상당한 거물인 셈이다.

다시 생각해 보니 그녀의 연예인 같은 얼굴은 TV에서 한두 번 본 것 같기도 했다.

“그런데…… 긴급 구조팀은 뭡니까? 아직 들어 본 적이 없어서요.”

“말 그대로예요. 긴급 구조팀. 오직 사람들을 구조하는 목적으로 이번에 신설된 곳이죠.”

“어느 정도 되는 길드가 구조팀을 갖춘 건 압니다. 하지만 저나 제 팀원들은 평화 길드 소속도 아닌데요.”

프리랜서 헌터나 소규모 길드는 정부 부처 소속의 도움을 받지만, 중견 길드만 되어도 자체적으로 구조팀을 운용한다는 것은 상식. 난데없이 평화 길드가 나타났다는 게 언뜻 이해가 가지 않았다.

“혹시 마음에 안 드세요?”

“아, 아니요. 제가 어떻게 감히 그런 생각을. 당연히 너무나 감사하죠. 변이 게이트에 휘말려서 죽을 뻔한 걸 구해 주셨는데.”

송송이가 피식 웃었다.

“그럼 해결됐네요. 그러려고 저희가 온 거니까.”

“예?”

“우리 평화 길드 긴급 구조팀은 수도권에 존재하는 중, 하급 게이트를 위주로 시범 운용 중이에요. 정부 부처와 협력 관계에 있고, 모든 헌터들을 대상으로 실시하고 있죠. 굳이 말하자면 공공의 안전을 위한 자원봉사라고 해야 하나.”

“자원……봉사요?”

“아, 물론. 저나 다른 분들은 급여 받고 하는 거지만요.”

눈을 휘둥그레 뜬 그는 송송이의 어깨너머를 바라보았다.

지금도 사방을 바쁘게 오가는 많은 헌터들. 그들의 가슴에는 하나같이 평화 길드의 앰블럼이 달려 있었다.

‘자원봉사? 이렇게 많은 인력을 동원해서?’

현대의 헌터 길드가 제아무리 황금알을 낳는 거위라고 해도 그 수입원 대부분은 결국 게이트에서 나오는 것.

그렇기에 길드는 엄청난 연봉을 줘 가며 헌터들을 고용하고, 게이트에서 그 이상의 이익을 창출해 낸다.

한데 평화 길드는 그들을 레이드가 아닌 구조 목적으로 파견한 것이다. 그것도 알맞은 수당까지 지급하면서.

‘다들 최소 중급 헌터는 되어 보이는데.’

척 보기에도 비싸 보이는 장비를 차려입은 헌터만 수십이다.

평화 길드가 오늘 하루 저들에게 지급한 금액이 어느 정도일지, 하급 헌터인 그로서는 짐작하기 어려웠다.

“저어. 송송이 팀장님이라고 하셨죠.”

“네. 말씀하세요.”

“그…… 다름이 아니라요. 혹시 치료비나 구조비, 그런 게 있습니까?”

“없죠. 소방관이 시민 구해 주고 요금 청구하는 거 보셨어요?”

“그럼?”

“당연히 이송부터 치료까지 전부 무료. 아, 정신적으로 다치신 분이 계시면 심리 상담 치료도 지원해 드리고 있어요. 트라우마 그런 거.”

“……?”

잠깐만. 뭔 치료? 내가 잘못 들었나?

넋이 나간 표정으로 송송이를 빤히 바라보던 그가 진심을 담아 물었다.

“아니. 평화 길드는 땅 파서 운영합니까?”

송송이가 눈을 찡긋했다.

“그건 아니고, 저희 물주님이 돈이 좀 많거든요.”

“물주님?”

“아실 텐데. 이미 직접 사인도 받으셨고.”

“……!”

“어쨌든 있어요, 그런 사람이. 말로는 매일 피가 빨리는 것 같다고 투덜거리면서 입은 웃고 있는.”

한 사람을 떠올린 송송이의 입가에 웃음이 맺혔다.

사실 처음 만났을 때만 해도 뭐 이런 미친놈이 있나 싶었는데…… 옆에서 지켜보며 알게 되었다.

진정한 의미의 헌터가 무엇인지. 사람 냄새라는 것이 무엇인지.



‘너, 나랑 일 하나 하자.’

‘……어디서 많이 들어 본 대사 같은데. 우선 내가 화교가 아니라는 것만 알아 둬.’



일주일 전, 진태경이 대뜸 찾아와 건넨 한마디다.

골드문, 아니 아레스 길드에 들어가 첩자 짓이라도 하라는 건가 잠깐 생각했지만, 이어진 이야기는 그녀의 예상을 완전히 빗나갔다.



‘생각보다 제법이네, 황소자리.’



조금 더 솔직히 말하자면, 이번에는 좀 멋졌다.

블랙 와이번의 사체를 판 돈으로 기부 재단을 설립했을 때도 마찬가지였다. 녀석은 가끔 이렇게 뜻밖의 모습을 보여 주고는 했다.

피식.

실소를 흘린 송송이가 문득 고개를 돌려 하늘을 바라보았다.

아직 추위가 가시지 않은 1월. 그러나 머리 위로 비추는 햇볕은 따스했다.



* * *



키이이잉.

- 진태경 님. 홍채 인식이 완료되었습니다.

동공을 스치는 붉은빛과 함께 흘러나오는 기계음.

자동으로 열린 문을 열고 길드 하우스에 들어가자, 각자 할 일을 위해 움직이던 사람들이 약속이라도 한 것처럼 발걸음을 우뚝 멈췄다.

“오, 오셨습니까.”

“오셨습니까!”

“고생하셨습니다!”

“아, 네. 다들 안녕하세요.”

이런 거 하지 말라니까. 무슨 조폭 사무실도 아니고.

도저히 익숙해지지 않는 광경에 어색하게 웃는 내게, 스켈레톤 킹이 속삭였다.

“간악한 인간이여. 이건 좀 아닌 것 같다.”

“네가 웬일이냐. 그런 생각도 다 하…….”

내 말이 끝나기도 전에 성큼 걸음을 내디딘 스켈레톤 킹이 신입으로 보이는 헌터를 지목했다.

“거기 너, 허리 각도가 80도밖에 되지 않는다. 90도까지 낮추도록. 아니면 그랜절을 시도하는 것도 좋은 방법이다.”

“예, 옙! 알겠습니다!”

“…….”

네 맘대로 각도 조절하지 마. 그리고 알긴 뭘 알아.

보는 것만으로도 기가 차는 광경이다.

나는 그랜절을 시도하려는 길드원을 만류하고, 이 병신의 말을 귀담아듣지 말라는 친절한 조언을 한 뒤에야 목적지로 향할 수 있었다.

그리고 그곳에는 익숙한 얼굴들이 나를 기다리고 있었다.

“태경아!”

“오셨습니까.”

양팔을 활짝 벌리며 환영하는 임꺽정과 뭔가를 바쁘게 처리하는 최 팀장님이 바로 그들이다.

“진정하세요, 진정. 상처 덧나면 어쩌시려고.”

“반가워서 그렇지, 인마.”

“매일 보는 얼굴인데요, 뭘.”

아직 재활 훈련 중인 임꺽정을 자리에 앉히자마자, 최 팀장이 불쑥 입을 열었다.

“핫라인으로 보고받았습니다. 네임드 몬스터가 출몰했다고요?”

“사이클롭스였어요. 엔트 삼백 마리는 덤이고.”

“F급 게이트에 사이클롭스라…… 때마침 진태경 씨가 주위에 있었던 게 천운이었군요.”

스켈레톤 킹이 거드름을 피우며 말했다.

“모두 이 몸의 위엄 앞에 무릎을 꿇었지.”

“한마디만 더 하면 무릎 꿇은 채로 들을 줄 알아라.”

“……미안하다.”

단 한마디로 녀석의 입을 닥치게 만든 내게, 최 팀장이 서류철 하나를 내밀었다.

“이건?”

“지난번 부탁하신 자료입니다. 최근 국내를 포함한 아시아에서 발생한 변이 게이트 건수를 집계했습니다.”

서류철을 살펴보는 데에는 그리 오랜 시간이 소요되지 않았다.

잠시 후, 원하는 내용을 모두 확인한 내가 신음처럼 중얼거렸다.

“지난 한 달 동안 국내에서만 다섯 번…….”

“변이 게이트 발생 확률이 폭발적으로 증가하는 추세입니다. 쓰촨성에서의 일이 대표적이고요.”

변이 게이트는 희박한 확률로 일어난다.

수백 개가 넘는 게이트가 존재하는 대한민국에서조차 일 년에 한두 번, 많아 봤자 세 번을 넘지 않는데 지난달에만 벌써 다섯 번을 넘겼다.

‘이번 달은 조금 전 처리하고 온 것까지 포함해서 벌써 두 번이고.’

도무지 설명할 수 없는 기이한 현상.

그러나 지금 이 순간, 머릿속에 무림에서의 일이 떠오르는 것은 결코 우연이 아닐 것이다.

‘뭔가 벌어지고 있다.’

툭. 툭툭.

말없이 손가락으로 테이블을 두드리던 내가 물었다.

“북미나 유럽 쪽 상황은 어떻습니까?”

“제 예상에 따르면 비슷할 겁니다. 하지만 보다 확실한 정보를 위해, 믿을 만한 분께 자료를 요청했습니다.”

“믿을 만한 분?”

최 팀장님께 반문한 다음 순간. 나는 모든 감각이 깨어나는 것을 느꼈다.

콰아아아.

갑작스러운 기의 폭풍.

A급 헌터조차 아득히 넘어서는 막대한 마나가 길드 하우스 어딘가를 향해 집약되고 있었다.

‘이건.’

익숙하다. 마나의 흐름도. 그리고 마나에서 느껴지는 누군가의 특징도.

“최 팀장님, 설마?”

“생각하시는 그분이 맞습니다. 직접 오실 줄은 몰랐지만요.”

담담한 최 팀장의 대답에, 스켈레톤 킹이 어리둥절한 얼굴로 내게 물었다.

“간악한 인간이여. 누굴 말하는 것이냐?”

“니 아빠.”

“……?”

의문도 잠시. 모두의 뇌를 파고드는 누군가의 메시지 마법에, 스켈레온 킹의 얼굴에 웃음이 번졌다.

- 다들 잘 지냈나?

힙합 소울과 그루브가 느껴지는 목소리. 피식 웃은 나는 한 사람을 떠올렸다.

‘매직 존슨.’

미국의 대마도사가 평화 길드에 방문했다.
```

## Final English reading copy

```markdown
# Chapter 558

*Flash.*

The man suddenly opened his eyes.

For a moment, his dazed gaze stared blankly into the air. Then he slowly began retracing the memories that had passed.

*An F-Rank Gate, goblins, an earthquake, and…*

*Jin Taekyung.*

At that final keyword, which brought everything rushing back, the man remembered it all. He sprang up from where he had been lying like a released spring.

“Gaaaaah!”

There was just one problem: the space wasn’t very large, and the man had the kind of massive build expected of a tank.

*Thump. Bang!*

“Gah! Huh?”

After hitting his head on the ceiling and crying out, the man stopped and opened his eyes wide.

It hurt. It really hurt.

But feeling pain meant…

*I-I’m alive!*

He never thought he would be having the kind of thoughts usually reserved for webnovel protagonists.

Only after the tension finally drained out of him did the man realize that he had been lying inside a vehicle.

More precisely, an ambulance.

*An ambulance?*

Escaping the brink of death was fortunate, but it wasn’t exactly a good sign. If he had survived only to become disabled, that would be a misfortune too.

The man hurriedly came to his senses and began checking his entire body.

That was when—

*Bang. Rattle.*

The door flew open, and light poured in. The man covered his face with both arms.

Or perhaps the dazzling beauty of the woman who had opened the door was the real reason.

“Oh, you’re awake. I heard a strange noise while I was passing by.”

The man opened his mouth toward the beautiful woman who had appeared without warning.

“W-Who are you?”

“You’re Team Leader Lee Seungyeop, right? You’re a free agent with no Guild affiliation, and you’re thirty-three.”

“H-How do you know that?”

“Questions later. First, are you feeling all right?”

Her tone was gentle but firm enough to cut him off. The man reflexively nodded.

“Though you should be fine. All you had were abrasions—barely enough to call them injuries. The others…”

*The others?*

At that casually mentioned word, the man’s eyes snapped wide open.

“R-Right! My team! Are my team members all right? Did anyone die? Is anyone hurt?”

“Hmm. Your team members are all safe, but if you keep shouting like that, my ears won’t be.”

“Really? Are you sure? Guh, is that really true?”

“I know someone who always stakes something dirty in situations like this. I don’t have any testicles, so I’ll stake my ovaries. Does that work?”

Her answer radiated such effortless cool that her voice continued without pause.

“And to answer your earlier question, I checked your belongings. Thanks to that, we were able to complete your identity verification quickly.”

*Tap.*

What she set down was a small extradimensional Pocket and a briefing board.

A short message had been scrawled across the brilliant white surface in atrocious handwriting.

<br>

**Go, Hunter Lee Seungyeop!**

—Jin Taekyung

<br>

The beautiful woman quietly laughed.

“Actually, that had fallen on the ground, but someone personally handed it to me. He said it was something that would become a family heirloom, so you absolutely couldn’t lose it.”

Team Leader Lee Seungyeop’s eyes grew wide.

“Really? Then the person who gave it to you was…”

“If a certain name just came to mind, that’s the correct answer.”

Her neatly arranged eyebrows lifted. Her voice was as clear and refreshing as her features.

“Oh, come to think of it, I’m late introducing myself. I’m Song Song.”

“Song? What kind of song?”

“…”

“It’d be faster to give you my business card from the start. Here.”

*Swish.*

The Team Leader accepted the business card held between her long, pale fingers and opened his eyes wide.

“Peace Guild?”

“My official title is Healer Team Leader. I’m also temporarily in charge of the emergency rescue team.”

“…”

The Team Leader swallowed a breath.

No matter how busy he was making a living, he knew enough about the Peace Guild.

*You’d have to be a monster not to know.*

It was the Guild that none other than Jin Taekyung belonged to.

With its enormous financial resources and the kind of buzz that drew public attention, the Peace Guild had grown explosively within a few months. It was no longer some unremarkable small or medium-sized Guild.

*I heard it’s harder to get into the Peace Guild than Ares Guild these days.*

The Guild offered some of the best treatment in the industry, and its potential for future growth was limitless. Naturally, talent flocked to it.

After Lee Jungryong’s national funeral a week earlier, he had even heard that Hunters from Ares Guild had transferred to the Peace Guild rather than renew their contracts.

And the beautiful woman in front of him was a team leader-level figure in that Peace Guild.

For someone who looked barely into her twenties, she was quite a major figure.

Now that he thought about it, her celebrity-like face seemed familiar too. He might have seen her once or twice on television.

“But… what exactly is the emergency rescue team? I haven’t heard of it before.”

“Exactly what it sounds like. An emergency rescue team. It was newly established for the sole purpose of rescuing people.”

“I know that Guilds of a certain size have rescue teams. But neither my team nor I belong to the Peace Guild.”

Freelance Hunters and small Guilds received help from government agencies, while it was common knowledge that even medium-sized Guilds operated their own rescue teams.

He couldn’t quite understand why the Peace Guild had suddenly appeared.

“Does that bother you?”

“N-No. How could I possibly think that? Of course I’m extremely grateful. You saved us when we were about to die after being caught in a Mutated Gate.”

Song Song quietly laughed.

“Then that settles it. That’s why we came.”

“What?”

“Our Peace Guild emergency rescue team is being piloted primarily at medium- and low-grade Gates in the capital region. We’re working with government agencies, and the service is available to all Hunters. If I had to put it simply, you could call it volunteer work for public safety.”

“Volunteer… work?”

“Of course, I and the others are getting paid.”

He opened his eyes wide and looked over Song Song’s shoulder.

Even now, dozens of Hunters were moving busily in every direction. Every one of them wore the Peace Guild emblem on their chest.

*Volunteer work? With this many people?*

No matter how much of a golden goose a modern Hunter Guild was, most of its income ultimately came from Gates.

That was why Guilds paid Hunters enormous salaries and then generated even greater profits from Gates.

But the Peace Guild had sent these people out not for raids, but for rescue work.

And it was even paying them appropriate compensation.

*They all look like at least mid-grade Hunters.*

There were dozens of Hunters dressed in equipment that looked expensive at a glance.

As a low-grade Hunter, he had no way of guessing how much the Peace Guild had paid them all today.

“Um. You said your name was Team Leader Song Song, right?”

“Yes. Go ahead.”

“Th-There’s something I wanted to ask. Are there any treatment fees or rescue fees or anything like that?”

“There aren’t. Have you ever seen a firefighter rescue a citizen and then send them a bill?”

“Then…?”

“Obviously, everything from transportation to treatment is free. Oh, and if anyone has suffered psychological injuries, we also provide counseling. Trauma and things like that.”

“…”

*Wait a minute. What kind of treatment? Did I hear that right?*

He stared blankly at Song Song before asking with genuine feeling,

“Does the Peace Guild run on money it digs out of the ground?”

Song Song gave him a playful wink.

“Not exactly. Our patron has quite a lot of money.”

“Your patron?”

“You must know who I mean. You even got his autograph.”

“…”

“Anyway, there’s someone like that. He complains every day that he feels as though he’s being bled dry, but he keeps smiling.”

A smile formed at the corner of Song Song’s mouth as she thought of him.

When she had first met him, she had wondered what kind of lunatic he was.

But after watching him from nearby, she had come to understand.

What it meant to be a true Hunter.

What it meant to have a human heart.

<br>

*You. Let’s do a job together.*

*…That sounds like a line I’ve heard somewhere before. First, just know that I’m not ethnic Chinese.*

<br>

That was what Jin Taekyung had suddenly said to her a week ago.

For a moment, she had wondered whether he was asking her to join Gold Moon—or rather, Ares Guild—and work as a spy.

But what he said next was nothing like what she had expected.

<br>

*You’re better than I expected, Taurus.*

<br>

To be a little more honest, he had been kind of cool this time.

It had been the same when he used the money from selling the Black Wyvern’s carcass to establish a charitable foundation.

Every now and then, he showed her an unexpected side of himself.

*Heh.*

Song Song let out a quiet laugh, then suddenly turned her head toward the sky.

It was January, and the cold had not yet faded.

But the sunlight shining down from overhead was warm.

* * *

*Kiiiiing.*

—Jin Taekyung. Iris recognition complete.

A red light swept across my pupil as the mechanical voice rang out.

I stepped through the automatically opened door and entered the Guild House.

Everyone who had been moving around to handle their own work stopped dead, as though they had planned it together.

“W-Welcome.”

“Welcome!”

“Thank you for your hard work!”

“Ah, yes. Hello, everyone.”

*I told them not to do this. What is this, a gangster office?*

I gave an awkward smile at the sight I still couldn’t get used to. The Skeleton King whispered beside me.

“Wretched human. This seems somewhat inappropriate.”

“You, of all people? You have thoughts like that too—”

Before I could finish speaking, the Skeleton King strode forward and pointed at a Hunter who looked like a new recruit.

“You there. You’re only bending eighty degrees at the waist. Make it ninety. Or you could try a grandjeol.[^1]”

[^1]: A comically exaggerated form of the Korean full bow, often performed with the body inverted.

“Yes, yes! Understood!”

“…”

*Don’t adjust the angle however you feel like it. And what exactly do you understand?*

It was enough to make me lose my mind just by looking at it.

I stopped the Guild member from attempting a grandjeol and kindly advised him not to take anything this idiot said seriously. Only then was I able to head toward my destination.

And familiar faces were waiting for me there.

“Taekyung!”

“Welcome.”

The first was Im Kkeokjeong, who was welcoming me with both arms spread wide. The second was Team Leader Choi, who was busy handling something.

“Take it easy, Kkeokjeong hyung. Take it easy. What if you reopen your wounds?”

“I’m just happy to see you, punk.”

“We see each other every day.”

As soon as I sat Im Kkeokjeong down—he was still undergoing rehabilitation training—Team Leader Choi suddenly spoke.

“I received a report over the hotline. A Named Monster appeared?”

“It was a Cyclops. With three hundred Ents thrown in for free.”

“A Cyclops in an F-Rank Gate… It was a stroke of luck that Mr. Jin Taekyung happened to be nearby.”

The Skeleton King spoke with exaggerated dignity.

“They all knelt before this body’s majesty.”

“One more word, and you’ll learn to listen while kneeling.”

“…Sorry.”

That single sentence was enough to shut him up.

Team Leader Choi handed me a folder.

“What’s this?”

“The material you asked for last time. I compiled the number of Mutated Gates that have appeared recently in Korea and throughout Asia.”

It didn’t take long to look through the folder.

A short while later, after confirming everything I wanted to know, I muttered like a groan,

“Five times in Korea alone over the past month…”

“The probability of Mutated Gates appearing is rising explosively. The incident in Sichuan Province is the most notable example.”

Mutated Gates occurred with an extremely low probability.

Even in Korea, where more than several hundred Gates existed, they appeared only once or twice a year—three times at most.

But there had already been more than five last month.

*And this month, it’s already happened twice, counting the one I just dealt with.*

It was a bizarre phenomenon that defied explanation.

But there was no way it was a coincidence that events in the Murim had come to mind at this exact moment.

*Something is happening.*

*Tap. Tap-tap.*

I tapped my fingers against the table without saying anything, then asked,

“What’s the situation in North America and Europe?”

“Based on my expectations, it should be similar. But I requested data from someone reliable to obtain more certain information.”

“Someone reliable?”

The moment after I asked Team Leader Choi that question, I felt every one of my senses snap awake.

*Whoooooosh.*

A sudden storm of energy.

An enormous amount of mana—far beyond even an A-rank Hunter—was converging somewhere inside the Guild House.

*This is…*

I knew it.

The flow of mana.

And the distinctive presence I could sense within it.

“Team Leader Choi, don’t tell me…”

“It’s the person you’re thinking of. I didn’t expect him to come in person, though.”

At Team Leader Choi’s calm answer, the Skeleton King turned to me with a bewildered expression.

“Wretched human. Whom are you talking about?”

“Your dad.”

“…”

The confusion lasted only a moment.

As someone’s message magic burrowed into everyone’s minds, a smile spread across the Skeleton King’s face.

—Have you all been doing well?

The voice carried a distinct hip-hop soul and groove.

I quietly laughed and thought of one man.

*Magic Johnson.*

The American Grand Mage had come to visit the Peace Guild.
```

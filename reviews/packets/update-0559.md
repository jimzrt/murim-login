<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0559.txt",
      "sha256": "fb2161fe049a9146f2d4b87a35d31ef68b879bf549a808830c455d485588e86c",
      "bytes": 13030
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2296d8fb1db28c9590c943a844d75149cae05398515bcc479c667ff868d3d5ff",
      "bytes": 4596
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "02b867d32eb3b50254ba4edafb970edb2018fc4f24d45aada585b4809a4ca201",
      "bytes": 176933
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "8b7f17187b08a2b186b9e9eb16a1e430df493dcdeca866a35866cbecf495aa7e",
      "bytes": 2367
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "774cdd81f53dda56f8db4911626ecb859d75c58a0c27dd1c72fd9f61961074ba",
      "bytes": 2280
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d777ec6c089a1cfd348a9decc2ba6d656eebfd00893108b87ef79d8cf2ddca40",
      "bytes": 622
    },
    {
      "path": "characters/Lee Jungryong.md",
      "sha256": "22a0794202ac3405029f3587c1873b47caf9051693920e89e696b6df7ce36a24",
      "bytes": 1182
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b402b24ed992548494e4379bcad6f7a24180e65e1a18410b9643c2d1f3394ba2",
      "bytes": 169730
    }
  ],
  "estimated_tokens": 11080
}
-->

# Durable State Update — Chapter 559

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 559. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 559. Profile updates may replace only one
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
  "chapter": 559,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 559,
    "continuity_sources": [559],
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
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, leadership of the Fire Dragon Pavilion’s first mission to Nanman, and the Peace Guild’s modern-world patronage.",
    "Mungyeong ended Taekyung’s direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven’s second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam’s transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon’s remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho’s dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi’s mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Lee is being honored as a Great Cataclysm hero, while Taekyung knows the actual deaths were caused by him.",
    "Go Jun is now Ares Guild’s Vice Guild Master and chief mourner for Lee Jungryong, with dozens of A-rank Hunters serving as his new subordinates; he intends to preserve Lee’s legacy and regards Jin Taekyung and Choi Minwoo as its enemies.",
    "Team Leader Choi deliberately revealed his connection to Cheon Taemin as the old hero’s only living blood relative and intends to acquire the Ares Guild with its influence intact before removing Lee’s corruption.",
    "Go Jun possesses a battered necklace recovered from the ruins of the Arch Lich’s former stronghold; it is not Lee Jungryong’s keepsake, but Go Jun bribed an investigation leader to obtain it because he considers it meaningful.",
    "The Peace Guild is piloting a free emergency rescue service for Hunters in the capital region; Mutated Gates are increasing sharply in Korea, and Magic Johnson, the American Grand Mage, has arrived to provide broader data."
  ],
  "continuity_sources": [
    558,
    557
  ],
  "open_questions": [
    "What is the Lord of Heaven’s identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung’s party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo’s political engagement end?",
    "What process created Jang Sam’s mutant form, whether Dark Heaven’s mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What did Lee Jungryong leave Go Jun beyond his dying wish, what is the necklace recovered from the Arch Lich’s ruins, and what is causing Mutated Gates to increase worldwide?"
  ],
  "safe_through": 558,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman and 남만을 못 가 as Can’t Go to Nanman.",
    "Render 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant’s Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, and 대마도사 as Grand Mage; retain the established renderings for Small Cataclysm, Arch Lich, Skeleton King, Forest of Giants, Cyclops, and Ent."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 이정룡    | **Lee Jungryong** |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 검법     | **sword technique**                              |                                                       |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 태원     | **Taiyuan**            |
| 도사      | **Daoist**                                                      |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 삼도천 | **Sanzu River** | Buddhist river associated with the boundary between life and death; footnote on first use. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |
| 국방부 | **Ministry of National Defense** | Government ministry referenced in Taekyung's comparison about the steady passage of time. |
| 청계천 | **Cheonggyecheon** | Stream invoked in Taekyung's joke about Dark Heaven. |
| 꺽정 | **Kkeokjeong** | Jin's injured ally, addressed as Uncle Kkeokjeong. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 텔레포트 | **Teleport** | Taekyung's label for the Blood Lord's unexplained disappearance. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 국가장 | **national funeral** | State funeral held for Lee Jungryong. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 진태경 | 존슨 | Allied Hunter to Grand Mage | Johnson | polite and familiar | Jin repeatedly addresses Magic Johnson directly while requesting explanations and permission to visit the site. |
| 힐러 | 진태경 | healer addressing the rescuer who stabilized the survivor | sir | deferential and grateful | The healer thanks Jin as 선생님 after witnessing his rescue and treatment. |
| 진태경 | 대통령 | Hunter_to_President | Mr. President | formal-polite | Taekyung addresses the President respectfully during their airport greeting. |
| 대통령 | 진태경 | President_to_Hunter | Mr. Jin Taekyung | formal-polite | The President addresses Taekyung by name at the airport photo line. |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 558
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** D-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild; attacked by three Black Hunters following a solo drinking outing, with both arms severed below the elbows; his wounds were treated with high-ranking healer recovery magic and advanced potions, his arms were reattached, and he regained consciousness after three days; he has chosen to continue as a Hunter and remain with the Peace Guild after recovering; after beginning the Jin Family’s Cultivation Technique, he completed a complete circulation and learned to perform the Small Circulation independently on the first day, adapting unexpectedly quickly; repeated circulation is expected to improve his physical foundations, and resolving his trauma may allow an early return to Guild work
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and remembers that Taekyung protected him during an E-Rank Gate attack; married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 558
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, can command coordinated raids against powerful monsters, serves as one of the two pavilion masters of the Alliance Leader's direct Fire Dragon Pavilion, leads its first mission to Nanman, and is the Peace Guild's wealthy patron in the modern world.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor and assigned him a final task to incorporate martial principles into his learned martial arts but declined Taekyung's recruitment after Cheongpung reached him first, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 558
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Jungryong.md

# Lee Jungryong (이정룡)

- **Safe through:** Chapter 558
- **Aliases:** None
- **Role:** Former Vice Guild Master of Ares Guild, one of Korea's two S-rank Hunters, and a Supreme Peak-level martial artist who was killed by Jin Taekyung.
- **Personality:** Outwardly genial, calm, and humorous; calculating, opportunistic, manipulative, coercive, and ruthless when challenged
- **Voice:** Smooth, good-natured, and indirect, using teasing conversation and veiled threats before becoming openly furious
- **Relationships:** Master of Park Jihoon and Go Jun (Team Leader Seok), whom he personally selected and trained; longtime Great Cataclysm acquaintance of Park Tae Seop; adversary of Jin Taekyung; knew Team Leader Choi from childhood; has an antagonistic history with Kim Hwajong, who saved his life at the collapse of Mapo Bridge eighteen years earlier; was visibly shaken by learning that Choi is Cheon Taemin's maternal grandson; regards Cheon Taemin as an older brother despite no blood relation and has long held him in respect and fear; operates as Ares Guild's senior authority beneath its Guild Master

## Korean source

```text
＃559화



순간이동. 소위 텔레포트(Teleport)라 불리는 공간 이동 마법은 마법사들 사이에서도 상당한 고난도로 악명 높다.

좌표라도 잘못 찍으면 골로 가는 건 한순간이요, 마나 소모도 극심하여 장거리 이동이라도 할라치면 뒷목 잡고 쓰러지기 딱 좋다고 했다.

‘이른바 극강의 똥성비.’

하지만 그게 뭐든 간에, 결국 ‘누가’ 하느냐의 차이다.

초절정 고수의 손에서 펼쳐지는 삼재검법이 여느 신공(神功)과 다를 바 없는 것처럼, 70억 인류를 통틀어 셋밖에 존재하지 않는 대마도사에게도 마찬가지였다.

「퍽킹 코리아. 매번 생각하는 거지만 거리가 너무 멀어. 오는 길에 멀미가 날 뻔했다고.」

투덜거리는 검은 피부의 대마도사, 매직 존슨을 보며 나는 피식 웃었다.

“대륙 간 이동에 멀미 정도면 싸게 먹힌 거죠. 다른 마법사였다면 삼도천에서 뱃멀미 하고 있을 텐데.”

「샘-두-천? 그게 뭐지? 서울의 청계천인가 하는 것과 비슷한 건가?」

“……조금 다르긴 한데. 예. 뭐, 넘어갑시다.”

단번에 서울을 지옥의 도시로 만들어 버린 매직 존슨이 방 내부의 사람들을 발견하고 활짝 웃었다.

「헤이, 왓섭 게이즈! 다들 오랜만이군.」

타임지가 선정한 ‘세계에서 가장 영향력 있는 성소수자 1위’의 인사에, 최 팀장이 세계에서 가장 단호한 목소리로 대답했다.

“가이즈입니다, 미스터 존슨. 게이즈가 아니라.”

「최, 이렇게 나오면 섭섭해. 네 요청에 한달음에 달려왔는데.」

“직접 와 주신 건 감사합니다만, 보안 메일로 보내면 되지 않습니까.”

「오랜만에 보는데, 너무한 거 아냐?」

“제 기억으로는 우리가 만난 지 일주일도 안 된 것 같은데요. 안 그렇습니까, 진태경 씨?”

내가 고개를 끄덕였다.

“그건 그렇지. 존슨이야 국가장 때도 왔었으니까.”

이번에 치러진 국가장의 규모는 엄청났다. 백만에 달하는 국민들의 조문과 함께 전 세계 각국의 유력 인사들이 방한(訪韓)한 것이다.

이정룡이 생전 지녔던 영향력을 알려 주듯, 조문객 중에는 한 나라의 대통령들도 제법 있어서 어느 언론에서는 ‘정상 회담’이라는 표현을 쓰기도 했다.

그리고 그 거물 중에는 미합중국의 상징 중 하나인 매직 존슨 역시 포함되어 있었다.

「헤이, 진. 이렇게 나올 건가? 그건 자네들을 만나기 위해서가 아니라, 단지 추모의 뜻이었잖아.」

“추모요?”

「그래. 옛 전우를 배웅하는 길에 온 것뿐이었다고.」

“그런데 이태원 게이바는 왜 가셨어요. 그것도 환영 마법으로 얼굴까지 바꾸시고.”

「……누가 그런 말도 안 되는 헛소리를 했지?」

“존슨이랑 같이 게이바 갔던 놈이 말해 주던데요. 아주 결정적인 증언이었습니다.”

처음 반가워하던 기색은 이제 어디에서도 찾아볼 수 없다. 그날의 피해자, 스켈레톤 킹이 분노 어린 표정으로 입을 열었다.

“이 몸의 엉덩이에 뭔가가 닿았을 때 잘못되었다는 것을 깨달았다. 저 빌어먹을 인간이 날 속였어.”

「이 은혜도 모르는 몬스터 머더 뻐커…….」

표정 봐라. 타임지가 선정한 ‘세계에서 가장 난폭한 성소수자 1위’라고 해도 믿겠다.

험악한 목소리로 중얼거리던 매직 존슨이 사람들의 시선을 의식하고 재빨리 진지한 표정을 지었다.

「모두들 오해하지 말게. 단지 한국의 문화를 체험하려고 간 거였으니까.」

“옛 전우를 위한 추모는 이베이에 팔아먹었습니까?”

「진, 이러지 마. 영결식에 참여한 것만으로도 추모는 끝났어. 자네야말로 미스터 리가 어떤 인간이었는지 잘 알잖아.」

알지. 나만큼 잘 아는 사람이 또 있을까.

그리고 매직 존슨은 아크 리치의 본거지에서 어떤 일이 벌어졌는지 아는 극소수의 인물 중 하나다.

「어쨌든 다시 만났는데 이런 이야기는 그만하자고. 거기 자네도 그렇게 생각하지 않나. 이름이…… 로빈훗이었지?」

불행하게도 통역 아이템을 소지하지 않은 한국의 로빈훗, 임꺽정이 얼어붙은 표정으로 대답했다.

“아, 아임 파인 땡큐. 앤 유…….”

「나야 당연히 괜찮지. 하지만 지금부터는 썩 좋지 않은 이야기를 할 수밖에 없겠군.」

슥.

매직 존슨이 한숨 섞인 말과 함께 내민 것은, 손톱만 한 크기의 작은 메모리 칩이었다.

그것을 받아 살피던 최 팀장의 눈매가 날카로워졌다.

“부탁드렸던 정보입니까?”

「그래. 알아보느라 오랜만에 힘 좀 썼지.」

“감사 인사는 자료를 살핀 후로 미루겠습니다.”

「얼마든지.」

툭. 솨아아악.

그야말로 순식간이었다.

최 팀장이 테이블 밑 어딘가를 두드리자, 개인 사무실 내부의 모든 창문과 틈새가 가려지고 보이지 않는 마나가 장막처럼 드리워졌다.

‘마법?’

나도 알아차린 것을 대마도사인 매직 존슨이 모를 리 없다. 그가 흥미로운 눈빛으로 사무실을 둘러보았다.

「중첩 마법이 일곱 개라. 생각했던 것 이상으로 보안이 철저하군. 이 정도 수준의 마법사는 우리 길드 내에서도 몇 안 되는데…… 누구 솜씨지?」

“어린 시절부터 제 손발이 되어 주셨던 분입니다.”

아직 김 집사와 매직 존슨은 서로를 마주한 적이 없다.

짤막하게 대답한 최 팀장이 메모리 칩을 스마트폰에 삽입하자, 곧 화면 위로 어떤 홀로그램 영상이 불쑥 튀어나왔다.

- 콰가가가각!

생생한 굉음과 함께 반경 수십여 미터에 달하는 지면이 뒤집히고, 모래 알갱이가 사방으로 튄다. 흡사 지진이라고 부를 만한 광경.

여러 인종이 뒤섞인 백여 명의 헌터들이 욕설 섞인 고함을 내질렀다.

- Fuck!

- 산개! 즉시 산개해라! 놈들이 온다!

- 힐러! 힐러어!

비명과 고함이 난무하는 현장. 메마른 나무와 사방에 가득한 모래 언덕 사이에는 무너져 내리는 수 채의 건물들이 보인다.

그것이 의미하는 바를 깨달은 임꺽정의 눈이 커졌다.

“모, 몬스터 웨이브(Monster Wave)?”

정답이다. 게이트 내부에 현대식 건물 따위가 있을 리 없으니까.

모든 게이트는 최소한의 마력을 지니고 있고, 등급은 각 게이트가 품고 있는 마력의 총량에 의해 결정된다.

하지만 해당 게이트의 등급을 훌쩍 뛰어넘는 몬스터가 출현하면 이야기는 달라진다.

‘그것이 변이(變異) 게이트.’

변이 게이트만으로도 심각한 문제지만, 그렇게 등장한 상위 몬스터의 존재로 인해 게이트가 수용할 수 있는 마력의 총량을 넘어선다면 더 큰 재앙이 기다리고 있다.

‘몬스터 웨이브.’

견고한 댐이 압력을 이기지 못해 무너진다면, 가둬 놓았던 물은 흘러넘치는 법.

지금 홀로그램을 통해 보이는 광경이 바로 그와 같았다.

- 쉬리리릭!

기묘한 울음소리를 흘리는 거대한 전갈이 무려 십여 마리.

모래 깊숙이 파고든 놈들의 꼬리가 지면 위로 솟구치고, 비명과 핏물이 사방에서 터져 나온다.

- 크아아아악!

- 조셉! 조셉을 구해!

- 일제 사격 개시잇!

콰드드득!

인간과 몬스터가 서로를 죽이기 위해 몸을 날리던 그 순간.

핏.

사무실 내부를 가득 메우고 있던 홀로그램 영상이 씻은 듯이 사라졌다.

영상 송출을 중지시킨 최 팀장이 가라앉은 목소리로 입을 열었다.

“언제 있었던 일입니까?”

매직 존슨이 어두운 표정으로 대답했다.

「나흘 전. 장소는 모하비 사막. 사막 지대가 여러 주에 걸쳐져 있지만, 애리조나주 쪽에 가까운 곳이었지. 정확한 좌표까지는 알지 못해.」

두 사람의 대화에 귀를 기울이고 있던 나는 문득 눈살을 찌푸렸다.

“나흘 전이라고요?”

「그래, 나흘 전.」

“그 정도라면 이미 공식 발표가 나왔어야 할 텐데요.”

게이트는 희박한 확률로 터지는 시한폭탄과 같다. 그렇기에 전 세계의 모든 나라는 게이트에 늘 주의를 기울인다.

이른바 ‘폭탄 제거반’이라 불리는 국가직 헌터들을 각 지역에 배치하고, 정해진 법에 따라 일정 시일 내에 그 사실을 알리는 것 역시 그런 이유에서다.

‘그런데 왜 이렇게 잠잠하지?’

변이 게이트도 드문 현상이지만 몬스터 웨이브는 그보다 수십 배는 더 희박한 확률로 발생하는 사건.

이 정도면 언론에 대서특필 되어 화제가 되고도 남았을 텐데…….

이렇게 큰일을 근래 들어 곳곳의 소식에 촉각을 기울이는 나나, 최 팀장이 모르고 있었다는 것은 말이 되지 않는다.

결국, 남은 답은 하나뿐이다.

“공식 발표는 없겠군요.”

내 중얼거림에, 매직 존슨이 작게 고개를 끄덕였다.

「그래. 국방부가 나서서 모든 걸 깔끔하게 덮었지. 몬스터에 의해 뒤집혔던 저 사막처럼.」

“그게 가능합니까?”

「가능? 왜 이래, 진. 이건 미합중국의 국방부가 기밀리에 처리한 일이야. 차라리 뭐가 불가능하냐고 물었어야지.」

매직 존슨이 실소를 흘리며 말을 이었다.

「스물두 명이 죽고 서른다섯 명이 다쳤어도 그 사실은 달라지지 않아. 민간인 출입이 금지된 군사 기지 지역에서 벌어진 사건이라 은폐하기에도 쉬웠겠지.」

“하지만 이건…… 말 그대로 은폐잖습니까.”

「맞아. 대격변 이후 대대적으로 수정된 헌법에 어긋나는 일이기도 하지. 하지만 가끔은 차가운 진실보다 선량한 거짓말이 오히려 나을 때가 있는 법이야.」

“……!”

순간 뒤통수를 한 대 얻어맞은 기분이었다.

이것이 잘못되었다는 것을 알면서도, 나 역시 지금 존슨과 같은 생각을 했던 것이 생각났기 때문이었다.

‘암천(暗天).’

아직 준비되지 않은 이들은 어느 날 찾아온 진실에 혼란을 겪기 마련이다.

무림에서 암천의 존재가 바로 그러했고, 나 역시 놈들의 정체가 알려지기에는 시기상조라는 것에 동의했다.

하지만 지금 뒤통수가 얼얼한 이유는 그것뿐만이 아니었다.

막연히 짐작했던 불안감이 실체로 드러난 것에 대한 충격 역시 포함되어 있었다.

“몇 번째입니까?”

주어가 없는 물음.

그러나 딱딱하게 굳어 있는 매직 존슨의 안색은 내 질문의 뜻을 충분히 알아들었다는 증거였다.

“존슨.”

「……Fuck.」

한숨처럼 욕설을 중얼거린 그가 최 팀장을 향해 고개를 돌렸다.

「최, 내가 준 칩에 저장된 영상이 몇 개지?」

말없이 스마트폰 화면을 응시하던 최 팀장이 신음처럼 내뱉었다.

“서른두 개.”

「그래. 그중 두 번은 몬스터 웨이브였고, 나머지는 변이 게이트였지. 중요한 건, 내가 입수한 자료만 그 정도라는 거야.」

매직 존슨이 미국에서 차지하는 위치와 위상, 그리고 영향력은 누구도 의심할 여지가 없이 막강하다.

하지만 여전히 세계 최강을 자처하는 미합중국의 국방부의 정보력에 비할 수는 없을 것이다.

‘존슨이 입수한 자료만 서른두 개라니.’

그렇다면 얼마나 더 많은 일이 벌어졌을까. 동시에 같은 생각을 떠올린 듯, 나와 최 팀장이 약속이라도 한 것처럼 입을 다문 그때였다.

“잠깐. 잠깐만.”

손가락으로 열심히 뭔가를 셈하던 스켈레톤 킹이 화등잔만 해진 눈동자로 매직 존슨을 바라보았다.

“더는 고맙지 않은 인간이여. 지금 네가 한 말에 따르면, 하루도 안 거르고 그런 사건이 터졌다는 것이 아니냐?”

「거기 입 싼 몬스터, 상황을 너무 호락호락하게 보는 것 아닌가?」

“응?”

그 뒤에 이어진 매직 존슨의 한 마디는, 차라리 안 듣는 편이 나을 뻔했다.

「한 달이 아니라. 최근 일주일 사이에 벌어진 일이다.」

“……!”

“……!”

순간 사방을 짓누른 숨 막히는 침묵 속에서, 유일하게 존슨의 말뜻을 알아듣지 못한 한 사람의 목소리가 울려 퍼졌다.

“아, 아임 파인 땡큐. 앤 유?”

“…….”

“…….”

앤 유는 개뿔이, 홀리 쓋이다. 시부럴.
```

## Final English reading copy

```markdown
# Chapter 559

Teleportation.

The spatial-transference magic commonly called Teleport was infamous for being extraordinarily difficult, even among mages.

One wrong coordinate and you could be killed in an instant. The mana consumption was so extreme that anyone attempting long-distance travel was liable to clutch the back of their neck and collapse.

*The ultimate shitty cost-to-benefit ratio.*

But no matter what it was, in the end, everything depended on *who* was using it.

Just as the Three Calamities Sword Technique performed by a Supreme Peak master was no different from some divine technique, the same held true for the Grand Mages—of whom only three existed among the seven billion people in the world.

“Fucking Korea. I think this every time, but it’s too damn far away. I almost got motion sickness on the way here.”

I gave a quiet laugh as I watched the dark-skinned Grand Mage, Magic Johnson, grumble.

“Getting motion sickness while traveling between continents is a small price to pay. If another mage had done it, they’d be seasick on the Sanzu River by now.”[^1]

[^1]: The Sanzu River is a Buddhist river associated with the boundary between life and death.

“Sanzu River? What’s that? Is it something like Cheonggyecheon in Seoul?”

“...It’s a little different. Yes. Anyway, let’s move on.”

Magic Johnson, who had turned Seoul into a city of hell in one sentence, spotted the people inside the room and broke into a wide smile.

“Hey, what’s up, guys! It’s been a while.”

In response to the greeting from Time magazine’s pick for the “world’s most influential LGBTQ person,” Team Leader Choi answered in the world’s most decisive voice.

“It’s *guys*, Mr. Johnson. Not gays.”

“Choi, now you’re hurting my feelings. I came running the moment you asked.”

“I appreciate you coming in person, but couldn’t you have sent the information through a secure email?”

“Is that any way to treat someone you haven’t seen in a while?”

“If I remember correctly, it hasn’t even been a week since we last met. Isn’t that right, Mr. Jin Taekyung?”

I nodded.

“That’s true. Johnson was here for the national funeral, too.”

The national funeral held this time had been enormous. Nearly a million citizens had come to pay their respects, and influential figures from countries around the world had traveled to Korea.

To show just how much influence Lee Jungryong had possessed in life, quite a few of the mourners had been presidents. One news outlet had even called it a “summit meeting.”

Among those heavyweights had been Magic Johnson, one of the symbols of the United States.

“Hey, Jin. Is this how you’re going to act? I didn’t come to meet you people. I came simply to pay my respects.”

“Pay your respects?”

“That’s right. I only came to see an old comrade off.”

“Then why did you go to a gay bar in Itaewon? And why did you even change your face with illusion magic?”

“...Who told you such ridiculous nonsense?”

“The guy who went to the gay bar with Johnson told me. His testimony was pretty conclusive.”

The warm welcome from earlier had vanished without a trace.

The victim of that day, the Skeleton King, spoke with an enraged expression.

“I realized something had gone wrong when something touched this body’s backside. That damned human deceived me.”

“You ungrateful monster motherfucker...”

Look at that expression. I could believe it if Time magazine had named him the “world’s most violent LGBTQ person.”

Magic Johnson muttered in a threatening voice, then noticed everyone’s eyes on him and quickly adopted a serious expression.

“Don’t misunderstand. I only went there to experience Korean culture.”

“Did you sell your tribute to an old comrade on eBay?”

“Jin, don’t be like this. Paying my respects ended when I attended the funeral. You know better than anyone what Mr. Lee was like.”

I did.

Who could possibly know better than me?

And Magic Johnson was one of the very few people who knew what had happened at the Arch Lich’s stronghold.

“Anyway, we’re meeting again, so let’s stop talking about this. You there, you agree, don’t you? Your name was... Robin Hood, right?”

Unfortunately, Korea’s Robin Hood—Im Kkeokjeong, who didn’t have a translation Item—answered with a frozen expression.

“I-I’m fine, thank you. And you...”

“I’m obviously fine. But from this point on, I’m afraid I have no choice but to tell you a rather unpleasant story.”

*Swish.*

With a sigh, Magic Johnson held out a tiny memory chip no bigger than a fingernail.

Team Leader Choi accepted it and examined it. His eyes sharpened.

“Is this the information I asked for?”

“That’s right. I had to pull a few strings for the first time in a while.”

“I’ll save my thanks until after I’ve reviewed the material.”

“Take all the time you need.”

*Tap. Whoooooosh.*

It happened in the blink of an eye.

When Team Leader Choi tapped somewhere beneath the table, every window and opening in the private office was covered, and invisible mana descended like a curtain.

*Magic?*

There was no way the Grand Mage, Magic Johnson, hadn’t noticed what I had.

He looked around the office with interest.

“Seven overlapping spells. Your security is more thorough than I expected. There are only a handful of mages in our Guild capable of magic at this level... Whose work is this?”

“Someone who has been my hands and feet since I was young.”

Team Leader Choi answered briefly.

Kim the Butler and Magic Johnson had never met face-to-face.

When Choi inserted the memory chip into his smartphone, a holographic video suddenly sprang up above the screen.

—Krrrraaaaaash!

With a vivid, thunderous roar, the ground within a radius of several dozen meters overturned, sending grains of sand flying in every direction.

It looked like an earthquake.

Around a hundred Hunters of different ethnicities shouted and cursed.

—Fuck!

—Spread out! Spread out immediately! They’re coming!

—Healer! Healeeer!

Screams and shouts filled the scene. Between the dead trees and the sand dunes stretching in every direction, several buildings were visible as they collapsed.

Im Kkeokjeong’s eyes widened as he realized what it meant.

“M-Monster Wave?”

Correct.

There was no way modern buildings could exist inside a Gate.

Every Gate contained at least a minimal amount of mana, and its Grade was determined by the total amount of mana it held.

But if a monster appeared that far exceeded the Gate’s Grade, the situation changed.

*That was a Mutated Gate.*

A Mutated Gate was already a serious problem. But if the presence of the higher-grade monster caused the Gate’s mana to exceed the total amount it could contain, an even greater disaster awaited.

*A Monster Wave.*

If a sturdy dam couldn’t withstand the pressure and collapsed, the water it had been holding back would overflow.

The scene visible through the hologram was exactly like that.

—Sssshhhk!

More than ten enormous scorpions let out strange cries.

The creatures had burrowed deep into the sand; their tails shot up through the surface, and screams and spurts of blood erupted in every direction.

—Gaaaaah!

—Joseph! Save Joseph!

—Commence volley fire!

*Krrrraack!*

At the very moment humans and monsters threw themselves at one another in an attempt to kill each other—

*Flick.*

The holographic video filling the office vanished as though it had been washed away.

Team Leader Choi stopped the transmission and spoke in a subdued voice.

“When did this happen?”

Magic Johnson answered with a dark expression.

“Four days ago. The Mojave Desert. The desert region stretches across several states, but it was somewhere closer to Arizona. I don’t know the exact coordinates.”

I had been listening closely to their conversation when I suddenly furrowed my brow.

“Four days ago?”

“That’s right. Four days ago.”

“At that point, there should already have been an official announcement.”

Gates were like ticking time bombs that exploded only with a very low probability. That was why every country in the world kept a constant watch on them.

It was also why government Hunters—often called “bomb disposal squads”—were stationed throughout each region, and why the authorities were required by law to announce such incidents within a specified period.

*Then why has everything been so quiet?*

Mutated Gates were rare enough, but Monster Waves occurred dozens of times less frequently than that.

An incident of this scale should have made headlines and become a global sensation.

With me and Team Leader Choi keeping a close eye on news from all over the world lately, it made no sense that neither of us had heard about it.

In the end, only one answer remained.

“There was no official announcement.”

At my muttered words, Magic Johnson gave a small nod.

“That’s right. The Ministry of National Defense stepped in and covered everything up neatly. Just like that desert, which the monsters turned upside down.”

“They can do that?”

“Can they? Come on, Jin. This was something the United States Ministry of National Defense handled in secret. You should’ve asked what they *can’t* do.”

Magic Johnson let out a dry laugh and continued.

“Twenty-two people died and thirty-five were injured, but that doesn’t change anything. Since it happened at a military base where civilians weren’t allowed, it was probably easy to conceal.”

“But this is... literally a cover-up.”

“It is. It also violates the constitution, which was extensively revised after the Great Cataclysm. But sometimes a kind lie is better than a cold truth.”

“...!”

For a moment, it felt as though someone had struck me in the back of the head.

I knew this was wrong.

And yet I had realized that I was thinking the same thing as Johnson.

*Dark Heaven.*

People who weren’t prepared would inevitably be thrown into confusion by a truth that arrived without warning.

That was exactly what Dark Heaven’s existence had been like in the Murim, and I agreed that it was too soon for their identities to become known.

But that wasn’t the only reason the back of my head felt numb.

I was also shocked that the vague anxiety I had been sensing had finally revealed itself as something real.

“How many times?”

It was a question without a subject.

But Magic Johnson’s rigid expression was proof that he understood exactly what I meant.

“Johnson.”

“...Fuck.”

He muttered the curse like a sigh, then turned toward Team Leader Choi.

“Choi, how many videos are stored on the chip I gave you?”

Team Leader Choi stared silently at the smartphone screen before answering in a voice that sounded almost like a groan.

“Thirty-two.”

“That’s right. Two of them were Monster Waves, and the rest were Mutated Gates. The important thing is that those are only the materials I managed to obtain.”

Magic Johnson’s position, status, and influence in the United States were undeniably immense.

But even he could not compare with the intelligence-gathering capabilities of the Ministry of National Defense of the United States, which still claimed to be the most powerful nation in the world.

*Thirty-two incidents in the data Johnson managed to acquire alone.*

How many more events had taken place?

At that moment, Team Leader Choi and I fell silent at the same time, as though we had arranged it in advance.

“Wait. Just wait.”

The Skeleton King had been diligently counting something on his fingers. Now he looked at Magic Johnson with eyes as round as lanterns.

“Human I am no longer grateful to, according to what you just said, doesn’t that mean incidents like this happened every single day?”

“You loose-lipped monster, aren’t you taking this situation a little too lightly?”

“Huh?”

What Magic Johnson said next was something I almost would have preferred not to hear.

“Not over the course of a month. These incidents happened within the past week.”

“...!”

“...!”

In the suffocating silence that pressed down on everyone, a single voice rang out—the only person present who hadn’t understood what Johnson meant.

“I-I’m fine, thank you. And you?”

“...”

“...”

*To hell with ‘and you.’ Holy shit. Fuck.*
```

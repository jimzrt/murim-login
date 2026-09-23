<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0750.txt",
      "sha256": "ba1c699351164702db8f5a22465581ce2449ca998c4d4263b4489a5ae7935878",
      "bytes": 12489
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "aab1d5aee5ad16ff6e68f16c4b1485e5ba12ba4cd7e79fd1b6352189bcee3ee1",
      "bytes": 2644
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bbf2803754fec4e3bbd05b5c8dc3b3bd6832c59d2bf84516edd85874a8d79504",
      "bytes": 217023
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "ff61cc9f90224cacc6c5fcfe073f98aab3b7c4453d2003922bc902d4d9fbd40e",
      "bytes": 2011
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4274576379ea3811c940f0b648daf163720d064de0e1c2381e0646154896134a",
      "bytes": 622
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "8084530d7a45615773c740be74a71afc641810bbb7062ab769cda600f299ecb8",
      "bytes": 699
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f5d8289bb9fb9f75b963eaa0e347a7b4e2b1134ead2f3a64f4f28c27aa4697c2",
      "bytes": 229305
    }
  ],
  "estimated_tokens": 9372
}
-->

# Durable State Update — Chapter 750

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 750. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 750. Profile updates may replace only one
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
  "chapter": 750,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 750,
    "continuity_sources": [750],
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
    "The Prophet commands the revived Hasasin and has announced a second series of terrorist attacks after the earlier attacks called Allah's Judgment.",
    "The Prophet can create a transparent concealment barrier that cannot be detected by science or Magic.",
    "The Prophet possesses at least ten unrefined S-rank Magic Gems that retain their original power.",
    "The retired Grand Mage Siegfried Wassmann was found dead in his sealed hideout after his life force was apparently drained by unknown magic.",
    "Michael Silbert remains the strongest suspect in Siegfried's death and has personally entered the Japanese battlefield while pursuing his ambition to become the undisputed best.",
    "Jin has accepted the Supreme Peak Quest Unknown Death, whose mission is to discover the truth behind Siegfried's death.",
    "Michael and Huginn continue manipulating events and media coverage to isolate Jin and punish countries and Guilds that support him.",
    "Magic Johnson is investigating stolen research materials from Siegfried's laboratory but has not yet produced results.",
    "Huginn has completed an undisclosed operation whose consequences remain pending.",
    "Japan has requested Korean emergency assistance, with five Ares Guild and Peace Guild teams and the Korean Air Force heading toward Tokyo.",
    "Leviathan has been severely wounded by Jin's One Annihilation, swallowed the Magic Gem it sought, and is fleeing underwater while Jin pursues it.",
    "Jin's Broken Body debuff remains active after a Top-Grade Potion removed his other status abnormalities, leaving his combat attributes reduced and risking permanent loss."
  ],
  "continuity_sources": [
    749
  ],
  "open_questions": [
    "Who killed Siegfried Wassmann, by what magic, and why?",
    "How did Michael Silbert learn about A Area and Cheon Taemin's condition, and did he order Siegfried's death?",
    "What is The Prophet's identity, and how are the Prophet's terrorist campaign and Leviathan's reappearance connected?",
    "What is Huginn's undisclosed operation, and can its consequences actually bring Jin down?",
    "Will Jin's second spear attack kill Leviathan, and what consequences will follow from the Magic Gem Leviathan swallowed?"
  ],
  "safe_through": 749,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 레비아탄 as Leviathan and 스사노오 as Susanoo.",
    "Render 마력 as magical power, distinct from mana.",
    "Render 마정 and 마정석 as Magic Gem.",
    "Render 마계어 as Demon Realm language and 광염 as light-flames."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 시스템              | **System**                     |
| 칭호               | **Title**                      |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 북한 | **North Korea** | Country referenced in Taekyung's comparison. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 고이즈미 | **Koizumi** | Japanese prime minister quoted in the news. |
| 외교부 | **Ministry of Foreign Affairs** | Korean government ministry angered by the Chinese branch director's damage to cultural relics. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 도쿄 | **Tokyo** | City visible behind Huginn's departing ship. |
| 일본 | **Japan** | Country requesting emergency assistance and under Leviathan's attack. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 방위대신 | 진태경 | Japanese Defense Minister to foreign Hunter | Jin Taekyung | insulting-shouting | The Minister calls for Jin using a deliberately mangled and contemptuous pronunciation of his name. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 748
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, a traveler between Murim and another world resembling the realm of immortals, and the creator of the beginner-accessible Smiling Mana Cultivation Method.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, trusted manager of media and official arrangements, and now the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 748
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 749
- **Aliases:** None
- **Role:** Leviathan is an ancient S-rank sea monster and ruler of the sea that has been severely wounded by Jin Taekyung's One Annihilation, swallowed the Magic Gem it sought, and is fleeing underwater while Jin pursues it.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

## Korean source

```text
＃750화



깊은 바닷속.

수많은 잔해와 시신으로 인해 한 치 앞도 내다보기 힘들 만큼 어두운 그곳에서, 돌연 청백색의 화염이 피어올랐다.

화륵, 콰아아아아!

물살이 갈라지고 수분이 증발한다.

자연의 순리(順理)마저 거스르는 기운이 실린 화염. 아니, 한 자루의 창이 빛살처럼 쏘아졌다.

믿을 수 없을 만큼 빠른 속도로 나아가는 거대한 그림자를 향해.

결코 살려 두어서는 안 될 재앙을 향해.

그러나 창에 담긴 기운이 그러했듯, 저 신화 속 괴물 역시 순리를 거스르는 존재였다.

콰르르륵!

바다가 요동친다.

동시에 깊은 수심에서 솟아오른 크고 작은 물의 회오리들이 힘차게 나아가던 창날을 막아섰다.

구구궁!

거센 충돌과 함께 겹겹이 퍼져 나가는 파동.

한바탕 세상을 뒤흔든 충격과 굉음이 가라앉을 무렵, 앞을 막아섰던 모든 장애물을 분쇄한 화염 역시 힘을 다하여 사그라지고 있었다.

저 멀리, 짙은 어둠 속으로 파묻히는 괴물의 동체에 끝내 닿지 못한 채.

스륵. 턱.

어느새 고요해진 바닷속.

힘없이 물결에 휩쓸려 가던 창이 누군가의 손에 붙잡혔다.

괴물이 사라진 방향을 말없이 바라보는 남자의 뒷모습에서는 활화산처럼 터질 듯한 감정이 느껴지는 듯했다.

아니, 정정한다.

터질 듯한 감정이 느껴지는 듯한 것이 아니라, 누군가 건드리기만 하면 터질 것 같았다.

살려 두어서는 안 될 괴물을 놓쳤던 저 순간에도.

……지금 이 순간에도.

“그만.”

나도 모르게 날 선 목소리가 흘러나온 그 순간.

파앗.

선명한 녹색 빛 무리와 함께 주위를 가득 채웠던 모든 것이 녹아내렸다.

밤처럼 어두컴컴한 바다와 고층 빌딩이 남긴 거대한 잔해, 눈을 부릅뜬 채 죽음을 맞이한 이름 모를 시신들까지.

그리고 그렇게 사라진 홀로그램의 빈자리를 채운 것은, 수십여 명의 낯선 얼굴들이었다.

척 보기에도 값비싸 보이는 맞춤 정장과 군복을 차려입은 사내들.

그중 내 맞은편 상석에 앉아 있던 노인이 침통한 표정으로 입을 열었다.

“허어. 레비아탄을 놓치다니.”

오늘 처음 본 얼굴이지만, 최 팀장이 알려 준 바에 의하면 저 노인은 일본에서도 세 손가락 안에 드는 권력자다.

아니, 주어진 실권만 따져 보면 첫째로 꼽힐지도 모른다.

방위대신이라는 직책은 평상시에도 엄청난 고위직이지만, 지금 같은 전시 상황에서 누구보다 큰 힘을 지니고 있으니까.

하지만 늙은 방위대신을 바라보는 내 기분은 썩 좋지 못했다.

사실 조금 더 솔직히 말하자면 당장 눈앞에 없는 레비아탄보다는 저 염병할 늙은이를 먼저 처리하고 싶을 정도다.

이유? 간단하다.

불과 한 시간 전, 레비아탄을 잡을 수 있는 마지막 가능성을 없앤 것이 바로 저 인간이니까.

이미 일련의 사정을 모두 파악한 나로서는 나오는 말이 고울 수가 없었다.

“그러게. 아쉽게 놓쳤네요. 마지막에 누가 도와줬으면 잡을 수 있었을지도 모르는데.”

“……!”

순식간에 얼어붙는 회의실의 공기. 눈치만 살피는 일본인들 사이에서 방위대신이 불쾌한 눈빛으로 나를 응시했다.

“자네가 한 말은 꼭 우리 일본에 책임이 있다는 뜻으로 들리네만. 이 늙은이의 귀가 어두워서 잘못 들은 겐가?”

“팔순 넘었다고 들었는데, 아직 정정하시네요. 노인네가 귀도 밝지.”

“뭣이?”

“진짜 귀가 어두워지셨나. 이미 들었으면서 뭘 자꾸 묻고 그래.”

“이 무슨……!”

쾅!

테이블을 내려친 방위대신이 최 팀장을 향해 고개를 돌렸다.

“자네는 이런 무례를 보고만 있을 셈인가!”

평소의 최 팀장이었다면 이쯤에서 내게 눈치를 줬을 거다.

그러니까, 평소였다면.

“방위대신께서 말씀하시는 무례라는 게, 혹시 이런 자리에서 책상을 치는 그런 행위를 말씀하시는 겁니까?”

“뭐라?”

“일본이 외교부를 통해 공식적으로 지원을 요청했고, 우리는 그에 응하여 위험을 무릅쓰고 여기까지 왔습니다. 그런데…….”

뚝 끊어진 말꼬리와 동시에 최 팀장의 눈빛이 차갑게 가라앉았다.

“귀측은 왜 병력을 추가로 투입하지 않았습니까?”

“…….”

“제가 알기로는 진태경 씨가 레비아탄을 공격한 그 시점에 적어도 이천 명 이상의 헌터들이 소집된 상황이었습니다. 육, 항공 자위대도 대기 중이었고요.”

“그건…….”

“압니다. 그들 대부분이 전투에 별 도움이 되지 못했을 거라는 것 정도는. 하지만 늦게나마 일본의 헌터들을 투입했다면, 도주하던 레비아탄의 발을 잠깐이나마 늦출 수는 있었을 겁니다.”

최 팀장의 말은 일목요연했고, 정확한 사실이었다.

내게 필요했던 건 바로 그 잠깐의 시간이었으니까.

상처 입은 몸뚱어리를 이끌고 도망치던 괴물을 교란하고, 지체하게 만들 만한 약간의 지원과 희생.

하지만 위험을 무릅쓰고 들어간 그 깊은 바다에서, 나는 멀어지는 놈의 뒷모습을 지켜봐야만 했다.

그리고 그것은 항공기에서 내려 진입할 준비 중이었던 최 팀장과 이백여 명의 헌터들에게도 해당되는 문제였다.

“보다 못한 제가 직접 헌터들을 이끌고 나서려 했더니 귀측에서 투입을 막더군요. 현장 작전 지휘권까지 들먹이면서.”

“……!”

“자신들의 희생은 최대한 줄이고, 전공만 세우고 싶었다면 차라리 제대로 하지 그랬습니까. 그럼 일이 이 지경까지 오진 않았을 텐데.”

입술을 질끈 깨문 방위대신이 입을 열었다.

“포위망은, 포위망은 완벽했어.”

그 말을 들은 스켈레톤 킹이 순수한 의문을 담아 내게 물었다.

“완벽하면 안 뚫렸어야 하는 거 아닌가?”

“어, 맞아.”

“근데 뚫린 것으로 아는데?”

“그래. 뚫렸지.”

“놈이 발산한 마력 때문에 위치도 놓치고?”

“어.”

내 친절한 대답을 모두 들은 스켈레톤 킹이 중얼거렸다.

“뭐지, 병신들인가……?”

“……!”

“……!”

진실을 정확히 관통한 한마디에 회의실 내부의 온도가 영하로 추락했다.

하지만 입을 싹 닫은 채 서로 눈치만 살피는 사람들의 모습을 보면서도, 통쾌한 기분은 조금도 들지 않았다.

‘미친 새끼들.’

몬스터보다 못한 벌레 새끼들이 작전 지휘부랍시고 앉아 있는 걸 보니 헛웃음도 안 나왔다.

‘이걸 좆 같다고 때려치울 수도 없고.’

지금까지 밝혀진 사상자만 어림잡아 10만.

그나마 불행 중 다행으로 레비아탄이 일으킨 쓰나미의 영향이 도쿄의 외곽 어림에서 멈췄기에 이 정도인 거다.

만약 내가 떠난 후 놈이 돌아온다면 그땐 도쿄의 지명이 아틀란티스로 바뀔 것이다.

‘혹시 놈이 일본을 포기하고 다른 곳을 노린다면…….’

그건 그것대로 문제였다.

물론 당장 눈앞에 보이는 저 늙은 원숭이 두목을 포함한 병신들은, 지들 살았다고 깨춤을 추고 좋아하겠지만.

“…….”

진짜 그러고도 남을 놈들이라 기분만 더 잡쳤다.

순도 100%의 깊은 한숨을 내쉰 나는 합죽이가 되어 버린 방위대신을 향해 입을 열었다.

“두말할 필요 없고, 다른 책임자 불러요.”

“채, 책임자?”

“총리. 아니면 일왕. 누구든 그쪽보단 낫겠지.”

“일왕이라니! 이자가 감히 대 일본제국의 천황께…….”

“돌겠네, 진짜. 도대체 언제적 제국 드립이야. 원자 폭탄 두 방 맞고 뻗었으면 천황 칭호도 반납해야지. 안 그래?”

“그건 미국 양키 놈들의 잔인무도한 파괴 행위였다!”

나는 빽 소리치는 방위 대신을 보며 귀를 틀어막았다.

“방사능 걸릴 것 같애. 방사능 걸릴 것 같애. 방사능 걸릴 것 같애. 방사능 걸릴 것 같애.”

“칙쇼옷!”

살 만큼 살아서 그런 걸까. 아니면 방사능 오염으로 겁을 상실한 걸까.

길길이 날뛰던 방위대신이 늙은 몸으로 나를 향해 달려오던 그때, 스켈레톤 킹이 손을 뻗어 그의 목덜미를 잡아챘다.

“멈춰라. 이 늙고 하찮은 인…… 아니, 옐로우 몽키야.”

“노옴! 당장 이 손 놓지 못하겠느냐! 털만 수북한 양키 놈 따위가 대 일본제국의 방위대신에게 손을 대다니!”

“감히 내 앞에서 위대한 미합중국을 모욕해?”

“나는 아직 잊지 않았다! 네놈들이 이 땅과 선량한 황국 신민들에게 어떤 끔찍한 짓을 저질렀는지!”

“진주만의 원혼이여, 내게 임하라!”

미친 새끼들…….

7080세대에 태어난 일본 제국주의자와 마계 출신 미국 몬스터의 치열한 논쟁이라니.

저 끔찍한 혼종들의 모습을 두 눈으로 보고 있자니 절로 가슴이 웅장해졌지만, 아직 모든 것이 끝난 게 아니었다.

스아아아.

“……?”

뭐여, 이거.

갑자기 오싹해지는 전신과 함께 흐릿해지는 형광등.

방위대신과 스켈레톤 킹을 떼어 놓기 위해 안간힘을 쓰고 있던 사람들조차 한기(寒氣)를 느끼며 몸을 부르르 떨었다.

‘갑자기 이게 무슨.’

의문과 함께 고개를 돌린 그때, 허공에서 최 팀장과 시선이 마주쳤다.

그 순간 나는 한 가지 사실을 깨닫고 멍하니 입을 벌렸다.

귓가에서는 조금 전 들었던 누군가의 외침이 생생하게 반복해서 들려오고 있었다.



‘진주만의 원혼이여, 내게 임하라!’



아니, 씨벌. 설마…….

슈와아악! 콰창!

스산한 기운이 돌풍으로 변해 천장의 형광등을 박살 냈다.

나는 이미 갑작스럽게 내려앉은 어둠을 가로질러 한 사람을 향해 달려가고 있었다.

“똑똑히 보아라, 그리고 그들의 원한을 느끼……!”

“야, 이 미친 새꺄!”

빠각!



* * *



천만다행이었다.

21세기에도 실력보다 가문과 인맥에 치중하는 전통 있는 승진 시스템 덕분에, 회의실 내부에 있던 고위 관료와 장군들은 대부분 일반인이었다. 그들은 겁에 질려 스켈레톤 킹의 외침조차 듣지 못했다.

그리고 책임자 부르라는 내 주장이 전해졌는지, 얼마 지나지 않아 지배인…… 아니, 총리가 도착했다.

“본국을 돕기 위해 여기까지 와 주다니! 참으로 고맙소, 진상!”

“아, 예. 만나서 반갑습니다. 고이즈미 총리님.”

이 양반을 실제로 보게 되는 날이 올 줄이야.

맨날 인터넷에서 어록 모음만 보다가 이렇게 만나게 되니 잠깐 연예인이라도 만난 듯한 기분이 들었다.

물론 상황이 상황인 만큼 그런 마음을 내비칠 수는 없었다. 지금 중요한 것은 레비아탄에 관한 문제였으니까.

적어도 최소한, 나는 그러고 싶었다.

나는.

“본론부터 얘기하겠습니다. 레비아탄을 추적하기 위해서는…….”

“방위대신이 진상에게 무례를 저질렀다고 들었소. 내 이번 일이 마무리되면, 진상의 마음을 위로하기 위해서라도 그를 크게 문책하리다!”

“어, 음. 되게 감사하네요.”

“표정이 왜 그러시오. 진상?”

“아니, 그…… 레비아탄 관련 얘기도 해야 하고. 또 절 부르시는 호칭이 좀.”

“무슨 호칭 말이오, 진상?”

“…….”

“아, 한국에서는 다른 의미로 들리는 모양이군. 그럼 이름 끝 글자를 따서 경상으로 부르면 되겠소?”

될 리가 있나.

똥을 피했더니 오줌을 맞은 기분이다.

‘다음에 레비아탄이랑 싸우면 꼭 다치란 소린가……?’

나는 진상과 경상 사이를 심각하게 고민하다가, 이내 한숨을 내쉬었다.

그래, 중상이 아닌 게 어디냐.
```

## Final English reading copy

```markdown
# Chapter 750

Deep beneath the sea.

It was so dark, with countless wrecks and corpses filling the water, that it was impossible to see even an inch ahead. Then, without warning, blue-white flames erupted.

*Fwoosh! KRAAAAAASH!*

The current split apart, and the water vaporized.

The flames carried a force that defied the laws of nature. No—a spear shot forward like a ray of light.

Toward the enormous shadow moving at an unbelievable speed.

Toward a calamity that could never be allowed to live.

But just as the force within the spear defied the laws of nature, so too did the mythical monster.

*KRRRRRUMBLE!*

The sea shook.

At the same time, large and small whirlpools of water surged up from the depths and blocked the spearhead as it raced forward.

*KOOOOONG!*

Waves spread outward in layers with the violent collision.

By the time the shock and thunderous roar that had shaken the world had subsided, the flames that had pulverized every obstacle in their path were also fading away, having exhausted their strength.

They had ultimately failed to reach the monster’s body, which was disappearing into the thick darkness in the distance.

*Swish. Clack.*

The sea had already grown quiet.

The spear, drifting helplessly with the current, was caught in someone’s hand.

The back of the man silently staring in the direction the monster had vanished seemed to radiate emotion ready to erupt like an active volcano.

No, let me correct that.

It was not merely that he seemed to radiate emotion ready to erupt.

It looked as though he would explode if anyone so much as touched him.

Even in that moment, when he had lost the monster that could never be allowed to live.

…Even now.

“Enough.”

The instant the sharp voice slipped from my lips without my realizing it—

*Flash.*

Everything that had filled the surroundings melted away in a vivid green light.

The sea, dark as night.

The enormous wreckage left behind by the skyscrapers.

Even the nameless corpses that had met their deaths with their eyes wide open.

The empty space where the hologram had disappeared was filled by several dozen unfamiliar faces.

Men dressed in custom-tailored suits and military uniforms that looked expensive at a glance.

Among them, the old man sitting in the seat of honor across from me opened his mouth with a grim expression.

“Good heavens. To think Leviathan got away.”

It was the first time I had seen his face, but according to Team Leader Choi, that old man was one of the three most powerful people in Japan.

No—if you counted only the authority he actually possessed, he might even have been number one.

The position of Defense Minister was an immensely powerful one even in peacetime. In a situation like this, with the country at war, he possessed more power than anyone.

But I was not in a good mood as I looked at the old Defense Minister.

To be a little more honest, I wanted to deal with that damned old man in front of me before Leviathan, who was not even there right now.

Why?

Simple.

Because that man had eliminated the last chance of catching Leviathan only an hour ago.

Now that I understood the whole situation, there was no way my words could be pleasant.

“Exactly. It was a shame we missed it. If someone had helped us at the end, we might have caught it.”

“……!”

The air in the conference room froze in an instant. While the Japanese men glanced around nervously, the Defense Minister glared at me with displeasure.

“What you said sounds as though you are implying that Japan is responsible. Did these old ears hear you incorrectly?”

“I heard you were over eighty, but you still seem remarkably healthy. Your ears work pretty well for an old man.”

“What did you say?”

“Have your ears actually gotten worse? You already heard me, so why do you keep asking?”

“What kind of—!”

*Bang!*

The Defense Minister slammed his hand on the table and turned toward Team Leader Choi.

“Are you simply going to stand by and watch this insolence?”

Normally, Team Leader Choi would have given me a warning look around this point.

That is, normally.

“When you speak of insolence, Defense Minister, are you perhaps referring to striking the table in a place like this?”

“What?”

“Japan formally requested assistance through the Ministry of Foreign Affairs, and we risked our lives to come all the way here in response. And yet…”

Team Leader Choi’s words cut off, and his gaze turned cold.

“Why did your side not deploy additional forces?”

“……”

“As I understand it, at the exact moment Jin Taekyung attacked Leviathan, at least two thousand Hunters had been mobilized. The Ground and Air Self-Defense Forces were also standing by.”

“That was…”

“I know. I know that most of them would not have been much help in battle. But if you had deployed Japan’s Hunters, even at the last moment, they could have delayed the fleeing Leviathan for a little while.”

Team Leader Choi’s words were clear and precise. They were also entirely true.

That little bit of time was exactly what I had needed.

A small amount of support and sacrifice to distract the wounded monster dragging its battered body away and make it lose precious time.

But in that deep sea, where I had risked my life to enter, all I could do was watch the monster’s back grow more distant.

The same problem applied to Team Leader Choi and the more than two hundred Hunters who had gotten off the aircraft and were preparing to enter.

“I was about to lead the Hunters in myself because I could not stand by and watch, but your side stopped us. You even invoked your authority over field operations.”

“……!”

“If you wanted to minimize your own sacrifices and take all the credit, you should have done it properly. Then things would never have reached this point.”

The Defense Minister clenched his lips tightly before speaking.

“The encirclement—the encirclement was perfect.”

The Skeleton King, who had been listening, asked me with genuine confusion.

“If it was perfect, shouldn’t it not have been breached?”

“Yeah, exactly.”

“But I heard it was breached?”

“That’s right. It was.”

“And you even lost its location because of the magical power it released?”

“Yep.”

After listening to all my helpful answers, the Skeleton King muttered,

“What the hell? Are they idiots…?”

“……!”

“……!”

With that single statement striking the truth with perfect accuracy, the temperature inside the conference room dropped below freezing.

But even as I watched everyone clamp their mouths shut and glance nervously at one another, I felt not the slightest bit satisfied.

*What a bunch of fucking lunatics.*

Seeing these bugs, worse than monsters, sitting there pretending to be an operations command center was not even enough to make me laugh bitterly.

*It’s not like I can call this fucking bullshit and quit, either.*

The number of casualties confirmed so far was roughly one hundred thousand.

It was only this low because, fortunately, the tsunami Leviathan had created had stopped around the outskirts of Tokyo.

If it returned after I left, Tokyo would be renamed Atlantis.

*And if it gives up on Japan and targets somewhere else…*

That would be a problem in its own way.

Of course, the idiots—including that old monkey chief standing before me—would probably celebrate and dance with joy just because they had survived.

“……”

They were exactly the kind of people who would do that.

The thought only made me feel worse.

After letting out a hundred-percent pure, deep sigh, I spoke to the Defense Minister, who had become completely silent.

“Enough with the pointless arguing. Call someone else in charge.”

“S-Someone else in charge?”

“The Prime Minister. Or the King of Japan. Anyone has to be better than you.”

“The King of Japan?! How dare you refer to His Majesty the Emperor of the Great Japanese Empire that way—”

“This is driving me crazy. How long are you going to keep using that empire crap? If you collapsed after taking two atomic bombs, you should have surrendered the title of Emperor too. Don’t you think?”

“That was a savage and barbaric act of destruction by those American Yankees!”

I covered my ears as the Defense Minister screamed.

“I think I’m going to get radiation poisoning. I think I’m going to get radiation poisoning. I think I’m going to get radiation poisoning. I think I’m going to get radiation poisoning.”

“Chikshō!”

Was it because he had already lived a full life? Or had radiation contamination robbed him of his fear?

Just as the Defense Minister was rampaging and charging at me with his old body, the Skeleton King reached out and seized him by the back of the neck.

“Stop, you old and insignificant per—no, Yellow Monkey.”

“You insolent dog! Release me at once! How dare a Yankee bastard covered in fur lay his hands on the Defense Minister of the Great Japanese Empire!”

“Do you dare insult the mighty United States in front of me?”

“I have not forgotten! I have not forgotten the terrible things you bastards did to this land and its innocent subjects of the Imperial State!”

“Vengeful spirits of Pearl Harbor, descend upon me!”

*What the hell are these lunatics…*

A heated argument between a Japanese imperialist from the ’70s–’80s generation and an American monster from the Demon Realm.

Watching those horrifying hybrids with my own two eyes made my chest swell with emotion despite itself, but it was not over yet.

*Fwoooooosh.*

“……?”

What the hell was this?

My entire body suddenly grew cold, and the fluorescent lights began to dim.

Even the people struggling desperately to pull the Defense Minister and the Skeleton King apart felt the chill and shuddered.

*What the hell is happening all of a sudden?*

I turned my head in confusion.

In midair, my eyes met Team Leader Choi’s.

And in that moment, I realized something and stood there with my mouth hanging open.

In my ears, someone’s shout from a moment earlier was repeating itself with vivid clarity.

*Vengeful spirits of Pearl Harbor, descend upon me!*

*No, fuck. Don’t tell me…*

*Whoooooosh! KRAAASH!*

The eerie energy transformed into a gale and shattered the fluorescent lights on the ceiling.

I was already running through the sudden darkness toward someone.

“Look closely, and feel the resentment of the—”

“Hey, you crazy bastard!”

*Crack!*

* * *

Thank goodness.

Thanks to a traditional promotion system that still prioritized family and connections over ability even in the twenty-first century, most of the high-ranking officials and generals inside the conference room were ordinary people. They were so frightened that they had not even heard the Skeleton King’s shout.

And apparently my demand to call someone in charge had gotten through, because not long afterward, the manager—no, the Prime Minister—arrived.

“Thank you so much for coming all the way here to help our homeland, Jinsang!”

“Ah, yes. It’s nice to meet you, Prime Minister Koizumi.”

I had never imagined I would live to see the day I met this man in person.

I had always seen collections of his famous quotes on the internet, so meeting him like this briefly made me feel as if I had run into a celebrity.

Of course, given the situation, I could not show it. The important matter right now was Leviathan.

At the very least, that was what I wanted.

I wanted to.

“I’ll get straight to the point. In order to track Leviathan—”

“I heard the Defense Minister was rude to you, Jinsang. Once this matter is settled, I will severely reprimand him, if only to soothe your feelings!”

“Uh, wow. I really appreciate that.”

“Why do you look like that, Jinsang?”

“No, it’s just… We also need to discuss Leviathan. And the way you keep addressing me is a little…”

“What is wrong with the way I address you, Jinsang?”

“……”

“Ah, I see. It must sound different in Korea. Then shall I call you Gyeongsang, using the last syllable of your name?”

There was no way that would work.

I felt as though I had dodged a pile of shit only to get pissed on.

*Is he wishing me a minor injury the next time I fight Leviathan…?*

I seriously considered Jinsang versus Gyeongsang, then sighed.

*Well, at least it isn’t Severe Injury.*[^1]

[^1]: Japanese *Jin-san* (“Mr. Jin”) sounds like the Korean *jinsang*, meaning an obnoxious or troublesome person. Koizumi’s proposed *Gyeong-san* sounds like Korean *gyeongsang*, meaning a minor injury.
```

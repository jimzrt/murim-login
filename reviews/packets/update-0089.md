<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0089.txt",
      "sha256": "73b30e4cc0753967bf1763bd1208f2c220f71bf5ad828c3263b023f57db35c6c",
      "bytes": 13405
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6148eb399b5154ef84a7ddb4c8c674a1eb1e60df0b935f4eaa4817556be9aaf3",
      "bytes": 2414
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "94906d49a44a4c93703363d029a289669b43a4298881226d4b6c0015db175fe7",
      "bytes": 8819
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "cfae9195067cbdc864aef44600f90d9e98f074c03fa343d6bf4449fe005c9e13",
      "bytes": 2803
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3d15e3b8de5f08c000f2818c9bb5d688bf4b0147c84ee2edafc8cc59a97c16ff",
      "bytes": 8689
    }
  ],
  "estimated_tokens": 13176
}
-->

# Durable State Update — Chapter 89

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 89. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 89. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 89,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 89,
    "continuity_sources": [89],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "The party sells The Minotaur's Labyrinth byproducts and Magic Gems to the Administration.",
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild.",
    "Im Chunsoo is Sangdong Guild's A-rank Guild Master and founder, known as Frozen for his exceptional ice magic.",
    "Im Chunsoo learns that Changsoo transferred 8 billion won to two accounts, fires him, and begins beating him with an ice club.",
    "Sangdong Guild's Team One Leader brings Changsoo to Im Chunsoo's office, which is closed to visitors for half a day.",
    "Im Changsoo transfers the promised four billion won to Jin Taekyung.",
    "Hayeon has a 39-degree fever, leaves school early, and studies at home before summer vacation.",
    "Hayeon knows that Kim Jeonghee is secretly working at a restaurant and asks Taekyung not to find her.",
    "Kim Jeonghee is Taekyung and Hayeon's fifty-year-old mother and has worked in a restaurant kitchen for over a year.",
    "Taekyung's father died when a Gate opened in downtown during the Great Cataclysm.",
    "Kim Jeonghee defends Taekyung against the restaurant owner's insults and curses the owner.",
    "Taekyung arrives at the restaurant and calls Kim Jeonghee Mom.",
    "Kim Jeonghee quits her restaurant kitchen job immediately after the owner insults and attacks Jin Taekyung, then leaves with him.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Jin Taekyung is now a C-rank Hunter rather than the F-rank Hunter the restaurant owner believed him to be; Im Changsoo confirms Taekyung received four billion won.",
    "Kim Jeonghee and Jin Taekyung return home, where she offers him cheonggukjang and kimchi pancakes."
  ],
  "continuity_sources": [
    88
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved."
  ],
  "safe_through": 88,
  "temporary_decisions": [
    "Use Frozen for 프로즌 and preserve the tiger-father/dog-son wordplay in 호부견자.",
    "Use ajumma for 아줌마 with an explanatory footnote.",
    "Retain goshiwon with an explanatory footnote.",
    "Use Minsu for 민수 as the short form of Kim Minsu."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |

## Exact glossary matches

| 무림     | **Murim**          |
| 조필     | **Jopil**          |
| 삼류     | **Third Rate**    |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 내공     | **internal energy**                              |                                                       |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 살기     | **killing intent**                               |                                                       |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 헌터      | **Hunter**            |
| 레이드     | **raid**              |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |

## Listed compact profiles

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 75
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

## Korean source

```text
＃89화



“아들, 천천히 먹어. 체하겠다.”

“헌터 관두고 먹방 스트리머 해도 되겠네.”

엄마의 걱정과 하연이의 감탄 속에서 식사를 끝마쳤다.

고봉밥만 다섯 그릇에 한 냄비 가득 끓인 청국장과 수십 장의 김치전이 사라진 후였다.

“휴, 이제 좀 배가 차네.”

“……미쳤나 봐. 평소에는 얼마나 먹는 거야?”

“맛있으면 끝도 없이 들어가지.”

예전에도 많이 먹긴 했지만 이 정도는 아니었다.

하지만 지금은 신진대사며 내부 장기가 전과는 비교할 수도 없이 향상되어서 그런지 어지간한 푸드파이터 저리 가라다.

“진짜 먹방 스트리머나 해 볼까.”

“아냐, 그 사람들도 먹고살아야지. 인간들끼리 경쟁하게 놔둬.”

“난 인간이 아니란 소리냐?”

“응, 내 눈에는 돼지 그 이상인데.”

혀를 내두른 하연이가 수저를 내려놨다. 밥그릇을 슬쩍 들여다보니 절반이 그대로다.

“밥 남기면 벌 받는다.”

“어르신처럼 말하네.”

“한국인은 곧 죽어도 밥심인 거 몰라? 먹어야 감기도 빨리 낫는 거야.”

“입맛이 없어. 머리도 아프고.”

“병원은?”

“다녀왔어. 처방받은 약도 먹었고.”

나는 가만히 하연이를 응시했다. 불그스름하게 달아오른 얼굴, 이마에는 땀이 송골송골 맺혀 있다. 기껏 조퇴해서 공부한답시고 버티더니 아까보다 더 열이 오른 모양이다.

‘처방받은 약이 효과가 별로 없는 것 같은데.’

솔직히 병이 낫는 가장 간단한 방법은 따로 있다.

전문 힐러에게 치료받거나, 혹은 시중에서 판매하는 포션을 마시는 것. 하지만 비싼 비용 때문에 대부분의 일반인들은 꺼리는 일이다.

‘미련하긴.’

내가 쉬지 않고 일했던 이유는 가족들이 안전하게, 아프지 않고 행복하게 살기를 바랐기 때문인데.

그 돈을 쉽게 쓰지 못하는 이유를 알면서도, 답답한 마음이 드는 건 어쩔 수 없다. 그깟 포션 한 병에 얼마나 한다고.

‘하다못해 운기조식 한 번이면 훨씬 괜찮아질…… 어라?’

문득 스치는 생각에 멈칫했다.

잠깐만, 혹시 이게 되려나?

“잠깐 손 줘 봐.”

“응?”

“쓰읍. 손 좀 줘 보라고.”

하연이가 희귀 생물을 보는 듯한 눈빛으로 나를 훑었다.

“이게 무슨 상황이지? 징그럽게 왜 이래?”

“하여간 내 말이라면 죽어도 안 듣지.”

덥석.

“우리 남매야, 알지?”

“헛소리 그만하고.”

나는 어느 때보다 신중하게 공력을 끌어 올렸다. 천천히, 아주 천천히 공력 한 줄기를 손을 따라 하연이의 몸을 향해 흘려보낸 그때.

“아!”

하연이의 탄성. 녀석도 공력이 주는 이질감을 알아챈 것이 분명했다.

순간 공력이 흩어질까 염려했지만 이미 경지에 오른 진가심법은 타인의 몸에서도 순순히 통제를 따랐다.

‘이 정도면 충분해.’

간단한 시범 테스트가 끝났으니 다음은 정규 테스트다. 이번엔 공력을 하연이의 단전으로 흘려보냈다.

평소였다면 숨 쉬는 것처럼 간단한 일이었겠지만 하연이의 신체는 달랐다. 혈도는 좁았고, 내부에는 노폐물들이 가득 끼어 있었다.

‘이건 좀 힘들겠는데.’

현대와 무림. 두 곳을 따로따로 분리하고 생각해 봐도 나는 일반인을 훨씬 뛰어넘는 신체의 소유자였다.

그러나 하연이는 평범한 고등학생. 지난 19년간 축적된 노폐물들의 존재는 어쩌면 당연했다.

‘그래도 되는 데까지는 해 봐야지.’

진가심법의 안정성과 내 통제력을 믿기에 가능한 일이다.

만약의 사태에 대비하여 하연이에게 미리 말하는 것도 잊지 않았다.

“조금 아파도 참아라, 알겠지?”

“뭐야, 뭔데?”

“음. 안정성이 굉장히 뛰어난 한의학 치료법이라고 해야 하나.”

설거지를 하던 엄마가 눈을 동그랗게 떴다.

“어머, 한의학? 아들 그런 것도 할 줄 알아?”

“그냥 좀 배웠어요.”

“잘됐네. 한번 해 봐.”

반면 하연이의 반응은 떨떠름했다.

“웬 한의학? 난 그런 거 좀 별론데.”

“그럼 나 믿고 조금만 참아 봐.”

“엄마, 그동안 키워 줘서 고마웠어. 못난 딸은 효도도 못 해 보고 가네.”

“…….”

아니, 이 새끼가?

하마터면 공력이 흐트러질 뻔했다. 한 시간을 뛰어다녀도 땀 한 방울 안 나는데 지금은 좀 덥다.

“농담이야. 설마 하나뿐인 여동생한테 안 좋은 짓이라도 하겠어?”

“그럼 입 다물고 있어. 좀 아파도 최대한 움직임 자제하고.”

“오케이.”

깊게 심호흡했다. 지금부터 하연이의 혈도를 깨끗이 청소할 생각이었다. 청소부는 나, 빗자루는 15년의 공력이다.

“준비됐지?”

“네네, 선생님. 그런데 이거 도대체 언제 시작하나요?”

“지금 바로.”

대답과 동시에 공력을 흘려보냈다.

스아아아.

부드럽고 강한 공력의 파도가 하연이의 전신 세맥을 휩쓸기 시작했다. 하연이의 몸 안 가득 쌓인 노폐물을 씻어 내리며…….



* * *



“후우.”

“푸하.”

손을 뗀 순간 동시에 터져 나온 두 개의 숨은 각각 의미가 달랐다. 나는 안도감, 하연이는 후련함이다.

띠링.



- [운기요상]을 성공적으로 완료했습니다.

- [공력]이 소량 증가합니다.



시스템의 말대로 운기요상은 성공적으로 끝났다.

진가심법은 공력 축적 속도가 느린 대신 안정성이 극히 뛰어난 내공심법. 쌓인 노폐물이 워낙 많이 탓에 다소 시간이 걸리긴 했지만 큰 위기 없이 끝냈다.

“오빠, 이게 뭐야?”

오빠 소리가 자연스럽게 나오는 걸 보니 하연이도 놀라긴 한 모양이다. 나는 긴장감 때문에 맺힌 땀방울을 닦아 내며 대답했다.

“말했잖아. 안정적인 한의학 치료라고.”

“손만 잡고 있었는데 그게 돼?”

되겠냐? 이게 다 네 오빠의 뛰어남 덕분이지.

나는 자연스럽게 화제를 돌렸다.

“그래서, 어땠어?”

“처음에는 아팠는데…… 시간이 가면 갈수록 시원해졌어. 몸도 가벼워지고 두통도 사라지고. 뭐랄까.”

미간을 좁힌 하연이가 한마디로 정의를 내렸다.

“다시 태어난 느낌? 내 안에 있던 안 좋은 기운들이 싹 씻겨 내려간다고 해야 하나. 아씨, 모르겠네.”

그 정도면 제법 정확하게 알고 있는 것 같은데?

어쨌건 확연히 나아진 안색을 보니 해 준 보람이 있다. 나는 피식 웃으며 말했다.

“어, 그럼 이제 씻고 와.”

“응?”

“응은 무슨 응이야. 너 코 막혔어? 냄새 장난 아니니까 빨리 샤워부터 하라고.”

“아침에 씻었는데 도대체 무슨 냄새가 난다는…… 악!”

자신의 몸에서 진동하는 악취를 깨달은 하연이가 코를 움켜쥐고 난리법석을 피운다.

‘자연스러운 일이지.’

몸 안에 있던 노폐물들이 어디로 가겠나. 다 몸 밖으로 분출되는 거지. 이를테면 땀이라든가, 아니면…….

꾸르륵. 뽕.

뭐, 저렇게도 나오는 거다.

“…….”

그런데 노폐물 양이 많아서 그런가. 냄새가 장난이 아니다.

이 정도면 똥을 싼 건 아닌지 의심해 봐야 하는 정도인데?

“아흑.”

몸을 흠뻑 적신 땀에 더해 배에서 오는 이상 신호까지. 거의 기어가다시피 화장실로 직행하는 하연이를 보며 엄마는 벌린 입을 다물지 못했다.

“세상에.”

“효과 좋죠?”

“그러게. 엄마도 어릴 때 한의원 몇 번 가 보긴 했는데 신통하다.”

“제가 잘 배워서 그래요. 혹시 한의원 가실 거면 그냥 저한테 오세요. 지금 바로 하셔도 좋고.”

“그럴까? 안 그래도 내가 요즘 소화가 잘…….”

엄마가 방긋 웃으며 손을 내준 그때였다.

부아아앙. 푸드득. 푸드득.

“…….”

“…….”

엄마가 슬그머니 손을 뺐다.

“……하연이 나오면 시작할까?”

“……네.”

우리 집은 화장실이 하나다.



* * *



쏴아아아.

화장실 물 내려가는 소리가 들리고 얼마 후, 세상 시원한 얼굴의 엄마가 나왔다.

“몸은 어떠세요?”

“10년은 젊어진 기분이야.”

결코 과장이 아니다. 열아홉 살인 하연이도 몸 안의 노폐물을 전부 배출하기까지 한 시간이 넘게 걸렸다.

중년에 접어든 엄마는 살아온 세월만큼 노폐물의 양도 많았다. 두 시간이 넘는 운기요상으로 전과는 비교할 수도 없을 만큼 몸 상태가 좋아졌을 것이다.

“그치? 나도 아까까지만 해도 머리 아프고, 어지럽고 그랬는데 지금은 싹 나았다니까? 화장실 나오자마자 열 재 봤는데 정상 체온이더라고.”

하연이가 신기한 듯이 나를 바라봤다. 녀석은 화장실에서 나오자마자 언제 입맛이 없다고 말을 했냐는 듯 밥을 두 공기나 비웠다.

“도대체 이런 건 어디서 배우는 거야? 오빠 힐러였어?”

“힐러는 무슨. 그냥 어쩌다가 배운 거지.”

“어디 한의원에서 배웠는데? 가까우면 나도 한 번 가 보게.”

“……너 거기 가면 큰일 난다.”

“왜?”

“몰라도 돼. 그냥 무서운 아저씨들 많다고만 알아 둬.”

“침을 아프게 놓나?”

“……좀 그런 편이야.”

그 침이 칼침이라는 걸 알면 저 녀석이 무슨 표정을 지을까.

나는 꼬치꼬치 캐묻는 하연이를 밀어 내며 주머니에 손을 넣었다.

‘인벤토리 오픈.’

익숙한 시스템 알림과 함께 반투명한 인벤토리창이 떴다.

만약 무림이었다면 조필을 쓰러트리고 얻은 전리품과 각종 병장기가 가득 쌓여 있었겠지만 이곳은 현실이다.

‘인벤토리가 통합되어 있으면 좋을 텐데.’

각각 인벤토리가 분리되어 있다는 게 생각할수록 아쉽다.

무림에 상급 포션 몇 개만 들고 가도 여벌의 목숨을 챙긴 거나 다름없을 테니까.

‘뭐, 레벨 업으로 어느 정도 회복할 수 있다는 것에 만족해야지.’

내심 혀를 차며 주머니에서 손을 뺐을 때, 내 손바닥에는 붉은색 액체가 찰랑거리는 작은 병 두 개가 들려 있었다.



아이템창



[하급 포션]

종류 : 치료제

등급 : 삼류

설명 : 미약한 치료 마법이 깃든 액체. 시중에서 쉽게 구할 수 있다.

효과 : 섭취 시 신체를 회복시켜 준다. 효과는 미비하다.





어제 레이드 보급품으로 지급받은 물건이다. 딱히 쓸 일이 없어 고스란히 남았던 것을 인벤토리에 넣어 뒀었다.

‘원래는 반납해야 하지만.’

아무리 하급 포션이라도 개당 20만 원이 넘어가는 고가의 물건.

최 팀장처럼 턱턱 내어 주는 후한 고용주는 찾아보기 힘들다.

“하나씩 드세요.”

“어? 포션이네.”

“뭘 또 포션까지…… 지금도 충분히 괜찮은데.”

“부작용이 있을까 봐 그래요. 지금 안 마시면 나중에 돈 더 나갈걸요.”

원기 보양 차원에서 권하는 것뿐, 사실 운기요상에 부작용은 없다.

“빨리 드세요. 하연이 너도.”

주저하던 엄마가 먼저 포션을 섭취했고, 눈치를 보던 하연이가 뒤를 이었다.

꿀꺽. 꿀꺽.

“어때?”

시원하게 원샷을 때린 하연이가 고개를 갸웃거렸다.

“힘이 좀 나는 것 같기도 하고, 아닌 것 같기도 하고. 내가 뭐 포션을 먹어 봤어야 알지.”

“엄마도 잘은 모르겠구나.”

“피곤하거나 아플 때 먹으면 효과가 확실히 느껴질 거예요. 한 박스 사다 놓을 테니까 그럴 때마다 드세요.”

“한 박스? 한 박스면 몇 개야?”

“큰 걸로 사면 50개?”

“하나에 20만 원쯤 하니까 50개면…… 천만 원? 오빠 미쳤어?”

깜짝 놀란 하연이가 내 팔뚝을 찰싹 때렸다.

“이번에 돈 좀 벌었다고 너무 막 쓰는 거 아냐? 그렇게 막 과소비하면 3억 그거 금방 사라져.”

“괜찮아. 요즘 잘 벌어.”

“내가 인터넷 검색해 봤는데 C급 헌터 되면 뭐 장비도 바꿔야 하고 그렇다며. 억 단위는 우습게 나가던데.”

“괜찮다니까. 어제도 40억 벌었어.”

“40억 있으면 이렇게 흥청망청…… 잠깐, 얼마라고?”

“40억.”

“…….”

순간 하연이의 몸이 딱 굳었다. 나를 멍한 눈빛으로 바라보던 녀석이 엄마를 향해 말했다.

“엄마, 오빠가 40억 벌었대.”

엄마는 어색하게 웃으며 고개를 끄덕였다. 그제야 하연이가 떨리는 목소리로 묻는다.

“진짜야?”

“응.”

“40억?”

“그렇다니까.”

하연이의 눈빛에 결심이 깃들었다.

“오빠. 나 학교 자퇴해도 돼?”

“…….”

배움에는 끝이 없다고 하지 않았냐?
```

## Final English reading copy

```markdown
# Chapter 89

“Son, slow down. You’ll make yourself sick.”

“You could quit being a Hunter and become a mukbang streamer.”

I finished my meal amid Mom’s concern and Hayeon’s admiration.

That was after five heaping bowls of rice, a whole pot of cheonggukjang, and dozens of kimchi pancakes had vanished.

“Whew. I’m finally starting to feel full.”

“……Are you insane? How much do you usually eat?”

“If it’s tasty, it just keeps going in.”

I had always eaten a lot, but never this much.

Maybe it was because my metabolism and internal organs had improved to a degree that couldn’t even be compared to before. These days, I could put even professional food fighters to shame.

“Maybe I really should become a mukbang streamer.”

“No. Those people need to make a living too. Let humans compete among themselves.”

“Are you saying I’m not human?”

“Yeah. In my eyes, you’re something beyond a pig.”

Hayeon could only shake her head in disbelief as she put down her spoon. I glanced into her rice bowl and saw that half of it was still there.

“If you leave rice, you’ll be punished.”

“You sound like an old man.”

“Don’t you know Koreans run on rice even at death’s door? You have to eat if you want your cold to go away faster.”

“I don’t have an appetite. My head hurts too.”

“Did you go to the hospital?”

“I did. I took the medicine they prescribed, too.”

I stared at Hayeon in silence. Her face was flushed, and beads of sweat had formed on her forehead. She had left school early and stubbornly tried to study, but it seemed her fever had risen even higher than before.

*The medicine she was prescribed doesn’t seem to be working very well.*

Honestly, there was a much simpler way to cure an illness.

She could get treated by a professional healer or drink a potion sold on the market. But most ordinary people avoided doing that because of the expense.

*What a fool.*

The reason I had worked nonstop was so my family could live safely, happily, and without getting sick.

Even though I knew why they couldn’t spend money so easily, I couldn’t help feeling frustrated. How much could one lousy potion cost?

*At the very least, circulating qi once would make her feel much better… Huh?*

A thought suddenly flashed through my mind, and I stopped.

*Wait. Could this actually work?*

“Give me your hand for a second.”

“Huh?”

“Tsk. I said give me your hand.”

Hayeon looked me over as if I were some rare creature.

“What is happening here? Why are you being so gross?”

“You’d rather die than listen to a word I say.”

I grabbed her hand.

“We’re siblings, okay?”

“Stop talking nonsense.”

I raised my internal energy more carefully than ever. Slowly—very slowly—I let a thread of internal energy flow along my hand and into Hayeon’s body.

“Aah!”

Hayeon let out a startled cry. She had clearly noticed the strange sensation caused by my internal energy.

I was worried that it might scatter, but the Jin Family’s Cultivation Technique had already reached a realm stage. It obeyed my control without resistance, even inside someone else’s body.

*This much should be enough.*

The simple demonstration test was over. Now came the real test.

This time, I guided my internal energy toward Hayeon’s dantian.

Under normal circumstances, it would have been as easy as breathing. But Hayeon’s body was different. Her acupoints were narrow, and her insides were clogged with waste.

*This is going to be difficult.*

Even if I separated the modern world and the Murim and considered them independently, I possessed a body far beyond that of an ordinary person.

Hayeon, however, was an ordinary high school student. The waste accumulated over her nineteen years of life was only natural.

*Still, I should do everything I can.*

I could only attempt this because I trusted the Jin Family’s Cultivation Technique’s stability and my own control.

I also remembered to warn Hayeon in advance, just in case.

“It might hurt a little, so bear with it, okay?”

“What? What are you doing?”

“Hmm. I suppose you could call it a particularly stable form of traditional Korean medicine.”

Mom, who had been washing dishes, opened her eyes wide.

“Oh my, traditional medicine? You know how to do that too?”

“I just learned a little.”

“That’s wonderful. Give it a try.”

Hayeon, on the other hand, looked less than enthusiastic.

“Why traditional medicine? I’m not really into that kind of thing.”

“Then trust me and put up with it for a little while.”

“Mom, thank you for raising me all this time. Your useless daughter is leaving without even getting the chance to repay you.”

“…….”

*What the hell, you little shit?*

I almost lost control of my internal energy. I could run around for an hour without sweating a drop, but I was starting to feel a little hot now.

“I’m joking. It’s not like you’d do anything bad to your only little sister, right?”

“Then shut up and stay as still as possible, even if it hurts.”

“Okay.”

I took a deep breath. From this moment on, I was going to clean out Hayeon’s acupoints.

The cleaner was me.

The broom was fifteen years of internal energy.

“Ready?”

“Yes, yes, Teacher. But when exactly are we starting?”

“Right now.”

As soon as I answered, I sent my internal energy flowing.

*Whooosh.*

A wave of gentle yet powerful internal energy began sweeping through the minor meridians throughout Hayeon’s body, washing away the waste that had built up inside her…

* * *

“Hoo.”

“Phew.”

The two breaths that escaped us simultaneously after I let go of her hand carried completely different meanings.

Mine expressed relief.

Hayeon’s expressed refreshment.

*Ding.*

> **System**
>
> - **Circulate Qi for Healing** has been completed successfully.
> - **Internal Energy** increases slightly.

As the System had announced, Circulate Qi for Healing had ended successfully.

The Jin Family’s Cultivation Technique was an internal energy cultivation technique that accumulated internal energy slowly but possessed exceptional stability. Hayeon had accumulated so much waste that the process took some time, but it ended without any major problems.

“Oppa, what was that?”

The fact that she naturally called me Oppa showed that she had been surprised too. I wiped away the sweat that had formed from the tension and answered.

“I told you. It’s a stable traditional medicine treatment.”

“That worked when you were only holding my hand?”

*Do you think it would? It’s all thanks to your brother’s excellence.*

I smoothly changed the subject.

“So? How was it?”

“It hurt at first, but as time passed, it started feeling better and better. My body feels lighter, and my headache is gone. What should I call it…”

Hayeon furrowed her brow before defining it in a single phrase.

“Like I was reborn? Like all the bad energy inside me was washed away. Ah, damn it, I don’t know.”

*That sounds pretty accurate to me.*

In any case, seeing how much better her complexion looked made all the effort worthwhile. I let out a short laugh and said,

“Yeah, then go wash up.”

“Huh?”

“What do you mean, ‘huh’? Is your nose stuffed up? You stink, so go take a shower. Now.”

“I washed this morning. What do you mean I smell—Aagh!”

Hayeon realized that a terrible stench was radiating from her own body, grabbed her nose, and began making a huge fuss.

*It’s only natural.*

Where else would the waste inside her body go? It had to come out somehow. Through sweat, for example, or maybe…

*Grrrbl. Pffft.*

Well, it could come out that way too.

“…….”

But maybe it was because there had been so much waste. The smell was unbelievable.

At this point, I had to wonder if she had actually crapped herself.

“Aah.”

On top of the sweat soaking her body, her stomach had begun sending strange signals. Hayeon almost crawled to the bathroom, while Mom stood there with her mouth hanging open.

“My goodness.”

“It works well, doesn’t it?”

“It really does. I went to a traditional medicine clinic a few times when I was young, but this is amazing.”

“I learned properly. If you ever want to go to a traditional medicine clinic, just come to me. You can do it right now, if you want.”

“Should I? As it happens, I’ve been having some trouble digesting lately…”

Mom smiled brightly and held out her hand.

That was when—

*Bwaaaang. Frrt. Frrt.*

“…….”

“…….”

Mom quietly withdrew her hand.

“……Should we start when Hayeon comes out?”

“……Yes.”

There was only one bathroom in our house.

* * *

*Whooosh.*

Some time after the sound of the toilet flushing, Mom emerged with the most refreshed expression in the world.

“How do you feel?”

“I feel ten years younger.”

That wasn’t an exaggeration.

Even Hayeon, who was only nineteen, had needed more than an hour to expel all the waste from her body.

Mom was middle-aged, so the amount of waste she had accumulated was proportional to the years she had lived. After more than two hours of circulating qi for healing, her condition must have improved to a degree that couldn’t even be compared to before.

“Right? Until just a little while ago, I had a headache and felt dizzy, but now I’m completely better. I took my temperature as soon as I came out of the bathroom, and it was normal.”

Hayeon looked at me as if I were some kind of marvel. The moment she came out of the bathroom, she ate two bowls of rice as if she had never once complained about having no appetite.

“Where did you learn something like this? Were you a healer, Oppa?”

“A healer? No. I just happened to learn it.”

“Which traditional medicine clinic did you learn it at? If it’s nearby, I’ll go there too.”

“……You’d be in big trouble if you went there.”

“Why?”

“You don’t need to know. Just know that there are lots of scary men there.”

“Do they stick the needles in painfully?”

“……They do tend to.”

*If she knew those ‘needles’ were actually knife stabs, what kind of expression would she make?*

I pushed Hayeon away as she kept peppering me with questions and slipped a hand into my pocket.

*Open Inventory.*

A translucent inventory window appeared along with the familiar System notification.

If I had been in the Murim, it would have been packed with the spoils I had obtained after defeating Jopil and various weapons.

But this was reality.

*It would be nice if the inventories were integrated.*

The fact that they were separate seemed more unfortunate the more I thought about it.

Taking just a few high-grade potions to the Murim would be no different from bringing along a few extra lives.

*Well, I should be satisfied that I can recover to some degree by leveling up.*

I clicked my tongue inwardly and pulled my hand from my pocket. Two small bottles filled with red liquid were sloshing in my palm.

### Item Window

**Lesser Potion**

- **Type:** Medicine
- **Grade:** Third Rate
- **Description:** A liquid infused with weak healing magic. It is readily available on the market.
- **Effect:** Restores the body when consumed. The effect is minimal.

They had been issued as raid supplies yesterday. Since I had no particular use for them, I had put them in my Inventory and left them untouched.

*I’m technically supposed to return them.*

Even lesser potions cost more than 200,000 won apiece. It was difficult to find an employer as generous as Team Leader Choi, who handed them out so freely.

“Take one each.”

“Huh? It’s a potion.”

“Why go as far as using a potion? I’m perfectly fine now.”

“I’m worried there might be side effects. If you don’t drink it now, it’ll cost you more later.”

In truth, I was only recommending them to restore their vitality. Circulating qi for healing had no side effects.

“Drink up. You too, Hayeon.”

Mom hesitated, then took hers first. Hayeon cautiously took her cue from Mom and followed suit.

*Gulp. Gulp.*

“How is it?”

Hayeon finished hers in one go and tilted her head.

“I feel a little stronger, maybe. Or maybe not. How would I know? It’s not like I’ve had a potion before.”

“I guess I don’t really know either.”

“You’ll definitely notice the effect when you’re tired or sick. I’ll buy a box and keep it here, so drink one whenever that happens.”

“A box? How many come in a box?”

“Fifty, if you buy the large one?”

“At about 200,000 won each, fifty would be… ten million won? Oppa, are you crazy?”

Hayeon smacked my forearm.

“Just because you made some money this time, are you really going to spend it so recklessly? If you keep overspending like that, that 300 million won will disappear in no time.”

“It’s fine. I’ve been earning well lately.”

“I searched online, and I heard that when you become a C-rank Hunter, you have to replace your equipment and all that. They said you can burn through hundreds of millions like it’s nothing.”

“I told you, it’s fine. I made four billion won yesterday, too.”

“Even if you had four billion won, you shouldn’t throw money around like—wait, how much did you say?”

“Four billion won.”

“…….”

Hayeon’s body went completely rigid.

She stared blankly at me, then turned toward Mom.

“Mom, Oppa says he made four billion won.”

Mom gave an awkward smile and nodded.

Only then did Hayeon ask in a trembling voice,

“Is that true?”

“Yeah.”

“Four billion won?”

“I’m telling you, it is.”

Determination filled Hayeon’s eyes.

“Oppa. Can I drop out of school?”

“…….”

*Didn’t you say there was no end to learning?*
```
